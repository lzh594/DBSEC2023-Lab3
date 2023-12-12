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
        meta: {
            title: '首页',
        },
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
    {
        path: '/AdvancedSearch',
        name: 'AdvancedSearch',
        meta: {
            title: '高级搜索',
        },
        component: () => import(/* webpackChunkName: "403" */ '../views/AdvancedSearch.vue'),
    },
    {
        path: '/SellRanking',
        name: 'SellRanking',
        meta: {
            title: '畅销排行榜',
        },
        component: () => import(/* webpackChunkName: "403" */ '../views/SellRanking.vue'),
    },
    {
        path: '/BookBrowser',
        name: 'BookBrowser',
        meta: {
            title: '书籍浏览',
        },
        component: () => import(/* webpackChunkName: "403" */ '../views/BookBrowser.vue'),
    },
    {
        path: '/usercollections',
        name: 'usercollections',
        meta: {
            title: '个人收藏夹',
        },
        component: () => import(/* webpackChunkName: "403" */ '../views/usercollections.vue'),
    },
    {
        path: '/UserInfo',
        name: 'UserInfo',
        meta: {
            title: '个人中心',
        },
        component: () => import(/* webpackChunkName: "403" */ '../views/UserInfo.vue'),
    },
    {
        path: '/Basket',
        name: 'Basket',
        meta: {
            title: '购物车',
        },
        component: () => import(/* webpackChunkName: "403" */ '../views/Basket.vue'),
    },
    {
        path: '/register',
        name: 'register',
        meta: {
            title: '注册',
        },
        component: () => import(/* webpackChunkName: "403" */ '../views/register.vue'),
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
