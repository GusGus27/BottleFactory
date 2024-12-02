<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Página de Inicio</title>
    <link rel="stylesheet" href="/styles.css">
</head>
<body>
    <header>
        <h1>Bienvenido a Mi Página</h1>
        <nav>
            <a href="/">Inicio</a>
            <a href="/nosotros">Acerca de</a>
            <a href="/servicios">Servicios</a>
            <a href="/contacto">Contacto</a>
        </nav>
    </header>
    <div class="container">
        <h2>Agregar Profesor</h2>
        <a href="/profesores">Retroceder</a>
        <form action="/profesor/create" method="post">
            <label>Nombre</>
            <input type="text" name="nombre_usuario"><br>
            <label>Apellidos</>
            <input type="text" name="apellido"><br>
            <label>Direccion</>
            <input type="text" name="direccion"><br>
            <label>Foto</>
            <input type="text" name="foto"><br>
            <label>Contrasena</>
            <input type="text" name="contrasena"><br>            
            <input type="submit" value="Enviar">
        </form>
    </div>
    <footer>
        <p>&copy; 2024 Mi Página. Todos los derechos reservados.</p>
    </footer>
</body>
</html>
