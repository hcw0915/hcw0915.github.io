<template>
    <div class="menu">
        <router-link to="/about">About</router-link>
        <router-link to="/courses">Courses</router-link>
        <router-link to="/booking">Booking</router-link>
    </div>
</template>

<style scoped>
  .menu {
    background-color: white;
    text-align: right;
    margin: 20px 0;
  }

  a {
    text-decoration: none;
    color: #42b983;
    font-size: 24px;
    padding: 1em 2em;
    font-size: 26px;
    
  }

  a:hover{
    background-color: #42b98320;
  }
</style>