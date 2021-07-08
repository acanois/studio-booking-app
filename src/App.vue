<template>
  <div id="app">
    <div id="nav">
     <router-link :to="{ name: 'components' }">components</router-link> |
     <router-link :to="{ name: 'landing' }">Landing</router-link> |
     <router-link :to="{ name: 'login' }">login</router-link> |
     <router-link :to="{ name: 'register' }">register</router-link> |
     <router-link :to="{ name: 'profile' }">profile</router-link> |
    </div>
    <router-view/>
  </div>
</template>

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
