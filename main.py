from bottle import route, run, template, static_file, request, redirect
from configs.database import Database


@route('/<filename>')
def server_static(filename):
    return static_file(filename, root='./static')



@route('/')
def home():
    db = Database()
    rs = db.fetchall(f"SELECT * FROM usuarios;")
    return template('index', usuarios=rs)


@route('/usuario/agregar')
def usuario_agregar():
    return template('usuario_agregar')


@route('/usuario/create', method='POST')
def create_usuario():
    # Obtener los datos del formulario
    nombre_usuario = request.forms.get('nombre_usuario')
    contrasena = request.forms.get('contrasena')
    # acceder a la base de datos
    #i = 'hola ' + str(edad) + ' ,  '
    db = Database()
    query = (
        f"INSERT INTO usuarios (nombre_usuario, contrasena) "
        f"VALUES ('{nombre_usuario}', '{contrasena}')"
    )
    print(query)
    db.execute(query)
    db.close()
    # ir al inicio
    redirect('/')


@route('/usuario/editar', method='GET')
def editar_usuario():
    # Obtener los datos del formulario
    usuario_id = request.query.id
    # acceder a la base de datos
    #i = 'hola ' + str(edad) + ' ,  '
    db = Database()
    # datos del pokemons
    query = (f"SELECT * FROM usuarios WHERE id = {usuario_id};")
    usuario = db.fetchone(query)
    # generacione
    db.close()
    # ir al inicio
    return template('usuario_editar', usuario=usuario)


@route('/usuario/edit', method='POST')
def edit_usuario():
    # Obtener los datos del formulario
    id = request.forms.get('id')
    nombre_usuario = request.forms.get('nombre_usuario')
    contrasena = request.forms.get('contrasena')
    # acceder a la base de datos
    #i = 'hola ' + str(edad) + ' ,  '
    db = Database()
    query = (
        f"UPDATE usuarios SET contrasena='{contrasena}', nombre_usuario = '{nombre_usuario}'"
        f" WHERE id = {id}")
    print(query)
    db.execute(query)
    db.close()
    # ir al inicio
    redirect('/')


@route('/usuario/eliminar', method='GET')
def eliminar_usuario():
    # Obtener los datos del formulario
    usuario_id = request.query.id
    # acceder a la base de datos
    #i = 'hola ' + str(edad) + ' ,  '
    db = Database()
    query = (f"DELETE FROM usuarios WHERE id = {usuario_id};")
    db.execute(query)
    db.close()
    # ir al inicio
    return redirect('/')


@route('/usuarios')
def usuario():
    db = Database()
    rs = db.fetchall(f"SELECT * FROM usuarios;")
    return template('usuarios', usuarios=rs)

@route('/profesores')
def home():
    db = Database()
    rs = db.fetchall("""SELECT 
                        p.id,
                        p.nombre,
                        p.apellidos, 
                        p.direccion, 
                        p.foto, 
                        p.codigo_institucional, 
                        p.usuario_id,
                        u.nombre_usuario
                    FROM profesores p
                    JOIN usuarios u ON p.usuario_id = u.id;""")
    return template('indexProfes', profesores=rs)



def obtener_usuarios_sin_profesor():
    db = Database()

    # Consulta para obtener usuarios sin profesor
    rs = db.fetchall("""
        SELECT id, nombre_usuario FROM usuarios
        WHERE id NOT IN (SELECT usuario_id FROM profesores)
    """)
    
    # Convertir el resultado a una lista de diccionarios
    usuarios = [{"id": row[0], "nombre_usuario": row[1]} for row in rs]
    
    db.close()
    return usuarios



@route('/profesor/agregar')
def profesor_agregar():
    # Obtener los usuarios sin profesor asociado
    usuarios_sin_profesor = obtener_usuarios_sin_profesor()
    # Pasar los usuarios a la plantilla
    return template('profesor_agregar', usuariosDisp=usuarios_sin_profesor)

@route('/profesor/create', method='POST')
def create_profesor():
    # Obtener los datos del formulario
    nombre = request.forms.get('nombre')
    apellidos = request.forms.get('apellidos')
    direccion = request.forms.get('direccion')
    foto = request.forms.get('foto')
    codigo_institucional = request.forms.get('codigo_institucional')
    usuario_id = request.forms.get('usuario_id')
    # acceder a la base de datos
    #i = 'hola ' + str(edad) + ' ,  '
    db = Database()
    query = (
        f"INSERT INTO profesores (nombre, apellidos, direccion, foto, codigo_institucional, usuario_id) "
        f"VALUES ('{nombre}', '{apellidos}', '{direccion}', '{foto}', {codigo_institucional}, {usuario_id})"
    )
    print(query)
    db.execute(query)
    db.close()
    # ir al inicio
    redirect('/profesores')

