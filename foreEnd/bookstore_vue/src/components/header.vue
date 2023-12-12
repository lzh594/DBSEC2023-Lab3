<template>
  <div class="header">
    <div class="logo">
      <el-image style="width: 150px; height: 40px;margin-top: 15px" :src="logoImg" :fit="'contain'"/>
    </div>


    <div class="header-right">
      <a class="basket_a" @click="toBasket">
            <span>
                <img src="../assets/img/basket.png" style="margin-right: 7px" height="35">
             </span>
        <span style="color: rgb(0, 70, 145)">购物车</span>
      </a>
      <div class="header-user-con">
        <!-- 用户头像 -->
        <el-avatar v-if="identity==='1'" class="user-avator" :size="30" :src="userImg" style="background-color: white"/>
        <el-avatar v-else class="user-avator" :size="30" :src="orgImg"/>
        <!-- 用户名下拉菜单 -->
        <el-dropdown class="user-name" trigger="click" @command="handleCommand">
                 <span class="el-dropdown-link">
                   {{ username }}
                   <el-icon class="el-icon--right">
                    <arrow-down/>
                  </el-icon>
                 </span>
          <template #dropdown>
            <el-dropdown-menu>
              <el-dropdown-item @click="toUserInfo">个人中心</el-dropdown-item>
              <el-dropdown-item @click="toUserBookStore">收藏夹</el-dropdown-item>
            </el-dropdown-menu>
          </template>
        </el-dropdown>
      </div>

    </div>
  </div>
  <nav>
    <ul>
      <li v-if="pageId == '1'" class=" currentPage" @click="toHome">首页</li>
      <li v-else class="" @click="toHome">首页</li>
      <li v-if="pageId == '2'" class=" currentPage" @click="toAdvancedSearch">高级搜索</li>
      <li v-else class="" @click="toAdvancedSearch">高级搜索</li>
      <li v-if="pageId == '4'" class=" currentPage" @click="toBookBrowser">书籍浏览</li>
      <li v-else class="" @click="toBookBrowser">书籍浏览</li>
      <li v-if="pageId == '5'" class=" currentPage" @click="toUserBookStore">收藏夹</li>
      <li v-else class="" @click="toUserBookStore">收藏夹</li>
      <li v-if="pageId == '6'" class=" currentPage" @click="toUserInfo">个人中心</li>
      <li v-else class="" @click="toUserInfo">个人中心</li>
    </ul>
  </nav>
</template>
<script setup lang="ts">
import {ref} from 'vue'
import {onMounted} from 'vue';

import {useRouter} from 'vue-router';
import userImg from '../assets/img/user.jpg';
import orgImg from '../assets/img/org.jpg';
import logoImg from '../assets/img/logo.png';
import {ArrowDown, Expand, Fold} from "@element-plus/icons-vue";

const username: string | null = localStorage.getItem('ms_username');
const identity = localStorage.getItem('ms_identity');



defineProps<{ pageId: string }>()
// 侧边栏折叠

const toHome = () => {
  router.push({
    path: '/home',
    query: {},
  })
}
const toAdvancedSearch = () => {
  router.push({
    path: '/AdvancedSearch',
    query: {},
  })
}

const toSellRanking = () => {
  router.push({
    path: '/SellRanking',
    query: {},
  })
}

const toBookBrowser = () => {
  router.push({
    path: '/BookBrowser',
    query: {},
  })
}

const toUserInfo = () => {
  router.push({
    path: '/UserInfo',
    query: {},
  })
}

const toBasket = () => {
  router.push({
    path: '/Basket',
    query: {},
  })
}
const toUserBookStore = () => {
  router.push({
    path: '/usercollections',
    query: {},
  })
}

const selected = ref('书名')

defineExpose({
  selected,
});


// 用户名下拉菜单选择事件
const router = useRouter();
const handleCommand = (command: string) => {
  if (command == 'loginout') {
    localStorage.removeItem('ms_username');
    router.push('/login');
  } else if (command == 'user') {
    router.push('/user');
  }
};

</script>
<style scoped>
.header {
  position: relative;
  box-sizing: border-box;
  width: 100%;
  height: 70px;
  font-size: 22px;
  background-color: #ffffff;
}


.search {
  width: 40%;
  background-color: rgb(0, 70, 145);
  display: inline-flex;
  align-items: center;
  margin-top: 17px;
  height: 40px;
}

.header-select {
  height: 36px;
  margin-left: 1px;
  text-align: center;
  font-size: 17px;
  font-family: "微软雅黑 Light";
  font-weight: 600;
  background-color: #F1F1F1FF;
}

.header .search span {
  width: 25%;
  height: 35px;
  font-size: 18px;
  line-height: 40px;
  text-align: center;
  color: #ffffff;
}

.searchInput {
  width: 70%;
  height: 36px;
  line-height: 2rem;
  border: #004691 2px solid;
  text-align: center;
  font-size: 18px;
}

nav {
  width: 100%;
  flex: 100%;
  height: 35px;
  display: flex;
  border-bottom: solid 1px;
  border-bottom-color: darkgray;
  border-top: solid 1px;
  border-top-color: darkgray;
}

nav ul {
  padding-bottom: 0;
  list-style-type: none;
  flex: 2;
  display: flex;

}

nav ul li {
  padding-top: 4px;
  display: inline;
  text-align: center;
  font-size: 18px;
  font-weight: bold;
  flex: 1;
}

nav ul li:hover {
  background-color: lightgray;
  border-bottom: solid 3px;
  border-bottom-color: rgb(0, 70, 145);
}

.header span {
  float: right;
  line-height: 70px;
  font-weight: bolder;
  font-size: 26px;
}

.header .logo {
  float: left;
  width: 270px;
  height: 70px;
  line-height: 70px;
  margin-right: 160px;
  margin-left: 20px;
}

.header-right {
  float: right;
  padding-right: 50px;
  display: flex;
  height: 70px;
}

.header-user-con {
  display: flex;
  height: 70px;
  align-items: center;
}

.user-name {
  margin-left: 10px;
}

.user-avator {
  margin-left: 10px;
}

.el-dropdown-link {
  color: rgb(0, 70, 145);
  cursor: pointer;
  display: flex;
  align-items: center;
}

.basket_a {
  display: flex;
  margin-bottom: 10px;
  margin-left: 20px;
}

.basket_a span {
  font-size: 23px;
}

.basket_a img {
  margin-top: 15px;
  margin-left: 10px;
}

nav .currentPage {
  border-bottom: solid 3px;
  border-bottom-color: rgb(0, 70, 145);
}
</style>
