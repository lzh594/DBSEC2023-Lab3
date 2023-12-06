<template>
  <div class="MainBox">
    <el-scrollbar class="scroll" height="720px">
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
    <v-Header ref="headerRef" :pageId="pageId"/>
    <div class="ListBox">
      <el-card class="box-card">
        <template #header>
          <div class="card-header">
            <span style="font-weight: bold; font-size: 20px">个人书单</span>
          </div>
        </template>
<!--    <div v-for="o in 4" :key="o" class="text item">{{ 'List item ' + o }}</div>-->
        <el-table :data="bookList" border :header-cell-style="{textAlign: 'center'}"
                  :cell-style="{ textAlign: 'center' }" style="width: 100%">
          <el-table-column type="index" label="序号" width="60" />
          <el-table-column prop="ImgAddress" label="图片" width="220" key="slot">
            <template slot-scope="scope" #default="scope">
            　<el-image :src="scope.row.ImgAddress" />
        　　</template>
          </el-table-column>
          <el-table-column prop="name" label="书名" width="200" />
          <el-table-column prop="author" label="作者" width="200" />
          <el-table-column label="操作">
            <template #default>
              <el-button type="primary" @click="ShowDetail">查看详情</el-button>
            </template>
          </el-table-column>
        </el-table>
        <template #footer>
<!--          <span style="font-size: 16px;font-weight: bold;color: #20a0ff;margin-left: 440px">回到首部</span>-->

        </template>
      </el-card>

    </div>
    </el-scrollbar>
</div>
</template>

<script setup lang="ts">
import vHeader from '../components/header.vue';
import {onMounted, reactive, ref} from "vue";
const pageId = ref('5')
const headerRef = ref(null)
onMounted(()=>{
  console.log(headerRef.value?.selected)
})
interface bookData{
  name:string,
  ImgAddress:string,
  author:string
}
const bookList =reactive<bookData[]>([
  {
    ImgAddress: "https://www.baidu.com/img/PCtm_d9c8750bed0b3c7d089fa7d55720d6cf.png",
    name: 'Fly',
    author: 'John Smith',
  },
  {
    ImgAddress: "https://www.baidu.com/img/PCtm_d9c8750bed0b3c7d089fa7d55720d6cf.png",
    name: 'Fly',
    author: 'John Smith',
  },
  {
    ImgAddress: "https://www.baidu.com/img/PCtm_d9c8750bed0b3c7d089fa7d55720d6cf.png",
    name: 'Fly',
    author: 'John Smith',
  },
  {
    ImgAddress: "https://www.baidu.com/img/PCtm_d9c8750bed0b3c7d089fa7d55720d6cf.png",
    name: 'Fly',
    author: 'John Smith',
  },
])
</script>

<style scoped>
.ListBox{
    left: 50px;
  right: 50px;
  top: 120px;
  width: 1000px;
  margin: 0 auto;
  padding-top: 25px;
  padding-bottom: 30px;
  -webkit-transition: left .3s ease-in-out;
  transition: left .3s ease-in-out;
  background: #ffffff;
}

</style>