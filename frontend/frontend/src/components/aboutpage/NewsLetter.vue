<template>
  <div class="newsletter">
    <p class="sign-up">Sign up to the newsletter</p>
    <p class="desc">Stay tuned for more great articles!</p>

    <form action="POST" @submit.prevent="subscribe">
    <input type="email" id="inlineFormInput" placeholder="Email" v-model="email">
    <button type="submit" class="btn-primary mb-2">Learn More</button>

    </form>
    <div v-if="subscribed"><p class="desc">Congratulations, you joined the newsletter</p></div>
  </div>

</template>


<script>

import { CreateEmail, EmailQuery } from '../../graphqlQueries/graphql'


export default {
    name:'NewsLetter',
    data(){
        return{
            email: '',
            subscribed: false
        }
    },
    methods:{
    async subscribe() {
    const email = this.email

    if (email !== ''){
      this.subscribed = true
  
      // Call to the graphql mutation
      let data = await this.$apollo.mutate({
        // Query
        mutation: CreateEmail,
        // Parameters
        variables: {
          email: email,
        },
        update: (store, { data: { createEmail } }) => {
          // Add to All tasks list
          const data = store.readQuery({ query: EmailQuery })
          data.emails.push(createEmail.email)
          store.writeQuery({ query: EmailQuery, data })
        },
        })
        console.log( data)
    }

    }
    }
    
}
</script>

<style scoped>

.newsletter{
  display: block;
  margin-left: auto;
  margin-right: auto;
  width: 100%;
  max-width: 90vh;

  background-color: #ffffff;
  background-image: linear-gradient(0deg, #ffffff 0%, #f7f7f7 74%);
  min-height: 33vh;
  padding: 5vh;

  border-top-style: solid;
  border-top-color: rgba(102, 138, 170, 1);
  border-top-width: 3px;

  margin-bottom: 10vh;
}

input {
    width: 40vh;
    height: 7vh;
    margin-top: 60px;
    font-size: 2vh;
    padding-left: 30px;
    outline: none;

}

button {
    width: 14vh;
    height: 7vh;
    font-size: 2vh;
    background-color: rgba(102, 138, 170, 1);
    border-style: none;
    border-color: rgba(102, 138, 170, 1);
    outline: none;
}


.sign-up{
  font-size:4vh;
  font-weight:700;
}
.desc{
  font-size:2.2vh;
}

</style>