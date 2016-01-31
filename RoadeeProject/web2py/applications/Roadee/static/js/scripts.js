		var isClicked = true;

		$(document).ready(function(){
			$("#inside").click(function() {
				if (isClicked) {
					$(this).animate({
						marginTop:"-=35px"}, 200);
						isClicked = false;

				}else {
					$(this).animate({
						marginTop:"+=35px"}, 200);
						isClicked = true;

				}
			});
		});



