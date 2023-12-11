<template>
  <div id="app" style="height: 100%">
    <v-Header ref="headerRef" :pageId="pageId"/>
    <el-scrollbar class="scroll" height="100%" style="overflow: auto;">

      <div class="FormBox">
        <el-form
        ref="ruleFormRef"
        :model="ruleForm"
        :rules="rules"
        :label-position="labelPosition"
        label-width="120px"
        class="SearchForm"
        :size="formSize"
        :status-icon="false"
        >
          <el-row>
            <el-col :span="10">
              <el-form-item label="作者" prop="name" class="UnitInput">
                <el-input v-model="ruleForm.name" />
              </el-form-item>
            </el-col>
            <el-col :span="13" :offset="1">
              <el-form-item label="书名" prop="bookName" class="UnitInput">
                <el-input v-model="ruleForm.bookName" />
              </el-form-item>
            </el-col>
          </el-row>

          <el-row>
            <el-col :span="10">
              <el-form-item label="类别" prop="type" class="UnitInput">
                <el-input v-model="ruleForm.type" placeholder="各个关键词之间用.隔开，如 bible.history" />
              </el-form-item>
            </el-col>
            <el-col :span="13" :offset="1">
              <el-form-item label="出版社" prop="Publisher" class="UnitInput">
                <el-input v-model="ruleForm.Publisher" />
              </el-form-item>
            </el-col>
          </el-row>

          <el-form-item label="出版时间范围" class="UnitInput">
            <el-col :span="10">
              <el-form-item prop="StartTime">
                <el-date-picker
                  v-model="ruleForm.StartTime"
                  type="year"
                  label="Pick Start Time"
                  placeholder="Pick Start Time"
                  style="width: 100%"
                />
              </el-form-item>
            </el-col>
            <el-col class="text-center" :span="2">
              <span class="text-gray-500" style="margin-left: 23px">----</span>
            </el-col>
            <el-col :span="12">
              <el-form-item prop="EndTime">
                <el-date-picker
                  v-model="ruleForm.EndTime"
                  type="year"
                  label="Pick End Time"
                  placeholder="Pick End Time"
                  style="width: 100%"
                />
              </el-form-item>
            </el-col>
          </el-form-item>

          <el-form-item class="UnitInput">
            <el-button type="primary" @click="submitForm(ruleFormRef)" style="margin-left: 25%;
            margin-right: 10%">
              提交
            </el-button>
            <el-button @click="resetForm(ruleFormRef)">重置</el-button>
          </el-form-item>
        </el-form>


        <div class="ListBox">
          <el-card class="box-card">
            <template #header>
              <div class="card-header">
                <span style="font-weight: bold; font-size: 20px">搜索结果</span>
              </div>
            </template>
            <el-table :key="tableKey" :data="BookListRef" :header-cell-style="{textAlign: 'center'}"
                      :cell-style="{ textAlign: 'center' }" style="width: 100%;--el-table-border-color: none;">
              <el-table-column type="index" label="序号" width="60"/>
              <el-table-column prop="ImgAddress" label="图片" width="200" key="slot">
                <template slot-scope="scope" #default="scope">
                  <el-image :src="scope.row.ImgAddress"/>
                </template>
              </el-table-column>
              <el-table-column prop="name" label="书名" width="200"/>
