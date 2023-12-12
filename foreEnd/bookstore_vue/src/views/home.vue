<template>
  <div class="MainBox" style="height: 100%">
    <el-scrollbar height="100%">
      <el-backtop target=".MainBox .el-scrollbar__wrap" :bottom="20">
        <div
            style="
               height: 100%;
               width: 100px;
               background-color: var(--el-bg-color-overlay);
               box-shadow: var(--el-box-shadow-lighter);
               text-align: center;
               line-height:40px;
               color: #1989fa;
               border-radius: 2px;
               font-size: 16px;
             "
        >
          顶部
        </div>
      </el-backtop>
      <v-header ref="headerRef" :pageId="pageId"/>
      <div class="content-box">
        <div class="home-bg">
          <el-image class="homeimg" :src="homeImg"/>
        </div>
        <div class="title-line">
          <span>随机推荐</span>
        </div>
        <div class="box" style="margin-top: 20px">
          <div class="unit-box" v-for="item in randList1" @click="ShowDetail(item)">
            <el-image class="boxImg" :src="item.url"/>
            <span class="boxTitle">{{ item.bname }}</span>
            <span class="boxPrice">{{ item.price }}</span>
          </div>
        </div>

        <div class="box">
          <div class="unit-box" v-for="item in randList2" @click="ShowDetail(item)">
            <el-image class="boxImg" :src="item.url"/>
            <span class="boxTitle">{{ item.bname }}</span>
            <span class="boxPrice">{{ item.price }}</span>
          </div>
        </div>

        <div class="box">
          <div class="unit-box" v-for="item in randList3" @click="ShowDetail(item)">
            <el-image class="boxImg" :src="item.url"/>
            <span class="boxTitle">{{ item.bname }}</span>
            <span class="boxPrice">{{ item.price }}</span>
          </div>
        </div>
        <el-dialog v-model="BookVisible" title="书籍信息" style="width: 80%;text-align: center">
          <div class="left-dialog">
            <el-image style="margin-top:20%;max-width:250px;object-fit: contain" :src=ShowingBook.ImgAddress></el-image>
            <div style="margin-top: 50px;font-size: 20px;">
              <span>书籍图片参考</span>
            </div>
          </div>
          <div class="right-dialog">
            <div class="unit-description">
              <span class="des-label">书名</span>
              <span class="des-content">{{ ShowingBook.name }}</span>

            </div>
            <div class="unit-description">
              <span class="des-label">作者</span>
              <span class="des-content">{{ ShowingBook.author }}</span>

            </div>
            <div class="unit-description">
              <span class="des-label">类型</span>
              <span class="des-content">{{ ShowingBook.type }}</span>

            </div>
            <div class="unit-description">
              <span class="des-label">出版社</span>
              <span class="des-content">{{ ShowingBook.name }}</span>

            </div>
            <div class="unit-description">
              <span class="des-label">出版年</span>
              <span class="des-content">{{ ShowingBook.date }}</span>

            </div>
            <div class="unit-description">
              <span class="des-label">书籍评分</span>
              <span class="des-content">{{ ShowingBook.rate }}</span>

            </div>
            <div class="unit-description">
              <span class="des-label">单价</span>
              <span class="des-content">{{ ShowingBook.price }}</span>

            </div>
            <div class="unit-description">
              <span class="des-label" style="margin-top: 5px">购买数量</span>
              <span class="des-content">
                          <div>

                          <el-input v-model="ShowingBook.buyNumber" style="width: 50px;vertical-align:middle;
                          border-radius: 0 " @change="ShowWarning"/>
                            <el-icon style="vertical-align:middle;border-radius:50%;border: 1px solid #d5d5d5;
                            margin-left: 8px;background-color: #d5d5d5" @click="addBuyNumber"><Plus/></el-icon>
                      <el-icon style="vertical-align:middle;border-radius:50%;border: 1px solid #d5d5d5;
                      margin-left: 5px;background-color: #d5d5d5" @click="deleteBuyNumber"><Minus/></el-icon>
                          </div>
                        </span>
            </div>
            <div v-if="showWarning" class="unit-description">
              <span class="des-content">购买数量必须大于1的整数</span>
            </div>
          </div>
          <div style="clear: both"></div>
          <template #footer>
                    <span class="dialog-footer">
                      <el-button @click="CacelUp">取消</el-button>
                      <el-button type="warning" :icon="Star" @click="addToCollections">收藏</el-button>
                      <el-button type="primary" @click="AddToBasket">
                        加入购物车
                      </el-button>
                    </span>
          </template>
        </el-dialog>
        <div style="height: 50px;margin-bottom: 30px">

        </div>
      </div>
    </el-scrollbar>
  </div>
</template>
<script setup lang="ts">
import vHeader from '../components/header.vue';
import homeImg from '../assets/img/home-bg.png'
import {onMounted, ref, reactive} from "vue";
import {requestData} from "../api";
import {Star} from "@element-plus/icons-vue";
import {ElMessage} from "element-plus";

