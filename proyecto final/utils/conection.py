import pymongo;

def connectar_db():
    uri = "mongodb+srv://client:szfIMWUx2Or9JGlX@cluster0.qzjrnxl.mongodb.net/deteccion_criminal";
    conexion_cliente = pymongo.MongoClient(uri);
    conexion_cliente.server_info();
    db = conexion_cliente.test;
    coleccion = db.users;
    return coleccion;

def crear_usuario(coleccion, usuario):
    resultado = coleccion.insert_one(usuario);
    print("id del usuario", resultado.inserted_id);

def agregar_reportes(coleccion, id_usuario, nuevo_reporte):
    usuario_actualizado = coleccion.find_one({"_id": id_usuario})
    usuario_actualizado["reportes"].append(nuevo_reporte);
    resultado = coleccion.replace_one({"_id": id_usuario}, usuario_actualizado);
    print("Documents updated:", resultado.modified_count);


def agregar_reportes_usuario(coleccion, id_usuario, reportes):
    usuario = coleccion.find_one({"_id": id_usuario});
    usuario["reportes"] = reportes;
    resultado = coleccion.replace_one({"_id": id_usuario}, usuario);
    print("Documents updated:", resultado.modified_count);


def desconectar_db(coleccion):
    coleccion.close();


if __name__ == "__main__":
    coleccion = connectar_db();

    usuario = {
        "email": "cliente1@gmail.com", 
        "contraseña": "password"
    };

    reporte1 = {
        "nombre_camara": "mi camara",
        "deteccion": "pistola",
        "presicion": "96%",
        "fecha_y_hora": "21/12/2023  18:48:00",
        "foto":"foto.png"
    };

    reporte2 = {
        "nombre_camara": "mi camara",
        "deteccion": "cuchillo",
        "presicion": "70%",
        "fecha_y_hora": "23/12/2023  11:00:00",
        "foto":"foto3.png"
    };

    reporte3 = {
        "nombre_camara": "mi otra camara",
        "deteccion": "pistola",
        "presicion": "75%",
        "fecha_y_hora": "22/12/2023  20:00:00",
        "foto":"foto2.png"
    };

    crear_usuario(coleccion, usuario);