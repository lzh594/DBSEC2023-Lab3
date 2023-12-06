<template>
    <div>
      <div class="header">
        <div class="logo">
           <el-image style="width: 150px; height: 40px;margin-top: 15px" :src="logoImg" :fit="'contain'"/>
        </div>

        <div class="search">
          <select v-model="selected" class="header-select">
            <option disabled value="">Please select one</option>
            <option>书名</option>
            <option>作者</option>
            <option>出版社</option>
            <option>书单</option>
          </select>
          <input  type="text" class="searchInput" placeholder="">
          <span>搜索</span>
        </div>
        <div class="header-right">
           <div class="header-user-con">
               <!-- 用户头像 -->
               <el-avatar v-if="identity==='1'" class="user-avator" :size="30" :src="userImg" style="background-color: white"/>
               <el-avatar v-else class="user-avator" :size="30" :src="orgImg"/>
               <!-- 用户名下拉菜单 -->
               <el-dropdown class="user-name" trigger="click" @command="handleCommand">
                 <span class="el-dropdown-link">
                   {{ username }}
                 </span>
               </el-dropdown>
           </div>
           <a  class="basket_a" @click="toBasket">
             <span style="color: rgb(0, 70, 145)" >购物车</span>
             <span>
                <img src="../assets/img/basket.png" height="35">
             </span>
           </a>
      </div>
    </div>
      <nav>
        <div v-if="pageId == '1'" class="el-menu-item currentPage" @click="toHome">首页</div>
        <div v-else class="el-menu-item" @click="toHome">首页</div>
        <div v-if="pageId == '2'" class="el-menu-item currentPage" @click="toAdvancedSearch">高级搜索</div>
        <div v-else class="el-menu-item" @click="toAdvancedSearch">高级搜索</div>
        <div v-if="pageId == '3'" class="el-menu-item currentPage" @click="toSellRanking">畅销排行榜</div>
        <div v-else class="el-menu-item" @click="toSellRanking">畅销排行榜</div>
        <div v-if="pageId == '4'" class="el-menu-item currentPage" @click="toBookBrowser">书籍浏览</div>
        <div v-else class="el-menu-item" @click="toBookBrowser">书籍浏览</div>
        <div v-if="pageId == '5'" class="el-menu-item currentPage" @click="toUserBookList">个性化书单</div>
        <div v-else class="el-menu-item" @click="toUserBookList" >个性化书单</div>
        <div v-if="pageId == '6'" class="el-menu-item currentPage" @click="toUserInfo">个人中心</div>
        <div v-else class="el-menu-item" @click="toUserInfo">个人中心</div>
      </nav>
    </div>
</template>
<script setup lang="ts">
import { ref } from 'vue'
import {onMounted} from 'vue';
import {useSidebarStore} from '../store/sidebar';
import {useRouter} from 'vue-router';
import userImg from '../assets/img/user.jpg';
import orgImg from '../assets/img/org.jpg';
import logoImg from '../assets/img/logo.png';
import {ArrowDown, Expand, Fold} from "@element-plus/icons-vue";

const username: string | null = localStorage.getItem('ms_username');
const identity = localStorage.getItem('ms_identity');

const sidebar = useSidebarStore();

defineProps<{ pageId: string }>()
// 侧边栏折叠
const collapseChage = () => {
    sidebar.handleCollapse();
};
const toHome=()=>{
  router.push({
    path: '/home',
    query: {},
  })
}
const toAdvancedSearch=()=>{
  router.push({
    path: '/AdvancedSearch',
    query: {},
  })
}

const toSellRanking=()=>{
  router.push({
    path: '/SellRanking',
    query: {},
  })
}

const toBookBrowser=()=>{
  router.push({
    path: '/BookBrowser',
    query: {},
  })
}

const toUserInfo=()=>{
  router.push({
    path: '/UserInfo',
    query: {},
  })
}

const toBasket=()=>{
  router.push({
    path: '/Basket',
    query: {},
  })
}
const toUserBookList=()=>{
  router.push({
    path: '/UserBookList',
    query: {},
  })
}

const selected = ref('书名')

defineExpose({
  selected,
});

onMounted(() => {
    if (document.body.clientWidth < 1500) {
        collapseChage();
    }
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


.search{
  width: 40%;
  background-color: rgb(0, 70, 145);
  display: inline-flex;
  align-items: center;
  margin-top: 17px;
  height: 40px;
}
.header-select{
  height: 36px;
  margin-left: 1px;
  text-align: center;
  font-size: 17px;
  font-family: "微软雅黑 Light";
  font-weight: 600;
  background-color: #F1F1F1FF;
}
.header .search span{
  width: 25%;
  height: 35px;
  font-size: 18px;
  line-height: 40px;
  text-align: center;
  color: #ffffff;
}
.searchInput{
  width: 70%;
  height: 36px;
  line-height: 2rem;
  border: #004691 2px solid;
  text-align: center;
  font-size: 18px;
}
nav {
  display: inline-flex;
  border-bottom: solid 1px;
  border-bottom-color: darkgray;
  border-top: solid 1px;
  border-top-color: darkgray;
}
nav .el-menu-item {
  color: #000000;
  padding-left: 90px;
  padding-right: 90px;
  height: 35px;
  position: relative;
  text-align: center;
  border-bottom: transparent;
  display: flex;
  transition: 0.4s;
  font-size: 16px;
  font-weight: bold;
}
nav .el-menu-item:hover {
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
    line-height: 70px;
    margin-right: 160px;
    margin-left: 20px;
}

.header-right {
    float: right;
    padding-right: 50px;
    display: flex;
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
    margin-left: 20px;
}

.el-dropdown-link {
    color: rgb(0, 70, 145);
    cursor: pointer;
    display: flex;
    align-items: center;
}

.basket_a{
  display: flex;
  margin-left: 20px;
}

.basket_a span{
  font-size: 23px;
}
.basket_a img{
  margin-top: 15px;
  margin-left: 10px;
}

nav .currentPage{
  border-bottom: solid 3px;
  border-bottom-color: rgb(0, 70, 145);
}
</style>
