$(function(){
	/**************The number of add and subtract***************/
	$(".num .sub").click(function(){
		var num = parseInt($(this).siblings("span").text());
		if(num<=1){
			$(this).attr("disabled","disabled");
		}else{
			num--;
			$(this).siblings("span").text(num);
			//Gets numbers other than currency symbols
			var price = $(this).parents(".number").prev().text().substring(1);
			//Multiply unit price and quantity and leave two decimal places
			$(this).parents(".th").find(".sAll").text('￥'+(num*price).toFixed(2));
			jisuan();
			zg();
		}
	});
	$(".num .add").click(function(){
		var num = parseInt($(this).siblings("span").text());
		if(num>=5){
			confirm("限购5件");
		}else{
			num++;
			$(this).siblings("span").text(num);
			var price = $(this).parents(".number").prev().text().substring(1);
			$(this).parents(".th").find(".sAll").text('￥'+(num*price).toFixed(2));
			jisuan();
			zg();
		}
	});
	//Calculate the total price
	function jisuan(){
		var all=0;
		var len =$(".th input[type='checkbox']:checked").length;
		if(len==0){
			 $("#all").text('￥'+parseFloat(0).toFixed(2));
		}else{
			 $(".th input[type='checkbox']:checked").each(function(){
			 	//Get the value in the subtotal
	        	var sAll = $(this).parents(".pro").siblings('.sAll').text().substring(1);
	        	//cumulative
	        	all+=parseFloat(sAll);
	        	//The assignment
	        	$("#all").text('￥'+all.toFixed(2));
	        })
		}
		
	}
	//Count the total number of items
	function zg(){
		var zsl = 0;
		var index = $(".th input[type='checkbox']:checked").parents(".th").find(".num span");
		var len =index.length;
		if(len==0){
			$("#sl").text(0);
		}else{
			index.each(function(){
				zsl+=parseInt($(this).text());
				$("#sl").text(zsl);
			})
		}
		if($("#sl").text()>0){
			$(".count").css("background","#c10000");
		}else{
			$(".count").css("background","#8e8e8e");
		}
	}
	/*****************All goods***********************/
	$("input[type='checkbox']").on('click',function(){
		var sf = $(this).is(":checked");
		var sc= $(this).hasClass("checkAll");
		if(sf){
			if(sc){
				 $("input[type='checkbox']").each(function(){  
	                this.checked=true;  
	           }); 
				zg();
	           	jisuan();
			}else{
				$(this).checked=true; 
	            var len = $("input[type='checkbox']:checked").length;
	            var len1 = $("input").length-1;
				if(len==len1){
					 $("input[type='checkbox']").each(function(){  
		                this.checked=true;  
		            }); 
				}
				zg();
				jisuan();
			}
		}else{
			if(sc){
				 $("input[type='checkbox']").each(function(){  
	                this.checked=false;  
	           }); 
				zg();
				jisuan();
			}else{
				$(this).checked=false;
				var len = $(".th input[type='checkbox']:checked").length;
	            var len1 = $("input").length-1;
				if(len<len1){
					$('.checkAll').attr("checked",false);
				}
				zg();
				jisuan();
			}
		}
		
	});
	/****************************proDetail Add to shopping cart*******************************/
	$(".btns .cart").click(function(){
		if($(".categ p").hasClass("on")){
			var num = parseInt($(".num span").text());
			var num1 = parseInt($(".goCart span").text());
			$(".goCart span").text(num+num1);
		}
	});
	
	//Delete cart items
	$('.del').click(function(){
		//A single delete
		if($(this).parent().parent().hasClass("th")){
			$(".mask").show();
			$(".tipDel").show();
			index = $(this).parents(".th").index()-1;
			$('.cer').click(function(){
				$(".mask").hide();
				$(".tipDel").hide();
				$(".th").eq(index).remove();
				$('.cer').off('click');
				if($(".th").length==0){
					$(".table .goOn").show();
				}
			})
		}else{
			//Select multiple and delete them together
			if($(".th input[type='checkbox']:checked").length==0){
				$(".mask").show();
				$(".pleaseC").show();
			}
			else{
				$(".mask").show();
				$(".tipDel").show();
				$('.cer').click(function(){
					$(".th input[type='checkbox']:checked").each(function(j){
						index = $(this).parents('.th').index()-1;
						$(".th").eq(index).remove();
						if($(".th").length==0){
							$(".table .goOn").show();
						}
					})
					$(".mask").hide();
					$(".tipDel").hide();
					zg();
					jisuan();
				})
			}
		}
	})
	$('.cancel').click(function(){
		$(".mask").hide();
		$(".tipDel").hide();
	})

//	$(".pro dd").hover(function(){
//		var html='';
//		html='<span class="edit">修改</span>';
//		$(this).addClass("on").append(html).parents(".th").siblings(".th").find(".pro dd").removeClass("on").find('.edit').remove();
//		$(".edit").each(function(i){
//			$(this).attr("id",'edit'+i);
//			$("#edit"+i).click(function(){
//				$(".proDets").show();
//				$(".mask").show();
//				$(".changeBtn .buy").attr("data-id",i);
//			})
//		})
//	},function(){
//		$(this).removeClass("on");
//	})
//	$(".changeBtn .buy").click(function(){
//		var index = $(this).attr("data-id");
//		var result = $(".smallImg .on").find("img").attr("alt");
//		$("#edit"+index).prev().text(result);
//		$(".proDets").hide();
//		$(".mask").hide();
//		$("#edit"+index).parent("dd").removeClass("on").find(".edit").remove();
//	});
//	$(".changeBtn .cart").click(function(){
//		$(".proDets").hide();
//		$(".mask").hide();
//	})
})