@route('/profesor/editar', method='GET')
def editar_profesor():
    # Obtener los datos del formulario
    profesor_id = request.query.id
    # acceder a la base de datos
    #i = 'hola ' + str(edad) + ' ,  '
    db = Database()
    # datos del pokemons
    query = (f"SELECT * FROM profesores WHERE id = {profesor_id};")
    profesor = db.fetchone(query)
    # generacione
    db.close()
    # ir al inicio
    return template('profesor_editar', profesor=profesor)

@route('/profesor/edit', method='POST')
def edit_profesor():
    # Obtener los datos del formulario
    id = request.forms.get('id')
    nombre = request.forms.get('nombre')
    apellidos = request.forms.get('apellidos')
    direccion = request.forms.get('direccion')
    foto = request.forms.get('foto')
    # acceder a la base de datos
    #i = 'hola ' + str(edad) + ' ,  '
    db = Database()
    query = (
        f"UPDATE profesores SET nombre='{nombre}', apellidos = '{apellidos}', direccion = '{direccion}', foto = '{foto}'"
        f" WHERE id = {id}")
    print(query)
    db.execute(query)
    db.close()
    # ir al inicio
    redirect('/profesores')

@route('/profesor/eliminar', method='GET')
def eliminar_profesor():
    # Obtener los datos del formulario
    profesor_id = request.query.id
    # acceder a la base de datos
    #i = 'hola ' + str(edad) + ' ,  '
    db = Database()
    query = (f"DELETE FROM profesores WHERE id = {profesor_id};")
    db.execute(query)
    db.close()
    # ir al inicio
    return redirect('/profesores')

@route('/secciones')
def seccion():
    db = Database()

    rs = db.fetchall("""SELECT 
                        s.id,
                        s.codigo,
                        cu.nombre AS curso, 
                        p.apellidos AS profe, 
                        pe.fecha_inicio AS inicio,
                        pe.fecha_fin AS fin
                    FROM secciones s
                    JOIN cursos cu ON s.curso_id = cu.id
                    JOIN profesores p ON s.profesor_id = p.id
                    JOIN periodos pe ON s.periodo_id = pe.id;""")

    return template('secciones', secciones=rs)


@route('/seccion/editar', method='GET')
def editar_seccion():
    # Obtener el ID de la sección desde los parámetros
    seccion_id = request.query.id

    db = Database()
    
    # Obtener datos de la sección
    query_seccion = f"SELECT s.id, s.codigo, cu.nombre AS curso FROM secciones s JOIN cursos cu ON s.curso_id = cu.id WHERE s.id = {seccion_id};"
    seccion = db.fetchone(query_seccion)

    # Obtener todos los estudiantes
    query_estudiantes = "SELECT id, nombre, apellidos FROM estudiantes;"
    estudiantes = db.fetchall(query_estudiantes)

    # Obtener estudiantes que pertenecen a la sección
    query_estudiantes_seccion = f"SELECT estudiante_id FROM estudiantes_secciones WHERE seccion_id = {seccion_id};"
    estudiantes_seccion = [row[0] for row in db.fetchall(query_estudiantes_seccion)]

    db.close()

    return template(
        'seccion_editar',
        seccion=seccion,
        estudiantes=estudiantes,
        estudiantes_seccion=estudiantes_seccion
    )


@route('/seccion/edit', method='POST')
def edit_seccion_submit():
    # Obtener los datos del formulario
    seccion_id = request.forms.get('seccion_id')  # Asegúrate de que sea el ID numérico de la sección
    estudiantes_ids = request.forms.getall('estudiantes')  # Lista de IDs de estudiantes seleccionados

    db = Database()
    
    # Paso 1: Borrar todas las relaciones actuales de esta sección en la tabla estudiantes_secciones
    db.execute(f"DELETE FROM estudiantes_secciones WHERE seccion_id = {seccion_id}")

    # Paso 2: Insertar nuevas relaciones para los estudiantes seleccionados
    for estudiante_id in estudiantes_ids:
        query = (
            f"INSERT INTO estudiantes_secciones (estudiante_id, seccion_id) "
            f"VALUES ({estudiante_id}, {seccion_id})"
        )
        db.execute(query)
    
    db.close()
    
    # Redirigir a la página de secciones después de guardar
    redirect('/secciones')


@route('/contacto')
def contacto():
    return template('contacto')


@route('/nosotros')
def nosotros():
    return template('nosotros')


if __name__ == '__main__':
    run(host='localhost', port=8080, reloader=True)