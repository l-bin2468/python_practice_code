<template>
<!--  <img alt="Vue logo" src="./assets/logo.png">-->
  <img alt="Vue logo" src="./assets/_logo.jpg">
  <HelloWorld msg="Welcome to Your Vue.js App"/>
</template>

<script>
import HelloWorld from './components/test.vue'

export default {
  name: 'App',
  components: {
    HelloWorld
  },

  methods: {

  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
