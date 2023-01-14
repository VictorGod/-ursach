<template>
  <div  class='main-wrapper'>
    <header>
      <div class="title">
        <a href="/">
          <h1 class='logo'>CoworkingTime</h1>
        </a>
      </div>
     <div class="search-field">
      <input
          type="text"
          v-model="searchValue"
      >
      <button class="search_btn" @click="search">
      поиск
      </button>
    </div>
    </header>

    <main>
      <router-view v-slot="{ Component }">
  <keep-alive>
    <component :is="Component" />
  </keep-alive>
</router-view>
    </main>
    <footer>
      <p>Savenckov Victor , 211-321</p>
    </footer>
  </div>
</template>

<script >
import {mapActions,mapGetters} from 'vuex'
export default {
  name: "MainWR",
 components: {

    },
 
   props: {},
    data() {
      return {
        searchValue:''
      };
      
    },
    filters: {
     
    },
    computed: {
      ...mapGetters([
            'SEARCH_VALUE'
        ])
    },
    methods: {
      ...mapActions([
        'GET_SEARCH_VALUE_TO_VUEX'

        ]),
        search(value){
            this.GET_SEARCH_VALUE_TO_VUEX(value);
            this.$router.push('/catolog')
            
        }
  
    
    },
    mounted() {
  
    },
  }
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
 .search-field {
      padding: 16px;
      position: relative;
      right: 200px;
      display: flex;
      justify-content: center;
      align-items: center;
    }
    .search_btn {
      margin-left: 16px;
      background: transparent;
      border: none;
    }
</style>