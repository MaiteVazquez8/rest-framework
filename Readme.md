# Gestión de Usuarios y Roles

Este proyecto Django implementa un sistema básico de gestión de usuarios y roles, con API REST para administrar ambas entidades.

## Estructura del Proyecto

### Modelos principales

#### Roles

Representa los roles que pueden asignarse a los usuarios.

Atributos:

- `id_rol` (AutoField): clave primaria.
- `nombre_rol` (CharField): nombre del rol.
- `descripcion` (TextField): descripción del rol.
- `estado` (BooleanField): estado activo/inactivo del rol.
- `fecha_creacion` (DateTimeField): fecha de creación.
- `fecha_actualizacion` (DateTimeField): fecha de actualización.

#### Usuarios

Representa los usuarios del sistema.

Atributos:

- `id_usuario` (AutoField): clave primaria.
- `nombre` (CharField): nombre del usuario.
- `apellido` (CharField): apellido del usuario.
- `email` (EmailField): correo electrónico.
- `contraseña` (CharField): contraseña del usuario.
- `telefono` (CharField): teléfono de contacto.
- `direccion` (CharField): dirección.
- `fecha_nacimiento` (DateField): fecha de nacimiento.
- `id_rol` (ForeignKey): referencia al modelo `Roles`.
- `estado` (BooleanField): estado activo/inactivo del usuario.
- `fecha_creacion` (DateTimeField): fecha de creación.
- `fecha_actualizacion` (DateTimeField): fecha de actualización.

## Funcionalidades

- Gestión de roles.
- Gestión de usuarios.
- Relación de usuarios con roles mediante ForeignKey.
- API REST para crear, listar, actualizar y eliminar usuarios y roles.

## Rutas principales

- `/` : vista de inicio.
- `/api/Roles/` : API para el modelo `Roles`.
- `/api/Usuarios/` : API para el modelo `Usuarios`.

## Requisitos

- Python
- Django
- Django REST framework

## Configuración del proyecto

### Crear entorno virtual

```bash
python -m venv venv
```

### Activar entorno virtual

Windows:

```bash
venv\Scripts\activate
```

Linux/Mac:

```bash
source venv/bin/activate
```

### Instalar dependencias

```bash
pip install django djangorestframework
```

### Aplicar migraciones

```bash
python manage.py makemigrations
python manage.py migrate
```

### Ejecutar servidor

```bash
python manage.py runserver
```