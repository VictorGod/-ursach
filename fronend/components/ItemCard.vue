<template>
  <div class="card">
        <div class="card__container">
            <div  class="title">
                <div v-if="this.item.type === 'rent'" class="stats__car">
                    <p class="point">ID коворкинга:{{ this.place_data.place_id }}</p>
                    <p class="point">Адресс:{{ this.place_data.address }}</p>
                    <p class="point">Цена за день: {{ this.place_data.place_id }}</p>

                </div>
            </div>
        </div>
  </div>
</template>

<script>
export default {
    props: {
        place_data: {
            type: Object,
            required: true
        }
    }
}
</script>

<style>
.card {
    position: relative;
    display: inline-block;
}
.card__container {
    margin: 10px;
    position: relative;
    border-radius: 15px;
    background:  #fff;
    box-shadow: 1px -1px 5px gray;
    display: inline-flex;
    display: block;
    justify-content: space-between;
    flex-direction: column;
    padding: 10px;
}

.img {
    width: 250px;
    height: 250px;
}
</style>