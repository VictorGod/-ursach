<template>
  <div class='card'>
    
    <text>
    <p class="CatalogItem__address">Название компании:  {{landlord_data.full_name}}</p>
    <p class="CatalogItem__address">Адрес:  {{landlord_data.address}}</p>
    <p class="CatalogItem__address">Почта:{{landlord_data.work_email}}</p>
    <p class="CatalogItem__address">телеграмм менеджера:{{landlord_data.manager_telegram_name}}</p>
    </text> 
    
 
  </div> 
</template>

<script>

  export default {
    name: 'LandLordIteam',
    components: {
    },
    props: {
      landlord_data: {
        type: Object,
        default() {
          return {}
        }
      }

    },
    data() {
      return {
  

      }
      
    },
    filters: {
     
    },
    computed: {},
    methods: {
     

      
      
     
    
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