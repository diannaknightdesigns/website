$(window).on("load",function(){
  $('.portfolio').masonry({});
  $('.portfolio .card').on("click",function(){
    $('.carousel-item').removeClass("active");
    $('#modal-'+this.id).addClass("active");
  });
});