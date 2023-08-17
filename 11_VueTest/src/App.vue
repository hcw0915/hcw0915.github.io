<template>
  <div class="app">
    <Menu />
    <div class="bg"></div>
    <div class="content">
      <router-view />
    </div>
    <Footer />
  </div>
</template>

<script>
import Menu from "./Menu.vue";
import Footer from "./Footer.vue";

export default {
  components: {
    Menu,
    Footer
  }
};
</script>

<style>
html,
body,
.app {
  height: 100%;
  padding: 0;
  margin: 0;
  font-family: Arial;
  color: #444;
}
</style>

<style scoped>
.bg {
  width: 100%;
  height: 550px;
  background: url("../src/assets/img/bg.jpg") center center;
  background-size: cover;
}
</style>