<!--              可以开show-overflow-tooptip 来避免过长字符串影响格式  -->
              <el-table-column prop="author" label="作者" width="80" />
              <el-table-column prop="publisher" label="出版社" width="200"/>
              <el-table-column prop="date" label="出版年" width="60" />
              <el-table-column label="操作" width="100">
                <template slot-scope="scope" #default="scope">
                  <el-button type="primary" @click="ShowBook(scope.$index)">查看</el-button>
                  <el-dialog v-model="BookVisible" title="书籍信息" style="width: 80%;">
                    <div class="left-dialog">
                      <el-image style="margin-top:20%;max-width:250px;object-fit: contain" :src=ShowingBook.ImgAddress></el-image>
                      <div style="margin-top: 50px;font-size: 20px;">
                        <span>书籍图片参考</span>
                      </div>
                    </div>
                    <div class="right-dialog">
                      <div class="unit-description" style="height: 100%">
                        <span class="des-label" style="width: 30%; height: 100%">书名</span>
                        <span class="des-content" style="width: 70%">{{ShowingBook.name}}</span>

                      </div>
                      <div class="unit-description">
                        <span class="des-label">作者</span>
                        <span class="des-content">{{ShowingBook.author}}</span>

                      </div>
                      <div class="unit-description">
                        <span class="des-label">类型</span>
                        <span class="des-content">{{ShowingBook.type}}</span>

                      </div>
                      <div class="unit-description">
                        <span class="des-label">出版社</span>
                        <span class="des-content">{{ShowingBook.name}}</span>

                      </div>
                      <div class="unit-description">
                        <span class="des-label">出版年</span>
                        <span class="des-content">{{ShowingBook.date}}</span>

                      </div>
                      <div class="unit-description">
                        <span class="des-label">单价</span>
                        <span class="des-content">{{ShowingBook.price}}</span>

                      </div>
                      <div class="unit-description">
                        <span class="des-label" style="margin-top: 5px">购买数量</span>
                        <span class="des-content">
                          <div >

                          <el-input v-model="ShowingBook.buyNumber" style="width: 50px;vertical-align:middle;
                          border-radius: 0 " @change="ShowWarning"/>
                            <el-icon style="vertical-align:middle;border-radius:50%;border: 1px solid #d5d5d5;
                            margin-left: 8px;background-color: #d5d5d5" @click="addBuyNumber"><Plus /></el-icon>
                      <el-icon style="vertical-align:middle;border-radius:50%;border: 1px solid #d5d5d5;
                      margin-left: 5px;background-color: #d5d5d5" @click="deleteBuyNumber"><Minus /></el-icon>
                          </div>
                        </span>
                      </div>
                      <div v-if="showWarning" class="unit-description" >
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
  <!--                <el-button type="danger" style="margin-left: 10px" @click="DeleteBook(scope.$index)">删除</el-button>-->
                </template>
              </el-table-column>
            </el-table>
          </el-card>
        </div>
      </div>
    </el-scrollbar>
  </div>
</template>



<script setup lang="ts">
import vHeader from '../components/header.vue';
import {onMounted, reactive, ref} from "vue";
import type { FormInstance, FormRules, FormProps } from 'element-plus';
import {requestData} from "../api";
import router from "../router"
import {ElMessage} from "element-plus";
const pageId = ref('2')
const headerRef = ref(null)
const BookVisible = ref(false)
const showWarning = ref(false)

var allresults = []
var allbooks = []
onMounted(()=>{
  console.log(headerRef.value?.selected)
  funcData();
})
const checkEndTime = (rule: any, value: string, callback: (arg0: Error | undefined) => void)=> {
    if (ruleForm.EndTime){
      if (!ruleForm.StartTime) {
        callback(new Error("请选择开始时间！"))
      } else if (Date.parse(ruleForm.StartTime) >= Date.parse(value)) {
      callback(new Error("结束时间必须大于开始时间！"))
      }
    }
    else {
      callback();
    }
}
const labelPosition = ref<FormProps['labelPosition']>('left')

interface RuleForm {
  name: string
  bookName: string
  Publisher: string
  StartTime: string
  EndTime: string
  type: string
}

const formSize = ref('default')
const ruleFormRef = ref<FormInstance>()
const ruleForm = reactive<RuleForm>({
  name: '',
  bookName: '',
  Publisher: '',
  StartTime: '',
  EndTime: '',
  type: '',
})

const rules = reactive<FormRules<RuleForm>>({
  name: [
    { required: false, message: 'Please input Activity name', trigger: 'blur' },
    { min: 1, max: 25, message: 'Length should be 3 to 5', trigger: 'blur' },
  ],
  bookName: [
    { required: false, message: 'Please input Activity name', trigger: 'blur' },
    { min: 1, max: 30, message: 'Length should be 3 to 5', trigger: 'blur' },
  ],
  // ISBN:[
  //   { required: false, message: 'Please input Activity name', trigger: 'blur' },
  //   { min: 1, max: 25, message: 'Length should be 3 to 5', trigger: 'blur' },
  // ],
  Publisher:[
    { required: false, message: 'Please input Activity name', trigger: 'blur' },
    { min: 1, max: 25, message: 'Length should be 3 to 5', trigger: 'blur' },
  ],
  StartTime: [
    {
      type: 'year',
      required: false,
      message: 'Please pick a year',
      trigger: 'change',
    },
  ],
  EndTime: [
    {
      type: 'year',
      required: false,
      message: 'Please pick a year',
      trigger: 'change',
    },
    {
      validator: checkEndTime,
      trigger: 'change'
    },
  ],
  type: [
    {
      required: false,
      message: 'Please input at least one activity type',
      trigger: 'change',
    },
  ],
})

