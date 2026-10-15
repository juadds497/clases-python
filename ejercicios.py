direccion = input("Introduce una dirrecion: ").split(",")
print(direccion)



lista = ["Nombre", "ApeLLIDo", "DiA"]

variable = ["john", "DOE", "sTaRlEtTe", "TesT"]
lista = []
for nombre in variable:
    lista.append(nombre.lower())

print(lista)




password = input("Introduce tu contraseña")
if len(password) < 8:
    password = None

if input("Introduce la contraseña: ") == password:
    print("Bienvenido")
else:
    print("Contraseña incorrecta")






