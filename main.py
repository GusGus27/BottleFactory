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
                        p.contrasena,
                        p.id_usuario,
                        u.nombre_usuario
                    FROM profesores p
                    JOIN usuarios u ON p.id_usuario = u.id;""")
    return template('indexProfes', profesores=rs)

@route('/profesor/agregar')
def profesor_agregar():
    return template('profesor_agregar')

@route('/profesor/create', method='POST')
def create_profesor():
    # Obtener los datos del formulario
    nombre = request.forms.get('nombre')
    apellidos = request.forms.get('apellidos')
    direccion = request.forms.get('direccion')
    foto = request.forms.get('foto')
    codigo_institucional = request.forms.get('codigo_institucional')
    contrasena = request.forms.get('contrasena')
    id_usuario = request.forms.get('id_usuario')
    # acceder a la base de datos
    #i = 'hola ' + str(edad) + ' ,  '
    db = Database()
    query = (
        f"INSERT INTO usuarios (nombre, apellidos, direccion, foto, codigo_institucional, contrasena, id_usuario) "
        f"VALUES ('{nombre}', '{apellidos}', '{direccion}', '{foto}', {codigo_institucional}, '{contrasena}', {id_usuario})"
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
    usuario = db.fetchone(query)
    # generacione
    db.close()
    # ir al inicio
    return template('profesor_editar', usuario=usuario)

@route('/profesor/edit', method='POST')
def edit_profesor():
    # Obtener los datos del formulario
    id = request.forms.get('id')
    nombre = request.forms.get('nombre')
    apellidos = request.forms.get('apellidos')
    direccion = request.forms.get('direccion')
    foto = request.forms.get('foto')
    contrasena = request.forms.get('contrasena')
    # acceder a la base de datos
    #i = 'hola ' + str(edad) + ' ,  '
    db = Database()
    query = (
        f"UPDATE profesores SET nombre='{nombre}', apellidos = '{apellidos}', direccion = '{direccion}', foto = '{foto}', contrasena = '{contrasena}'"
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


@route('/contacto')
def contacto():
    return template('contacto')


@route('/nosotros')
def nosotros():
    return template('nosotros')


if __name__ == '__main__':
    run(host='localhost', port=8080, reloader=True)
