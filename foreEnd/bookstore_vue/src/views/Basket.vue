<template>
    <div>
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
                <!--    <div v-for="o in 4" :key="o" class="text item">{{ 'List item ' + o }}</div>-->
                <el-table :key="tableKey" :data="tableData" border :header-cell-style="{textAlign: 'center'}"
                          :cell-style="{ textAlign: 'center' }" height="450" style="width: 100%">
                    <el-table-column prop="ImgAddress" label="图片" width="220" key="slot">
                        <template slot-scope="scope" #default="scope">
                            　
                            <el-image :src="scope.row.ImgAddress"/>
                            　　
                        </template>
                    </el-table-column>
                    <el-table-column prop="BookName" label="书名" width="150"/>
                    <el-table-column prop="Author" label="作者" width="150"/>
                    <el-table-column prop="UnitPrice" label="单价（元）" width="180"/>
                    <el-table-column prop="Number" label="数量（个）" width="130"/>
                    <el-table-column label="操作" key="slot">
                        <template slot-scope="scope" #default="scope">
                            <el-button type="danger" @click="DeleteBook(scope.$index)">删除</el-button>
                        </template>
                    </el-table-column>
                </el-table>
                <template #footer>
                    <span style="font-size: 18px;font-weight: bold">总金额:{{ PriceSum }}</span>
                    <el-button type="primary" style="font-size: 18px; margin-left:770px">支付</el-button>
                </template>
            </el-card>
        </div>
    </div>
</template>

<script setup lang="ts">
import vHeader from '../components/header.vue';
import {onMounted, reactive, ref} from "vue";
import router from "../router";
import {Delete} from "@element-plus/icons-vue";

const pageId = ref('9')
const headerRef = ref(null)
const PriceSum = ref<number>(0)
onMounted(() => {
    console.log(headerRef.value?.selected)
    PriceSum.value = 0;
    for (let item of tableData) {
        PriceSum.value += item.UnitPrice * item.Number;
    }
    PriceSum.value = Number(PriceSum.value.toFixed(2));
    console.log(PriceSum.value);
})

interface tableUnit {
    ImgAddress: string,
    BookName: string,
    Author: string,
    UnitPrice: number,
    Number: number,
}

let tableData = reactive<tableUnit[]>(
    [
        {
            ImgAddress: "https://www.baidu.com/img/PCtm_d9c8750bed0b3c7d089fa7d55720d6cf.png",
            BookName: 'Fly1',
            Author: 'John Smith',
            UnitPrice: 1.1,
            Number: 2,
        },
        {
            ImgAddress: "https://www.baidu.com/img/PCtm_d9c8750bed0b3c7d089fa7d55720d6cf.png",
            BookName: 'Fly2',
            Author: 'John Smith',
            UnitPrice: 4.1,
            Number: 3,
        },
        {
            ImgAddress: "https://www.baidu.com/img/PCtm_d9c8750bed0b3c7d089fa7d55720d6cf.png",
            BookName: 'Fly3',
            Author: 'John Smith',
            UnitPrice: 4.1,
            Number: 3,
        },
    ]
)

let tableKey = 1;
const toHome = () => {
    router.push({
        path: '/home',
        query: {},
    })
}

const DeleteBook = (index: number) => {
    PriceSum.value -= tableData[index].UnitPrice * tableData[index].Number;
    PriceSum.value = Number(PriceSum.value.toFixed(2));
    tableData.splice(index, 1);
    console.log(index)
    console.log(tableData)
    tableKey++;
    console.log(tableKey)
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