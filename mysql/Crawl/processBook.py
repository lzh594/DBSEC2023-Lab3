import pandas as pd
import pymysql

all_book = []

# 连接mysql
conn = pymysql.connect(host="127.0.0.1", port=3306, user="root", password="142857", charset="utf8", db="bookStoreDB")
cursor = conn.cursor()

# 获取所有书籍信息
def getBooks():
    filename = "data.csv"
    alldata = pd.read_csv(filename)

    num = len(alldata)
    for i in range(num):
        row = alldata.iloc[i]
        all_book.append(
            {
                'title': row['title'],
                'author': row['author'],
                'pub_year': row['pub_year'],
                'publisher': row['publisher'],
                'price': row['price'],
                'img': row['img'],
                'category': row['class'],
            }
        )

# 初始化publishers
def processPub():
    already = []  # 已被初始化完的publisher
    id = 0
    for book in all_book:
        if book['publisher'] not in already:
            sql = "insert into publishers(pub_id,pname) values(%s, %s)"
            cursor.execute(sql, [id, book['publisher']])
            conn.commit()
            already.append(book['publisher'])
            id += 1

# 初始化category
def processCategory():
    already = []  # 已被初始化完的category
    id = 0
    for book in all_book:
        if book['category'] not in already:
            sql = "insert into category(category_id,category_name) values(%s, %s)"
            cursor.execute(sql, [id, book['category']])
            conn.commit()
            already.append(book['category'])
            id += 1

# 初始化author
def processAuthor():
    already = []  # 已被初始化完的author
    id = 0
    for book in all_book:
        if book['author'] not in already:
            sql = "insert into authors(author_id,aname) values(%s, %s)"
            if pd.isna(book['author']):
                cursor.execute(sql, [id, 'No author'])
            else:
                cursor.execute(sql, [id, book['author']])
            conn.commit()
            already.append(book['author'])
            id += 1

# 初始化Book
def processBook():
    already = []  # 已被初始化完的book
    id = 0
    for book in all_book:
        if book['title'] not in already:
            # 获取author_id
            if pd.isna(book['author']):
                cursor.execute("select author_id from authors where aname=%s", ['No author'])
            else:
                cursor.execute("select author_id from authors where aname=%s", [book['author']])
            author_id = cursor.fetchone()
            # 获取category_id
            cursor.execute("select category_id from category where category_name=%s", [book['category']])
            category_id = cursor.fetchone()
            # 获取pub_id
            cursor.execute("select pub_id from publishers where pname=%s", [book['publisher']])
            pub_id = cursor.fetchone()

            sql = "insert into books(book_id, bname, author_id, pub_id, category_id, price, pub_year) values(%s,%s,%s,%s,%s,%s,%s)"
            cursor.execute(sql, [id, book['title'], author_id, pub_id, category_id, book['price'], book['pub_year']])
            conn.commit()
            already.append(book['title'])
            id += 1

if __name__ == "__main__":
    getBooks()
    processBook()
