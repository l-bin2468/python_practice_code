import { createApp } from 'vue'
import App from './App.vue'
// import router from './router/index.js'
import axios from 'axios'

//设置默认后端地址
axios.defaults.baseURL = "http://192.168.3.13:8000"
// Vue.prototype.$ajax = axios
createApp(App).mount('#app')
// createApp(App).use(router).mount('#app')


// Vue.config.productionTip = false
// new Vue({
//     // 注册路由器  Vue.prototype.$router=router
//     router,
//     render: h => h(App),
// }).$mount('#app')
