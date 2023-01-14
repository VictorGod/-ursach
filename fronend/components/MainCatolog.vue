<template>
  <div class='cart'>
     <router-link :to="{ name: 'Cart'}"> 
    <button class="btn--primary addTask">Вариантов в корзине:    {{CART.length}}</button>
    </router-link>
    <SelectPlace
      :selected="selected"
      :options="Categories"
      @select="sortByCategories"
      />
      <div class='range-slider'> 
        определи границы стоимости: 
        <input type="range" min='0' max='5000' step="500" v-model.number="minPrice"
        @change="setChngeSlider"
        >
        <input type="range" min='0' max='5000' step="500" v-model.number="maxPrice"
        @change="setChngeSlider"
        >
          
      </div>
      <div class="range-values">
        <p>Минимальная цена:      {{minPrice}}</p>
        <p>Максимальная цена:     {{maxPrice}}</p>
      </div>
    <h1>Каталог</h1>
    <h2>На сервисе {{PLACE.length}} коворкингов
      из них на качество проверено {{PLACE.length}}
    </h2>
      <CatalogItem 
        v-for="place in filteredPlace"
        :key="place.id"
        :place_data ='place'
        :cart_data="CART"
        @addToCart="addToCart"  
      />
      <router-link :to="{ name: 'LandLord'}"> 
    <button class="btn--primary addTask">Арендодатели</button>
    </router-link>
      
      
  </div>
</template>

<script>
   import {mapActions,mapGetters} from 'vuex'
  import CatalogItem from './CatalogItem.vue'
  import SelectPlace from './SelectPlace.vue'

  export default {
    name: "MainCatalog",
    components: {
       CatalogItem,
       SelectPlace,
    
       
      

    },
    props: {},
    data() {
      return {
        Categories:[
          {name:'Метро:',value:'All'},
          {name:'Люблино',value:'l'},
          {name:'Печатники',value:'p'}
        ],
        selected: 'Выбери Метро',
        sortedPlase:[],
        minPrice:0,
        maxPrice:5000
        

        
  }
    },
    computed: {
       ...mapGetters([
         'PLACE',
         'CART',
         'SEARCH_'
     ]),
     filteredPlace(){
      if (this.sortedPlase.length){
        return this.sortedPlase
      }
      else{
        return this.CART
      }
     }
    
    },
    methods: {
      ...mapActions([
        'GET_PLASE_FROM_API',
        'ADD_TO_CART'
      ]),
      setRangeSlider() {
        if (this.minPrice > this.maxPrice) {
          let tmp = this.maxPrice;
          this.maxPrice = this.minPrice;
          this.minPrice = tmp;
        }
        this.sortByCategories()
      },
      sortByCategories(undeground) {
        let vm = this;
        this.sortedPlase = [...this.PLACE]
        this.sortedPlase = this.sortedPlase.filter(function (item) {
          return item.price >= vm.minPrice && item.price <= vm.maxPrice
        })
        if (undeground) {
          this.sortedPlase = this.sortedPlase.filter(function (e) {
            vm.selected === undeground.name;
            return e.undeground === undeground.name
          })
        }
      },

      addToCart(data){
        this.ADD_TO_CART(data)
      },

  

       
      
    },
    watch: {
     
      },

   mounted() {
    this.GET_PLASE_FROM_API()
    
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
