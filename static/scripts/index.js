$(function(){
	   $("#skin li").click(function(){
	   	    var index=$("#skin").find("li").index(this);
	        $(this).addClass("selected").siblings().removeClass("selected");
	        $("#skinStyle").attr("href","./css/skin/skin_"+index+".css");
	        $.cookie("MyCssSkin",index,{path:'/',expires:10});
	   })
		var cookieSkin=$.cookie("MyCssSkin");
		if (cookieSkin) {
			  $("#skin_"+cookieSkin).addClass("selected").siblings().removeClass("selected");
			  $("#skinStyle").attr("href","./css/skin/skin_"+cookieSkin+".css");
	   }
	/*input.js  Input field effect*/
	$("#my").focus(function(){
		/*By default, you don't have to change the border anymore*/
		if($(this).val()==this.defaultValue){
			$(this).val("");
		}
	}).blur(function(){
		if ($(this).val()=="") {
			$(this).val(this.defaultValue);
		}

	}).keyup(function(e){
		if (e.which==13) {
			alert("开始搜索");
		}
	})
   /*skin.js  In the skin effect*/


   /*nav.js  Effect of navigation*/
   $(".nav li").hover(function(){
   	    $(this).find(".subItem").show();
     }, function(){
    	$(this).find(".subItem").hide();
   })

   $(".classification .promoted").append("<s class='hot'></s>")/*Jquery adds elements*/

   var index=0;
   var timer1=null;
   var len=$("#RsidePictureTurn div a").length;
   $("#RsidePictureTurn div a").mouseover(function(){
          index=$("#RsidePictureTurn div a").index(this);
          showImage(index);
   }).eq(0).mouseover();
   $("#RsidePictureTurn").hover(function(){
          if (timer1) {
          	clearInterval(timer1)
          }
	   },function(){
          timer1=setInterval(function(){
             showImage(index);
             index++;
             if (index==len) {
             	index=0;
             }
          },3000)
	   }).trigger("mouseleave");
   function showImage(num){
   	    var iNow=$("#RsidePictureTurn").find("div>a")
        var iNowHref=iNow.eq(num).attr("href");
        $("#RsidePictureTurn>a").attr("href",iNowHref).find("img").eq(num).stop(true,true).fadeIn()
        .siblings().fadeOut();
        iNow.removeClass("chos").css("opacity","0.7").eq(num).addClass("chos").css("opacity","1")
   }

  /* Hyperlink prompt，tooltip.js*/
  var x=10;
  var y=10;
  $("#RsideBrand a").mouseover(function(e){
  	  this.myTitle=this.title;
  	  var tooltip="<div id='tooltip'>"+this.myTitle+"</div>";
  	  $("body").append(tooltip);
  	  $("#tooltip").css({
           "top":(e.pageY+y)+"px",
           "left":(e.pageX+x)+"px"
  	  }).show("fast");
  }).mousemove(function(e){
      $("#tooltip").css({
           "top":(e.pageY+y)+"px",
           "left":(e.pageX+x)+"px"
  	  })
  }).mouseout(function(){
  	 $("#tooltip").remove();

  })
  /*imgSlide.js Horizontal scrolling effect*/

  $("#jnBrandTab a").click(function(){
        $(this).parent().addClass("chos").siblings().removeClass("chos");
        var index=$("#jnBrandTab a").index(this);
        showBrandList(index);
  })
  function showBrandList(num){
      var moveLeft=$("#jnBrandList").find("li").outerWidth()+10;
      var totalMove=moveLeft*4;
      $("#jnBrandList").stop(true,false).animate({left:-totalMove*num},1000)/*不需要单位*/
  }

  /*imgHover.js The cursor across*/
  $("#jnBrandList li").each(function(index){
      var $img=$(this).find("img");
      var imgW=$img.width();
      var imgH=$img.height();
      var spanHTML='<span style="position:absolute;top:0;left:0;width:'+imgW+'px;height:'+imgH+'px;" class="imageMask"></span>';
      $(spanHTML).appendTo(this);
  })
  $("#jnBrandList").delegate(".imageMask","hover",function(){
  	  $(this).toggleClass("imageOver");
  })

})