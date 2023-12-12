<template>
    <div class="login-wrap">
        <div class="ms-login">
            <div class="ms-title">网上书店</div>
            <el-divider content-position="center"></el-divider>
            <el-form :model="param" :rules="rules" ref="login" class="ms-content">
                <el-form-item prop="username" class="form-item">
                    <el-input v-model="param.username" placeholder="用户名" class="input-field">
                        <template #prepend>
                            <el-button icon="User" disabled></el-button>
                        </template>
                    </el-input>
                </el-form-item>
                <el-form-item prop="password" class="form-item">
                    <el-input
                        type=text
                        show-password
                        placeholder="密码"
                        v-model="param.password"
                        @keyup.enter="submitForm(login)"
                        class="input-field"
                    >
                        <template #prepend>
                            <el-button icon="Lock" disabled></el-button>
                        </template>
                    </el-input>
                </el-form-item>
                <span class="login-btn">
                    <el-button round type="primary" @click="submitForm(login)" class="login-button">登 录</el-button>
                    <el-button round type="primary" @click="toSignUp" class="login-button">注 册</el-button>
                </span>
            </el-form>
            <p class="login-tips">Tips : 请正确填写用户名和密码~</p>
        </div>
    </div>
</template>

<script setup lang="ts">
import {ref, reactive} from 'vue';
import {usePermissStore} from '../store/permiss';
import {useRouter} from 'vue-router';
import {ElMessage} from 'element-plus';
import type {FormInstance, FormRules} from 'element-plus';
import user from "./user.vue";
import {requestData} from "../api";
import {sha256} from '../store/sha256';

interface LoginInfo {
    username: string;
    password: string;
}

const router = useRouter();
const param = reactive<LoginInfo>({
    username: '',
    password: '',
});
const errorVisible = ref(false)
const rules: FormRules = {
    username: [ {required: true, message: '请输入用户名', trigger: 'blur' }],
    password: [ {required: true, message: '请输入密码', trigger: 'blur'}],
};
const login = ref<FormInstance>();
const request = reactive({
    url: 'users/custom_filter/',
    method: 'get',
    query: {uname:''}
})
const submitForm = (formEl: FormInstance | undefined) => {
    if (!formEl) return;

    formEl.validate((valid: boolean) => {
        if (valid) {
            visitsUp();
            localStorage.setItem('ms_username', param.username);
            request.query.uname = param.username
            requestData(request)!.then((res) => {
              // 核验用户名是否存在
              if (res.data.length == 0){
                ElMessage.error('用户不存在！');
              } else{
                // 核验密码是否正确
                localStorage.setItem('ms_uid', res.data[0].uid);
                console.log(localStorage.getItem('ms_uid'))
                impsha256(param.password)!.then((inputhash) =>{
                  console.log('input hash: ', inputhash)
                  console.log('backend hash: ', res.data[0].pwdhash)
                  if (inputhash == res.data[0].pwdhash){
                    ElMessage.success('登录成功！')
                    router.push('/home');
                  } else{
                    ElMessage.error('用户名或密码错误！')
                  }
                }).catch((hasherror) => {
                  console.log('Error in Calculating Hash')
                });
              }
            }).catch((error) => {
              // 请求出错处理
              console.log('Error : ', error)
            });
        } else {

            ElMessage.error('操作失败');
            return false;
        }
    });
};
const visitsUp = () => {
    const last = localStorage.getItem("visits")
    if (last === null) {
        localStorage.setItem("visits", "1")
    } else {
        localStorage.setItem("visits", (parseInt(last) + 1).toString())
    }
}

const toSignUp = () =>{
  console.log("Jumping to Register");
  router.push('/register');
}

async function impsha256(str: string) {
  return sha256(str);
}
</script>

<style scoped>
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

.identity-group {
    width: 60%;
    border-radius: 8px;
    margin: 20px auto;
//color: white; text-align: center;
    display: block;
    align-items: center;
}

.login-button {
    font-size: 24px; /* adjust as needed */
  margin-left: 35px;
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
    height: 530px;
    border-radius: 25px;
    text-align: center;
    padding: 5px 40px;
    box-sizing: border-box;
}

.ms-content {
    padding: 30px 50px;
}

.login-btn {
    font-size: 24px;
    text-align: center;
}

.login-btn button {
    width: 50%;
    height: 50px;
    margin-top: 10px;
}

.login-tips {
    font-size: 18px;
    color: grey;
}

</style>
