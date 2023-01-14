<template>
  <div class='comment'>
     
        <h3>

            Коментарии
            <form @submit.prevent>
            <input v-bind:value="title" 
            class="input" 
            type="text" 
            @input="title=$event.target.value"
            placeholder="Название">
            <input v-bind:value="body"
             class="input"
             type="text" 
             @input="body=$event.target.value"
             placeholder="Описание">
            <button @click="createPost">создать</button>
            </form>
            <div class="post" v-for="post in posts" :key="post.id" >
    <div><strong>Название:</strong>{{post.title}}</div>
    <div><strong>Название:</strong>{{post.body}}</div>
    </div>
       
        </h3>
        
</div>




</template>

<script>
  export default {
    name: 'CommentPlace',
    components: {
    },
    props: {
    },
    data() {
        return{
            post:[
                {id:1,title:"Коментарий1",body:"Описание Коммаентария1"},
                {id:1,title:"Коментарий1",body:"Описание Коммаентария1"},
                {id:1,title:"Коментарий1",body:"Описание Коммаентария1"},
            ],
            title:'',
            body:''
        }
      
    },
    filters: {
     
    },
    computed: {},
    methods: {
        createPost(){
            const newPost={
                id:Date.now(),
                title:this.title,
                body:this.body,
            }
        this.posts.push(newPost)

        },
    
    },
  
    mounted() {
  
    }
  }
</script>

<style lang="scss">

</style>