import random

from lxml import etree
import requests
import json
import threading
import csv
import urllib3
from fake_useragent import UserAgent
from proxyPool import send_request

urllib3.disable_warnings()

baseUrl = 'https://www.abebooks.com'
db = []

ua = UserAgent()
headers = {
    'User-Agent': ua.random
}

s = requests.session()
s.keep_alive = False

# 获取所有的类别的相关信息
def getClass():
    with open("source_code.html", "r") as f:
        # 将获取到的源代码转换成html
        source_code = f.read()
        html = etree.HTML(source_code)
        all_class = []  # 所有的类别
        all_class_url = []
        all_pub = []  # 所有的出版商
        for i in range(6):
            all_class += html.xpath(
                f'//div[@class="col-xs-6 col-sm-4 col-md-3 col-xl-2 collection-rollup-{i}"]/div/a/div/h4/text()')
            all_pub += html.xpath(
                f'//div[@class="col-xs-6 col-sm-4 col-md-3 col-xl-2 collection-rollup-{i}"]/div/a/div/p[1]/small/text()')
            all_class_url += html.xpath(
                f'//div[@class="col-xs-6 col-sm-4 col-md-3 col-xl-2 collection-rollup-{i}"]/div/a/@href')
        all_class_url = [baseUrl + x for x in all_class_url]
        return all_class, all_class_url, all_pub

# 获取每一类的书籍信息
def getBookOfClass(cla, url, pub):
    """
    :param cla: 所属的类
    :param url: 该类的网址
    :param pub: 所属的出版社
    :return:
    """
    res = requests.get(url, headers=headers, verify=False)
    source_code = res.text  # 首先获取该类书籍的源代码
    html = etree.HTML(source_code)  # 将该源代码解析为html

    prices = []
    titles = html.xpath(
        '//div[@class="grid-item col-xs-6 col-sm-fifteen-5 col-md-3 col-lg-fifteen-3 col-xl-2 col-xxl-fourteen-2"]/div/a/div/div[1]/text()')  # 该类的所有书名
    authors = html.xpath(
        '//div[@class="grid-item col-xs-6 col-sm-fifteen-5 col-md-3 col-lg-fifteen-3 col-xl-2 col-xxl-fourteen-2"]/div/a/div/div[2]/text()')  # 该类所有书的作者
    pub_years = html.xpath(
        '//div[@class="grid-item col-xs-6 col-sm-fifteen-5 col-md-3 col-lg-fifteen-3 col-xl-2 col-xxl-fourteen-2"]/div/a/div/div[3]/text()')  # 该类所有书的出版日期
    urls = html.xpath(
        '//div[@class="grid-item col-xs-6 col-sm-fifteen-5 col-md-3 col-lg-fifteen-3 col-xl-2 col-xxl-fourteen-2"]/div/a/@href')  # 该类中每本书对应的url
    urls = [baseUrl + x for x in urls]
    isbns = []
    for child_url in urls:
        child_res = requests.get(child_url, headers=headers, verify=False)
        child_code = child_res.text  # 获取该书对应网址的源代码
        child_html = etree.HTML(child_code)  # 将该源代码解析为html
        prices += child_html.xpath('//*[@id="book-price"]/text()')
        isbns += child_html.xpath('//*[@id="isbn"]/a[1]/text()')
        child_res.close()
    imgs = html.xpath(
        '//div[@class="grid-item col-xs-6 col-sm-fifteen-5 col-md-3 col-lg-fifteen-3 col-xl-2 col-xxl-fourteen-2"]/div/a/img/@src')  # 该类所有书的图片的url
    imgs = ['https:' + x for x in imgs]

    for title, author, pub_year, price, img, isbn in zip(titles, authors, pub_years, prices, imgs, isbns):
        db.append(
            {
                "title": title,
                "author": author,
                "pub_year": pub_year,
                "publisher": pub,
                "price": price,
                "img": img,
                "class": cla,
                "isbn": isbn.strip().replace("\n", "")
            }
        )
    print("class " + cla + " is over!")
    res.close()

# 将数据录入csv文件
def writeCSV():
    with open("data1.csv", "w", encoding="utf-8", newline='') as f:
        csv_writer = csv.writer(f)
        # 表头
        head = ["title", "author", "pub_year", "publisher", "price", "img", "class", "isbn"]
        csv_writer.writerow(head)
        # 写入csv文件内容
        for book in db:
            ele_list = [book["title"], book["author"], book["pub_year"], book["publisher"], book["price"], book["img"], book["class"], book["isbn"]]
            csv_writer.writerow(ele_list)

if __name__ == "__main__":
    all_class, all_class_url, all_pub = getClass()
    threads = []
    # 多线程爬取各类书籍信息
    ips = send_request()  # 获取所有代理ip
    num = len(ips)  # 获得代理ip的数目
    for cla, url, pub in zip(all_class, all_class_url, all_pub):
        i = random.randint(0, num - 1)
        proxy = ips[i]
        thread = threading.Thread(target=getBookOfClass, args=(cla, url, pub))
        threads.append(thread)
        thread.start()
    # 等待所有线程执行完毕
    for thread in threads:
        thread.join()

    # 剔除无效数据
    for book in db:
        book["author"] = book["author"].strip()
        if book["author"] == "\n":
            db.remove(book)
            length = len(db)

    print(json.dumps(db))
    # 将数据录入csv文件
    writeCSV()