const submitForm = async (formEl: FormInstance | undefined) => {
  if (!formEl) return
  await formEl.validate(async (valid: any, fields: any) => {
    if (valid) {
      console.log('submit')
      const searchCriteria: { [key: string]: string } = {};

      // 遍历表单对象的属性
      for (const key in ruleForm) {
        if (ruleForm[key] !== undefined && ruleForm[key] !== null && ruleForm[key] !== '') {
          // 如果属性有值，将其添加到搜索条件中
          searchCriteria[key] = ruleForm[key];
          console.log("搜索条件： ", searchCriteria)
        }
      }
      const searchResults = searchBooks(searchCriteria);
      const convertedResults = searchResults.map((result: any) => ({
        ImgAddress: result.url,
        name: result.bname,
        author: result.authors.aname,
        publisher: result.publishers.pname,
        date: result.pub_year,
        price: result.price,
        type: result.category.category_name,
      }));

      BookListRef.value = convertedResults;
      console.log('BookList: ', BookListRef.value);
      ElMessage({
        message: 'Submit Succeeded, Books Matched: '+String(BookListRef.value.length),
        type: 'success',
        })
    } else {
      console.log('error submit!', fields)
      ElMessage({
        message: 'Invalid Submit',
        type: 'warning',
        });
      }
  })
}
const searchBooks = (criteria: RuleForm): Array<any> => {
  // 存储匹配的书籍
  const matchingBooks: Array<any> = allresults.filter((book) => {
    // 检查书名是否匹配
    const isBookNameMatch = !criteria.bookName || book.bname.toLowerCase().includes(criteria.bookName.toLowerCase());

    // 检查作者是否匹配
    const isAuthorMatch = !criteria.name || book.authors.aname.toLowerCase().includes(criteria.name.toLowerCase());

    // 检查出版社是否匹配
    const isPublisherMatch = !criteria.Publisher || book.publishers.pname.toLowerCase().includes(criteria.Publisher.toLowerCase());

    // 检查类别关键字是否匹配（太多类了，只能用输入框
    const isTypeMatch = !criteria.type || book.category.category_name.toLowerCase().includes(criteria.type.toLowerCase());

    // 检查出版年份是否在范围内
    const startYear = parseInt(new Date(criteria.StartTime).toLocaleDateString(), 10);
    const endYear = parseInt(new Date(criteria.EndTime).toLocaleDateString(), 10);

    // 时间为null时对应变量值为NaN
    const isYearInRange = (
      (!criteria.StartTime || Number(book.pub_year) >= startYear) &&
      (!criteria.EndTime || Number(book.pub_year) <= endYear)
    );

    // 如果所有条件都匹配，返回 true
    return isBookNameMatch && isAuthorMatch && isPublisherMatch && isYearInRange && isTypeMatch;
  });

  // 返回匹配的书籍数组
  return matchingBooks;
};
 //校验结束时间

const resetForm = (formEl: FormInstance | undefined) => {
  if (!formEl) return
  formEl.resetFields()
}
const request = reactive({
    url: 'books/',
    method: 'get',
    query: {page:'1'}
})

const funcData = async () => {
    let page = 1;

  while (page < 3) {
      // 修改请求的 page 参数
      request.query.page = String(page);

      try {
        // 发送请求
        const res = await requestData(request);

        console.log(res.data);
        // 处理返回的数据，这里可以将数据合并到 allbooks 数组中
        allbooks = allbooks.concat(res.data);
        // 增加 page 值
        page++;
      } catch (error) {
        // 发生错误时进行处理
        console.error('Error fetching data:', error);
        console.log(allbooks);
        ElMessage.error('Error Fetching Data');
        break;
      }
    }

  for (const book of allbooks) {
    // 检查每个子数组是否包含 results 属性
    if (book.results && Array.isArray(book.results)) {
      // 将当前子数组的 results 拼接到 allResults 中
      allresults = allresults.concat(book.results);
    }
}
    // allbooks = allbooks.reduce((acc, curr) => acc.concat(curr), []);
    console.log(allresults);

}
interface bookData {
  name: string,
  ImgAddress: string,
  author: string,
  publisher:string,
  date:string,
  price:number,
  type:string
}

