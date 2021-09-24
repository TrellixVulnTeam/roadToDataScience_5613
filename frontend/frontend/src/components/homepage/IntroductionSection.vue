<template>
    <div id="intro">
        <h1 style="font-size:15vh; margin-top:2vh;letter-spacing: 0.05vw;">Road to Data Science</h1>
        <p>Data science is one of the hottest topics of the moment, learning it it's a smart investment for your future</p>
        <p>Begin your road to data science here</p>

        <form method="POST" @submit.prevent="subscribe">
        <div id="email-btn">
            <span>
            <input type="email" id="inlineFormInput" placeholder="Email" v-model="email">
            </span>
            <span>
            <button type="submit" class="btn-primary mb-2">Learn</button>
            </span>
        </div>
        </form>
        <div v-if="subscribed"><p>Congratulations, you joined the newsletter</p></div>

    </div>
</template>

<script>

import { CreateEmail, EmailQuery } from '../../graphqlQueries/graphql'

export default {
    name: "IntroductionSection",
    data () {
        return {
        email: '',
        subscribed: false,
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

.intro{
  width: 90vw;
}


p {
    margin-top: 5vh;
    font-size: 3vh;
    line-height: 4.2vh;
    letter-spacing: 0.05vw;
    text-rendering: optimizeLegibility;
}

input {
    width: 40vh;
    height: 7vh;
    margin-top: 5vh;
    font-size: 2.5vh;
    padding-left: 2vw;
    outline: none;
    font-weight: 500;

}


button {
    width: 14vh;
    height: 7vh;
    font-size: 2.5vh;
    font-weight: 500;
}


</style>