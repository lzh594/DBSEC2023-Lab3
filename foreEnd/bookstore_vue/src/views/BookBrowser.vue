<template>
    <!-- 重构为layout! -->
    <v-header ref="headerRef" :pageId="pageId" />
    <div class="main-interface">
        <div class="filters-area">
            <h3>年份</h3>
            <el-checkbox-group v-model="selectedYear" size="large">
                <el-checkbox-button v-for="item in years" :label="item">
                    {{ item }}
                </el-checkbox-button>
            </el-checkbox-group>
            <div>
                <h3>分类</h3>
                <el-radio-group v-model="selectedType" size="large" @change="handleTypeChange">
                    <el-radio-button v-for="item in types" :label="item" :key="item">
                        {{ item }}
                    </el-radio-button>
                </el-radio-group>
            </div>
            <div>
                <h3>价格（元）</h3>
                <el-checkbox-group v-model="selectedPrice" size="large">
                    <el-checkbox-button v-for="item in prices" :label="item" :key="item">
                        {{ item }}
                    </el-checkbox-button>
                </el-checkbox-group>
            </div>
        </div>
        <div class="content-area">
            <el-scrollbar>
                <el-scrollbar>
                    <div class="hscroll">
                        <div v-for="book in books" class="book-card">
                            <book-card :book="book" @clicked="onCardClick" />
                        </div>
                    </div>
                </el-scrollbar>
                <div class="spacer"></div>
            </el-scrollbar>
        </div>
    </div>
    <div v-if="isPopup">
    <bookPopup :book="clickedBook" @close="onPopupClose" />
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

onMounted(async () => {
    // books.value.push(...myBookService.getBooks())
    const myBookService = new BookService();
    books.value = myBookService.getBooks();
})


// filter
const selectedType = ref([]);
const types = [
    'fiction', 'art', 'history', 'biology', 'travel', 'novel',
] //fiction, histor, biolo, art(music), travel, cookbooks

const selectedPrice = ref([]);
const prices = [
    '小于30', '30-50', '50-100', '100-200', '200以上',
]

const years = [
    '<1980', '1980s', '1990s', '2000s', '2010s', '2020s',
]
const selectedYear = ref([])

const options = [
    '按热度', '按价格', '按时间',
]
const selectedOption = ref([])

const handleTypeChange = () => {
    console.log(selectedType.value.map(item => {
        return item
    }))
}


// callback for card
const isPopup = ref(false);
const clickedBook = ref<Book|null>(null);
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

.main-interface {
    display: flex;
    flex-direction: column;
    align-items: center;
    width: 60%;
    margin: auto;
    /* min-height: 100vh;
 justify-content: center; */
    padding: 10px;
    /* background: var(--el-color-primary-light-9); */
    color: var(--el-color-primary);
}


.filters-area {
    width: 100%;
    display: flex;
    flex-direction: column;
    align-items: flex-start;
}

.content-area {
    width: 100%;
    display: flex;
    overflow: hidden;
    align-items: flex-start;
    justify-content: flex-start;
}

.hscroll {
    width: 100%;
    display: flex;
    /* margin: 10px; */
    padding: 20px;
}

.spacer {
    height: 5px;
    margin-bottom: 5px;
}

.book-card {
    margin: 7px;
    display: flex;
    justify-content: center;
    align-items: center;
}


/* .content-box {
    left: 50px;
    right: 50px;
    top: 120px;
    width: 1400px;
    height: 1050px;
    margin: 0 auto;
    padding-top: 10px;
    padding-bottom: 30px;
    -webkit-transition: left .3s ease-in-out;
    transition: left .3s ease-in-out;
    background: #ffffff;
} */
</style>