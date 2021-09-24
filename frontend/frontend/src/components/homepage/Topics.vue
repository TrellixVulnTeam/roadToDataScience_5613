<template>
<div class="container">
    <div class="title">
        <h1>Are you ready to learn Data Science?</h1>
        <hr>
    </div>
     <p id="introduction-text">
         As you may know data science is one of most trending topics on the internet. The profession of the data scientist infact is one of the most requested on the job market. If you want to explore this amazing world this blog is what you were looking for. In Road to Data Science
         i will talk about the main stages of a data science project. In particular i will explore four topics that i really like: web scraping, data preparation and exploration, machine learning and deep learning. 
    </p>
       <div id="cards_landscape_wrap-2">
        <div class="container">
            <div class="row">
                <div class="col-xs-6 col-sm-3 col-md-3 col-lg-3">
                    <router-link to="topic/Web scraping">
                        <div class="card-flyer">
                            <div class="text-box">
                                <div class="image-box">
                                    <img src="../../assets/web scraping.jpg" alt="" />
                                </div>
                                <div class="text-container">
                                    <h6>Web Scraping</h6>
                                    <p>Web scraping is one of the many ways that a data scientist can use to access data from the internet. If you want to learn more about it click here.</p>
                                </div>
                            </div>
                        </div>
                    </router-link>
                </div>
                <div class="col-xs-12 col-sm-3 col-md-3 col-lg-3">
                    <router-link to="topic/Exploratory data analysis">
                        <div class="card-flyer">
                            <div class="text-box">
                                <div class="image-box">
                                    <img src="../../assets/eda.jpg" alt="" />
                                </div>
                                <div class="text-container">                                    
                                    <h6>EDA</h6>
                                    <p>Before running any ML algorithm data exploration is a fondamental task to do. In this way we can have an idea of how our data behaves.</p>
                                </div>
                            </div>
                        </div>
                    </router-link>
                </div>
                <div class="col-xs-12 col-sm-3 col-md-3 col-lg-3">
                    <router-link to="topic/Machine learning">
                        <div class="card-flyer">
                            <div class="text-box">
                                <div class="image-box">
                                    <img src="../../assets/machine learning.svg" alt="" />
                                </div>

                                <div class="text-container">
                                    <h6>Machine Learning</h6>
                                   <p>Machine Learning consists in the study of a series of algorithms that can learn throught experience. Click here if you want to learn more.</p>
                                </div>
                            </div>
                        </div>
                    </router-link>
                </div>
                <div class="col-xs-12 col-sm-3 col-md-3 col-lg-3">
                    <router-link to="topic/Deep learning">
                        <div class="card-flyer">
                            <div class="text-box">
                                <div class="image-box">
                                    <img src="../../assets/deep learning.svg" alt="" />
                                </div>
                                <div class="text-container">
                                    <h6>Deep Learning</h6>
                                   <p>Deep learning is a subset of machine learning that uses architectures with multiple layers to extract informations from the data.</p>
                                </div>
                            </div>
                        </div>
                    </router-link>
                </div>
            </div>
        </div>
    </div>
</div>
</template>

<script>
export default {
    name: 'Topics'
}
</script>

<style scoped>
h1 {
    margin-bottom: 20px;
    font-size: 6vh;
    font-weight: lighter;
}

.title{
    width: 100%;
    text-align: center;
    margin-bottom: 5vh;
}
hr{
    display: block;
    margin-left: auto;
    margin-right: auto;
    width: 7vw;
    height: 0.5vh;
    color: rgb(14, 99, 173);
}

#introduction-text{
    text-align: center;
    font-size: 3vh;
    margin-bottom: 1vh;
    color: rgba(41, 41, 41, 1);
    line-height: 4vh;
    letter-spacing: -0.1vh;
}

.container{
    min-height: 100%;
    margin-bottom: 30px;
}
.card-flyer{
    display: block;
    margin-left: auto;
    margin-right: auto;
    min-height: 30vw;
    min-width: 15vh;
    max-width: 70vw;
}

#cards_landscape_wrap-2{
  text-align: center;
  background: #ffffff;
}
#cards_landscape_wrap-2 .container{
  padding-top: 80px; 
  padding-bottom: 100px;
}
#cards_landscape_wrap-2 a{
  text-decoration: none;
  outline: none;
}
#cards_landscape_wrap-2 .card-flyer {
  border-radius: 5px;
}
#cards_landscape_wrap-2 .card-flyer .image-box{
  background: #ffffff;
  overflow: hidden;
  box-shadow: 0px 2px 15px rgba(0, 0, 0, 0.50);
  border-radius: 5px;
}
#cards_landscape_wrap-2 .card-flyer .image-box img{
  -webkit-transition:all .9s ease; 
  -moz-transition:all .9s ease; 
  -o-transition:all .9s ease;
  -ms-transition:all .9s ease; 
  width: 100%;
  height: 200px;
}
#cards_landscape_wrap-2 .card-flyer:hover .image-box img{
  opacity: 0.7;
  -webkit-transform:scale(1.15);
  -moz-transform:scale(1.15);
  -ms-transform:scale(1.15);
  -o-transform:scale(1.15);
  transform:scale(1.15);
}
#cards_landscape_wrap-2 .card-flyer .text-box{
  text-align: center;
}
#cards_landscape_wrap-2 .card-flyer .text-box .text-container{
  padding: 30px 18px;
}
#cards_landscape_wrap-2 .card-flyer{
  background: #FFFFFF;
  margin-top: 50px;
  -webkit-transition: all 0.2s ease-in;
  -moz-transition: all 0.2s ease-in;
  -ms-transition: all 0.2s ease-in;
  -o-transition: all 0.2s ease-in;
  transition: all 0.2s ease-in;
  box-shadow: 0px 3px 4px rgba(0, 0, 0, 0.40);
}
#cards_landscape_wrap-2 .card-flyer:hover{
  background: #fff;
  box-shadow: 0px 15px 26px rgba(0, 0, 0, 0.50);
  -webkit-transition: all 0.2s ease-in;
  -moz-transition: all 0.2s ease-in;
  -ms-transition: all 0.2s ease-in;
  -o-transition: all 0.2s ease-in;
  transition: all 0.2s ease-in;
  margin-top: 50px;
}
#cards_landscape_wrap-2 .card-flyer .text-box p{
  display: block;
  margin-top: auto;
  margin-bottom: auto;

  padding-top: 2vh;
  
  padding-bottom: 2vh; 
  font-size: 2.5vh;
  letter-spacing: 0.05vw;
  color: #000000;
}
#cards_landscape_wrap-2 .card-flyer .text-box h6{
  margin-top: 0px;
  margin-bottom: 4px; 
  font-size: 18px;
  font-weight: bold;
  text-transform: uppercase;
  font-family: 'Roboto Black', sans-serif;
  letter-spacing: 0.05vw;
  color: rgba(102, 138, 170, 1);
}


</style>
