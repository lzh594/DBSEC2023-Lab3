from django.db.models import IntegerField, ForeignKey, CharField, Model, CASCADE, EmailField, UniqueConstraint, \
    CheckConstraint, Q, DateTimeField


class Users(Model):
    uid = IntegerField(primary_key=True)
    uname = CharField(max_length=100, null=False)
    pwdhash = CharField(max_length=255, null=False)
    email = EmailField(max_length=100, null=True)
    tel = CharField(max_length=11, null=True)

    class Meta:
        db_table = 'users'


class Authors(Model):
    author_id = IntegerField(primary_key=True)
    aname = CharField(max_length=255, null=False)

    class Meta:
        db_table = 'authors'


class Publishers(Model):
    pub_id = IntegerField(primary_key=True)
    pname = CharField(max_length=255, null=False)

    class Meta:
        db_table = 'publishers'


class Category(Model):
    category_id = IntegerField(primary_key=True)
    category_name = CharField(max_length=255, null=False)

    class Meta:
        db_table = 'category'


class Books(Model):
    book_id = IntegerField(primary_key=True)
    bname = CharField(max_length=255, null=False)
    authors = ForeignKey(Authors, on_delete=CASCADE)
    publishers = ForeignKey(Publishers, on_delete=CASCADE, db_column='pub_id')
    category = ForeignKey(Category, on_delete=CASCADE)
    price = CharField(max_length=255, null=False)
    pub_year = IntegerField(null=False)

    class Meta:
        db_table = 'books'


class Shoppingcarts(Model):
    uid = IntegerField(null=False)
    book = ForeignKey(Books, on_delete=CASCADE)
    amount = IntegerField(null=False)
    user = ForeignKey(Users, on_delete=CASCADE)

    class Meta:
        # 定义复合主键
        constraints = [
            UniqueConstraint(fields=['uid', 'book'], name='shoppingcarts'),
            CheckConstraint(check=Q(amount__gt=0), name="amount__gt=0")
        ]
        db_table = 'shoppingcarts'


class Shoppinghistory(Model):
    uid = IntegerField(null=False)
    book = ForeignKey(Books, on_delete=CASCADE)
    date = DateTimeField(auto_now_add=True)
    user = ForeignKey(Users, on_delete=CASCADE)

    class Meta:
        # 定义复合主键
        constraints = [
            UniqueConstraint(fields=['uid', 'book'], name='shoppinghistory'),
        ]
        db_table = 'shopponghistory'


class Collection(Model):
    uid = IntegerField(null=False)
    book = ForeignKey(Books, on_delete=CASCADE)
    user = ForeignKey(Users, on_delete=CASCADE)

    class Meta:
        # 定义复合主键
        constraints = [
            UniqueConstraint(fields=['uid', 'book'], name='collection'),
        ]
        db_table = 'collection'
