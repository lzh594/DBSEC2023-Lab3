<template>
    <div class="MainBox">
        <el-scrollbar class="scroll" height="720px">
            <el-backtop target=".MainBox .el-scrollbar__wrap" :bottom="20">
                <div style="
               height: 100%;
               width: 100px;
               background-color: var(--el-bg-color-overlay);
               box-shadow: var(--el-box-shadow-lighter);
               text-align: center;
               line-height:40px;
               color: #1989fa;
               border-radius: 2px;
               font-size: 16px;
             ">
                    顶部
                </div>
            </el-backtop>
            <v-Header ref="headerRef" :pageId="pageId" />
            <div class="TableBox">
                <el-card class="box-card">
                    <template #header>
                        <div class="card-header">
                            <span style="font-weight: bold; font-size: 20px">畅销书排行榜</span>
                        </div>
                    </template>
                    <!--    <div v-for="o in 4" :key="o" class="text item">{{ 'List item ' + o }}</div>-->
                    <el-table :data="RankData" border :header-cell-style="{ textAlign: 'center' }"
                        :cell-style="{ textAlign: 'center' }" height="1480" style="width: 100%">
                        <el-table-column type="index" label="排名" width="60" />
                        <el-table-column prop="ImgAddress" label="图片" width="220" key="slot">
                            <template slot-scope="scope" #default="scope">
                            　
                                <el-image :src="scope.row.ImgAddress" />
                            　　
                            </template>
                        </el-table-column>
                        <el-table-column prop="BookName" label="书名" width="150" />
                        <el-table-column prop="Author" label="作者" width="150" />
                        <el-table-column prop="UnitPrice" label="单价（元）" width="180" />
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
import { onMounted, ref } from "vue";
import router from "../router";

const pageId = ref('3')
const headerRef = ref(null)
const RankData = [
    {
        ImgAddress: "https://www.baidu.com/img/PCtm_d9c8750bed0b3c7d089fa7d55720d6cf.png",
        BookName: 'Fly',
        Author: 'John Smith',
        UnitPrice: 1.1,
        Number: 2,
    },
    {
        ImgAddress: "https://www.baidu.com/img/PCtm_d9c8750bed0b3c7d089fa7d55720d6cf.png",
        BookName: 'Fly',
        Author: 'John Smith',
        UnitPrice: 4.1,
        Number: 3,
    },
    {
        ImgAddress: "https://www.baidu.com/img/PCtm_d9c8750bed0b3c7d089fa7d55720d6cf.png",
        BookName: 'Fly',
        Author: 'John Smith',
        UnitPrice: 4.1,
        Number: 3,
    },
    {
        ImgAddress: "https://www.baidu.com/img/PCtm_d9c8750bed0b3c7d089fa7d55720d6cf.png",
        BookName: 'Fly',
        Author: 'John Smith',
        UnitPrice: 4.1,
        Number: 3,
    },
    {
        ImgAddress: "https://www.baidu.com/img/PCtm_d9c8750bed0b3c7d089fa7d55720d6cf.png",
        BookName: 'Fly',
        Author: 'John Smith',
        UnitPrice: 4.1,
        Number: 3,
    },
    {
        ImgAddress: "https://www.baidu.com/img/PCtm_d9c8750bed0b3c7d089fa7d55720d6cf.png",
        BookName: 'Fly',
        Author: 'John Smith',
        UnitPrice: 4.1,
        Number: 3,
    },
    {
        ImgAddress: "https://www.baidu.com/img/PCtm_d9c8750bed0b3c7d089fa7d55720d6cf.png",
        BookName: 'Fly',
        Author: 'John Smith',
        UnitPrice: 4.1,
        Number: 3,
    },
    {
        ImgAddress: "https://www.baidu.com/img/PCtm_d9c8750bed0b3c7d089fa7d55720d6cf.png",
        BookName: 'Fly',
        Author: 'John Smith',
        UnitPrice: 4.1,
        Number: 3,
    },
    {
        ImgAddress: "https://www.baidu.com/img/PCtm_d9c8750bed0b3c7d089fa7d55720d6cf.png",
        BookName: 'Fly',
        Author: 'John Smith',
        UnitPrice: 4.1,
        Number: 3,
    },
    {
        ImgAddress: "https://www.baidu.com/img/PCtm_d9c8750bed0b3c7d089fa7d55720d6cf.png",
        BookName: 'Fly',
        Author: 'John Smith',
        UnitPrice: 4.1,
        Number: 3,
    },
]


onMounted(() => {
    // console.log(headerRef.value?.selected)
})

const ShowDetail = () => {
    router.push({
        path: '/home',
        query: {},
    })
}
</script>

<style scoped>
.TableBox {
    left: 50px;
    right: 50px;
    top: 120px;
    width: 1000px;
    height: 1650px;
    margin: 0 auto;
    padding-top: 25px;
    padding-bottom: 30px;
    -webkit-transition: left .3s ease-in-out;
    transition: left .3s ease-in-out;
    background: #ffffff;
}
</style>