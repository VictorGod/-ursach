<template>
  <div class='card'>
    <ModalInfo
    
    v-if="ModalInfoVisible"
    rightBtnTitle="+"
    :popupTitle="place_data.id"
    @closePopup='closeInfoPopup'
    @rightBtnAction="addToCart"
    
  >
    <div>
    <p class="CatalogItem__bio"> о месте:{{place_data.openings_hourss_data}}</p> 
    </div>
   


  
    
    </ModalInfo>
    <text>
      <!-- <img class="CatalogItem__img" :src="require('../assets/img/'+place_data.image) "> -->
    <p class="CatalogItem__address">Адрес:{{place_data.address}}</p>
    <p class="CatalogItem__undeground">Метро:{{place_data.undeground}}</p>
    <p class="CatalogItem__table">место:{{place_data.table}}</p>
    <p class="CatalogItem__square">площадь:{{place_data.square}}</p>
    <p class="CatalogItem__floor">этаж:{{place_data.floor}}</p>
    <p class="CatalogItem__bio"> о месте:{{place_data.bio}}</p> 
    <p class="CatalogItem__price">Цена:{{place_data.price}}</p> 
    
    </text> 
    
    
    
    <button class="pencil" @click="addToCart" >
      <img src="@/assets/img/cart.svg" alt="Delete" color=white />
    </button>
    <button class="check" @click="showModalInfo" >
       <img src="@/assets/img/zoom-in.svg" alt="Delete" color=white />
    </button>
    

  </div> 
</template>

<script>
import ModalInfo from './ModalInfo.vue'
  export default {
    name: 'CatalogItem',
    components: {
      ModalInfo
    },
    props: {
      place_data: {
        type: Object,
        default() {
          return {}
        }
      }

    },
    data() {
      return {
        ModalInfoVisible:false

      }
      
    },
    filters: {
     
    },
    computed: {},
    methods: {
      addToCart(){
        this.$emit('addToCart',this.place_data)
      },
      showModalInfo(){
        this.ModalInfoVisible=true

      },
      closeInfoPopup(){
        this.ModalInfoVisible=false

      },

      
      
     
    
    },
    mounted() {
  
    }
  }
</script>

<style lang="scss">
.CatalogItem {
    position: relative;
	min-height: 250px;
	height: fit-content;
	width: 30%;
	background: var(--gray);
	box-shadow: 4px 4px 10px -5px var(--black);
	border-radius: 15px;
	padding: 15px;
	padding-bottom: 90px;
	margin:  0 auto;
    
}

</style>