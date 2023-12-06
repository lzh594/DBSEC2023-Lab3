<template>
    <el-col>
      <el-card class="card" @click="onCardClicked" shadow="hover">
        <img
          src="https://pictures.abebooks.com/isbn/9781560430896-us-300.jpg"
          class="image"
          fit="none"
        />
        <div style="padding: 14px">
          <span>Yummy hamburger</span>
          <div class="bottom">
            <time class="time">{{ currentDate }}</time>
            <!-- <el-button text class="button">Operating</el-button> -->
          </div>
        </div>
      </el-card>
    </el-col>
    <!-- use <el-row>  -->
</template>


<script lang="ts" setup>
import { ref } from 'vue'

const currentDate = ref(new Date())

const onCardClicked = () => {
    console.log('Card cliked');
}

</script>

<style>
.time {
  font-size: 12px;
  color: #999;
}

.bottom {
  margin-top: 13px;
  line-height: 12px;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.button {
  padding: 0px;
  min-height: auto;
}

.image {
  width: 100%;
  display: block;
}

.card {
    padding: 0px;
    max-width: 250px;
}
</style>
