<template>
<div class="container">

    <div class="row">

      <div class="col-lg-8 col-lg-offset-2">

        <h1>Send me a message</h1>

        <p class="lead">Do you want to ask me something?</p>
        <p>Fill the form and send me your message!</p>

        <form id="contact-form" method="post" action="contact.php" role="form" @submit.prevent="sendMessage">

        <div class="messages"></div>

        <div class="controls">

          <div class="row">
            <div class="col-md-6">
              <div class="form-group">
                <label for="form_name">Firstname *</label>
                <input id="form_name" type="text" name="name" class="form-control" placeholder="Please enter your firstname *" required="required" data-error="Firstname is required." v-model="firstName">
                <div class="help-block with-errors"></div>
              </div>
            </div>
            <div class="col-md-6">
              <div class="form-group">
                <label for="form_lastname">Lastname *</label>
                <input id="form_lastname" type="text" name="surname" class="form-control" placeholder="Please enter your lastname *" required="required" data-error="Lastname is required."  v-model="lastName">
                <div class="help-block with-errors"></div>
              </div>
            </div>
          </div>
          <div class="row">
            <div class="col-md-6">
              <div class="form-group">
                <label for="form_email">Email *</label>
                <input id="form_email" type="email" name="email" class="form-control" placeholder="Please enter your email *" required="required" data-error="Valid email is required." v-model="email">
                <div class="help-block with-errors"></div>
              </div>
            </div>
            <div class="col-md-6">
              <div class="form-group">
                <label for="form_phone">Phone</label>
                <input id="form_phone" type="tel" name="phone" class="form-control" placeholder="Please enter your phone" v-model="phone">
                <div class="help-block with-errors"></div>
              </div>
            </div>
          </div>
          <div class="row">
            <div class="col-md-12">
              <div class="form-group">
                <label for="form_message">Message *</label>
                <textarea id="form_message" name="message" class="form-control" placeholder="Write your message here" rows="4" required="required" data-error="Please,leave us a message." v-model="msg"></textarea>
                <div class="help-block with-errors"></div>
              </div>
            </div>
            <div class="col-md-12">
              <input type="submit" class="btn btn-success btn-send" value="Send message">
            </div>
          </div>
          <div class="row">
            <div class="col-md-12">
              <p class="text-muted"><strong>*</strong> These fields are required.</p>
            </div>
          </div>
          
          <div v-if="messageSent"><p class="desc">Your message has been sent</p></div>

        </div>

        </form>

      </div>

    </div>


</div>
</template>

<script>

import { CreateMessage, MessageQuery } from '../../graphqlQueries/graphql'


export default {
  name: 'ContactForm',

  data(){
    return{
      firstName: '',
      lastName: '',
      email: '',
      phone: '',
      msg: '',

      messageSent: false

    }
  },

  methods:{
    
    async sendMessage() {
    const firstName = this.firstName
    const lastName = this.lastName
    const email = this.email
    const phone = this.phone
    const message = this.msg

    if (message !== ''){
      this.messageSent = true
  
      // Call to the graphql mutation
      let data = await this.$apollo.mutate({
        // Query
        mutation: CreateMessage,
        // Parameters
        variables: {
          firstName: firstName,
          lastName:lastName,
          email: email,
          phone: phone,
          message:message
        },
        update: (store, { data: { createMessage } }) => {
          // Add to All tasks list
          const data = store.readQuery({ query: MessageQuery })
          data.messages.push(createMessage.message)
          store.writeQuery({ query: MessageQuery, data })
        },
        })
        console.log(data)
    }

    }
  }
}
</script>


<style scoped>

.container{
    min-height: 100vh;
    margin-top: 10vh;
    margin-bottom:10vh;
    width: 80vw;

}

.col-lg-8 {
    width: 100%;
}


h1{
    margin-bottom: 5vh;
}

input{
    margin-top: 3vh;
}

p{
    font-size: 2.5vh;
}

label{
    font-size: 2vh;
    font-weight: 600;
    margin-bottom: 1vh;
    margin-top: 3vh;
}

</style>