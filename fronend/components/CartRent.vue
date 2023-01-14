<template>
  <div class='Cart'>
   <h1>Корзина</h1>
   <router-link :to="{ name: 'Catolog'}"> 
    <button class="btn--primary addTask">Каталог</button>
    </router-link> 
  <CartRentItem 
      v-for="(item,index) in CART"
        :key="item.id"
        :cart_item_data ='item'
        @deleteFromCart='deleteFromCart(index)'
        @addToRent='addToRent'
  
      
  />
  
  </div>
</template>
<script>
  import CartRentItem from './CartRentItem.vue'
  import {mapActions,mapGetters} from 'vuex'
  export default {
    name: "CartRent",
    components: {
       CartRentItem,
    },
    props: {
      cart_data:{
        type:Array,
        default(){
          return[]
        }
      }
    },
    data() {
      return { 
  }
    },
    computed: {
        ...mapGetters([
          'CART',

        ])
    },
    methods:{
      ...mapActions([
        'DELETE_FROM_CART',
         'ADD_TO_RENT'
      ]),
      deleteFromCart(index){
        this.DELETE_FROM_CART(index)
        
      },
      addToRent(data){
        this.ADD_TO_RENT(data)
      } 

    }

  }
</script>

<style lang="scss" scoped>

  
</style>
  