const headerRef = ref(null)
const pageId = ref('1')
const BookVisible = ref(false)
const showWarning = ref(false)

interface book {
  book_id: string,
  author_id: string,
  aname: string,
  pub_id: string,
  pname: string,
  category_id: string,
  category_name: string,
  bname: string,
  price: string,
  pub_year: string,
  url: string,
  isbn: string,
  sales: string,
  rate: string,
}

const randList1 = reactive<book[]>([])
const randList2 = reactive<book[]>([])
const randList3 = reactive<book[]>([])

interface ShowBookData {
  id: string
  name: string,
  ImgAddress: string,
  author: string,
  publisher: string,
  date: string,
  price: number,
  buyNumber: number,
  type: string,
  rate: string,
}

const ShowingBook = reactive<ShowBookData>(
    {
      id: '',
      name: '',
      ImgAddress: '',
      author: '',
      publisher: '',
      date: '',
      price: 0,
      buyNumber: 1,
      type: '',
      rate: ''
    }
)


onMounted(() => {
  let Rand = Math.random();
  let rand_length = 12;
  let Min = 0;
  let Max = 20;
  let range = Max - Min;
  let rand_int = Min + Math.round(Rand * range)
  let rand_list1 = [rand_int, rand_int + 20, rand_int + 40, rand_int + 60]
  let rand_list2 = [rand_int + 80, rand_int + 100, rand_int + 120, rand_int + 140]
  let rand_list3 = [rand_int + 160, rand_int + 180, rand_int + 200, rand_int + 220]
  for (let i = 0; i < rand_list1.length; i++) {
    let readRequest = {
      url: 'books/' + rand_list1[i].toString() + '/',
      method: 'get',
      query: {},
    }
    requestData(readRequest)!.then((res) => {
      randList1.push({
        book_id: res.data['book_id'],
        pub_id: res.data['publisher']['pub_id'],
        bname: res.data['bname'],
        author_id: res.data['author']['author_id'],
        aname: res.data['author']['aname'],
        category_name: res.data['category']['category_name'],
        category_id: res.data['category']['category_id'],
        isbn: res.data['sales'],
        price: res.data['price'],
        pub_year: res.data['pub_year'],
        pname: res.data['publisher']['pname'],
        rate: res.data['rate'],
        url: res.data['url'],
        sales: res.data['sales'],
      })
    })
  }
  for (let i = 0; i < rand_list2.length; i++) {
    let readRequest = {
      url: 'books/' + rand_list2[i].toString() + '/',
      method: 'get',
      query: {},
    }
    requestData(readRequest)!.then((res) => {
      randList2.push({
        book_id: res.data['book_id'],
        pub_id: res.data['publisher']['pub_id'],
        bname: res.data['bname'],
        author_id: res.data['author']['author_id'],
        aname: res.data['author']['aname'],
        category_name: res.data['category']['category_name'],
        category_id: res.data['category']['category_id'],
        isbn: res.data['sales'],
        price: res.data['price'],
        pub_year: res.data['pub_year'],
        pname: res.data['publisher']['pname'],
        rate: res.data['rate'],
        url: res.data['url'],
        sales: res.data['sales'],
      })
    })
  }
  for (let i = 0; i < rand_list3.length; i++) {
    let readRequest = {
      url: 'books/' + rand_list3[i].toString() + '/',
      method: 'get',
      query: {},
    }
    requestData(readRequest)!.then((res) => {
      randList3.push({
        book_id: res.data['book_id'],
        pub_id: res.data['publisher']['pub_id'],
        bname: res.data['bname'],
        author_id: res.data['author']['author_id'],
        aname: res.data['author']['aname'],
        category_name: res.data['category']['category_name'],
        category_id: res.data['category']['category_id'],
        isbn: res.data['sales'],
        price: res.data['price'],
        pub_year: res.data['pub_year'],
        pname: res.data['publisher']['pname'],
        rate: res.data['rate'],
        url: res.data['url'],
        sales: res.data['sales'],
      })
    })
  }
})

const ShowDetail = (item: any) => {
  ShowingBook.id = item['book_id']
  ShowingBook.author = item['aname']
  ShowingBook.date = item['pub_year']
  ShowingBook.name = item['bname']
  ShowingBook.type = item['category_name']
  ShowingBook.buyNumber = 1
  ShowingBook.ImgAddress = item['url']
  ShowingBook.publisher = item['pname']
  ShowingBook.price = item['price']
  ShowingBook.rate = item['rate']
  BookVisible.value = true;
}

const CacelUp = () => {
  BookVisible.value = !BookVisible.value;
}
const ShowWarning = () => {
  const point: RegExp = /\./;
  if (point.test(ShowingBook.buyNumber.toString())) {
    console.log(ShowingBook.buyNumber)
    showWarning.value = true
  } else {
    if (ShowingBook.buyNumber < 1) {
      showWarning.value = true
    } else {
      showWarning.value = false
    }
  }
}

