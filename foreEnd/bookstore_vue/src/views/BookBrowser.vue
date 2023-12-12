<template>
    <!-- 重构为layout! -->
    <v-header ref="headerRef" :pageId="pageId" />
    <div class="page">
        <el-row align="middle">
            <el-col :span="3" :offset="2">
                <h3>年份</h3>
            </el-col>
            <el-col :span="17">
                <el-radio-group v-model="chosenYear" size="large" @change="onYearChange">
                    <el-radio-button v-for="item in years" :label="item">
                        {{ item }}
                    </el-radio-button>
                </el-radio-group>
            </el-col>
        </el-row>
        <el-row align="middle">
            <el-col :span="3" :offset="2">
                <h3>分类</h3>
            </el-col>
            <el-col :span="17">
                <el-radio-group v-model="chosenType" size="large" @change="onTypeChange">
                    <el-radio-button v-for="item in types" :label="item" :key="item">
                        {{ item }}
                    </el-radio-button>
                </el-radio-group>
            </el-col>
        </el-row>
        <el-row align="middle">
            <el-col :span="3" :offset="2">
                <h3>价格</h3>
            </el-col>
            <el-col :span="17">
                <el-radio-group v-model="chosenPrice" size="large" @change="onPriceChange">
                    <el-radio-button v-for="item in prices" :label="item" :key="item">
                        {{ item }}
                    </el-radio-button>
                </el-radio-group>
            </el-col>
        </el-row>
        <el-row align="middle">
            <el-col :span="12" :offset="3">
                <el-button v-for="button in sortOrders" :key="button.label"
                    :type="chosenSortOrder === button.label ? 'primary' : 'default'" @click="onSortChange(button.label)">
                    {{ button.label }}
                </el-button>
            </el-col>
            <el-col :span="9">
                <el-button icon="download" @click="download">下载CSV格式统计结果</el-button>
            </el-col>
        </el-row>
        <el-row align="middle">
            <el-scrollbar>
                <div class="gallery">
                    <div v-for="book in books" class="book-card">
                        <book-card :book="book" @clicked="onCardClick" />
                    </div>
                </div>
            </el-scrollbar>
        </el-row>
        <div v-if="isPopup">
            <bookPopup :book="clickedBook" @close="onPopupClose" />
        </div>
    </div>
</template> 

<script setup lang="ts">
import vHeader from '../components/header.vue';
import { onMounted, reactive, ref } from "vue";
import bookCard from '../components/bookCard.vue'
import { ElScrollbar } from 'element-plus';

import { Book } from "../api/models"
import { BookService } from '../api/services';

const pageId = ref('4')
const headerRef = ref(null)

// data  
const books = ref<Book[]>([]);
const oracle = new BookService();

onMounted(async () => {
    await oracle.AddBooks();
    books.value = oracle.getBooks();
})


// category filter
const chosenType = ref('全部');
const types = [
    '全部', '小说', '艺术', '历史', '生物', '旅游', '手册',
]
const typeMap: { [key: string]: string[] } = {
    '全部': ['all'],
    '小说': ['fiction', 'novel'],
    '艺术': ['art', 'music'],
    '历史': ['histor'],
    '生物': ['biolo'],
    '旅游': ['travel'],
    '手册': ['cookbook']
};
const onTypeChange = () => {
    const types = typeMap[chosenType.value]
    books.value = oracle.filterBooks().byCategory(types).getBooks()
}

// price filter
const chosenPrice = ref('全部');
const prices = [
    '全部', '小于30', '30-50', '50-100', '100-200', '200以上',
]
const onPriceChange = (chosenPrice: string) => {
    console.log(chosenPrice)
}

// year filter
const years = [
    '全部', '<1980', '1980s', '1990s', '2000s', '2010s', '2020s',
]
const yearMap: { [key: string]: number[] } = {
    '全部': [0, 3000],
    '<1980': [0, 1980],
    '1980s': [1980, 1990],
    '1990s': [1990, 2000],
    '2000s': [2000, 2010],
    '2010s': [2010, 2020],
    '2020s': [2020, 2030],
};
const chosenYear = ref('全部')
const onYearChange = () => {
    if (chosenYear.value == '全部'){
        books.value = oracle.getBooks();
    }
    else {
        const types = typeMap[chosenYear.value]
        // oracle.filterBooks().byPrice(...types)
    }
}


// button
const chosenSortOrder = ref<string>('');
const sortOrders = [
    { label: '随机排序' },
    { label: '按热度排序' },
    { label: '按价格排序' },
    { label: '按时间排序' },
];

function onSortChange(label: string) {
    chosenSortOrder.value = label;
    if (label == '随机排序') {
        oracle.sortBooks().byRandom();
    } else if (label == '按价格排序') {
        oracle.sortBooks().byPrice();
        
    } else if (label == '按时间排序') {
        oracle.sortBooks().byYear();
    } else {
        oracle.sortBooks().bySales();
    }
    books.value = oracle.getBooks();
}


// download csv
function download() {
    oracle.output2CSV();
}


// callback for card
const isPopup = ref(false);
const clickedBook = ref<Book | null>(null);
const onCardClick = (values: Book) => {
    clickedBook.value = values
    isPopup.value = true;
}
const onPopupClose = () => {
    // console.log(isPopup.value)
    isPopup.value = false;
}
</script>


<style scoped>
* {
    margin-bottom: 7px;
}

.page {
    color: var(--el-color-primary);
    /* background: var(--el-color-primary-light-9); */
    width: 70%;
    margin: 5px auto;
    /* 居中显示, 外边距 */
    border: 2px solid var(--el-border-color);
    border-radius: 6%;
    padding: 20px;
    /* 内边距 */
}

.gallery {
    width: 100%;
    display: flex;
    /* 动态排列搭配横滚动条*/
}

.book-card {
    margin: 7px;
    /* 卡片间距 */
    display: flex;
}

.el-row {
    margin-bottom: 10px;
    margin-left: 20px;
}

.button-group {
    display: flex;
    align-items: center;
}
</style>