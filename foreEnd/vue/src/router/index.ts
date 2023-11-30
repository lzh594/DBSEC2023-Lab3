import { createRouter, createWebHashHistory, RouteRecordRaw } from 'vue-router';
import Home from '../views/home.vue';

const routes: RouteRecordRaw[] = [
    {
        path: '/',
        redirect: '/login',
    },
    {
        path: '/home',
        name: 'Home',
        component: Home,
        children: [
            {
                path: '/dashboard',
                name: 'dashboard',
                meta: {
                    title: '系统首页',
                },
                component: () => import(/* webpackChunkName: "dashboard" */ '../views/dashboard.vue'),
            },
        ],
    },
    {
        path: '/login',
        name: 'Login',
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
    {
        path: '/404',
        name: '404',
        meta: {
            title: '知识荒原',
        },
        component: () => import(/* webpackChunkName: "403" */ '../views/404.vue'),
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
    }else {
        next();
    }
});

export default router;
