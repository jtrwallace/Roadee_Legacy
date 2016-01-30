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
function initAutocomplete() {
  var map = new google.maps.Map(document.getElementById('map'), {
    center: {lat: 37.8019, lng: -122.4189},
    zoom: 15,
    mapTypeId: google.maps.MapTypeId.ROADMAP
  });

  // Create the search box and link it to the UI element.
  var input = document.getElementById('pac-input');
  var inputStart = document.getElementById('pac-input-start');
  var inputEnd = document.getElementById('pac-input-end');
  var searchBox = new google.maps.places.SearchBox(input);
  var searchBoxStart = new google.maps.places.SearchBox(inputStart);
  var searchBoxEnd = new google.maps.places.SearchBox(inputEnd);
  map.controls[google.maps.ControlPosition.TOP_LEFT].push(input);
  //map.controls[google.maps.ControlPosition.TOP_LEFT].push(inputEnd);

  // Bias the SearchBox results towards current map's viewport.
  map.addListener('bounds_changed', function() {
    searchBox.setBounds(map.getBounds());
  });

  // Bias the SearchBox results towards current map's viewport.
  map.addListener('bounds_changed', function() {
    searchBoxStart.setBounds(map.getBounds());
  });

   // Bias the SearchBox results towards current map's viewport.
  map.addListener('bounds_changed', function() {
    searchBoxEnd.setBounds(map.getBounds());
  });

  var markers = [];

  // Listen for the event fired when the user selects a prediction and retrieve
  // more details for that place.
  searchBox.addListener('places_changed', function() {
    var places = searchBox.getPlaces();

    if (places.length == 0) {
      return;
    }

    // Clear out the old markers.
    markers.forEach(function(marker) {
      marker.setMap(null);
    });
    markers = [];

    // For each place, get the icon, name and location.
    var bounds = new google.maps.LatLngBounds();
    places.forEach(function(place) {
      var icon = {
        url: place.icon,
        size: new google.maps.Size(71, 71),
        origin: new google.maps.Point(0, 0),
        anchor: new google.maps.Point(17, 34),
        scaledSize: new google.maps.Size(25, 25)
      };

      // Create a marker for each place.
      markers.push(new google.maps.Marker({
        map: map,
        icon: icon,
        title: place.name,
        position: place.geometry.location
      }));

      if (place.geometry.viewport) {
        // Only geocodes have viewport.
        bounds.union(place.geometry.viewport);
      } else {
        bounds.extend(place.geometry.location);
      }
    });
    map.fitBounds(bounds);
  });

  var markersStart = [];
  // Listen for the event fired when the user selects a prediction and retrieve
  // more details for that place.
  searchBoxStart.addListener('places_changed', function() {
    var places = searchBoxStart.getPlaces();

    if (places.length == 0) {
      return;
    }

    // Clear out the old markers.
    markersStart.forEach(function(marker) {
      marker.setMap(null);
    });
    markersStart = [];

    // For each place, get the icon, name and location.
    var bounds = new google.maps.LatLngBounds();
    places.forEach(function(place) {
      var icon = {
        url: place.icon,
        size: new google.maps.Size(71, 71),
        origin: new google.maps.Point(0, 0),
        anchor: new google.maps.Point(17, 34),
        scaledSize: new google.maps.Size(25, 25)
      };

      // Create a marker for each place.
      markersStart.push(new google.maps.Marker({
        map: map,
        icon: icon,
        title: place.name,
        position: place.geometry.location
      }));

      if (place.geometry.viewport) {
        // Only geocodes have viewport.
        bounds.union(place.geometry.viewport);
      } else {
        bounds.extend(place.geometry.location);
      }
    });
    map.fitBounds(bounds);
  });


  var markersEnd = [];
  // Listen for the event fired when the user selects a prediction and retrieve
  // more details for that place.
  searchBoxEnd.addListener('places_changed', function() {
    var places = searchBoxEnd.getPlaces();

    if (places.length == 0) {
      return;
    }

    // Clear out the old markers.
    markersEnd.forEach(function(marker) {
      marker.setMap(null);
    });
    markersEnd = [];

    // For each place, get the icon, name and location.
    var bounds = new google.maps.LatLngBounds();
    places.forEach(function(place) {
      var icon = {
        url: place.icon,
        size: new google.maps.Size(71, 71),
        origin: new google.maps.Point(0, 0),
        anchor: new google.maps.Point(17, 34),
        scaledSize: new google.maps.Size(25, 25)
      };

      // Create a marker for each place.
      markersEnd.push(new google.maps.Marker({
        map: map,
        icon: icon,
        title: place.name,
        position: place.geometry.location
      }));

      if (place.geometry.viewport) {
        // Only geocodes have viewport.
        bounds.union(place.geometry.viewport);
      } else {
        bounds.extend(place.geometry.location);
      }
    });
    map.fitBounds(bounds);
  });
}
