<template>
    <div class="login-wrap">
        <div class="ms-login">
            <div class="ms-title">S.Encryption</div>
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
                </span>
            </el-form>
            <p class="login-tips">Tips : 请正确填写用户名和密码~</p>
        </div>
    </div>
</template>

<script setup lang="ts">
import {ref, reactive} from 'vue';
import {useTagsStore} from '../store/tags';
import {usePermissStore} from '../store/permiss';
import {useRouter} from 'vue-router';
import {ElMessage} from 'element-plus';
import type {FormInstance, FormRules} from 'element-plus';
import user from "./user.vue";


interface LoginInfo {
    username: string;
    password: string;
    identity: string;
}

const router = useRouter();
const param = reactive<LoginInfo>({
    username: '',
    password: '',
    identity: '用户'
});

const rules: FormRules = {
    username: [
        {
            required: true,
            message: '请输入用户名',
            trigger: 'blur'
        }
    ],
    password: [{required: true, message: '请输入密码', trigger: 'blur'}],
    identity: [{required: true, message: '请选择身份', trigger: 'blur'}]
};
const permiss = usePermissStore();
const login = ref<FormInstance>();
const submitForm = (formEl: FormInstance | undefined) => {
    if (!formEl) return;
    formEl.validate((valid: boolean) => {
        if (valid) {
            ElMessage.success('操作成功');
            visitsUp();
            localStorage.setItem('ms_username', param.username);
            const keys = permiss.defaultList[param.identity == '用户' ? 'admin' : 'user'];
            permiss.handleSet(keys);
            localStorage.setItem('ms_keys', JSON.stringify(keys));
            // window.userIdentity = param.identity === '用户' ? 1 : 0;
            localStorage.setItem('ms_identity', param.identity === '用户' ? '1' : '0');
            router.push('/home');
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
const tags = useTagsStore();
tags.clearTags();
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
    //color: white;
    text-align: center;
    display: block;
    align-items: center;
}

.login-button {
    font-size: 24px; /* adjust as needed */
}

.login-wrap {
    position: absolute;
    width: 100%;
    height: 100%;
    background-image: url(../assets/img/login.jpg);
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
