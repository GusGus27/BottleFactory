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
        <p>A continuación se muestran los usuarios registardos</p>
        <a href="/usuario/agregar">Agregar Usuario</a>
        <table>
            <thead>
                <th>ID</th>
                <th>nombre_usuario</th>
                <th>ACCIONES</th>
            </thead>
            <tbody>
                % for u in usuarios:
                <tr>
                    <td>{{u['id']}}</td>
                    <td>{{u['nombre_usuario']}}</td>
                    <td>
                        <a href="/usuario/editar?id={{u['id']}}">Editar</a>
                        <a href="/usuario/eliminar?id={{u['id']}}">Eliminar</a>
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
