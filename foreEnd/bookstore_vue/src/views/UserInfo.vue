<template>
    <div>
        <v-Header ref="headerRef" :pageId="pageId"/>
        <div class="InfoBox">
            <el-card class="box-card">
                <template #header>
                    <div class="card-header">
                        <span style="font-weight: bold; font-size: 20px;margin-left: 417px;">个人信息</span>
                    </div>
                </template>
                <div class="flex-container">
                    <div class="left-panel">
                        <img src="../assets/img/user.jpg">
                    </div>
                    <div class="right-panel">
                        <div class="unit-input" style="margin-top: 10px">
                            <span class="left-input">用户名：</span>
                            <span class="right-input">{{ userdata.name }}</span>
                        </div>
                        <div class="unit-input">
                            <span class="left-input">电话：</span>
                            <span class="right-input">{{ userdata.phoneNumber }}</span>
                        </div>
                        <div class="unit-input">
                            <span class="left-input">地址：</span>
                            <span class="right-input">{{ userdata.address }}</span>
                        </div>
                    </div>
                </div>
                <!--    <div v-for="o in 4" :key="o" class="text item">{{ 'List item ' + o }}</div>-->
            </el-card>
            <div class="bottom-section">
                <div class="home-child">
                    <a @click="toAdvancedSearch">
                        <p><img src="../assets/img/user.jpg"></p>
                        <p>高级搜索</p>
                    </a>
                </div>
                <div class="home-child">
                    <a @click="toUserBookList">
                        <p><img src="../assets/img/user.jpg"></p>
                        <p>个人书单</p>
                    </a>
                </div>
                <div class="home-child">
                    <a @click="toBasket">
                        <p><img src="../assets/img/basket.png"></p>
                        <p>购物车</p>
                    </a>
                </div>
                <div class="home-child">
                    <a>
                        <p><img src="../assets/img/user.jpg"></p>
                        <p>历史记录</p>
                    </a>
                </div>
            </div>
        </div>
    </div>
</template>

<script setup lang="ts">
import vHeader from '../components/header.vue';
import {onMounted, reactive, ref} from "vue";
import {useRouter} from 'vue-router';
import homeImg from "../assets/img/home-bg.png";

const router = useRouter()
const pageId = ref('6')
const headerRef = ref(null)
const username: string | null = localStorage.getItem('ms_username');

interface UserData {
    name: string | null,
    phoneNumber: string,
    address: string,
}

const userdata = reactive<UserData>({
    name: localStorage.getItem('ms_username'),
    phoneNumber: '123456789',
    address: 'beihang',
})
onMounted(() => {
    console.log(headerRef.value?.selected)
})

const toAdvancedSearch = () => {
    router.push({
        path: '/AdvancedSearch',
        query: {},
    })
}

const toBasket = () => {
    router.push({
        path: '/Basket',
        query: {},
    })
}
const toUserBookList = () => {
    router.push({
        path: '/UserBookList',
        query: {},
    })
}
</script>

<style scoped>
.InfoBox {
    position: absolute;
    left: 50px;
    right: 50px;
    top: 135px;
    width: 1000px;
    height: 1050px;
    margin: 0 auto;
    padding-top: 10px;
    padding-bottom: 30px;
    -webkit-transition: left .3s ease-in-out;
    transition: left .3s ease-in-out;
    background: #ffffff;
}

.left-panel {
    flex: auto;
    display: block;
    border-radius: 1px;
    border: 1px lightgray;
    width: 35%;
    margin-left: 8%;
}

.right-panel {
    flex: auto;
    display: block;
    width: 50%;
    height: 200px;
}

.flex-container {
    display: flex;
    margin-top: 20px;
}

.unit-input {
    margin-bottom: 40px;
}

.left-input {
    display: inline-block;
    font-weight: bolder;
    font-size: 20px;
    width: 100px;
}

.right-input {
    display: inline-block;
    font-weight: lighter;
    margin-left: 20%;
    font-size: 20px;
}

.bottom-section {
    display: flex;
    justify-content: center;
    width: 100%;
    height: 300px;
    margin-top: 42px;
    margin-bottom: 100%;
}

.home-child {
    width: 25%;
    height: 60%;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    box-shadow: lightgray 0 0 10px;
    border-radius: 5px;
    margin-right: 7%; /* 添加右侧的外边距 */
    margin-top: 1%;
    background-color: rgba(255, 255, 255, 1);
    text-align: center; /* 让内容居中 */
}

.home-child:last-child {
    margin-right: 0;
}

.home-child a {
    color: #000000;
}

.home-child p {
    padding-top: 10%;
    font-size: 18px;
}

.home-child p img {
    width: 85px;
    height: 85px;
}

</style>