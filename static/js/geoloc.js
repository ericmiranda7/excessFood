// Get user lat lon
geoFindMe();

let lat = 1;
let lon = 2;

function geoFindMe() {
  function success(position) {
	
    lat  = position.coords.latitude;
	lon = position.coords.longitude;

	if (!(window.location.search.indexOf('lat') > -1)) {
		sendLoc(lat, lon)
	}


  }

  navigator.geolocation.getCurrentPosition(success);
}

function sendLoc(lat, lon) {
	redir = '/food/display/?lat=' + lat + '&lon=' + lon
	console.log(redir)
	window.location.href = redir
}