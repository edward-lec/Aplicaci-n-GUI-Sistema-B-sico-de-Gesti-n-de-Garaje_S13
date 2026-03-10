# Sistema Básico de Gestión de Garaje

## Descripción

Este proyecto es una aplicación de escritorio desarrollada en Python utilizando la biblioteca Tkinter para la creación de interfaces gráficas. El sistema permite registrar vehículos que ingresan a un garaje y visualizar la información en una tabla dentro de la aplicación.

El proyecto fue desarrollado siguiendo una arquitectura modular que separa el código en diferentes carpetas para organizar mejor la lógica del programa.

---

## Objetivo del programa

El objetivo del sistema es permitir al usuario:

* Registrar vehículos dentro de un garaje.
* Visualizar los vehículos registrados en una lista o tabla.
* Limpiar los campos del formulario después de ingresar datos.

Este proyecto también tiene como finalidad practicar el uso de interfaces gráficas en Python y la organización del código utilizando una arquitectura modular.

---

## Interfaz del sistema

La aplicación cuenta con una interfaz gráfica simple que incluye:

* Título de la aplicación.
* Campos de texto para ingresar información del vehículo.
* Botón para agregar un vehículo.
* Botón para limpiar los campos del formulario.
* Tabla para mostrar los vehículos registrados.

Cada vehículo registrado contiene la siguiente información:

* Placa
* Marca
* Propietario

---

## Funcionamiento del programa

1. El usuario ingresa los datos del vehículo en los campos de texto correspondientes:

   * Placa
   * Marca
   * Propietario

2. Al presionar el botón "Agregar Vehículo":

   * Se crea un objeto de tipo Vehiculo.
   * El vehículo se envía al servicio del garaje.
   * El vehículo se almacena en una lista.
   * La tabla de la interfaz se actualiza mostrando el nuevo vehículo registrado.

3. Al presionar el botón "Limpiar":

   * Se eliminan los datos ingresados en los campos del formulario.

---

## Estructura del proyecto

```
garaje_app/
│
├── main.py
│
├── modelos/
│   └── vehiculo.py
│
├── servicios/
│   └── garaje_servicio.py
│
├── ui/
│   └── app_tkinter.py
```

### modelos

Contiene la clase Vehiculo, que representa los datos de cada vehículo registrado.

### servicios

Contiene la lógica del sistema, como agregar vehículos y obtener la lista de vehículos registrados.

### ui

Contiene la interfaz gráfica desarrollada con Tkinter, donde el usuario interactúa con el sistema.

### main.py

Es el archivo principal que inicia la aplicación y ejecuta la interfaz gráfica.

---

## Autor

Leiber Correa Bravo
