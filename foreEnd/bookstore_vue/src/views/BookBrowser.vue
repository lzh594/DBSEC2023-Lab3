<template>
    <div style="height: 100%; overflow-y: scroll;overflow-x: hidden">
        <v-scroll native>
            <v-header ref="headerRef" :pageId="pageId" />
            <div class="content-box">
                <h3>分类</h3>
                <div class="BookTypeBox">
                    <el-checkbox-group v-model="BookTypeList" @change="handleBookTypeListChange">
                        <el-checkbox v-for="BookType in BookTypes" :label=BookType :key="BookType">
                            {{ BookType }}
                        </el-checkbox>
                    </el-checkbox-group>
                </div>
                <h3>标签（可多选）</h3>
                <div class="LabelBox">
                    <el-checkbox-group v-model="LabelTypeList" @change="handleLabelTypeListChange">
                        <el-checkbox v-for="LabelType in LabelTypes" :label=LabelType :key="LabelType">
                            {{ LabelType }}
                        </el-checkbox>
                    </el-checkbox-group>
                </div>
                <h3>书籍</h3>
                <div class="box">
                    <div class="unit-box" v-for="item in BookList">
                        <el-image class="boxImg" :src="item.imgUrl" />
                        <span class="boxTitle">{{ item.name }}</span>
                        <span class="boxTitle">{{ item.author }}</span>
                    </div>
                </div>
                <div>
                    <card></card>
                </div>
                <div style="height: 50px;margin-bottom: 30px"></div>
            </div>
        </v-scroll>
    </div>
    <!-- 选中的条件栏 
        <div>
        <el-checkbox-group v-model="checkboxGroup1" size="large">
            <el-checkbox-button v-for="city in cities" :key="city" :label="city">
                {{ city }}
            </el-checkbox-button>
        </el-checkbox-group>
    </div>
    <div class="demo-button-style">
        <el-checkbox-group v-model="checkboxGroup2">
            <el-checkbox-button v-for="city in cities" :key="city" :label="city">{{
                city
            }}</el-checkbox-button>
        </el-checkbox-group>
    </div>
    <div class="demo-button-style">
        <el-checkbox-group v-model="checkboxGroup3" size="small">
            <el-checkbox-button v-for="city in cities" :key="city" :label="city" :disabled="city === 'Beijing'">{{ city
            }}</el-checkbox-button>
        </el-checkbox-group>
    </div>
    <div class="demo-button-style">
        <el-checkbox-group v-model="checkboxGroup4" size="small" disabled>
            <el-checkbox-button v-for="city in cities" :key="city" :label="city">{{
                city
            }}</el-checkbox-button>
        </el-checkbox-group>
    </div> -->
</template>

<script setup lang="ts">
import vHeader from '../components/header.vue';
import { onMounted, ref, reactive } from "vue";
import { requestData } from '../api';
import card from '../components/card.vue'

const pageId = ref('4')
const headerRef = ref(null)
onMounted(() => {
    //console.log(headerRef.value?.selected)
})

const BookTypeList = ref([]);
const BookTypes = [
    '小说类', '教育类', '纪实类', '科幻类'
];

const LabelTypeList = ref([]);
const LabelTypes = [
    '玄幻', '言情', '亲情', '爱情'
];
var BookList = [
    { name: "1", author: 'kaluo', imgUrl: "https://www.baidu.com/img/PCtm_d9c8750bed0b3c7d089fa7d55720d6cf.png" },
    { name: "1", author: 'kaluo', imgUrl: "https://www.baidu.com/img/PCtm_d9c8750bed0b3c7d089fa7d55720d6cf.png" },
    { name: "1", author: 'kaluo', imgUrl: "https://www.baidu.com/img/PCtm_d9c8750bed0b3c7d089fa7d55720d6cf.png" },
    { name: "1", author: 'kaluo', imgUrl: "https://www.baidu.com/img/PCtm_d9c8750bed0b3c7d089fa7d55720d6cf.png" },
    { name: "1", author: 'kaluo', imgUrl: "https://www.baidu.com/img/PCtm_d9c8750bed0b3c7d089fa7d55720d6cf.png" },
    { name: "1", author: 'kaluo', imgUrl: "https://www.baidu.com/img/PCtm_d9c8750bed0b3c7d089fa7d55720d6cf.png" },
]

const handleBookTypeListChange = () => {
    console.log(BookTypeList.value.map(item => {
        return item;
    }))
}

const handleLabelTypeListChange = () => {
    console.log(BookTypeList.value.map(item => {
        return item;
    }))
}



// check out
// const checkboxGroup1 = ref(['Shanghai'])
// const checkboxGroup2 = ref(['Shanghai'])
// const checkboxGroup3 = ref(['Shanghai'])
// const checkboxGroup4 = ref(['Shanghai'])
// const cities = ['Shanghai', 'Beijing', 'Guangzhou', 'Shenzhen']


</script>

<style scoped>
.box {
    width: 100%;
    padding-left: 5px;
    padding-right: 5px;
    display: flex;
    flex-wrap: wrap;
}

.unit-box {
    display: inline-block;
    width: 240px;
    margin-right: 10px;
    background-color: #f0f0f0;
    margin-bottom: 15px;
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
    height: 30px;
    margin-right: 10px;
    font-size: 15px;
    text-align: center;
}

/* .demo-button-style {
  margin-top: 24px;
} */

</style>