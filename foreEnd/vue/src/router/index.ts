import {createRouter, createWebHashHistory, RouteRecordRaw} from 'vue-router';
import home from '../views/home.vue';

const routes: RouteRecordRaw[] = [
    {
        path: '/',
        redirect: '/login',
    },
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
                component: () => import(/* webpackChunkName: "dashboard" */ '../views/HelloWorld.vue'),
            },
        ],
    },
    {
        path: '/login',
        name: 'login',
        meta: {
            title: '登录',
        },
        component: () => import(/* webpackChunkName: "login" */ '../views/login.vue'),
    },
    {
        path: '/403',
        name: '403',
        meta: {
            title: '没有权限',
        },
        component: () => import(/* webpackChunkName: "403" */ '../views/403.vue'),
    },
];

const router = createRouter({
    history: createWebHashHistory(),
    routes,
});

router.beforeEach((to, from, next) => {
    document.title = `${to.meta.title} | bookStore`;
    const role = localStorage.getItem('ms_username');
    if (!role && to.path !== '/login') {
        next('/login');
    } else {
        next();
    }
});

export default router;
