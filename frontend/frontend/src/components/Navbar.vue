<template>
 <nav class="navigation">
      <router-link to="/" class="navbar-logo">Logo</router-link>
      <div class="navbar-right">
        <router-link style="text-decoration:none" to="/about">About</router-link>
        <router-link style="text-decoration:none" to="/blog">Blog</router-link>
        <router-link style="text-decoration:none" to="/contact">Contact</router-link>
      </div>
    </nav>

</template>

<script>
export default {
    name: 'Navbar'
}
</script>

<style scoped>
.navigation{
  padding-top:30px;
  padding-bottom:30px;
  position:absolute;
  top:0;
  min-width:100%;
  z-index:10;
}

.navbar-right{
  float:right;
  padding-right:10%;
  font-size: 2vh;
}

.navbar-right a{
  text-decoration:none;
  padding:10px;
  color: white;
}

.navbar-right a:hover{
  text-decoration:underline;
}
.navbar-logo{
  padding-left:10%;
  font-size:2vh;
  text-decoration:none;
  color:#fff; 
}

</style>