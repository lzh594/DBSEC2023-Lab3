<template>
  <div class="MainBox">
    <el-scrollbar height="720px">
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
      <div class="content-box" >
        <div class="home-bg">
          <el-image class="homeimg" :src="homeImg" />
        </div>
        <div class="title-line">
          <span>热销书籍</span>
        </div>
        <div class="box">
          <div class="unit-box" v-for="item in bookList">
            <el-image class="boxImg" :src="item.imgUrl" />
            <span class="boxTitle">{{item.name}}</span>
            <span class="boxPrice">${{item.price}}</span>
          </div>
        </div>
        <div class="title-line">
          <span>作家推荐</span>
        </div>
        <div class="box">
          <div class="unit-box" v-for="item in authorList">
            <el-image class="boxImg" :src="item.imgUrl" />
            <span class="boxTitle">{{item.name}}</span>
          </div>
        </div>
        <div class="title-line">
          <span>书单推荐</span>
        </div>
        <div class="box">
          <div class="unit-box" v-for="item in paperList">
            <el-image class="boxImg" :src="item.imgUrl" />
            <span class="boxTitle">{{item.name}}</span>
          </div>
        </div>
        <div style="height: 50px;margin-bottom: 30px">

        </div>
      </div>
    </el-scrollbar>
  </div>
</template>
<script setup lang="ts">
import vHeader from '../components/header.vue';
import homeImg from '../assets/img/home-bg.png'
import {onMounted, ref} from "vue";
const headerRef = ref(null)
onMounted(()=>{
  console.log(headerRef.value?.selected)
})
const pageId = ref('1')

var bookList=[
  {name: "1", price: 4.5, imgUrl: "https://www.baidu.com/img/PCtm_d9c8750bed0b3c7d089fa7d55720d6cf.png"},
  {name: "1", price: 4.5, imgUrl: "https://www.baidu.com/img/PCtm_d9c8750bed0b3c7d089fa7d55720d6cf.png"},
  {name: "1", price: 4.5, imgUrl: "https://www.baidu.com/img/PCtm_d9c8750bed0b3c7d089fa7d55720d6cf.png"},
  {name: "1", price: 4.5, imgUrl: "https://www.baidu.com/img/PCtm_d9c8750bed0b3c7d089fa7d55720d6cf.png"},
]

var authorList=[
  {name: "1", imgUrl: "https://www.baidu.com/img/PCtm_d9c8750bed0b3c7d089fa7d55720d6cf.png"},
  {name: "1", imgUrl: "https://www.baidu.com/img/PCtm_d9c8750bed0b3c7d089fa7d55720d6cf.png"},
  {name: "1", imgUrl: "https://www.baidu.com/img/PCtm_d9c8750bed0b3c7d089fa7d55720d6cf.png"},
  {name: "1", imgUrl: "https://www.baidu.com/img/PCtm_d9c8750bed0b3c7d089fa7d55720d6cf.png"},
]

var paperList=[
  {name: "1", imgUrl: "https://www.baidu.com/img/PCtm_d9c8750bed0b3c7d089fa7d55720d6cf.png"},
  {name: "1", imgUrl: "https://www.baidu.com/img/PCtm_d9c8750bed0b3c7d089fa7d55720d6cf.png"},
  {name: "1", imgUrl: "https://www.baidu.com/img/PCtm_d9c8750bed0b3c7d089fa7d55720d6cf.png"},
  {name: "1", imgUrl: "https://www.baidu.com/img/PCtm_d9c8750bed0b3c7d089fa7d55720d6cf.png"},
]
</script>

<style>
.home-bg{
    margin: 0px auto;
}

.homeimg{
  width: 100%;
  //height: 300px;
  aspect-ratio: auto 988 / 318;
  height: 318px;
}

.title-line{
  width: 100%;
  height: 50px;
  margin-top: 10px;
  background-color: rgb(0, 70, 145);
}

.title-line span{
  color: #ffffff;
  font-size: 18px;
  line-height: 50px;
  width: 20%;
  margin-left: 460px;
}

.box{
  width: 100%;
  padding-left: 5px;
  padding-right: 5px;
  display: flex;
}
.unit-box{
  display: inline-block;
  width: 240px;
  margin-right: 10px;
  background-color: #f0f0f0;
}
.boxImg{
  display: block;
  width: 240px;
  height: 200px;
  margin-right: 10px;
}

.boxTitle{
  display: block;
  width: 240px;
  height: 30px;
  margin-right: 10px;
  font-size: 15px;
  text-align: center;
}

.boxPrice{
  display: block;
  width: 240px;
  height: 30px;
  margin-right: 10px;
  font-size: 15px;
  text-align: center;
}
</style>