interface ShowBookData {
  name: string,
  ImgAddress: string,
  author: string,
  publisher:string,
  date:string,
  price:number,
  buyNumber:number,
  type:string
}
const bookList = reactive<bookData[]>([])
const BookListRef = ref(bookList);

const ShowingBook = reactive<ShowBookData>(
    {
      name: '',
  ImgAddress: '',
  author: '',
  publisher:'',
  date:'',
  price:0,
  buyNumber:1,
  type:'',
    }
)
let tableKey = 1;

const DeleteBook = (index: number) => {
  bookList.splice(index, 1);
  console.log(index)
  console.log(bookList)
  tableKey++;
  console.log(tableKey)
}
const options = Array.from({ length: 10000 }).map((_, idx) => ({
  value: `${idx + 1}`,
  label: `${idx + 1}`,
}))

let buynumber = 1;
const ShowBook = (index:number)=>{
  console.log('bookList to show:', bookList);
  ShowingBook.name = BookListRef.value[index].name
  ShowingBook.author = BookListRef.value[index].author
  ShowingBook.ImgAddress = BookListRef.value[index].ImgAddress
  ShowingBook.publisher = BookListRef.value[index].publisher
  ShowingBook.date = BookListRef.value[index].date
  ShowingBook.price = BookListRef.value[index].price
  ShowingBook.buyNumber = buynumber;
  ShowingBook.type = BookListRef.value[index].type;
  buynumber += 1;
  BookVisible.value = !BookVisible.value
}

const CacelUp= () => {
   BookVisible.value = !BookVisible.value;
}
const ShowWarning = ()=>{
  const point:RegExp = /\./;
  if (point.test(ShowingBook.buyNumber.toString())) {
    console.log(ShowingBook.buyNumber)
    showWarning.value = true
  } else {
    if (ShowingBook.buyNumber <1){
      showWarning.value = true
    }
    else {
      showWarning.value = false
    }
  }
}
const AddToBasket = () =>{
  console.log("Book Added")
}

const addBuyNumber = () =>{
  ShowingBook.buyNumber = Number(ShowingBook.buyNumber) + 1;
}

const deleteBuyNumber = () =>{
  if (ShowingBook.buyNumber > 0){
    ShowingBook.buyNumber = Number(ShowingBook.buyNumber) - 1;
  }
}
</script>

<style scoped>

.FormBox{
  box-sizing: border-box;
  position: absolute;
  left: 50px;
  right: 50px;
  top: 20px;
  bottom: 0;
  width: 1000px;
  height: 240px;
  //width: 60%;
  //height: 40%;
  margin: 0 auto;
  padding-top: 10px;
  padding-bottom: 30px;
  padding-left: 10px;
  padding-right: 10px;
  -webkit-transition: left .3s ease-in-out;
  transition: left .3s ease-in-out;
  background: #f2f2f2;
  box-shadow: 0 0 10px 0 rgba(0,0,0,.1);
  border: 1px solid #ddd;
  border-radius: 8px;
}
.SearchForm{
  box-sizing: border-box;
  margin-top: 10px;
  line-height: 1; /* 调整为适当的行高 */
}
.UnitInput{
  line-height: 1; /* 调整为适当的行高 */
  box-sizing: border-box;
  margin-top: 10px;
  font-weight:bold;
}



.ListBox {
  left: 50px;
  right: 50px;
  top: 300px;
  width: 100%;
  //margin: 0 auto;
  margin-top: 30px;
  padding-top: 25px;
  padding-bottom: 100px;
  -webkit-transition: left .3s ease-in-out;
  transition: left .3s ease-in-out;
  //background: #ffffff;
}

.dialog-footer button:first-child {
  margin-right: 10px;
}

.left-dialog{
  display: inline-block;
   width: 40%;
  float: left;
  height: 100%;
  margin-left: 50px;
}

.right-dialog{
  display: inline-block;
  margin-left: 5px;
   width: 40%;
  float: right;
  height: 100%;
  margin-right: 70px;
}

.unit-description{
  margin-bottom: 40px;
  width: 100%;
  height: 40px;
}

.unit-description .des-label{
  font-weight: bold;
  font-size: 18px;
  float: left;
  width: 40%;
  text-align: left;
}

.unit-description .des-content{
  font-size: 18px;
  float:right;
  width: 60%;
  text-align: left;
}

.unit-description:first-child{
  margin-top: 30px;
}



</style>
