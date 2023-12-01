# foreEnd-vue+vite+ts

> 本文档如有任何问题请联系刘征昊

## 目录结构

```
. vue
├── LICENSE
├── auto-imports.d.ts
├── components.d.ts
├── index.html
├── node_modules
├── package-lock.json
├── package.json
├── public
├── src
├── tsconfig.json
├── tsconfig.node.json
└── vite.config.ts
```

## 如何启动

```sh
# ./vue
npm run dev
```

+ 如果你是*nix：

    + 实际上先获取你主机ip，并将服务器启动在该ip上（package.json中可设置）

    ```sh
    vite --host $(ifconfig getifaddr en0)
    ```

+ 如果你是windows，请在package.json中手动设置：

    ```sh
    vite --host your_ipaddr
    ```

## src

```
. src
├── App.vue
├── api
│   └── index.ts
├── assets
│   ├── css
│   └── img
├── components
│   ├── header.vue
│   ├── sidebar.vue
│   └── tags.vue
├── main.ts
├── router
│   └── index.ts
├── store
│   ├── permiss.ts
│   ├── sidebar.ts
│   └── tags.ts
├── utils
│   └── request.ts
├── views
│   ├── 403.vue
│   ├── HelloWorld.vue
│   ├── home.vue
│   └── login.vue
└── vite-env.d.ts
```

+ ### router

    + #### 页面路由配置（都写在`const routes: RouteRecordRaw[] = [...];`中）

        + ##### 一级页面：home、login、403（404）... 

            ```typescript
            const routes: RouteRecordRaw[] = [
            	// 根目录重定向到登录界面    
                {
                    path: '/',
                    redirect: '/login',
                },
                // 登录界面url
                {
                    path: '/login',
                    name: 'Login',
                    meta: {
                        title: '登录',
                    },
                    component: () => import( '../views/login.vue'),
                },
            ];
            ```

        + ##### 二级页面：home/dashboard、home/search ...

            ```typescript
            const routes: RouteRecordRaw[] = [
            	// 主页面url，需要构建home.vue（构筑header、sidebar、tags等基础组建的页面）    
            	{
                    path: '/home',
                    name: 'home',
                    component: home,
                    children: [
                        {
                            path: '/HelloWorld',
                            name: 'HelloWorld',
                            meta: {
                                title: 'HelloWorld',
                            },
                            component: () => import('../views/HelloWorld.vue'),
                        },
                    ],
                },
            ];
            ```
    
+ ### utils/request.ts

    + #### 建立了axios实例service：

        ```typescript
        const service: AxiosInstance = axios.create({
            baseURL: "http://10.192.148.240:8000/bookStore",
            timeout: 5000
        });
        ```

    + ####  实例提供给api/index.ts调用

+ ### api/index.ts

    + #### 建立axios的http请求api：requestData

        ```typescript
        export function requestData(     {url, method, query}: RequestDataParams): Promise<AxiosResponse<any, any>> | undefined
        ```

    + #### usage-axios[官方文档](https://axios-http.com/zh/docs/intro)：

        + ##### 请求数据体接口定义

            ```typescript
            interface RequestDataParams {
                url: string;
                method: string;
                query: any;
            }
            ```

        + ##### 任意前端界面文件：func.vue

            + 创建请求体变量：参数可初始化时指定，也可以后续赋值

                ```typescript
                const request = reactive({
                    url: '',
                    method: '',
                    query: {}
                })
                ```

            + 设请求发送函数为：funcData，其可调用axios的api：

                ```typescript
                const funcData = () => {
                    request.url = '/backend_page_url/';
                	// 注意“/”前后都有，backend_page_url是后端某view的相对路径
                    // eg: request.url = '/func/';
                    request.method = 'post'
                    // 可以初始化时指定
                    request.query = funcQuery;
                	// funcQuery为json变量，请求体的具体参数
                    console.log(funcQuery)
                    requestData(request)!.then(res => {
                		// do something，eg：
                   	 	console.log(res.data)
                        // 发送请求后得到后端的http响应体在res里
                        //响应体的具体数据在res.data中
                    });
                }
                ```

+ ### components

    + #### 存放header、sidebar和tags

        ```typescript
        . components
        ├── header.vue
        ├── sidebar.vue
        └── tags.vue
        ```

+ ### views

    + #### 存放各个页面vue

        ```typescript
        . views
        ├── test.vue // 没用，占位文件
        ├── 404.vue //以下页面待设计
        ├── ...
        └── dashboard.vue
        ```

        