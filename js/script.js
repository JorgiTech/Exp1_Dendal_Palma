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

//var form = document.getElementById('form');
//    form.addEventListener('submit', function(event){
//        event.preventDefault();
//        var mensajeError = [];
//
//        if(nombres.value.length <6 || null || nombres.value === '' ){
//            mensajeError.push('El nombre no es valido <br>');
//        }
//       if(apellido_paterno.value.length <6 || null || apellido_paterno.value === '' ){
//            mensajeError.push('El apellido paterno no es valido <br>');
//        }
//        if(apellido_materno.value.length <6 || null || apellido_materno.value === '' ){
//            mensajeError.push('El apellido materno no es valido <br>');
//        }
//        if(rut.value.length <6 || null || rut.value === '' ){
//            mensajeError.push('El rut no es valido <br>');
//        }
//        if(direccion.value.length <6 || null || direccion.value === '' ){
//            mensajeError.push('La dirección no es valida <br>');
//        }
//        if(correo_electronico.value.length <6 || null || correo_electronico.value === '' ){
//            mensajeError.push('El correo electrónico no es valido <br>');
//        }
//        if(telefono.value.length <6 || null || telefono.value === '' ){
//            mensajeError.push('El telefono no es valido <br>');
//        }
//
//    error.innerHTML = mensajeError.join(' ');
//
//    return false;
//});



const nombre = document.getElementById("nombres")
const apellidoP = document.getElementById("apellido_paterno")
const apellidoM = document.getElementById("apellido_materno")
const rut = document.getElementById("rut")
const dir = document.getElementById("direccion")
const email = document.getElementById("correo_electronico")
const tel = document.getElementById("telefono")
const form = document.getElementById("form")
const parrafo = document.getElementById("warnings")

form.addEventListener("submit", e=>{
    e.preventDefault()
    let entrar = false
    let regexemail = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,4})+$/
    if(nombre.value.length <6){
        alert("El Nombre no es valido.")
    }
    if(apellidoP.value.length <6){
        alert("El Apellido Paterno no es valido.")
    }
    if(apellidoM.value.length <6){
        alert("El Apellido Materno no es valido.")
    }
    if(rut.value.length <10){
        alert("El rut no es valido.")
    }
    if(dir.value.length <6){
        alert("La Dirección no es valida.")
    }
    if(!regexemail.test(email.value)) {
        alert("El Correo Electronico no es valido.")
    }
    if(tel.value.length <6){
        alert("El Teléfono no es valido.")
    }
})