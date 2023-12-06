<template>
  <div>
    <v-Header ref="headerRef" :pageId="pageId"/>
  </div>
  <div class="FormBox">
    <el-form
    ref="ruleFormRef"
    :model="ruleForm"
    :rules="rules"
    :label-position="labelPosition"
    label-width="120px"
    class="SearchForm"
    :size="formSize"
    status-icon
    >
    <el-form-item label="作者" prop="name" class="UnitInput">
      <el-input v-model="ruleForm.name" />
    </el-form-item>
    <el-form-item label="书名" prop="bookName" class="UnitInput">
      <el-input v-model="ruleForm.bookName" />
    </el-form-item>
<!--    <el-form-item label="ISBN" prop="ISBN" class="UnitInput">-->
<!--      <el-input v-model="ruleForm.ISBN" />-->
<!--    </el-form-item>-->
    <el-form-item label="出版社" prop="Publisher" class="UnitInput">
      <el-input v-model="ruleForm.Publisher" />
    </el-form-item>
    <el-form-item label="出版时间范围" class="UnitInput">
      <el-col :span="11">
        <el-form-item prop="StartTime">
          <el-date-picker
            v-model="ruleForm.StartTime"
            type="date"
            label="Pick a date"
            placeholder="Pick a date"
            style="width: 100%"
          />
        </el-form-item>
      </el-col>
      <el-col class="text-center" :span="2">
        <span class="text-gray-500" style="margin-left: 23px">-----</span>
      </el-col>
      <el-col :span="11">
        <el-form-item prop="EndTime">
          <el-date-picker
            v-model="ruleForm.EndTime"
            type="date"
            label="Pick a date"
            placeholder="Pick a date"
            style="width: 100%"
          />
        </el-form-item>
      </el-col>
    </el-form-item>
    <el-form-item label="类别" prop="type" class="UnitInput">
      <el-checkbox-group v-model="ruleForm.type">
        <el-checkbox label="小说类" name="type" />
        <el-checkbox label="教育类" name="type" />
        <el-checkbox label="纪实类" name="type" />
        <el-checkbox label="科幻类" name="type" />
      </el-checkbox-group>
    </el-form-item>
    <el-form-item class="UnitInput">
      <el-button type="primary" @click="submitForm(ruleFormRef)" style="margin-left: 300px;
      margin-right: 20px">
        提交
      </el-button>
      <el-button @click="resetForm(ruleFormRef)">重置</el-button>
    </el-form-item>
    </el-form>
  </div>
</template>

<script setup lang="ts">
import vHeader from '../components/header.vue';
import {onMounted, reactive, ref} from "vue";
import type { FormInstance, FormRules, FormProps } from 'element-plus';
const pageId = ref('2')
const headerRef = ref(null)

onMounted(()=>{
  console.log(headerRef.value?.selected)
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
  type: string[]
}

const formSize = ref('default')
const ruleFormRef = ref<FormInstance>()
const ruleForm = reactive<RuleForm>({
  name: '',
  bookName: '',
  Publisher: '',
  StartTime: '',
  EndTime: '',
  type: [],
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
      type: 'date',
      required: false,
      message: 'Please pick a date',
      trigger: 'change',
    },
  ],
  EndTime: [
    {
      type: 'date',
      required: false,
      message: 'Please pick a time',
      trigger: 'change',
    },
    {
      validator: checkEndTime,
      trigger: 'change'
    },
  ],
  type: [
    {
      type: 'array',
      required: false,
      message: 'Please select at least one activity type',
      trigger: 'change',
    },
  ],
})

const submitForm = async (formEl: FormInstance | undefined) => {
  if (!formEl) return
  await formEl.validate((valid: any, fields: any) => {
    if (valid) {
      console.log('submit')
    } else {
      console.log('error submit!', fields)
    }
  })
}

 //校验结束时间

const resetForm = (formEl: FormInstance | undefined) => {
  if (!formEl) return
  formEl.resetFields()
}

const options = Array.from({ length: 10000 }).map((_, idx) => ({
  value: `${idx + 1}`,
  label: `${idx + 1}`,
}))
</script>

<style scoped>
.SearchForm{
  margin-top: 20px;
}

.FormBox{
  position: absolute;
  left: 50px;
  right: 50px;
  top: 170px;
  bottom: 0;
  width: 1000px;
  height: 450px;
  margin: 0 auto;
  padding-top: 10px;
  padding-bottom: 30px;
  padding-left: 25px;
  padding-right: 40px;
  -webkit-transition: left .3s ease-in-out;
  transition: left .3s ease-in-out;
  background: #f2f2f2;
  box-shadow: 0 0 10px 0 rgba(0,0,0,.1);
  border: 1px solid #ddd;
  border-radius: 8px;
}

.UnitInput{
  margin-top: 43px;
  font-weight:bold;
}

</style>

