# Sistema de Gestión de Productos y Categorías

## Descripción

Este proyecto fue desarrollado utilizando Django y permite la administración de productos organizados por categorías. El sistema almacena información de cada producto, incluyendo nombre, precio, stock disponible, descripción e imagen asociada.

Además, cada producto pertenece a una categoría específica, lo que facilita la clasificación y organización de los datos dentro de la aplicación.

## Tecnologías Utilizadas

- Python
- Django
- SQLite3
- HTML5
- CSS3
- JavaScript

## Estructura del Proyecto

El sistema se compone de dos modelos principales:

### Categoría

Representa las categorías a las que pueden pertenecer los productos.

#### Atributos

| Campo | Tipo |
|---------|---------|
| CodigoCategoria | AutoField |
| Nombre | CharField |

### Producto

Representa los productos registrados dentro del sistema.

#### Atributos

| Campo | Tipo |
|---------|---------|
| Codigo | AutoField |
| Nombre | CharField |
| Precio | FloatField |
| Stock | IntegerField |
| Descripcion | TextField |
| Imagen | ImageField |
| Categoria | ForeignKey |

## Relación entre Entidades

- Una categoría puede contener múltiples productos.
- Un producto pertenece a una única categoría.

Relación:

```
Categoria (1) ------ (N) Productos
```

## Funcionalidades

- Registro de categorías.
- Registro de productos.
- Asociación de productos con categorías.
- Carga de imágenes para cada producto.
- Administración de stock.
- Gestión de precios.
- Visualización de información detallada de los productos.

## Configuración del Proyecto

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
pip install django pillow
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

## Autor

Proyecto desarrollado con Django para la gestión de productos y categorías, implementando una relación uno a muchos entre ambas entidades y permitiendo el almacenamiento de imágenes asociadas a cada producto.