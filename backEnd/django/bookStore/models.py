from django.db import models


class Users(models.Model):
    uid = models.AutoField(primary_key=True)
    uname = models.CharField(max_length=100, null=False)
    passwd = models.CharField(max_length=100, null=False)
    email = models.EmailField(max_length=100, null=True)
    tel = models.CharField(max_length=11, null=True)


class Authors(models.Model):
    author_id = models.AutoField(primary_key=True)
    aname = models.CharField(max_length=255, null=False)


class Publishers(models.Model):
    pub_id = models.AutoField(primary_key=True)
    pname = models.CharField(max_length=255, null=False)


class Category(models.Model):
    category_id = models.AutoField(primary_key=True)
    category_name = models.CharField(max_length=255, null=False)


class Books(models.Model):
    book_id = models.AutoField(primary_key=True)
    bname = models.CharField(max_length=255, null=False)
    author = models.ForeignKey(Authors, on_delete=models.CASCADE)
    publishers = models.ForeignKey(Publishers, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.CharField(max_length=255, null=False)
    pub_year = models.IntegerField(null=False)


class ShoppingCarts(models.Model):
    uid = models.IntegerField(null=False)
    book = models.ForeignKey(Books, on_delete=models.CASCADE)
    amount = models.IntegerField(null=False)
    user = models.ForeignKey(Users, on_delete=models.CASCADE)

    class Meta:
        # 定义复合主键
        constraints = [
            models.UniqueConstraint(fields=['uid', 'book'], name='shoppingCarts'),
            models.CheckConstraint(check=models.Q(amount__gt=0), name="amount__gt=0")
        ]


class ShoppingHistory(models.Model):
    uid = models.IntegerField(null=False)
    book = models.ForeignKey(Books, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(Users, on_delete=models.CASCADE)

    class Meta:
        # 定义复合主键
        constraints = [
            models.UniqueConstraint(fields=['uid', 'book'], name='shoppingHistory'),
        ]


class Collection(models.Model):
    uid = models.IntegerField(null=False)
    book = models.ForeignKey(Books, on_delete=models.CASCADE)
    user = models.ForeignKey(Users, on_delete=models.CASCADE)

    class Meta:
        # 定义复合主键
        constraints = [
            models.UniqueConstraint(fields=['uid', 'book'], name='collection'),
        ]
