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
            <a href="/usuarios">Usuarios</a>
            <a href="/servicios">Servicios</a>
            <a href="/contacto">Contacto</a>
        </nav>
    </header>
    <div class="container">
        <h2>Lista de Usuarios</h2>
        <table>
            <thead>
                <th>ID</th>
                <th>Nombre</th>
                <th>Usuario</th>
                <th>Correo</th>
                <th>Imagen</th>
            </thead>
            <tbody>
                % for p in usuarios:
                <tr>
                    <td>{{p['id']}}</td>
                    <td>{{p['name']}}</td>
                    <td>{{p['user']}}</td>
                    <td>{{p['email']}}</td>
                    <td><img src="/{{p['image_url']}}"/></td>
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
