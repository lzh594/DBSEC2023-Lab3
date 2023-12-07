from django.core.exceptions import FieldDoesNotExist
from django.db.models import IntegerField, ForeignKey, CharField, Model, CASCADE, EmailField, UniqueConstraint, \
    CheckConstraint, Q, DateTimeField, DecimalField


class Authors(Model):
    author_id = IntegerField(primary_key=True, help_text="作者序号")
    aname = CharField(max_length=255, null=False, help_text="作者名称")

    @property
    def name(self):
        # 在这里根据需要返回具体的属性，例如，返回 aname 或 bname
        return self.aname

    @classmethod
    def help(cls, field_name):
        # 获取指定字段的 help_text 值
        try:
            return cls._meta.get_field(field_name).help_text
        except FieldDoesNotExist:
            return f"Field '{field_name}' not found in model."

    class Meta:
        db_table = 'authors'


class Publishers(Model):
    pub_id = IntegerField(primary_key=True, help_text="出版社序号")
    pname = CharField(max_length=255, null=False, help_text="出版社名称")

    @property
    def name(self):
        return self.pname

    @classmethod
    def help(cls, field_name):
        # 获取指定字段的 help_text 值
        try:
            return cls._meta.get_field(field_name).help_text
        except FieldDoesNotExist:
            return f"Field '{field_name}' not found in model."

    class Meta:
        db_table = 'publishers'


class Category(Model):
    category_id = IntegerField(primary_key=True, help_text="种类序号")
    category_name = CharField(max_length=255, null=False, help_text="种类名称")

    @property
    def name(self):
        return self.category_name

    @classmethod
    def help(cls, field_name):
        # 获取指定字段的 help_text 值
        try:
            return cls._meta.get_field(field_name).help_text
        except FieldDoesNotExist:
            return f"Field '{field_name}' not found in model."

    class Meta:
        db_table = 'category'


class Books(Model):
    book_id = IntegerField(primary_key=True, help_text="书的序号")
    bname = CharField(max_length=255, null=False, help_text='书名')
    authors = ForeignKey(Authors, on_delete=CASCADE, db_column='author_id')
    publishers = ForeignKey(Publishers, on_delete=CASCADE, db_column='pub_id')
    category = ForeignKey(Category, on_delete=CASCADE, db_column='category_id')
    price = DecimalField(max_digits=10, decimal_places=2, null=False, help_text="价格")
    pub_year = IntegerField(null=False, help_text='出版年份')
    url = CharField(max_length=255, null=False, help_text="书籍图片链接")
    isbn = CharField(max_length=10, null=False, help_text="书籍isbn号")
    sales = IntegerField(null=True, default=0, help_text="书籍销售量")
    rate = DecimalField(max_digits=2, decimal_places=1, null=False, help_text="书籍评分")

    @property
    def name(self):
        return self.bname

    class Meta:
        db_table = 'books'


class Users(Model):
    uid = IntegerField(primary_key=True, help_text="用户序号")
    uname = CharField(max_length=100, null=False, help_text="用户昵称")
    pwdhash = CharField(max_length=255, null=False, help_text="用户密码的哈希值")
    email = EmailField(max_length=100, null=True, help_text="用户邮箱")
    tel = CharField(max_length=11, null=True, help_text="用户电话")

    class Meta:
        db_table = 'users'


class Shoppingcarts(Model):
    user = ForeignKey(Users, on_delete=CASCADE, help_text="用户序号", db_column='uid', name='uid')
    book = ForeignKey(Books, on_delete=CASCADE, help_text="书的序号", db_column='book_id', name='book_id')
    amount = IntegerField(null=False, help_text="购买数量")

    class Meta:
        # 定义复合主键
        constraints = [
            UniqueConstraint(fields=['user', 'book'], name='shoppingcarts_id'),
            CheckConstraint(check=Q(amount__gt=0), name="amount__gt=0")
        ]
        db_table = 'shoppingcarts'


class Shoppinghistory(Model):
    user = ForeignKey(Users, on_delete=CASCADE, help_text="用户序号", db_column='uid', name='uid')
    book = ForeignKey(Books, on_delete=CASCADE, help_text="书的序号", db_column='book_id', name='book_id')
    date = DateTimeField(auto_now_add=True, help_text="购买日期")

    class Meta:
        # 定义复合主键
        constraints = [
            UniqueConstraint(fields=['user', 'book'], name='shoppinghistory_id'),
        ]
        db_table = 'shoppinghistory'


class Collection(Model):
    user = ForeignKey(Users, on_delete=CASCADE, help_text="用户序号", db_column='uid', name='uid')
    book = ForeignKey(Books, on_delete=CASCADE, help_text="书的序号", db_column='book_id', name='book_id')

    class Meta:
        # 定义复合主键
        constraints = [
            UniqueConstraint(fields=['user', 'book'], name='collection_id'),
        ]
        db_table = 'collection'
