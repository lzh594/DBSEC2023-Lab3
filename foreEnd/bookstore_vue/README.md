# 前端说明

前端基于Vue+Typescript开发，为用户提供线上书店的实用性页面
## 开发环境
 操作系统：Windows11（home）   
 环境配置：Nodejs-21.3.0，vue-2.9.6, npm-10.2.4
 IDE：Pycharm
## 前端项目使用
#### 安装依赖包
输入命令：  
```    
npm install
```   
#### 项目运行
在安好依赖包后，输入命令：      
``` 
npm run dev
```
#### 项目打包（非必要）
在安好依赖包后，输入命令： 
```
 npm run build
```
## 项目目录结构介绍
项目树形结构图如下：  
```
    bookstore_vue    
    ├─.idea     
    │   └─inspectionProfiles     
    ├─node_modules      
    └─src   
      ├─api     
      ├─assets     
      │   ├─css          
      │   └─img     
      ├─components     
      ├─router     
      ├─store     
      ├─utils     
      └─views   
```
### .idea
 Pycharm运行项目自动生成的相关配置文件    
### node_modules
 前端项目的依赖包集合
### src 
  关键文件夹，内包括页面组件以及前后端交互组件。具体见下。
<ul>
<li>
    <h4>api</h4><br>
        api文件夹内均为ts文件，内含前端页面所需的函数，便于后续调用
    </li>
    <li>
    <h4>assets</h4><br>
        assets文件夹为前端项目的静态资源，里面提供了可使用的css样式和图片Img资源。
    </li>
    <li>
    <h4>components</h4><br>
        components文件夹为前端页面的子组件，被调用后，可以供views文件夹内父组件使用（包括样式和方法）。
    </li>
    <li>
    <h4>router</h4><br>
        router文件夹内的index.ts对前端所有页面路由进行了声明，便于后续使用。
    </li>
<li>
    <h4>store</h4><br>
        store文件夹内的ts、js文件包含处理函数，供页面组件使用。
    </li>
<li>
    <h4>utils</h4><br>
        utils文件夹内的request.ts使用了axios函数，构建了通用的前后端交互接口函数，供页面组件调用。
    </li>
<li>
    <h4>views</h4><br>
        views文件夹内为前端的所有页面组件，每个组件包括template,css,ts三个部分，结合调用内容，构建具体的网页和处理函数。
    </li>
</ul>
&emsp;&emsp;组件与页面对应关系如下：

|         组件          | 网页              |    
|:-------------------:|-----------------|      
|      home.vue       | 线上书店的首页         |      
|     Basket.vue      | 购物车界面，可查看、删除、支付 |       
| AdvancedSearch.vue  | 高级搜索界面，可多条件查询书籍 |         
|   BookBrowser.vue   | 书籍浏览，含简单分类      |    
|      login.vue      | 用户登录界面          |
|    register.vue     | 用户注册界面          |
| usercollections.vue | 用户收藏夹页面         |
|    UserInfo.vue     | 个人中心页面          |
### book_store/内的剩余文件
 package.json主要用于运行配置，例如修改前端服务器启动ip       
 components.d.ts用于声明前端的一些组件，便于其它文件调用        
 其余为一些环境配置文件，不做过多介绍