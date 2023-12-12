<template>
    <div style="height: 100%">
        <v-Header ref="headerRef" :pageId="pageId"/>
        <div class="TableBox">
            <el-card class="box-card">
                <template #header>
                    <div class="card-header">
                        <span style="font-weight: bold; font-size: 20px">购物车</span>
                        <el-button type="danger" style="font-size: 18px; margin-left: 800px" @click="toHome">关闭
                        </el-button>
                    </div>
                </template>
                <el-table :key="tableKey" :data="tableData" border :header-cell-style="{textAlign: 'center'}"
                          :cell-style="{ textAlign: 'center' }" height="450" style="width: 100%">
                    <el-table-column prop="ImgAddress" label="图片" width="220" key="slot">
                        <template slot-scope="scope" #default="scope">
                            　
                            <el-image :src="scope.row.ImgAddress"/>
                            　　
                        </template>
                    </el-table-column>
                    <el-table-column prop="bname" label="书名" width="150"/>
                    <el-table-column prop="author" label="作者" width="150"/>
                    <el-table-column prop="price" label="单价（元）" width="180"/>
                    <el-table-column prop="amount" label="数量（个）" width="130"/>
                    <el-table-column label="操作" key="slot">
                        <template slot-scope="scope" #default="scope">
                            <el-button type="danger" @click="DeleteBook(scope.$index)">删除</el-button>
                        </template>
                    </el-table-column>
                </el-table>
                <template #footer>
                    <span style="font-size: 18px;font-weight: bold">总金额:{{ PriceSum }}</span>
                  <el-button type="primary" style="font-size: 18px; margin-left:77%" @click="buyBooks">支付</el-button>

                </template>
            </el-card>
        </div>
    </div>
</template>

<script setup lang="ts">
import vHeader from '../components/header.vue';
import {onMounted, reactive, ref, watch} from "vue";
import router from "../router";
import {Delete} from "@element-plus/icons-vue";
import {requestData} from "../api";
import {toRaw} from "vue";
import {updateHandler} from "md-editor-v3/lib/types/MdEditor/utils/dom";

const pageId = ref('9')
const headerRef = ref(null)
const PriceSum = ref<number>(0)


interface tableUnit {
  basket_id: string,
  book_id: string,
  bname: string,
  author: string,
  author_id:string,
  pub_id:string,
  category_id:string,
  category: string,
  price: string,
  pub_year: string,
  pname: string,
  rate: string,
  ImgAddress: string,
  isbn:string,
  sales:string,
  // buy_date: string,
  amount: string,
}

let tableData = reactive<tableUnit[]>([])

let tableKey = 1;
const toHome = () => {
    router.push({
        path: '/home',
        query: {},
    })
}

onMounted(() => {
    console.log(headerRef.value?.selected)
  let uid = localStorage.getItem('ms_uid')
  let collectionRequest = {
    url: 'shoppingcarts/custom_filter/',
    method: 'get',
    query: {
      'user_id': uid
    },
  }
  console.log('uid', uid)
  requestData(collectionRequest)!.then(res => {
    for (let item of res.data) {
      tableData.push({
        basket_id: item['id'],
        book_id: item['book']['book_id'],
        pub_id: item['book']['publisher']['pub_id'],
        bname: item['book']['bname'],
        author_id: item['book']['author']['author_id'],
        author: item['book']['author']['aname'],
        category: item['book']['category']['category_name'],
        category_id: item['book']['category']['category_id'],
        isbn: item['book']['sales'],
        price: item['book']['price'],
        pub_year: item['book']['pub_year'],
        pname: item['book']['publisher']['pname'],
        rate: item['book']['rate'],
        ImgAddress: item['book']['url'],
        sales: item['book']['sales'],
        amount: item['amount'],
      })
    }
  });

})

watch(tableData,(ov, nv)=>{
  PriceSum.value = 0;
    for (let i=0;i<tableData.length;i++) {
      PriceSum.value += Number(tableData[i].price) * Number(tableData[i].amount);
    }
    PriceSum.value = Number(PriceSum.value.toFixed(2));
})
const DeleteBook = (index: number) => {
  let deleteRequest = {
    url: 'shoppingcarts/' + tableData[index].basket_id + '/',
    method: 'delete',
    query: {},
  }
  console.log(deleteRequest)
  requestData(deleteRequest)!.then(() => {})
  console.log('delete one in basket')
  tableData.splice(index, 1);
  tableKey++;
}

const buyBooks = ()=>{
  let uid = localStorage.getItem('ms_uid')
  for (let i=0;i<tableData.length;i++){
    let addToHistoryRequest = {
      url: 'shoppinghistory/',
    method: 'post',
    query: {
        uid: uid,
        book_id: tableData[i].book_id,
    },
    }
    requestData(addToHistoryRequest)!.then(() => {})

    let updateBookRequest ={
      url: 'books/' + tableData[i].book_id +'/',
    method: 'put',
    query: {
        book_id: tableData[i].book_id,
      author_id: tableData[i].author_id,
      pub_id: tableData[i].pub_id,
      category_id: tableData[i].category_id,
      bname: tableData[i].bname,
      price: tableData[i].price,
      pub_year: tableData[i].pub_year,
      url: tableData[i].ImgAddress,
      isbn: tableData[i].isbn,
      sales: (Number(tableData[i].sales)+ Number(tableData[i].amount)).toString(),
      rate:tableData[i].rate,
    },
    }
    requestData(updateBookRequest)!.then(() => {})
    let deleteRequest = {
    url: 'shoppingcarts/' + tableData[i].basket_id + '/',
    method: 'delete',
    query: {},
    }
    requestData(deleteRequest)!.then(() => {})
  }
  tableData.splice(0, tableData.length)
  tableKey++;
  console.log('buy')
}
</script>


<style scoped>
.TableBox {
    left: 50px;
    right: 50px;
    top: 120px;
    width: 1000px;
    height: 1050px;
    margin: 0 auto;
    padding-top: 10px;
    padding-bottom: 30px;
    -webkit-transition: left .3s ease-in-out;
    transition: left .3s ease-in-out;
    background: #ffffff;
}
</style>