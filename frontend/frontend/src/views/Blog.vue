<template>
    <div>
        <header>
             <!-- This div is  intentionally blank. It creates the transparent black overlay over the video which you can modify in the CSS -->
        <div class="overlay"></div>

        <!-- The HTML5 video element that will create the background video on the header -->
        <video playsinline="playsinline" autoplay="autoplay" muted="muted" loop="loop">
            <source src="../assets/videoTitle.mp4" type="video/mp4">
        </video>

        <!-- The header content -->
        <div class="container h-100">
            <div class="d-flex h-100 text-right align-items-center">
            <div class="w-150 text-white">
              
            <BlogHeader />
            
            </div>
            </div>
        </div>
        </header>

        <div class="topics-container">
          <div class="row align-items-center">
            <router-link style="text-decoration:none; color:black" to="/topic/Web scraping" class="col-sm">Web Scraping</router-link>
            <router-link style="text-decoration:none; color:black" to="/topic/Exploratory data analysis" class="col-sm">Exploratory Data Analysis</router-link>
            <router-link style="text-decoration:none; color:black" to="/topic/Machine learning" class="col-sm">Machine Learning</router-link>
            <router-link style="text-decoration:none; color:black" to="/topic/Deep learning" class="col-sm">Deep Learning</router-link>
          </div>
        </div>


        
 

        <div class="container">
            
            <PostList />


        </div>


    </div>
</template>

<script>

import BlogHeader from '../components/blogpage/BlogHeader.vue'
import PostList from '../components/blogpage/PostList.vue'


export default {
    name: "Blog",
    components: {
        BlogHeader,
        PostList
    }
}
</script>




<style scoped>
header {
  position: relative;
  background-color: black;
  height: 50vh;
  min-height: 100%;
  width: 100%;
  overflow: hidden;
}

video {
  opacity: 0.3;
}

header video {
  position: absolute;
  top: 50%;
  left: 50%;
  min-width: 100%;
  min-height: 100%;
  width: auto;
  height: auto;
  z-index: 0;
  -ms-transform: translateX(-50%) translateY(-50%);
  -moz-transform: translateX(-50%) translateY(-50%);
  -webkit-transform: translateX(-50%) translateY(-50%);
  transform: translateX(-50%) translateY(-50%);
}

header .container {
  position: relative;
  z-index: 2;
}

header .overlay {
  position: absolute;
  top: 0;
  left: 0;
  height: 100%;
  width: 100%;
  background-color: black;
  opacity: 0.5;
  z-index: 1;
}

.topics-container{
  display: grid;
  font-size: 2.5vh;
  text-align: center;

  overflow:hidden;

  background-color: #f7f7f7;
  margin-bottom: 10vh;
  padding: 2vh;
}

.row{
  display: flex;
  
}


</style>
