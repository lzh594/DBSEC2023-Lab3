# mysql README

### 本项目的mysql数据库中数据获取和数据初始化的内容

### 子目录结构

```
mysql
├── Crawl
├── Process
├── ERDiagram
│   ├── concepts.drawio
│   ├── logics.drawio
│   └── physics.drawio
├── SQL
│   ├── 1_database.sql
│   ├── 2_tables.sql
│   ├── 3_trigger.sql
│   └── 4_data.sql
└── README.md # 数据库项目README
```

### Crawl

+ 爬虫程序相关

### Process

+ 数据初始化程序

### ERDiagram

+ 存放ER图，包含概念、逻辑、物理三层结构
+ 需要时用draw.io打开

### SQL

+ [数据库创建](./SQL/1_database.sql)
+ [数据库表创建](./SQL/2_tables.sql)
+ [数据库触发器创建](./SQL/3_trigger.sql)
+ [数据库导入](./SQL/4_data.sql)（建议使用后端Django项目的数据导入）

  