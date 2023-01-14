<template>
  <div id="app">
  <MainWR />
  </div>

</template>

<script >
import MainWR from './components/main-wrapper.vue';


export default {
  name: "App",
  components: {
    MainWR
   
    
  },
};
</script>

<style lang="scss">
@import url("~@/assets/styles/style.css");
#app {
  max-width: 2000px;
  margin: auto;
}
body {
  overflow: overlay;
}
</style>