<template>
  <div class="hello">
<!--    <h1>{{ msg }}</h1>-->
    <input type= 'text' v-model="page" placeholder="edit me"><br/>
    <button @click="test()">CheckThis</button><br/>
    <button @click="test_post()">CheckThis</button><br/>
    <li>{{ text }}</li>
  </div>
</template>

<script>
import axios from 'axios'
// import qs from "querystring"


// export default {
//   data() {
//     return {
//       data: {
//         "name": "张三",
//       },
//     }
//   },
//   methods: {
//     test() {
//       axios({
//         url: '/jango/list',
//         method: 'post',
//         responseType: 'json',
//         data: this.data
//       }).then((res) => {
//         console.log(res, '后端返回的数据');
//       })
//     },
//   }
// }


export default {
  name: "hello",
  props: {
    // msg: String
  },
  data(){
    return{
      text: 'null'
    }
  },
  methods: {
    test(){
      axios.post('/jango/list',{"name": this.page})
          .then(response=>{
            this.text = response.data;  // 返回数据显示到 text
            console.log(response.data);  // 返回的数据
            // alert(this.text);
          })
          .catch(err=>{
            this.text = 'error' + err;
          })
    },
    test_post() {
      // axios.get('/jango/testList', {params: {page: 2}})
      axios.get('/jango/testList?page=' + this.page)
          .then(response => {
            this.text = response.data;
            console.log(response.data)
          })
          .catch(error => {
            console.log(error)
          })
    },
  }
}
</script>

<style scoped>

</style>