function consumir_api(url) {
	return fetch(url)
		.then(function (response) {
			// Verificar si la solicitud fue exitosa (código de estado 200)
			if (response.ok) {
				return response.json();
			} else {
				throw new Error("Error en la solicitud. Código de estado: " + response.status);
			}
		})
		.catch(function (error) {
			throw new Error("Error de conexión: " + error);
		});
}

function mostrarFotos() {
	var url = "https://jsonplaceholder.typicode.com/photos";
	consumir_api(url)
		.then(function (data) {
			var photoContainer = document.getElementById("photo-container");

			// Crear una tarjeta para cada foto
			data.forEach(function (photo) {
				var photoCard = document.createElement("div");
				photoCard.classList.add("photo-card");

				var photoTitle = document.createElement("h3");
				photoTitle.classList.add("photo-title");
				photoTitle.innerText = photo.title;

				var photoImage = document.createElement("img");
				photoImage.classList.add("photo-image");
				photoImage.src = photo.url;
				photoImage.alt = photo.title;

				photoCard.appendChild(photoTitle);
				photoCard.appendChild(photoImage);
				photoContainer.appendChild(photoCard);
			});
		})
		.catch(function (error) {
			console.log("Error en la llamada a la API:", error);
		});
}

// Llamar a la función para mostrar las fotos al cargar la página
mostrarFotos();

/**
 
function consumir_api(url) {
	return fetch(url)
		.then(function(response) {
			// Verificar si la solicitud fue exitosa (código de estado 200)
			if (response.ok) {
				return response.json();
			} else {
				throw new Error("Error en la solicitud. Código de estado: " + response.status);
			}
		})
		.catch(function(error) {
			throw new Error("Error de conexión: " + error);
		});
}

function llamarAPI() {
	var url = "https://jsonplaceholder.typicode.com/photos";
	consumir_api(url)
		.then(function(data) {
			// Procesar los datos de respuesta
			// ...
			document.getElementById("resultado").innerText = "Respuesta de la API: " + JSON.stringify(data);
		})
		.catch(function(error) {
			console.log("Error en la llamada a la API:", error);
		});
}

 *
 /

/*
const API_URL = "http://jsonplaceholder.typicode.com";
 
const xhr = new XMLHttpRequest();

function onRequestHandler() {

	if (this.readyState == 4 && this.status == 200) {
		//0=unset
		//1=opened
		//2=headers received
		//3=loading
		//4=done
		const data = JSON.parse(this.response);
		//console.log(data);
		const HTMLResponse = document.querySelector("#app");

		const array = data.map((user) => `<li>${user.name} ${user.email} </li>`);
		HTMLResponse.innerHTML = `<ul>${array}</ul>`;
	}
}

xhr.addEventListener("load", onRequestHandler);
xhr.open("GET", `${API_URL}/users`);
xhr.send();

*/




