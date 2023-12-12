<template>
    <div class="login-wrap">
        <div class="ms-login">
            <div class="ms-title">注&emsp;册</div>
            <el-divider content-position="center" style="height: 4px"></el-divider>
            <el-form
          ref="ruleFormRef"
          :model="ruleForm"
          :rules="rules"
          :label-position="labelPosition"
          label-width="120px"
          class="SearchForm"
          :size="formSize"
          :status-icon="true"
          >
            <el-form-item label="用户名" prop="username" class="UnitInput">
              <el-input v-model="ruleForm.username" placeholder="输入用户名(必填)" />
            </el-form-item>

            <el-form-item label="密码" prop="userpwd" class="UnitInput">
              <el-input v-model="ruleForm.userpwd" placeholder="输入密码(必填)"/>
            </el-form-item>

            <el-form-item label="邮箱" prop="email" class="UnitInput">
              <el-input v-model="ruleForm.email" placeholder="电邮地址(选填)"/>
            </el-form-item>
            <el-form-item label="电话号码" prop="telenum" class="UnitInput">
              <el-input v-model="ruleForm.telenum" placeholder="11位电话号(选填)"/>
            </el-form-item>

            <el-form-item label="地址" prop="address" class="UnitInput">
              <el-input v-model="ruleForm.address" placeholder="选填"/>
            </el-form-item>

            <el-form-item class="UnitInput">
              <el-button type="primary" size="large" @click="submitForm(ruleFormRef)" style="margin-left: 8%;
              margin-right: 8%">注册</el-button>
              <el-button size="large" @click="back_to_login">返回</el-button>
            </el-form-item>
          </el-form>
        </div>
    </div>
</template>

<script setup lang="ts">
import vHeader from '../components/header.vue';
import {onMounted, reactive, ref} from "vue";
import type { FormInstance, FormRules, FormProps } from 'element-plus';
import {requestData} from "../api";
import router from "../router"
import {ElMessage} from "element-plus";
import {sha256} from '../store/sha256';
import {create} from "axios";
const pageId = ref('2')
const headerRef = ref(null)
// localStorage.getItem("msuid")
onMounted(()=>{
  console.log(headerRef.value?.selected)
})
const nameCheck = (rule: any, value: string, callback: (arg0: Error | undefined) => void)=> {
  const reg = /^[a-zA-Z0-9]+$/;
  if (reg.test(value)) {
    callback();
  } else {
    callback(new Error("用户名只能包含字母和数字"));
  }
}
const pwdCheck = (rule: any, value: string, callback: (arg0: Error | undefined) => void)=> {
  const reg = /^[a-zA-Z0-9]+$/;
    if (reg.test(value)) {
      callback();
    } else {
      callback(new Error("密码只能包含字母和数字"));
    }
}
const mailCheck = (rule: any, value: string, callback: (arg0: Error | undefined) => void)=> {
  const reg = /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,6}$/;
  if (reg.test(value) || value.length==0) {
      callback();
    } else {
      callback(new Error("请输入正确的邮箱格式如12345678@buaa.edu.cn"));
    }
}
const labelPosition = ref<FormProps['labelPosition']>('left')

interface RuleForm {
  username: string
  userpwd: string
  address: string
  email: string
  telenum: string
}

const formSize = ref('default')
const ruleFormRef = ref<FormInstance | null>(null);
const ruleForm = reactive<RuleForm>({
  username: '',
  userpwd: '',
  address: '',
  email: '',
  telenum: '',
})

const rules = reactive<FormRules<RuleForm>>({
  username: [
    { required: true, message: 'Please input your name', trigger: 'blur' },
    { min: 1, max: 20, message: 'Length should be 1 to 20', trigger: 'blur' },
    { validator: nameCheck, trigger: 'change' },
  ],
  userpwd: [
    { required: true, message: 'Please input your password', trigger: 'blur' },
    { min: 6, max: 20, message: 'Length should be 6 to 20, ', trigger: 'blur' },
    { validator: pwdCheck, trigger: 'change' },
  ],
  telenum:[
    { required: false, message: 'Please input your telephone number', trigger: 'blur' },
    { min: 11, max: 11, message: 'Length should be 11', trigger: 'blur' },
  ],
  address:[
    { required: false, message: 'Please input your address', trigger: 'blur' },
    { min: 1, max: 30, message: 'Length should be 1 to 30', trigger: 'blur' },
  ],
  email:[
    { required: false, message: 'Please input your email address', trigger: 'blur' },
    { min: 2, max: 25, message: 'Length should be 2 to 25, ', trigger: 'blur' },
    { validator: mailCheck, trigger: 'change' },
  ]
})
const request = reactive({
    url: 'users/custom_filter/',
    method: 'get',
    query: {uname:''}
})
const getid = reactive({
  url: 'users/get_id/',
  method: 'get',
  query: {uname:''}
})
const createuser = reactive({
  url: 'users/',
  method: 'post',
  query: {uid:'', uname:'', pwdhash:'', email:'', tel:''}
})

