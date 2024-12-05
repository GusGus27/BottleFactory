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
        <h1>Whiteboard</h1>
        <nav>
            <a href="/">Usuarios</a>
            <a href="/profesores">Profesores</a>
            <a href="/secciones">Secciones</a>
        </nav>
    </header>
    <div class="container">
        <h2>Agregar Profesor</h2>
        <a href="/profesores">Retroceder</a>
        <form action="/profesor/create" method="post">
            <label>Nombre</>
            <input type="text" name="nombre"><br>
            <label>Apellidos</>
            <input type="text" name="apellidos"><br>
            <label>Direccion</>
            <input type="text" name="direccion"><br>
            <label>Foto</>
            <input type="text" name="foto"><br>
            <label>Codigo</>
            <input type="text" name="codigo_institucional"><br>
            <label>Contrasena</>
            <input type="text" name="contrasena"><br> 

            <label>Usuario Asociado</label>
            <select name="id_usuario" required>
                <option value="">Selecciona un usuario</option>
                % for usuario in usuariosDisp:
                    <option value="{{usuario['id']}}">{{usuario['nombre_usuario']}}</option>
                % end
            </select><br>

            <input type="submit" value="Enviar">
        </form>
    </div>
    <footer>
        <p>&copy; 2024 Mi Página. Todos los derechos reservados.</p>
    </footer>
</body>
</html>
