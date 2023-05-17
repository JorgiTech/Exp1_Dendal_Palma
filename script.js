function iniciarMap() {
    var coord = { lat: -33.539009,lng: -70.7728858 };
    var map = new google.maps.Map(document.getElementById('map'), {
        zoom: 10,
        center: coord

    }); 
    var marker = new google.maps.Marker({   
        position: coord,
        map: map

    });
}
//var nombre = document.getElementById('nombres');
//var email = document.getElementById('correo_electronico');
//var error = document.getElementById('error');
//error.style.color = 'green';
//function enviarFormulario(){
//    console.log('Enviando formulario...');

//    var mensasjeError = [];

//    if(nombre.value === null || nombre.value === ''){
//        mensajesError.push('Ingresa tu nombre');
//    }

//    error.innerHTML = mensasjeError.join(', ');

//    return false;
//}


var form = document.getElementById('form');
    form.addEventListener('submit', function(event){
        event.preventDefault();
        var mensajeError = [];

        if(nombres.value.length <6 || null || nombres.value === '' ){
            mensajeError.push('Ingresa tu nombre');
        }

    error.innerHTML = mensajeError.join(', ');

    return false;
});