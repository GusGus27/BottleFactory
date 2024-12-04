<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Editar Sección</title>
    <link rel="stylesheet" href="/styles.css">
</head>
<body>
    <header>
        <h1>Editar Sección: {{seccion['codigo']}}</h1>
        <nav>
            <a href="/">Usuarios</a>
            <a href="/profesores">Profesores</a>
            <a href="/secciones">Secciones</a>
        </nav>
    </header>
    <div class="container">
        <h2>Estudiantes</h2>
            <form method="POST" action="/seccion/edit">
                <input type="hidden" name="seccion_id" value="{{seccion['id']}}">
                
                <h2>Editar Sección: {{seccion['codigo']}}</h2>
                
                <ul>
                    % for estudiante in estudiantes:
                    <li>
                        <label>
                            <input type="checkbox" name="estudiantes" value="{{estudiante['id']}}" 
                                {{'checked' if estudiante['id'] in estudiantes_seccion else ''}}>
                            {{estudiante['nombre']}} {{estudiante['apellidos']}}
                        </label>
                    </li>
                    % end
                </ul>
                
                <button type="submit">Guardar Cambios</button>
            </form>
    </div>
    <footer>
        <p>&copy; 2024 Mi Página. Todos los derechos reservados.</p>
    </footer>
</body>
</html>
