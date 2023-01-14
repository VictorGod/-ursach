<template>
  <div class='cart'>
     <h1>Арендодатели</h1>
     <LandLordIteam
     v-for="landlord in LANDLORD"
        :key="landlord.id"
        :landlord_data="landlord"  
     
     />
     
      
  </div>
</template>

<script>
   import {mapActions,mapGetters} from 'vuex'
  import LandLordIteam from './LandLordIteam.vue'

  export default {
    name: "LandLord",
    components: {
    LandLordIteam  

    
       
      

    },
    props: {},
    data() {
      return { 
      }
    },
    computed: {
       ...mapGetters([
        "LANDLORD"
        
     ]),
    
    },
    methods: {
      ...mapActions([
        "GET_LANDLORDS_FROM_API"
      
      ]),
       
    },
    watch: {
     
      },

   mounted() {
    this.GET_LANDLORDS_FROM_API()
    
    
  },
  }
</script>

<style lang="scss" scoped>
@import url("~@/assets/styles/style.css");
.catalog {
    &__list {
      display: flex;
      flex-wrap: wrap;
      justify-content: space-between;
      align-items: center;
    }
    &__image {
      width: 100%;
    height: auto;
   }
   
}

</style>
