import pandas as pd
from Crypto.Random import get_random_bytes
import random
import pymysql
import hashlib

names = []
passwd = []

# 连接mysql
conn = pymysql.connect(host="127.0.0.1", port=3306, user="root", password="142857", charset="utf8", db="bookStoreDB")
cursor = conn.cursor()

# 获取用户名
def getUserName():
    filename = "CUSTOMERS.csv"
    alluser = pd.read_csv(filename, header=None)
    alluser.columns = ['id', 'name', 'address', 'web', 'salary']
    return alluser['name']

# 生成所有用户的密码
def getPasswd(num: int):
    """
    :param num: 用户个数
    :return:
    """
    passwd = []
    for i in range(num):
        e = get_random_bytes(4)
        s = ""
        for byte in e:
            s += '{:02x}'.format(byte)
        passwd.append(s)
    return passwd

# 生成随机邮箱
def generateRandomMail():
    list_sum = [i for i in range(10)] + ["a", "b", "c", "d", "e", "f", "g", "h", 'i', "j", "k",
                                         "l", "M", "n", "o", "p", "q", "r", "s", "t", "u", "v",
                                         "w", "x", "y", "z"]
    email_str = ""
    email_suffix = ["@163.com", "@qq.com", "@gmail.com", "@mail.hk.com", "＠yahoo.co.id"]
    for i in range(10):
        a = str(random.choice(list_sum))
        email_str = email_str + a

    # 随机拼接不同的邮箱后缀
    return email_str + random.choice(email_suffix)

# 生成随机电话
def generateRandomPhone():
    headList = ["130", "131", "132", "133", "134", "135", "136", "137", "138", "139", "147", "150", "151", "152", "153",
                "155", "156", "157", "158", "159", "186", "187", "188", "189"]
    mo = random.choice(headList)
    li = "0123456789"
    lis = []
    lie = ''
    for i in range(8):
        lis.append(random.choice(li))
        lie = ''.join(lis)
    return mo + lie

def processUser():
    user_passwd = []
    id = 0
    for name, pwd in zip(names, passwd):
        email = generateRandomMail()  # 得到该用户的邮箱
        phone = generateRandomPhone()  # 得到该用户的电话
        # 得到该用户的密码对应的sha256值
        sha256 = hashlib.sha256()
        sha256.update(pwd.encode('utf-8'))
        hashvalue = sha256.hexdigest()
        sql = "insert into users(uid,uname,email,tel,pwdhash) values(%s,%s,%s,%s,%s)"
        cursor.execute(sql, [id, name, email, phone, hashvalue])
        conn.commit()
        id += 1
        user_passwd.append([id, name, pwd])
    # 将用户与密码的对应关系存进表中方便测试
    csv = pd.DataFrame(user_passwd, columns=['id', 'name', 'passwd'])
    csv.to_csv("user_passwd.csv")

if __name__ == "__main__":
    names = getUserName()
    num = len(names)
    passwd = getPasswd(num)
    processUser()
