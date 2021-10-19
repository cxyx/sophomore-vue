<template>
<!-- todo:step1:应用路由 -->
  <div id="app">
    <img src="./assets/logo.png"><br />
    <router-link to="/">Root</router-link>
    <router-link to="/user">User</router-link>
    <hr />
    <router-view/>
  </div>
</template>

<script>
export default {
  name: 'App'
}
</script>
<!--样式-->
<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
