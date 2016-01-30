/*var map;
		function initMap() {
		  map = new google.maps.Map(document.getElementById('map'), {
			center: {lat: 37.8019, lng: -122.4189},
			zoom: 15
		  });
		}*/

		//Prints Map
		function initMap() {
  		var myLatLng = {lat: 37.8019, lng: -122.4189};

  		var map = new google.maps.Map(document.getElementById('map'), {
    	zoom: 15,
		mapTypeControl: false,
    	center: myLatLng

  		});

  		//Adds customer marker
		var image = "{{=IMG(_src = URL('static','images/RoadeeMarker(Shadow).png'))}}";

		var marker = new google.maps.Marker({
			position: myLatLng,
			map: map,
			icon: image
  		});

		}
