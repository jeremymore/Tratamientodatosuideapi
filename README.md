# 🎓 Proyecto Maestría – UIDE
## Parte 1 – Construcción del API
API de Inventario Tecnológico
Descripción

Este proyecto consiste en el desarrollo de una API utilizando FastAPI, enfocada en la gestión de dispositivos tecnológicos. Su objetivo principal es permitir el control de un inventario de equipos como laptops, routers y otros dispositivos, facilitando el manejo de su información de forma sencilla.

🛠️ Tecnologías utilizadas
Python

FastAPI

Uvicorn

Pydantic

### Endpoints de la API
🏠 Ruta principal
GET /

Devuelve un mensaje indicando que la API está activa.

 Obtener todos los dispositivos
 
GET /devices  

Devuelve la lista completa de dispositivos.
#### TIPO DE DATOS 
<img width="328" height="204" alt="json_dispos" src="https://github.com/user-attachments/assets/8f527bd8-fe13-4add-88ec-8df549898936" />

#### Endpoint: Ruta principal
   
@app.get("/")

def home():

    return {"message": "API Inventario activa"}
    
📌 Explicación

Método: GET

Ruta: /

Devuelve un mensaje indicando que la API está activa.


#### Endpoint: Ver dispositivos

@app.get("/devices", response_model=List[Device])

def get_devices():

    return devices
    
📌 Explicación

Método: GET

Ruta: /devices

Devuelve todos los dispositivos almacenados.

Usa response_model para validar la respuesta.

#### Endpoint: Agregar dispositivo
<img width="574" height="201" alt="agregar_dispositivo" src="https://github.com/user-attachments/assets/14b302bd-ef5c-4238-9dfe-023ca5b26fb9" />

📌 Explicación

Método: POST

Ruta: /devices

Recibe un dispositivo en formato JSON, en la cual colocaremos cada uno de los dispositivos, con el formato de datos que se indico al inicio. 
#### Endpoint: Actualizar estado
<img width="592" height="181" alt="actualizacion_estado" src="https://github.com/user-attachments/assets/84587fea-c041-4fa0-8496-adb783d10e1b" />
📌 Explicación

Método: PUT

Ruta: /devices/{device_id}

Parámetros:

device_id: ID del dispositivo

status: nuevo estado

✔ Busca el dispositivo

✔ Si lo encuentra, actualiza el estado

❌ Si no, devuelve error 404

#### Endpoint: Eliminar dispositivo

<img width="594" height="190" alt="eliminar" src="https://github.com/user-attachments/assets/1e5c2272-1886-418c-83ca-1517459a7556" />

📌 Explicación
Método: DELETE

✔ Elimina el dispositivo si existe

❌ Si no existe, devuelve error 404

#### Endpoint: Conteo por tipo
<img width="425" height="147" alt="conteo" src="https://github.com/user-attachments/assets/4eae6689-96f3-4611-b6d1-01c4ed7a331c" />

📌 Explicación

Método: GET

✔ Cuenta cuántos dispositivos hay por tipo

✔ Devuelve un diccionario con los resultados

### Ejecución

uvicorn main:app --reload

Abrir en navegador:

http://127.0.0.1:8000

http://127.0.0.1:8000/docs

### Funcionalidad

La API cuenta con varias funcionalidades que permiten gestionar completamente los dispositivos. En primer lugar, es posible registrar nuevos equipos mediante el endpoint POST /devices, donde se envía la información del dispositivo como su nombre, tipo, marca y estado.
<img width="1240" height="572" alt="image" src="https://github.com/user-attachments/assets/b19f3eea-1b32-4348-942e-19d3f2fc04d6" />


Una vez registrados, los dispositivos pueden ser consultados utilizando GET /devices, lo que devuelve el listado completo del inventario.
<img width="1250" height="572" alt="image" src="https://github.com/user-attachments/assets/3190fa63-55c7-42c3-bd4b-077805f6bfe5" />


También se implementó la posibilidad de actualizar el estado de un dispositivo mediante PUT /devices/{id}, lo cual permite modificar su condición, por ejemplo, de activo a dañado o en mantenimiento.

En caso de que un dispositivo ya no sea necesario, puede eliminarse del sistema utilizando DELETE /devices/{id}, removiéndolo completamente del inventario.
<img width="1252" height="625" alt="image" src="https://github.com/user-attachments/assets/aab0a2a1-1e79-4095-bbfb-8690b6432a61" />


Como funcionalidad adicional, la API incluye el endpoint GET /devices/count, el cual permite obtener un conteo de los dispositivos agrupados por tipo. Esto resulta útil para tener una visión general del inventario.
