<template>
  <div class='Rent'>
   <h1>Аренда</h1>
   <form @submit.prevent class="inp-form">
   <RentInput
   v-modal="start_data"
   type="text"
   placeholder="Дата начала аренды"
   />
   <RentInput
   v-modal="end_data"
   type="text"
   placeholder="Дата окончания аренды"
   />
   <RentInput
   v-modal="client_email"
   type="text"
   placeholder="Ваша Почта"
   />
    <button class="btn--primary addTask" @click="CreateRent();">Арендовать</button>
    </form>
  
    <RentPageItem 
     v-for="item_data in RENT"
        :rent_item_data ='item_data'
        :key="item_data.id"
        @addToRent='addToRent'
    
  />
  </div>
</template>
<script>
  import {mapGetters,mapActions} from 'vuex'
import RentPageItem from './RentPageItem.vue'
import RentInput from './RentInput.vue'
  export default {
    name: "RentPage",
    components: {
      RentPageItem,
      RentInput
    },
    props: {
      rent_data:{
        type:Array
        
      }
    },
    data() {
      return { 
        start_data:this.start_data,
        end_data:this.end_data,
        client_email:this.client_email

  }
    },
    computed: {
        ...mapGetters([
          'RENT',
          'RENTSS'

        ])
    },
    methods:{
      CreateRent(){
        console.log(this.start_data)
        this.$store.commit('SET_RENTSS',{ 
                                                "start_data": this.RENTSS.start_data,  
                                                "area": this.RENTSS.end_data, 
                                                "floor": this.RENTSS.client_email, 


                });

        

      },
      ...mapActions([
        'GET_RENTSS_FROM_API'

      ])
    

    },
    mounted() {
    this.GET_RENTSS_FROM_API()
    
  },
    

  }
</script>

<style lang="scss" scoped>
.inp-form {
    margin: 15px;
    display: flex;
    flex-direction: column;
    align-items: center;
}
  
</style>
  