const addToCollections = () => {
  let uid = localStorage.getItem('ms_uid');
  let filterToBasketRequest = {
    url: 'collection/custom_filter/',
    method: 'get',
    query: {
      'user_id': uid,
      'book_id': ShowingBook.id,
    },
  }
  requestData(filterToBasketRequest)!.then(res => {
    if (res.data.length > 0) {
      ElMessage.error('该书籍已添加到收藏单,重复提交')
    } else {
      let createBasketRequest = {
        url: 'collection/',
        method: 'post',
        query: {
          'uid': uid,
          'book_id': ShowingBook.id,
        },
      }
      requestData(createBasketRequest)!.then(res => {
        console.log('create to basket.')
        ElMessage.success('添加成功')
      })
    }

  })
}
const AddToBasket = () => {
  const point: RegExp = /\./;
  if (point.test(ShowingBook.buyNumber.toString())) {
    showWarning.value = true
    return
  } else {
    if (ShowingBook.buyNumber < 1) {
      showWarning.value = true
      return;
    } else {
      showWarning.value = false
    }
  }
  let uid = localStorage.getItem('ms_uid');
  let filterToBasketRequest = {
    url: 'shoppingcarts/custom_filter/',
    method: 'get',
    query: {
      'user_id': uid,
      'book_id': ShowingBook.id,
    },
  }
  requestData(filterToBasketRequest)!.then(res => {
    console.log(res.data)
    if (res.data.length > 0) {
      let basket_id = res.data[0]['id']
      let old_amount = res.data[0]['amount']
      let new_amount = (Number(old_amount) + ShowingBook.buyNumber).toString()
      let updateBasketRequest = {
        url: 'shoppingcarts/' + basket_id + '/',
        method: 'put',
        query: {
          'uid': uid,
          'book_id': ShowingBook.id,
          'amount': new_amount,
        },
      }
      console.log(updateBasketRequest)
      requestData(updateBasketRequest)!.then(res => {
        console.log('add to basket.')
      })
    } else {
      let createBasketRequest = {
        url: 'shoppingcarts/',
        method: 'post',
        query: {
          'uid': uid,
          'book_id': ShowingBook.id,
          'amount': ShowingBook.buyNumber.toString(),
        },
      }
      requestData(createBasketRequest)!.then(res => {
        console.log('create to basket.')
      })
    }
  })
  console.log(ShowingBook)
  console.log("submit")
  BookVisible.value = !BookVisible.value;
}

const addBuyNumber = () => {
  ShowingBook.buyNumber = Number(ShowingBook.buyNumber) + 1;
}

const deleteBuyNumber = () => {
  if (ShowingBook.buyNumber > 0) {
    ShowingBook.buyNumber = Number(ShowingBook.buyNumber) - 1;
  }
}
</script>

<style>
.home-bg {
  margin: 0px auto;
}

.homeimg {
  width: 100%;
//height: 300px; aspect-ratio: auto 988 / 318; height: 318px;
}

.title-line {
  width: 100%;
  height: 50px;
  margin-top: 10px;
  background-color: rgb(0, 70, 145);
}

.title-line span {
  color: #ffffff;
  font-size: 18px;
  line-height: 50px;
  width: 20%;
  margin-left: 460px;
}

.box {
  width: 100%;
  padding-left: 5px;
  padding-right: 5px;
  display: flex;
  margin-bottom: 50px;
}

.unit-box {
  display: inline-block;
  width: 240px;
  margin-right: 10px;
  background-color: #f0f0f0;
}

.boxImg {
  display: block;
  width: 240px;
  height: 200px;
  margin-right: 10px;
}

.boxTitle {
  display: block;
  width: 240px;
  height: 65px;
  margin-top: 10px;
  margin-right: 10px;
  font-size: 15px;
  text-align: center;
}

.boxPrice {
  display: block;
  width: 240px;
  height: 30px;
  margin-right: 10px;
  font-size: 15px;
  text-align: center;
}

.dialog-footer button:first-child {
  margin-right: 10px;
}

.left-dialog {
  display: inline-block;
  width: 40%;
  float: left;
  height: 100%;
  margin-left: 50px;
}

.right-dialog {
  display: inline-block;
  margin-left: 5px;
  width: 40%;
  float: right;
  height: 100%;
  margin-right: 70px;
}

.unit-description {
//margin-bottom: 40px; margin-top: 40px;
  width: 100%;
  height: 40px;
}

.unit-description .des-label {
  font-weight: bold;
  font-size: 18px;
  float: left;
  width: 40%;
  text-align: left;
}

.unit-description .des-content {
  font-size: 18px;
  float: right;
  width: 60%;
  text-align: left;
}

.unit-description:first-child {
  margin-top: 30px;
}


</style>
