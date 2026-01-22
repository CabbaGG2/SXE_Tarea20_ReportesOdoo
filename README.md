# Proyecto de Módulos de Reportes en Odoo

Este proyecto demuestra la creación y modificación de reportes en Odoo 18, utilizando una estructura de desarrollo basada en Docker.

## Descripción General

El repositorio contiene dos módulos de Odoo personalizados que interactúan con el sistema de reportes de ventas:

1.  **`modulo_reportes`**: Crea un reporte de ventas completamente nuevo desde cero.
2.  **`modulo_reporte_heredado`**: Modifica un reporte de ventas existente para añadir una sección de firma.

El entorno de desarrollo y producción se gestiona a través de Docker y Docker Compose, facilitando la instalación y el despliegue.

## Módulos Incluidos

### `modulo_reportes`

-   **Resumen**: Módulo que realiza un reporte desde cero para las ventas del servicio Odoo.
-   **Descripción**: Este módulo introduce un nuevo formato de reporte que puede ser impreso o descargado desde las órdenes de venta en Odoo. Es un ejemplo práctico de cómo construir la estructura de un reporte, incluyendo sus vistas, acciones y plantillas QWeb.

### `modulo_reporte_heredado`

-   **Resumen**: Módulo que realiza una modificación menor en el reporte de ventas.
-   **Descripción**: Este módulo hereda del reporte de presupuesto/orden de venta estándar de Odoo (`sale.report_saleorder`) y le añade un campo de firma al final. Es un ejemplo de cómo extender y personalizar reportes existentes sin alterar el código original.

## Estructura del Proyecto

```
/
├── docker-compose.yml      # Orquesta los servicios de Odoo, PostgreSQL y pgAdmin.
├── .config/
│   └── odoo.conf           # Archivo de configuración de Odoo.
└── extra-addons/
    ├── modulo_reportes/    # Módulo para crear un reporte de ventas desde cero.
    └── modulo_reporte_heredado/ # Módulo para modificar el reporte de ventas existente.
```

-   **`docker-compose.yml`**: Define los tres servicios principales:
    -   `odoo`: El servicio de la aplicación Odoo.
    -   `db`: La base de datos PostgreSQL.
    -   `pgadmin`: Una interfaz web para administrar la base de datos.
-   **`.config/odoo.conf`**: Contiene la configuración del servidor Odoo. Se monta en el contenedor para que los cambios persistan.
-   **`extra-addons/`**: Directorio donde residen los módulos personalizados. Odoo carga automáticamente los módulos que se encuentran en esta carpeta.

## Prerrequisitos

Para ejecutar este proyecto, necesitas tener instalados:

-   [Docker](https://www.docker.com/get-started)
-   [Docker Compose](https://docs.docker.com/compose/install/)

## Cómo Empezar

### 1. Clonar el Repositorio

```bash
git clone <URL_DEL_REPOSITORIO>
cd Tarea20_ModuloOdooReportes
```

### 2. Iniciar los Contenedores

Ejecuta el siguiente comando en la raíz del proyecto para construir e iniciar los servicios en segundo plano:

```bash
docker-compose up -d
```

### 3. Acceder a los Servicios

-   **Odoo**: La instancia estará disponible en `http://localhost:8069`.
-   **pgAdmin**: Puedes acceder a la interfaz de pgAdmin en `http://localhost:5050`.
    -   **Email**: `admin@admin.com`
    -   **Contraseña**: `admin1234`

### 4. Configurar la Base de Datos de Odoo

Al acceder a Odoo por primera vez, se te pedirá que crees una nueva base de datos. Completa el formulario:

-   **Master Password**: La encontrarás en los logs del contenedor de Odoo (`docker-compose logs odoo`).
-   **Database Name**: Elige un nombre para tu base de datos (ej. `odoo_reports_db`).
-   **Email** y **Password**: Serán tus credenciales de administrador en Odoo.
-   **Demo data**: Es recomendable marcar esta casilla para tener datos con los que probar los reportes.

### 5. Instalar los Módulos Personalizados

Una vez que la base de datos esté lista y hayas iniciado sesión:

1.  Haz clic en el menú superior y selecciona **"Apps"**.
2.  En la barra de búsqueda, elimina el filtro "Apps" por defecto para que aparezcan todos los módulos.
3.  Busca `modulo_reportes` y haz clic en **"Install"**.
4.  Busca `modulo_reporte_heredado` y haz clic en **"Install"**.

## Uso

-   **Para probar `modulo_reportes`**:
    1.  Ve a **Sales** -> **Quotations**.
    2.  Selecciona o crea una orden de venta.
    3.  Haz clic en **"Print"** y verás la opción para imprimir el nuevo reporte.

-   **Para probar `modulo_reporte_heredado`**:
    1.  Ve a **Sales** -> **Quotations**.
    2.  Selecciona o crea una orden de venta.
    3.  Imprime el reporte de presupuesto (`Quotation / Order`).
    4.  El PDF generado incluirá una sección de firma al final.

## Autor

**CabbaGG Corp.**

-   [GitHub](https://cabbagg.github.io/)