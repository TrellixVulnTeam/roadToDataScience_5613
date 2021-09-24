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
              
              <IntroductionSection />


            </div>
            </div>
        </div>
        </header>
        <HomePageSection content="about" color="#e6e6e6" />
        <HomePageSection content="topics" color="white" />

    </div>
</template>

\<script>

import IntroductionSection from '../components/homepage/IntroductionSection.vue'
import HomePageSection from '../components/homepage/HomePageSection.vue'

export default {
    name: "TitleSection",

    components: {
      IntroductionSection,
      HomePageSection
    }
}
</script>


<style scoped>
header {
  position: relative;
  background-color: black;
  height: 115vh;
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
</style>