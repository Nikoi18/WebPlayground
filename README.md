# WebPlayground

WebPlayground es una aplicación web desarrollada con Django que sirve como una plataforma interactiva con diversas funcionalidades. Permite a los usuarios 
registrarse, personalizar sus perfiles y comunicarse entre ellos a través de un sistema de mensajería integrado.

## Características Principales

*   **Autenticación de Usuarios:** Sistema completo de registro, inicio y cierre de sesión.
*   **Perfiles de Usuario:**
    *   Visualización de perfiles de otros usuarios.
    *   Posibilidad de personalizar el perfil propio con avatar, biografía y enlaces.
*   **Mensajería Instantánea:**
    *   Creación de hilos de conversación entre usuarios.
    *   Envío y recepción de mensajes en tiempo real (simulado mediante fetch API).
*   **Gestión de Páginas Estáticas:** Creación y edición de páginas de contenido simple.
*   **Tema Personalizable:** Interfaz con selector de tema claro/oscuro para mejorar la experiencia de usuario, con persistencia en `localStorage`.
*   **Diseño Responsivo:** Interfaz adaptable a diferentes tamaños de pantalla gracias a Bootstrap.

## Tecnologías Utilizadas

*   **Backend:** Django (Python)
*   **Frontend:** HTML, CSS, JavaScript, Bootstrap 4
*   **Base de Datos:** SQLite (por defecto con Django, fácilmente configurable para otras como PostgreSQL o MySQL)

## Estructura del Proyecto

El proyecto está organizado en las siguientes aplicaciones de Django:

*   `core`: Contiene la configuración base, plantillas globales (como `base.html`), y la página de inicio. También gestiona la lógica del cambio de tema.
*   `registration`: Maneja la autenticación de usuarios (registro, inicio de sesión, cierre de sesión, cambio de contraseña).
*   `profiles`: Gestiona los perfiles de usuario, permitiendo su visualización y edición (avatar, biografía, enlace).
*   `messenger`: Implementa el sistema de mensajería entre usuarios, incluyendo la creación de hilos de conversación y el envío/recepción de mensajes.
*   `pages`: Permite la creación y gestión de páginas estáticas simples a través de un panel de administración o interfaz.

## Instalación y Ejecución

Sigue estos pasos para configurar y ejecutar el proyecto en tu entorno local:

1.  **Clonar el repositorio:**
    ```bash
    git clone https://github.com/tu-usuario/WebPlayground.git
    cd WebPlayground
    ```

2.  **Crear y activar un entorno virtual (recomendado):**
    ```bash
    python -m venv venv
    # En Windows
    venv\Scripts\activate
    # En macOS/Linux
    source venv/bin/activate
    ```

3.  **Instalar dependencias:**
    Asegúrate de tener un archivo `requirements.txt` en la raíz de tu proyecto. Si no lo tienes, puedes generarlo con `pip freeze > requirements.txt`
    después de instalar las dependencias manualmente.
    ```bash
    pip install Django Pillow # Pillow es necesario para ImageField (avatares)
    # Añade aquí otras dependencias si las tienes, por ejemplo:
    # pip install django-crispy-forms
    ```
    Si ya tienes un `requirements.txt`:
    ```bash
    pip install -r requirements.txt
    ```

5.  **Realizar migraciones de la base de datos:**
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

6.  **Crear un superusuario (para acceder al panel de administración de Django):**
    ```bash
    python manage.py createsuperuser
    ```
    Sigue las instrucciones para establecer un nombre de usuario, correo electrónico y contraseña.

7.  **Recolectar archivos estáticos (importante para producción, buena práctica en desarrollo):**
    Asegúrate de que `STATIC_ROOT` esté configurado en tu `settings.py` si aún no lo está (por ejemplo, `STATIC_ROOT = BASE_DIR / 'staticfiles'`).
    ```bash
    python manage.py collectstatic
    ```

8.  **Ejecutar el servidor de desarrollo:**
    ```bash
    python manage.py runserver
    ```
    La aplicación estará disponible en `http://127.0.0.1:8000/`.




