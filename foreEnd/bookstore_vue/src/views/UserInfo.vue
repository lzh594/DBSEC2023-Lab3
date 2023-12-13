<template>
  <div style="height: 100%">
    <v-Header ref="headerRef" :pageId="pageId"/>
    <div class="LeftBox">
      <el-card class="box-card">
        <template #header>
          <div class="card-header">
            <span style="font-weight: bold; font-size: 20px;margin-left: 38%;">个人信息</span>
          </div>
        </template>
        <div class="flex-container">
          <div class="left-panel">
            <div class="unit-input">
              <span class="left-input" style="">头像：</span>
              <img src="../assets/img/user.jpg" style="width:30%;display: inline-block;  margin-left:15%;">
            </div>
            <div class="unit-input top-justify">
              <span class="left-input">用户名：</span>
              <span class="right-input">{{ userdata.name }}</span>
            </div>
            <div class="unit-input top-justify">
              <span class="left-input">电话：</span>
              <span class="right-input">{{ userdata.phoneNumber }}</span>
            </div>
            <div class="unit-input top-justify">
              <span class="left-input">邮箱：</span>
              <span class="right-input">{{ userdata.email }}</span>
            </div>
            <div class="unit-input top-justify">
              <span class="left-input">地址：</span>
              <span class="right-input">{{ userdata.address }}</span>
            </div>
          </div>
        </div>
      </el-card>
    </div>
    <div class="rightBox">
      <div class="right-top-box">
        <el-card class="box-card">
          <template #header>
            <div class="card-header">
              <span style="font-weight: bold;font-size: 18px">收藏书单</span>
              <el-button type="primary" style="margin-left: 75%" @click="toUserBookStore">
                <el-icon>
                  <ArrowRight/>
                </el-icon>
                收藏夹
              </el-button>
            </div>
          </template>
          <div>
            <el-table :data="collectionList" stripe style="width: 100%;height:160px;">
              <el-table-column prop="bname" label="书名" width="160%"/>
              <el-table-column prop="author" label="作者" width="160%"/>
              <el-table-column prop="pname" label="出版社" width="160%"/>
              <el-table-column prop="pub_year" label="出版日期"/>

            </el-table>
          </div>
        </el-card>
      </div>
      <div class="right-bottom-box">
        <el-card class="box-card">
          <template #header>
            <div class="card-header">
              <span style="font-weight: bold;font-size: 18px">书籍浏览历史</span>
            </div>
          </template>
          <div>
            <el-table :data="shoppingHistoryList" stripe style="width: 100%;height:160px;">
              <el-table-column prop="bname" label="书名" width="100%"/>
              <el-table-column prop="price" label="单价" width="100%"/>
              <el-table-column prop="amount" label="数量" width="100%"/>
              <el-table-column prop="buy_date" label="日期"/>
            </el-table>
          </div>
        </el-card>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import vHeader from '../components/header.vue';
import {onMounted, reactive, ref} from "vue";
import {useRouter} from 'vue-router';
import homeImg from "../assets/img/home-bg.png";
import {requestData} from "../api";

const router = useRouter()
const pageId = ref('6')
const headerRef = ref(null)
const username: string | null = localStorage.getItem('ms_username');

interface UserData {
  name: string | null,
  phoneNumber: string,
  email: string,
  address: string,
}

const userdata = reactive<UserData>({
  name: localStorage.getItem('ms_username'),
  phoneNumber: '',
  email: '',
  address: 'beihang',
})
onMounted(() => {
  let uid = localStorage.getItem('ms_uid')
  let UserReadRequest = {
    url: 'users/' + uid + '/',
    method: 'get',
    query: {},
  }
  requestData(UserReadRequest)!.then(res=>{
    userdata.phoneNumber = res.data['tel']
    userdata.email = res.data['email']
    if (res.data['address'] != undefined){
       userdata.address = res.data['address']
    }

  })
})



const toUserBookStore = () => {
  router.push({
    path: '/usercollections',
    query: {},
  })
}

interface collectionUnit {
  book_id: string,
  bname: string,
  author: string,
  category: string,
  price: string,
  pub_year: string,
  pname: string,
  rate: string,
  ImgAddress: string,
}

interface shoppingHistoryUnit {
  book_id: string,
  bname: string,
  author: string,
  category: string,
  price: string,
  pub_year: string,
  pname: string,
  rate: string,
  ImgAddress: string,
  buy_date: string,
  amount: string,
}

const collectionList = reactive<collectionUnit[]>([])

const shoppingHistoryList = reactive<shoppingHistoryUnit[]>([])
onMounted(() => {
  let uid = localStorage.getItem('ms_uid')
  let collectionRequest = {
    url: 'collection/custom_filter/',
    method: 'get',
    query: {
      'user_id': uid
    },
  }
  console.log(uid)
  requestData(collectionRequest)!.then(res => {
    for (let item of res.data) {
      collectionList.push({
        book_id: item['book']['book_id'],
        bname: item['book']['bname'],
        author: item['book']['author']['aname'],
        category: item['book']['category']['category_name'],
        price: item['book']['price'],
        pub_year: item['book']['pub_year'],
        pname: item['book']['publisher']['pname'],
        rate: item['book']['rate'],
        ImgAddress: item['book']['url'],
      })
    }
  });
  let ShoppingHistoryRequest = {
    url: 'shoppinghistory/custom_filter/',
    method: 'get',
    query: {
      'user_id': uid
    },
  }
  requestData(ShoppingHistoryRequest)!.then(res => {
    console.log(res.data)
    for (let item of res.data) {
      shoppingHistoryList.push({
        book_id: item['book']['book_id'],
        bname: item['book']['bname'],
        author: item['book']['author']['aname'],
        category: item['book']['category']['category_name'],
        price: item['book']['price'],
        pub_year: item['book']['pub_year'],
        pname: item['book']['publisher']['pname'],
        rate: item['book']['rate'],
        ImgAddress: item['book']['url'],
        buy_date: item['date'],
        amount: item['amount']
      })
    }
  });
})
</script>

<style scoped>
.LeftBox {
  display: inline-block;
  margin-top: 2%;
  width: 30%;
  margin-left: 7%;
  padding-top: 10px;
  padding-bottom: 30px;
  -webkit-transition: left .3s ease-in-out;
  transition: left .3s ease-in-out;
  background: #ffffff;
}

.flex-container {
  display: block;
  margin-top: 20px;
}

.unit-input {
  margin-bottom: 30px;
}

.top-justify {
  margin-top: 50px;
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

.rightBox {
  display: inline-block;
  margin-left: 10%;
  width: 47%;
}

.right-bottom-box {
  margin-top: 5%;
}
</style>