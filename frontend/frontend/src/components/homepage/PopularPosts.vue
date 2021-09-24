<template>

<div class="container">
<h1>Popular Posts</h1>
<div id="cards_landscape_wrap-2">
    <div>
        <div class="row">
            <div class="col-xs-12 col-sm-6 col-md-3 col-lg-3" v-for="post in posts" :key="post.title">
                <a href="">
                    <div class="card-flyer">
                        <div class="tag"><router-link style="color:black" to="/posts">{{post.tags[0].name}}</router-link></div>
                        <div class="text-box">
                            <div class="image-box">
                                <img src="https://cdn.pixabay.com/photo/2018/03/30/15/11/deer-3275594_960_720.jpg" alt="" />
                            </div>
                            <div class="text-container">
                                <h6>{{post.title}}</h6>
                                <p>{{post.subtitle}}</p>
                            </div>
                            <div class="ftr">
                                      <div class="author">
                                          <a href="#"> <img src="https://picsum.photos/id/1005/5760/3840" alt="..." class="avatar img-raised"> <span>{{post.author.user.firstName}} {{post.author.user.lastName}}</span> </a>
                                      </div>
                                      <div class="stats"> <i class="far fa-clock"></i> 10 min </div>
                                  </div>

                        </div>
                    </div>
                </a>
            </div>
            
        </div>
    </div>
  </div>
</div>
</template>

<script>

export default {
    name: 'PopularPosts',
    
    props: {
      posts: Array
    },

    computed: {
    popularPosts () {
      return this.posts.filter(post => post.popular)
      }
    }
}
</script>

<style scoped>
h1 {
    margin-bottom: 30px;
    font-size: 5vh;
    font-weight: lighter;
    color:black;
}

.card-flyer .ftr div {
    display: inline-block;
    margin-right: 50px;
}

.tag{
  position: absolute;
  float: left;
  padding-top: 5px;
  min-width: 7vh;
  text-align: left;
  border-style: solid;
  border-width: 1px;
  border-color: rgb(75, 75, 75);
  background-color: rgb(192, 192, 192);
  border-radius: 10px;
  padding:5px;
  text-align: center;
  font-size: 1.5vh;
  color: black;
  font-weight: 600;
  z-index: 100;
}
.avatar {
    width: 36px;
    height: 36px;
    overflow: hidden;
    border-radius: 50%;
    margin-right: 5px;
}
.card-flyer .ftr .stats {
    top: 1px;
    font-size: 14px;
}
.card-flyer .ftr .stats {
    float: right;
    line-height: 30px;
}
.card-flyer{
    min-height: 400px;
}

#cards_landscape_wrap-2{
  text-align: center;
  background: inherit;
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
  box-shadow: 0px 3px 4px rgba(0, 0, 0, 0.50);
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
  margin-top: 10px;
  margin-bottom: 0px;
  padding-bottom: 0px; 
  font-size: 14px;
  letter-spacing: 1px;
  color: #000000;
}
#cards_landscape_wrap-2 .card-flyer .text-box h6{
  margin-top: 0px;
  margin-bottom: 4px; 
  font-size: 18px;
  font-weight: bold;
  text-transform: uppercase;
  font-family: 'Roboto Black', sans-serif;
  letter-spacing: 1px;
  color: #00acc1;
}


</style>