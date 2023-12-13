<template>
    <el-card class="card" @click="onClick" shadow="hover">
      <div class="image-container">
        <!-- <el-image src="book.imageUrl" class="my-image" fit="cover" lazy /> -->
        <el-image :src="book.url" class="my-image" fit="cover" lazy />
      </div>
      <div class="bottom">
        <time class="time">{{ book.year }}</time>
        <span class="title">{{ book.title }}</span>
      </div>
    </el-card>
</template>


<script lang="ts" setup>
import { ref, defineProps } from 'vue'
import { Book } from '../utils/models'

// 定义传入的书籍信息
const props = defineProps({  
  book: {
    type: Object as () => Book,
    required: true
  }
})

const emit = defineEmits(['clicked']);
const onClick = () => {
    emit('clicked', props.book);
}
</script>


<style>

.time {
  font-size: 10px;
  color: #999;
  margin-bottom: 5px; 
}

.bottom {
  margin-top: 13px;
  display: flex;
  flex-direction: column; 
  align-items: flex-start; 
}

.image-container {
  width: 100%;
  height: 270px;
}

.my-image {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.card {
  padding: 0;
  display: flex;
  width: 220px;
  height: 370px;
  border-radius: 8px;
  flex-direction: column;
  align-items: flex-start;
  box-shadow: 0 10px 10px rgba(0, 0, 0, 0.2); 
}

.title {
  font-size: 12px;
  max-height: 43px;
  overflow: hidden;
  text-overflow: ellipsis;
}

</style>
