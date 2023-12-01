<template>
    <div class="sidebar">
        <el-menu
            class="sidebar-el-menu"
            :default-active="onRoutes"
            :collapse="sidebar.collapse"
            background-color="#324157"
            text-color="#bfcbd9"
            active-text-color="#20a0ff"
            unique-opened
            router
        >
            <template v-for="(item, index) in items">
                <template
                    class="item"
                    v-if="identity === '1' && (item.index !== '/intersection')">
                    <el-menu-item :index="item.index" :key="item.index" style="margin-bottom: 20px">
                        <el-icon size="28">
                            <component :is="item.icon"></component>
                        </el-icon>
                        <div v-if="sidebar.collapse===false" class="side-font">{{ item.title }}</div>
                    </el-menu-item>
                </template>
            </template>
        </el-menu>
    </div>
</template>

<script setup lang="ts">
import {computed} from 'vue';
import {useSidebarStore} from '../store/sidebar';
import {useRoute} from 'vue-router';

const items = [
    {
        icon: 'Odometer',
        index: '/HelloWorld',
        title: 'HelloWorld',
    },
    {
        icon: 'Edit',
        index: '/403',
        title: ' 403',
    },
];

const route = useRoute();
const onRoutes = computed(() => {
    return route.path;
});

const sidebar = useSidebarStore();
const identity = localStorage.getItem('ms_identity')
</script>

<style scoped>
.side-font {
    display: block;
    margin: 0 auto;
    font-size: 40px;
}

.sidebar {
    display: block;
    position: absolute;
    left: 0;
    top: 70px;
    bottom: 0;
    overflow-y: scroll;
    font-size: 120px;
}

.sidebar::-webkit-scrollbar {
    width: 0;
}

li {
    font-size: 28px;
    font-weight: bolder;
    font-family: "宋体", serif;
}

.sidebar-el-menu:not(.el-menu--collapse) {
    width: 250px;
}

.sidebar > ul {
    height: 100%;
}
</style>