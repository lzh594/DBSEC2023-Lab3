<template>
  <el-dialog v-model="visible" title="书籍详细信息" style="width: 960px;height:550px;" @close="onClose">
    <el-row>
      <el-col :span="7" :offset="1">
        <el-image style="margin-left: 10px; max-width:250px;object-fit: contain" fit="cover" :src=book.url></el-image>
      </el-col>
      <el-col :span="15" :offset="1">
        <el-row align="middle">
          <!-- :gutter 添加space -->
          <el-col :span="4"><span>书名</span></el-col>
          <el-col :span="20"><span>{{ book.title }}</span></el-col>
        </el-row>
        <el-row align="middle">
          <el-col :span="4"><span>作者</span></el-col>
          <el-col :span="20"><span>{{ book.author }}</span></el-col>
        </el-row>
        <el-row align="middle">
          <el-col :span="4"><span>出版社</span></el-col>
          <el-col :span="20"><span>{{ book.publisher }}</span></el-col>
        </el-row>
        <el-row align="middle">
          <el-col :span="4"><span>出版年份</span></el-col>
          <el-col :span="20"><span>{{ book.year }}</span></el-col>
        </el-row>
        <el-row align="middle">
          <el-col :span="4"><span>类型</span></el-col>
          <el-col :span="20"><span>{{ book.category }}</span></el-col>
        </el-row>
        <el-row align="middle">
          <el-col :span="4"><span>ISBN</span></el-col>
          <el-col :span="20"><span>{{ book.isbn }}</span></el-col>
        </el-row>
        <el-row align="middle">
          <el-col :span="4"><span>书籍评分</span></el-col>
          <el-col :span="20">
            <el-rate v-model="book.rate" disabled show-score size="large" allow-half/>
          </el-col>
        </el-row>
        <el-row align="middle">
          <el-col :span="4"><span>单价（元）</span></el-col>
          <el-col :span="20"><span>{{ book.price }}</span></el-col>
        </el-row>
        <el-row align="middle">
          <el-col :span="4"><span>购买数量</span></el-col>
          <el-col :span="20">
            <div>

              <el-input v-model="buyQty" style="width: 50px;vertical-align:middle;
                          border-radius: 0 " @change="checkQty"/>
              <el-icon style="vertical-align:middle;border-radius:50%;border: 1px solid #d5d5d5;
                            margin-left: 8px;background-color: #d5d5d5" @click="addBuyQty">
                <Plus/>
              </el-icon>
              <el-icon style="vertical-align:middle;border-radius:50%;border: 1px solid #d5d5d5;
                      margin-left: 5px;background-color: #d5d5d5" @click="reduceBuyQty">
                <Minus/>
              </el-icon>
            </div>

            <div v-if="invalidQty">
              <span style="color: red;">购买数量必须大于1的整数</span>
            </div>
          </el-col>
        </el-row>
        <el-row>
          <el-col :span="12"></el-col>
          <el-col :span="6">
            <el-button type="warning" :icon="Star" @click="addToFavorites">收藏</el-button>
          </el-col>
          <el-col :span="6">
            <el-button type="primary" @click="addToCart">加入购物车</el-button>
          </el-col>
        </el-row>
      </el-col>
    </el-row>
  </el-dialog>
</template>

<script lang="ts" setup>
import {defineProps, ref, defineEmits} from 'vue';
import {Book} from '../utils/models'
import {ElCol, ElMessage} from 'element-plus';
import {Star} from "@element-plus/icons-vue";
import {requestData} from "../api";

const props = defineProps({
  book: {
    type: Object as () => Book,
    required: true
  }
})
const visible = ref(true) // 默认将显示控制权移交外部
const emit = defineEmits(['closed']);
const onClose = () => {
  emit('closed');
}


// user logic
// 购买数量及其检查
const buyQty = ref(1)
const invalidQty = ref(false)
const checkQty = () => {
  const point: RegExp = /\./;
  if (point.test(buyQty.toString())) {
    invalidQty.value = true
    buyQty.value = 1
  } else {
    if (buyQty.value < 1) {
      invalidQty.value = true
      buyQty.value = 1
    } else {
      invalidQty.value = false
    }
  }
}
const addBuyQty = () => {
  buyQty.value = Number(buyQty.value) + 1;
}

const reduceBuyQty = () => {
  if (buyQty.value > 0) {
    buyQty.value = Number(buyQty.value) - 1;
  }
}

// 购物车
const addToCart = () => {
  const point: RegExp = /\./;
  if (point.test(buyQty.toString())) {
    invalidQty.value = true
    buyQty.value = 1
    return
  } else {
    if (buyQty.value < 1) {
      invalidQty.value = true
      buyQty.value = 1
      return;
    } else {
      invalidQty.value = false
    }
  }
  let uid = localStorage.getItem('ms_uid');
  let filterToBasketRequest = {
    url: 'shoppingcarts/custom_filter/',
    method: 'get',
    query: {
      'user_id': uid,
      'book_id': props.book.id.toString(),
    },
  }
  requestData(filterToBasketRequest)!.then(res => {
    console.log(res.data)
    if (res.data.length > 0) {
      let basket_id = res.data[0]['id']
      let old_amount = res.data[0]['amount']
      let new_amount = (Number(old_amount) + buyQty.value).toString()
      let updateBasketRequest = {
        url: 'shoppingcarts/' + basket_id + '/',
        method: 'put',
        query: {
          'uid': uid,
          'book_id': props.book.id.toString(),
          'amount': new_amount,
        },
      }
      requestData(updateBasketRequest)!.then(res => {
        console.log('add to basket.')
      })
    } else {
      let createBasketRequest = {
        url: 'shoppingcarts/',
        method: 'post',
        query: {
          'uid': uid,
          'book_id': props.book.id.toString(),
          'amount': buyQty.value.toString(),
        },
      }
      requestData(createBasketRequest)!.then(res => {
        console.log('create to basket.')
      })
    }
  })
  console.log("submit")
  visible.value = !visible.value;
};

// 收藏
const addToFavorites = () => {
  let uid = localStorage.getItem('ms_uid');
  let filterToBasketRequest = {
    url: 'collection/custom_filter/',
    method: 'get',
    query: {
      'user_id': uid,
      'book_id': props.book.id.toString(),
    },
  }
  console.log('book_id', props.book.id)
  requestData(filterToBasketRequest)!.then(res => {
    if (res.data.length > 0) {
      ElMessage.error('该书籍已添加到收藏单,重复提交')
    } else {
      let createBasketRequest = {
        url: 'collection/',
        method: 'post',
        query: {
          'uid': uid,
          'book_id': props.book.id.toString(),
        },
      }
      requestData(createBasketRequest)!.then(res => {
        console.log('create to basket.')
        ElMessage.success('添加成功')
      })
    }

  })
};


</script>

<style scoped>
.el-row {
  margin-bottom: 20px;
}

.el-row:last-child {
  margin-bottom: 10px;
}

.el-col {
  border-radius: 4px;
}

</style>