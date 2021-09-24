<template>
    <div>
        <!-- Footer -->
<footer class="bg-dark text-center text-white">
  <!-- Grid container -->
  <div class="container p-4">
    <!-- Section: Social media -->
    <section class="mb-4">
      <!-- Facebook -->
      <a class="btn btn-outline-light btn-floating m-1 social" href="#!" role="button"
        >
        <img src="../assets/facebook.svg" alt="">
        <i class="fab fa-facebook-f">Facebook</i
      ></a>

      <!-- Twitter -->
      <a class="btn btn-outline-light btn-floating m-1 social" href="#!" role="button">
        <img src="../assets/twitter.svg" alt="">
        <i class="fab fa-twitter">Twitter</i
      ></a>


      <!-- Instagram -->
      <a class="btn btn-outline-light btn-floating m-1 social" href="#!" role="button">
        <img src="../assets/instagram.svg" alt="">
        <i class="fab fa-instagram">Instagram</i
      ></a>

      <!-- Linkedin -->
      <a class="btn btn-outline-light btn-floating m-1 social" href="#!" role="button">
        <img src="../assets/linkedin.svg" alt="">
        <i class="fab fa-linkedin-in">Linkedin</i
      ></a>

      <!-- Github -->
      <a class="btn btn-outline-light btn-floating m-1 social" href="#!" role="button">
        <img src="../assets/github.svg" alt="">
        <i class="fab fa-github">Github</i
      ></a>
    </section>
    <!-- Section: Social media -->

    <!-- Section: Form -->
    <section class="">
      <form action="POST" @submit.prevent="subscribe">
        <!--Grid row-->
        <div class="row d-flex justify-content-center">
          <!--Grid column-->
          <div class="col-auto">
            <p class="pt-2">
              <strong>Join the newsletter</strong>
            </p>
          </div>
          <!--Grid column-->

          <!--Grid column-->
          <div class="col-md-5 col-12">
            <!-- Email input -->
            <div class="form-outline form-white mb-4">
              <input type="email" id="form5Example2" class="form-control" v-model="email"/>
              <label class="form-label" for="form5Example2">Email address</label>
            </div>
          </div>
          <!--Grid column-->

          <!--Grid column-->
          <div class="col-auto">
            <!-- Submit button -->
            <button type="submit" class="btn btn-outline-light mb-4">
              Subscribe
            </button>
          </div>
          <!--Grid column-->
        </div>
        <!--Grid row-->
      </form>
      <div v-if="subscribed" style="text-align:center; width:100%"><p>Congratulations, you joined the newsletter</p></div>

    </section>
    <!-- Section: Form -->

  </div>

  <!-- Copyright -->
  <div class="text-center p-3" style="background-color: rgba(0, 0, 0, 0.2);">
    {{copyRight}}
    <a class="text-white" href="https://mdbootstrap.com/">RoadtoDataScience.com</a>
  </div>
  <!-- Copyright -->
</footer>
<!-- Footer -->
    </div>
</template>

<script>

import { CreateEmail, EmailQuery } from '../graphqlQueries/graphql'


export default {
    name: "Footer",
    data() {
    return {
      email: '',
      currentYear: new Date().getFullYear(), // 2020
      subscribed: false
    }
  },
  computed:{
    copyRight(){
      return '@ ' + this.currentYear + ' Copyright: '
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
img{
  width: 5vh;
}

.social{  
  margin-right: 1vh;
  margin-left: auto;
  widows: 3vw;
}



</style>