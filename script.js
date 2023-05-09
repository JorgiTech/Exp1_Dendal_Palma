function iniciarMap() {
    var coord = { lat: -33.5113338,lng: -70.7525613 };
    var map = new google.maps.Map(document.getElementById('map'), {
        zoom: 10,
        center: coord

    }); 
    var marker = new google.maps.Marker({   
        position: coord,
        map: map

    });
}