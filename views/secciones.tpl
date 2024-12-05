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
        <p>A continuación se muestran las secciones registrados</p>
        <table>
            <thead>
                <th>ID</th>
                <th>Codigo</th>
                <th>Curso</th>
                <th>Profesor</th>
                <!-- <th>foto</th> -->
                <th>Fecha_inicio</th>
                <th>Fecha_fin</th>
                <th>ACCIONES</th>
            </thead>
            <tbody>
                % for s in secciones:
                <tr>
                    <td>{{s['id']}}</td>
                    <td>{{s['codigo']}}</td>
                    <td>{{s['curso']}}</td>
                    <td>{{s['profe']}}</td>
                    <td>{{s['inicio']}}</td>
                    <td>{{s['fin']}}</td>
                    <td>
                        <a href="/seccion/editar?id={{s['id']}}">Editar</a>
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