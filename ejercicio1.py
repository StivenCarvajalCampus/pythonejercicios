def agregar_usuario():
    global usuarios
    name = input("Ingrese el nombre: ")
    edad = input("Ingrese la edad: ")
    phone = input("Ingrese el telefono: ")

    usuarios[name] = edad,phone

def listar():
    global usuarios
    for user in usuarios:
        print(
        """
            Nombre: {}
            Edad: {}
            Telefono: {}
        
        """.format(user,usuarios[user][0],usuarios[user][1]))

def delete(name):
    global usuarios
    del(usuarios[name])
    print("Usuario eliminado")

def ordenar():
    global usuarios
    for x in sorted(usuarios):
        print(
        """
            Nombre: {}
            Edad: {}
            Telefono: {}
        
        """.format(x,usuarios[x][0],usuarios[x][1]))





def agregar_usuarioSput():
    global usuariosSput
    name = input("Ingrese el nombre: ")
    edad = input("Ingrese la edad: ")
    phone = input("Ingrese el telefono: ")

    usuariosSput[name] = edad,phone

def listarSput():
    global usuarios
    for user in usuariosSput:
        print(
        """
            Nombre: {}
            Edad: {}
            Telefono: {}
        
        """.format(user,usuariosSP[user][0],usuariosSP[user][1]))

def deleteSput(name):
    global usuariosSP
    del(usuariosSP[name])
    print("Usuario eliminado")

def ordenarSput():
    global usuariosSput
    for x in sorted(usuariosSput):
        print(
        """
            Nombre: {}
            Edad: {}
            Telefono: {}
        
        """.format(x,usuariosSput[x][0],usuariosSput[x][1]))
try:
    menu = float(input("---------------------MENU-------------------------\n"
        "1.  CREAR GRUPO ARTEMIS: \n"
        "1.1 LISTAR CAMPERS DE ARTEMIS \n"
        "1.2 AGREGAR CAMPERS A ARTEMIS \n"
        "1.3 ELIMINAR CAMPERS DE ARTEMIS\n"
        "1.4 ORDENAR ALFABETICAMENTE EN LISTA DE ARTEMIS\n"
        "1.5 BUSCAR CAMPER EN LISTA DE ARTEMIS\n"
        "2.  CREAR GRUPO SPUTNIK: \n"
        "2.1 LISTAR CAMPERS DE SPUTNIK: \n"
        "2.2 AGREGAR CAMPERS A SPUTNIK\n"
        "2.3 ELIMINAR CAMPERS DE SPUTNIK\n"
        "2.4 ORDENAR ALFABETICAMENTE EN LISTA DE SPUTNIK\n"
        "2.5 BUSCAR CAMPER EN LISTA DE SPUTNIK\n"
        "Digite opcion: "))
    while menu != 0:
        if menu == 1:
            usuarios = {}
            print("El grupo ARTEMIS fue creado exitosamente")
        elif menu == 1.1:
            listar()
        elif menu == 1.2:
            agregar_usuario()
        elif menu == 1.3:
            name = input("Ingrese el nombre: ")
            delete(name)
        elif menu == 1.4:
            ordenar()
        elif menu == 1.5:
            name = input("Ingrese el nombre: ")
            print(usuarios.get(name))

        elif menu == 2:
            usuariosSput = {}
            print("El grupo SPUTNIK fue creado exitosamente")
        elif menu == 2.1:
            listarSput()
        elif menu == 2.2:
            agregar_usuarioSput()
        elif menu == 2.3:
            name = input("Ingrese el nombre: ")
            deleteSput(name)
        elif menu == 2.4:
            ordenarSput()
        elif menu == 2.5:
            name = input("Ingrese el nombre: ")
            print(usuariosSput.get(name))
        else:
            print("opcion no valida")
        menu = float(input("---------------------MENU-------------------------\n"
        "1.  CREAR GRUPO ARTEMIS: \n"
        "1.1 LISTAR CAMPERS DE ARTEMIS \n"
        "1.2 AGREGAR CAMPERS A ARTEMIS \n"
        "1.3 ELIMINAR CAMPERS DE ARTEMIS\n"
        "1.4 ORDENAR ALFABETICAMENTE EN LISTA DE ARTEMIS\n"
        "1.5 BUSCAR CAMPER EN LISTA DE ARTEMIS\n"
        "2.  CREAR GRUPO SPUTNIK: \n"
        "2.1 LISTAR CAMPERS DE SPUTNIK: \n"
        "2.2 AGREGAR CAMPERS A SPUTNIK\n"
        "2.3 ELIMINAR CAMPERS DE SPUTNIK\n"
        "2.4 ORDENAR ALFABETICAMENTE EN LISTA DE SPUTNIK\n"
        "2.5 BUSCAR CAMPER EN LISTA DE SPUTNIK\n"
        "Digite opcion: "))
except:
    print("caracter invalido")