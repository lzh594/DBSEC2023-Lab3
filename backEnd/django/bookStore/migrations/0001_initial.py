# Generated by Django 4.2.1 on 2023-12-11 12:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Authors',
            fields=[
                ('author_id', models.IntegerField(help_text='作者序号', primary_key=True, serialize=False)),
                ('aname', models.CharField(help_text='作者名称', max_length=255)),
            ],
            options={
                'db_table': 'authors',
            },
        ),
        migrations.CreateModel(
            name='Books',
            fields=[
                ('book_id', models.IntegerField(help_text='书的序号', primary_key=True, serialize=False)),
                ('bname', models.CharField(help_text='书名', max_length=255)),
                ('price', models.DecimalField(decimal_places=2, help_text='价格', max_digits=10)),
                ('pub_year', models.IntegerField(help_text='出版年份')),
                ('url', models.CharField(help_text='书籍图片链接', max_length=255)),
                ('isbn', models.CharField(help_text='书籍isbn号', max_length=10)),
                ('sales', models.IntegerField(default=0, help_text='书籍销售量', null=True)),
                ('rate', models.DecimalField(decimal_places=1, help_text='书籍评分', max_digits=2)),
                ('author', models.ForeignKey(db_column='author_id', on_delete=django.db.models.deletion.CASCADE, to='bookStore.authors')),
            ],
            options={
                'db_table': 'books',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('category_id', models.IntegerField(help_text='种类序号', primary_key=True, serialize=False)),
                ('category_name', models.CharField(help_text='种类名称', max_length=255)),
            ],
            options={
                'db_table': 'category',
            },
        ),
        migrations.CreateModel(
            name='Publishers',
            fields=[
                ('pub_id', models.IntegerField(help_text='出版社序号', primary_key=True, serialize=False)),
                ('pname', models.CharField(help_text='出版社名称', max_length=255)),
            ],
            options={
                'db_table': 'publishers',
            },
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('uid', models.IntegerField(help_text='用户序号', primary_key=True, serialize=False)),
                ('uname', models.CharField(help_text='用户昵称', max_length=100)),
                ('pwdhash', models.CharField(help_text='用户密码的哈希值', max_length=255)),
                ('email', models.CharField(blank=True, help_text='用户邮箱', max_length=100, null=True)),
                ('tel', models.CharField(blank=True, help_text='用户电话', max_length=11, null=True)),
            ],
            options={
                'db_table': 'users',
            },
        ),
        migrations.CreateModel(
            name='Shoppinghistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True, help_text='购买日期')),
                ('amount', models.IntegerField(default=1, help_text='购买数量')),
                ('book', models.ForeignKey(db_column='book_id', help_text='书的序号', on_delete=django.db.models.deletion.CASCADE, to='bookStore.books')),
                ('user', models.ForeignKey(db_column='uid', help_text='用户序号', on_delete=django.db.models.deletion.CASCADE, to='bookStore.users')),
            ],
            options={
                'db_table': 'shoppinghistory',
            },
        ),
        migrations.CreateModel(
            name='Shoppingcarts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField(default=1, help_text='购买数量')),
                ('book', models.ForeignKey(db_column='book_id', help_text='书的序号', on_delete=django.db.models.deletion.CASCADE, to='bookStore.books')),
                ('user', models.ForeignKey(db_column='uid', help_text='用户序号', on_delete=django.db.models.deletion.CASCADE, to='bookStore.users')),
            ],
            options={
                'db_table': 'shoppingcarts',
            },
        ),
        migrations.CreateModel(
            name='Collection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book', models.ForeignKey(db_column='book_id', help_text='书的序号', on_delete=django.db.models.deletion.CASCADE, to='bookStore.books')),
                ('user', models.ForeignKey(db_column='uid', help_text='用户序号', on_delete=django.db.models.deletion.CASCADE, to='bookStore.users')),
            ],
            options={
                'db_table': 'collection',
            },
        ),
        migrations.AddField(
            model_name='books',
            name='category',
            field=models.ForeignKey(db_column='category_id', on_delete=django.db.models.deletion.CASCADE, to='bookStore.category'),
        ),
        migrations.AddField(
            model_name='books',
            name='publisher',
            field=models.ForeignKey(db_column='pub_id', on_delete=django.db.models.deletion.CASCADE, to='bookStore.publishers'),
        ),
        migrations.AddConstraint(
            model_name='shoppingcarts',
            constraint=models.UniqueConstraint(fields=('user', 'book'), name='shoppingcarts_id'),
        ),
        migrations.AddConstraint(
            model_name='shoppingcarts',
            constraint=models.CheckConstraint(check=models.Q(('amount__gt', 0)), name='amount__gt=0'),
        ),
        migrations.AddConstraint(
            model_name='collection',
            constraint=models.UniqueConstraint(fields=('user', 'book'), name='collection_id'),
        ),
    ]