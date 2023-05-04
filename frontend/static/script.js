/* Карусель слайдер */

 function carouselFn(){
 if ($(window).width() < 820){
    $("#slider").owlCarousel({
        items: 4,
        margin: 5,
     });
  }
  else{
   $("#slider").owlCarousel({
        items: 8,
        margin: 10,
   });
  }
 }

 $(document).ready(function() {
     carouselFn();
});
$(window).resize(function(){
     carouselFn();
 });
