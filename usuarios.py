usuarios = ["joaquin", "ana", "maria", "pablo"]

usuario = input("Introduce un usuario: ").lower()
    
if usuario in usuarios:
    print("El usuario ya exite")
else:
    usuarios.append(usuario)
    print("El usuario ha sido añadido")
