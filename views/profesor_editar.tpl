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
        <h2>Editar Usuario</h2>
        <a href="/">Retroceder</a>
        <form action="/profesor/edit" method="post">
            <input type="hidden" name="id" value="{{profesor['id']}}"><br>
            <label>Nombre</label>
            <input type="text" name="nombre" value="{{profesor['nombre']}}"><br>
            <label>Apellidos</label>
            <input type="text" name="apellidos" value="{{profesor['apellidos']}}"><br>
            <label>Direccion</label>
            <input type="text" name="direccion" value="{{profesor['direccion']}}"><br>
            <label>Foto</label>
            <input type="text" name="foto" value="{{profesor['foto']}}"><br>
            <label>contrasena</>
            <input type="text" name="contrasena" value="{{profesor['contrasena']}}"><br>

            <input type="submit" value="Enviar">
        </form>
    </div>
    <footer>
        <p>&copy; 2024 Mi Página. Todos los derechos reservados.</p>
    </footer>
</body>
</html>
