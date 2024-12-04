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
        <h2>Contenido Principal</h2>
        <p>A continuación se muestran los profesores registrados</p>
        <a href="/profesor/agregar">Agregar Profesor</a>
        <table>
            <thead>
                <th>ID</th>
                <th>nombre</th>
                <th>apellido</th>
                <th>direccion</th>
                <!-- <th>foto</th> -->
                <th>codigo_institucional</th>
                <th>nombre_usuario</th>
            </thead>
            <tbody>
                % for p in profesores:
                <tr>
                    <td>{{p['id']}}</td>
                    <td>{{p['nombre']}}</td>
                    <td>{{p['apellidos']}}</td>
                    <td>{{p['direccion']}}</td>
                    <!-- <td><img src="{{p['foto']}}" class="img-responsive"/></td> -->
                    <td>{{p['codigo_institucional']}}</td>
                    <td>{{p['nombre_usuario']}}</td>
                    <td>
                        <a href="/profesor/editar?id={{p['id']}}">Editar</a>
                        <a href="/profesor/eliminar?id={{p['id']}}">Eliminar</a>
                    </td>
                </tr>
                % end
            </tbody>
        </table>
        
    </div>
    <footer>
        <p>&copy; 2024 Mi Página. Todos los derechos reservados.</p>
    </footer>
</body>
</html>