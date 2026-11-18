# Viajes Aventura

Sistema de gestión para una agencia de viajes: administración de **destinos**, **paquetes** y **reservas** de clientes.

Proyecto — Sprint 1 / Hito 1.

---

## Descripción

Viajes Aventura necesita una aplicación que permita:

- Registrar, modificar, eliminar y listar **destinos**.
- Crear **paquetes** que combinen destinos, con fechas, costos y disponibilidad.
- Que los **clientes** se registren, inicien sesión, reserven paquetes y consulten su historial.
- **Recuperar una reserva** a partir de un código o de los datos del cliente.

La solución se construye con **arquitectura por capas** (presentación, lógica de negocio y persistencia) y **SQLite** como motor de base de datos en el Hito 1. MySQL se incorpora en el primer flujo del Hito 2.

 **Convención del proyecto:** código Python y SQL **en inglés**; mensajes al usuario **en español**.

---

## Requisitos previos

- Python **3.10+**
- Git
- SQLite3 (incluido con Python)

---

## Preparar el entorno

1. **Clonar el repositorio**

   ```bash
   git clone https://github.com/<usuario>/viajes-aventura.git
   cd viajes-aventura

2. **Crear y activar un entorno virtual**
   python -m venv venv
# Linux / macOS
  source venv/bin/activate
# Windows
  venv\Scripts\activate

3. **Instalar dependencias**
   pip install -r requirements.txt

4. **Configurar variables de entorno**
   cp .env.example .env
# Contenido del .env.example:
DB_ENGINE=sqlite
DB_PATH=./data/viajes_aventura.db
APP_ENV=development
