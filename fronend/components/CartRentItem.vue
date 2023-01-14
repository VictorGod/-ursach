<template>
  <div class='card'>
  <!-- <img class="cart_item__img" :src="require('../assets/img/'+cart_item_data.image) "> -->
   <p>{{cart_item_data.address}}</p>
    <p>{{cart_item_data.undeground}}</p>
    <p>{{cart_item_data.price}}</p>
 

   
  <button class="pencil" @click="deleteFromCart"  >
  <img src="@/assets/img/x-octagon.svg" alt="Delete" color=white />
  </button>
    <router-link :to="{ name: 'Rent'}"> 
     <button class="check" @click="addToRent"  >
  <img src="@/assets/img/check-mark.svg" alt="Арендовать" color=white />
     </button>
    </router-link> 
  
  </div>
</template>

<script> 

  export default {
    name: "CartRentItem",
    components: {
    

    },
    props: {
      cart_item_data:{
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
      deleteFromCart(){
        this.$emit('deleteFromCart')
      },
      addToRent(){
       this.$emit('addToRent',this.cart_item_data);
      }

      

     

       
      
    },
    watch: {
     
      },

   mounted() {

    
    
  },
  }
</script>

<style lang="scss">
.cart_item{
    position: relative;
	min-height: 250px;
	height: fit-content;
	width: 90%;
	background: var(--gray);
	box-shadow: 4px 4px 10px -5px var(--black);
	border-radius: 15px;
	padding: 15px;
	padding-bottom: 90px;
	margin:  0 auto;

   &__image {
      width: 130px;
   }
  
}

</style>
