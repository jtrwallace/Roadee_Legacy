/*var map;
		function initMap() {
		  map = new google.maps.Map(document.getElementById('map'), {
			center: {lat: 37.8019, lng: -122.4189},
			zoom: 15
		  });
		}*/

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

		//Prints Map
		function initMap() {
			var myLatLng = {lat: 37.8019, lng: -122.4189};

			var map = new google.maps.Map(document.getElementById('map'), {
				zoom: 15,
				mapTypeControl: false,
				center: myLatLng
			});


  		//Adds customer marker
		var image = 'static/images/waypoint.png';

		var marker = new google.maps.Marker({
			position: myLatLng,
			map: map,
			icon: image
  		});

		}
