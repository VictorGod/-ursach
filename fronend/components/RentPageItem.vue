<template>
  <div class='rent_item'>
  <div class='card'>
    <p>ID места:{{rent_item_data.id}}</p>
    <p>Адрес:{{rent_item_data.address}}</p>
    <p>Метро:{{rent_item_data.undeground}}</p>
    <p>Цена за день:{{rent_item_data.price}}</p>
  </div>
  </div>
</template>
   
<script> 

  export default {
    name: "CartRentItem",
    components: {
    

    },
    props: {
      rent_item_data:{
        type: Object,
        default() {
          return{}

        }
      }


    },
    data() {
      return {
        
  }
    },
    computed: {
  
    },
    methods: {
      addToRent(){
       this.$emit('addToRent',this.rent_item_data);
      }

      

     

       
      
    },
    watch: {
     
      },

   mounted() {

    
    
  },
  }
</script>

<style lang="scss">


</style>