const submitForm = async (formEl: FormInstance | undefined) => {
  if (!formEl) return
  console.log('input: ', ruleForm)
  await formEl.validate(async (valid: any, fields: any) => {
    if (valid) {
      // 查询是否存在重名
      request.query.uname = ruleForm.username;
      requestData(request)!.then((req_res) => {
        console.log('重名查询结果： ', req_res);
        if (req_res.data.length > 0) {
          ElMessage({
            message: '用户重名，请重新输入',
            type: 'warning',
          });
        } else {
          // 查询uid，然后create
          getid.query.uname = ruleForm.username;
          requestData(getid)!.then((idres) => {
            console.log('get id: ', idres.data);
            const uidstring = idres.data.uid;
            const pwdstring = ruleForm.userpwd;
            const namestring = ruleForm.username;
            const telstring = ruleForm.telenum;
            // const addstring = ruleForm.address;
            const emailstring = ruleForm.email;
            console.log('reach 1 ');
            impsha256(pwdstring)!.then((hashValue) => {
              console.log('uid: ', uidstring);
              console.log('uname: ', namestring);
              console.log('password: ', pwdstring, ' SHA-256 Hash:', hashValue);
              console.log('email: ', emailstring);
              console.log('tel: ', telstring);
              createuser.query.uid = uidstring;
              createuser.query.uname = namestring;
              createuser.query.pwdhash = hashValue;
              createuser.query.email = emailstring;
              createuser.query.tel = telstring;
              requestData(createuser)!.then((creatres) => {
                console.log('post info: ', createuser);
                console.log('post response: ', creatres)
                ElMessage({
                  message: '注册成功！',
                  type: 'success',
                });
                router.push('/login');
              }).catch((error) => {
                console.error('Error creating ', error)
              });
            }).catch((error) => {
              console.error('Error:', error)
            });
          }).catch((error) => {
            console.error('Error:', error);
          });
        }
      });
    }
  }).catch((error) => {
    console.error('Error:', error);
  });
}
const back_to_login = () =>{
  console.log("Jumping Back")
  router.push('/login');
}
async function impsha256(str: string) {
  return sha256(str);
}
</script>

<style scoped>


.SearchForm{
  box-sizing: border-box;
  margin-top: 30px;
  line-height: 1; /* 调整为适当的行高 */
}
.UnitInput{
  line-height: 1; /* 调整为适当的行高 */
  box-sizing: border-box;
  margin-top: 30px;
  font-weight:bold;
}



.form-item {
    font-size: 50px; /* adjust as needed */
}

.divider {
    text-align: center;
    font-size: 16px;
    width: 200px;
}

.input-field {
    background-color: whitesmoke;
    width: 100%;
    height: 60px;
    margin-bottom: 10px;
    border: none;
    border-bottom: 2px solid silver;
    font-size: 20px;
}


.login-wrap {
    position: absolute;
    width: 100%;
    height: 100%;
    background-image: url(../assets/img/login.png);
    background-position: center center;
    background-size: 100%;
}

.ms-title {
    width: 100%;
    line-height: 80px;
    text-align: center;
    font-size: 36px;
    font-weight: bold;
    color: black;
    border-bottom: 2px solid grey;
}

.ms-login {
    position: absolute;
    top: 50%;
    margin-top: -300px;
    left: 75%;
    margin-left: -280px;
    /* absolute居中的一种方法 */
    background-color: rgba(245, 245, 245, 0.9);
    width: 500px;
    height: 500px;
    border-radius: 25px;
    text-align: center;
    padding: 5px 40px;
    box-sizing: border-box;
}


.login-btn button {
    width: 50%;
    height: 50px;
    margin-top: 10px;
}

</style>

