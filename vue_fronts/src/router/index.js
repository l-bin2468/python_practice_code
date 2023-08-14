import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../components/test.vue'

Vue.use(VueRouter)

const routes = [
    {
        path: '/',
        name: 'Home',
        component: Home
    },
    // {
    //     path: '/about',
    //     name: 'About',
    //     component: () => import(/* webpackChunkName: "about" */ '../views/About.vue')
    // },
    // {
    //     path: '/class',
    //     name: 'class',
    //     component: () => import(/* webpackChunkName: "about" */ '../views/class.vue')
    // }
]

const router = new VueRouter({
    routes
})

export default router

