from django.db import models


class Users(models.Model):
    uid = models.IntegerField(primary_key=True)
    uname = models.CharField(max_length=100, null=False)
    pwdhash = models.CharField(max_length=255, null=False)
    email = models.EmailField(max_length=100, null=True)
    tel = models.CharField(max_length=11, null=True)

    class Meta:
        db_table = 'users'


class Authors(models.Model):
    author_id = models.IntegerField(primary_key=True)
    aname = models.CharField(max_length=255, null=False)

    class Meta:
        db_table = 'authors'


class Publishers(models.Model):
    pub_id = models.IntegerField(primary_key=True)
    pname = models.CharField(max_length=255, null=False)

    class Meta:
        db_table = 'publishers'


class Category(models.Model):
    category_id = models.IntegerField(primary_key=True)
    category_name = models.CharField(max_length=255, null=False)

    class Meta:
        db_table = 'category'


class Books(models.Model):
    book_id = models.IntegerField(primary_key=True)
    bname = models.CharField(max_length=255, null=False)
    authors = models.ForeignKey(Authors, on_delete=models.CASCADE)
    publishers = models.ForeignKey(Publishers, on_delete=models.CASCADE, db_column='pub_id')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.CharField(max_length=255, null=False)
    pub_year = models.IntegerField(null=False)

    class Meta:
        db_table = 'books'


class Shoppingcarts(models.Model):
    uid = models.IntegerField(null=False)
    book = models.ForeignKey(Books, on_delete=models.CASCADE)
    amount = models.IntegerField(null=False)
    user = models.ForeignKey(Users, on_delete=models.CASCADE)

    class Meta:
        # 定义复合主键
        constraints = [
            models.UniqueConstraint(fields=['uid', 'book'], name='shoppingcarts'),
            models.CheckConstraint(check=models.Q(amount__gt=0), name="amount__gt=0")
        ]
        db_table = 'shoppingcarts'


class Shoppinghistory(models.Model):
    uid = models.IntegerField(null=False)
    book = models.ForeignKey(Books, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(Users, on_delete=models.CASCADE)

    class Meta:
        # 定义复合主键
        constraints = [
            models.UniqueConstraint(fields=['uid', 'book'], name='shoppinghistory'),
        ]
        db_table = 'shopponghistory'


class Collection(models.Model):
    uid = models.IntegerField(null=False)
    book = models.ForeignKey(Books, on_delete=models.CASCADE)
    user = models.ForeignKey(Users, on_delete=models.CASCADE)

    class Meta:
        # 定义复合主键
        constraints = [
            models.UniqueConstraint(fields=['uid', 'book'], name='collection'),
        ]
        db_table = 'collection'
