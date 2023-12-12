<template>
  <div class="MainBox" style="height: 100%">
    <el-scrollbar class="scroll" height="100%">
      <v-Header ref="headerRef" :pageId="pageId"/>
      <div class="ListBox">
        <el-card class="box-card">
          <template #header>
            <div class="card-header">
              <span style="font-weight: bold; font-size: 20px">个人收藏夹</span>

            </div>
          </template>
          <el-table :key="tableKey" :data="collectionList" :header-cell-style="{textAlign: 'center'}"
                    :cell-style="{ textAlign: 'center' }" style="width: 100%;--el-table-border-color: none;">
            <el-table-column type="index" label="序号" width="60"/>
            <el-table-column prop="ImgAddress" label="图片" width="200" key="slot">
              <template slot-scope="scope" #default="scope">
                <el-image :src="scope.row.ImgAddress"/>
              </template>
            </el-table-column>
            <el-table-column prop="bname" label="书名" width="100%"/>
            <el-table-column prop="author" label="作者" width="100%"/>
            <el-table-column prop="pname" label="出版社" width="100%"/>
            <el-table-column prop="pub_year" label="出版日期"/>
            <el-table-column label="操作">
              <template slot-scope="scope" #default="scope">
                <el-button type="primary" @click="ShowBook(scope.$index)">查看</el-button>
                <el-dialog v-model="BookVisible" title="书籍信息" style="width: 80%;">
                  <div class="left-dialog">
                    <el-image style="margin-top:20%;max-width:250px;object-fit: contain"
                              :src=ShowingBook.ImgAddress></el-image>
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
                      <el-button type="primary" @click="AddToBasket">
                        加入购物车
                      </el-button>
                    </span>
                  </template>
                </el-dialog>
                <el-button type="danger" style="margin-left: 10px" @click="DeleteBook(scope.$index)">删除</el-button>
              </template>
            </el-table-column>
          </el-table>
        </el-card>
      </div>
    </el-scrollbar>
  </div>
</template>

<script setup lang="ts">
import vHeader from '../components/header.vue';
import {onMounted, reactive, ref} from "vue";
import router from "../router";
import {ElMessage, FormInstance, FormRules} from "element-plus";
import {requestData} from "../api";
import {Star} from "@element-plus/icons-vue";

const pageId = ref('5')
const headerRef = ref(null)
const BookVisible = ref(false)
const showWarning = ref(false)

interface collectionUnit {
  collection_id: string,
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

const collectionList = reactive<collectionUnit[]>([])
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
    console.log(res.data)
    for (let item of res.data) {
      collectionList.push({
        collection_id: item['id'],
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
    console.log(collectionList)
  });
})


interface ShowBookData {
  id: string,
  name: string,
  ImgAddress: string,
  author: string,
  publisher: string,
  date: string,
  price: number,
  buyNumber: number,
  type: string,
  rate: number,
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
      rate: 0,
    }
)
let tableKey = 1;
const DeleteBook = (index: number) => {
  let deleteRequest = {
    url: 'collection/' + collectionList[index].collection_id + '/',
    method: 'delete',
    query: {},
  }
  requestData(deleteRequest)!.then(res => {})
  console.log('delete one')
  collectionList.splice(index, 1);
  tableKey++;
}

const ShowBook = (index: number) => {
  ShowingBook.id = collectionList[index].book_id
  ShowingBook.name = collectionList[index].bname
  ShowingBook.author = collectionList[index].author
  ShowingBook.ImgAddress = collectionList[index].ImgAddress
  ShowingBook.publisher = collectionList[index].pname
  ShowingBook.date = collectionList[index].pub_year
  ShowingBook.buyNumber = 1
  ShowingBook.type = collectionList[index].category
  BookVisible.value = !BookVisible.value
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

<style scoped>
.ListBox {
  left: 50px;
  right: 50px;
  top: 120px;
  width: 70%;
  margin: 0 auto;
  padding-top: 25px;
  padding-bottom: 30px;
  -webkit-transition: left .3s ease-in-out;
  transition: left .3s ease-in-out;
  background: #ffffff;
}

.dialog-footer button:first-child {
  margin-right: 10px;
}

.left-dialog {
  display: inline-block;
  width: 40%;
  float: left;
  height: 100%;
  margin-left: 70px;
}

.right-dialog {
  display: inline-block;
  margin-left: 5px;
  width: 30%;
  float: right;
  height: 100%;
  margin-right: 80px;
}

.unit-description {
  margin-bottom: 40px;
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
  width: 50%;
  text-align: left;
}

.unit-description:first-child {
  margin-top: 30px;
}
</style>