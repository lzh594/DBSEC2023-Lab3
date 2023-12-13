# README

## 后端项目Django结构

```
.
├── backend_django
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── bookStore
│   ├── migrations
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── serializers.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── django.json
├── manage.py
└── README.md
```

## 运行环境配置要求

### Python：3.10.8

### IDE：PyCharm 2023.2

### Django：4.2.1

### django rest framework：3.14.0

### coreapi：2.3.3

## 配置数据库

### 在mysql中创建数据库`bookStoreDB`

```shell
mysql -u root -p
# 输入密码
create database bookStoreDB；
```

## 配置Django中mysql相关设置

```shell
# ./backend_django/settings.py

```



## 启动后端命令

### 使用命令行

```shell
# DBSEC2023-Lab3/backEnd/bookstore_django
python3 manage.py runserver [[ip]:[port]]
```

+ #### windows系统下输入的可能是`python`

+ #### `[[ip]:[port]]`用于将**服务器启动**在指定ip和port下，默认为`localhost:8000`

+ #### 由于前后端分离的架构，应将其指定为运行主机的局域网ip上，查看ip方法如下

    ##### *nix：

    ```shell
    ifconfig getifaddr en0
    ```

    ##### windows：

    ```shell
    ipconfig
    ```

### 使用PyCharm

#### 在IDE右上角进行项目配置

![image-20231213104331104](./README/image-20231213104331104.png)

#### 可以设置主机IP与端口

![image-20231213104359265](./README/image-20231213104359265.png)