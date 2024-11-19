clientes = {}  # Lista para almacenar clientes registrados
pedidos = []   # Lista para almacenar los pedidos realizados

# Función para registrar un nuevo cliente
def registro_cliente():
    id_cliente = input("Seleccione su ID cliente: ")  # Pedir al cliente que seleccione un ID único.
    if id_cliente in clientes:  # Verificar si el ID ya existe
        print("Este ID ya a sido registrado, intentelo con otro ID.")  # Mensaje de de que ese ID ya esta en uso, pruebe con otro ID.
        return
    # Registrar los datos del cliente
    clientes[id_cliente] = {
        "nombre": input("Introduzca su nombre: "),      # Pedir al usuario introducir su nombre
        "email": input("Introduzca su email: "),        # Pedir al usuario introducir su email
        "telefono": input("Introduzca su Teléfono: ")   # Pedir al usuario introducir su teléfono
    }
    print("Ha sido registrado, bienvenido")  # Mensaje de confirmación de registro
    
# Productos disponibles con su nombre y precio
productos = {
    1: {"nombre": "Producto A", "precio": 10.0},
    2: {"nombre": "Producto B", "precio": 20.0},
    3: {"nombre": "Producto C", "precio": 30.0}
}

# Función para mostrar la lista de productos
def imprimir_productos():
    print("Productos disponibles:")  # Frase que aparece al principio
    for codigo, prod in productos.items():  # Itera por cada producto
        print(f"{codigo}. {prod['nombre']} - ${prod['precio']:.2f}")  # Mouestra el código, el nombre y el precio del producto


# Función para realizar una compra
def compra():
    id_cliente = input("ID cliente: ")  # Pide al cliente que introduzca su ID 
    if id_cliente not in clientes:  # Verificación para ver si el cliente está registrado
        print("Cliente no encontrado. Regístrese primero.")  # Mensaje de error y pedir que se registre de nuevo, ya que ese ID no a sido registrado.
        return

    imprimir_productos()  # Muestra los productos disponibles
    carrito = []  # Lista para almacenar los productos seleccionados
    while (codigo := int(input("Código del producto (0 para finalizar): "))) != 0:  # Bucle que aparece para seleccionar los productos
        if codigo in productos:  # Verifición para ver si el código del producto es válido
            cantidad = int(input(f"Cantidad de {productos[codigo]['nombre']}: "))  # Pedir al cliente la cantidad que quiere de ese producto
            carrito.append({"producto": productos[codigo], "cantidad": cantidad})  # Se añade al carrito
        else:
            print("Código inválido.")  # Mensaje que aparece si el código de producto que a seleccionado el cliete no es válido

    if not carrito:  # Verificación para ver si el carrito está vacío
        print("No hay productos en el carrito.")  # Mensaje si el carrito está vacío
        return

    # Calcular el total de la compra
    total = sum(item["producto"]["precio"] * item["cantidad"] for item in carrito)
    numero_pedido = len(pedidos) + 1  # Genera el número de pedido
    # Registra el pedido en el programa
    pedidos.append({
        "numero_pedido": numero_pedido,
        "cliente_id": id_cliente,
        "productos": carrito,
        "total": total
    })
    print(f"Compra realizada. Número de pedido: {numero_pedido}")  # Mensaje de confirmación de la compra con el numero del pedido.

# Función para ver el estado de un pedido
def seguimiento():
    numero_pedido = int(input("Número de pedido: "))  # Pedir el número de pedido
    # Buscar el pedido en la lista de pedidos
    pedido = next((p for p in pedidos if p["numero_pedido"] == numero_pedido), None)
    if pedido:  # Si se encuentra el pedido
        cliente = clientes[pedido["cliente_id"]]  # Obtiene los datos del cliente que a realizado ese pedido
        print(f"Cliente: {cliente['nombre']}, Email: {cliente['email']}, Teléfono: {cliente['telefono']}") # Datos de dicho cliente
        for item in pedido["productos"]:  # Muestra los productos del pedido
            print(f"{item['producto']['nombre']} - Cantidad: {item['cantidad']}") #productos y canttidad del pedido
        print(f"Precio Total: ${pedido['total']:.2f}")  # Muestra el precio total
    else:
        print("Pedido no encontrado.")  # Mensaje que aparece si el pedido no existe

# Menú principal
def menu():
    opciones = {  # Diccionario con las opciones del menú
        "1": registro_cliente,  # Registrar cliente
        "2": compra,            # Realizar compra
        "3": seguimiento        # Seguimiento de pedido
    }
    while True:  # Bucle que se repite hasta seleccionar salir del programa
        print("\n--- Menú ---")
        print("1. Registrar Cliente\n2. Realizar Compra\n3. Seguimiento de Pedido\n4. Salir")
        opcion = input("Seleccione una opción: ")  # Leer opción del usuario
        if opcion == "4":  # Salir del programa
            print("Saliendo del programa...")
            break
        elif funcion := opciones.get(opcion):  # Ejectua la opción seleccionada
            funcion()
        else:
            print("Opción no válida.")  # Mensaje si la opción no es válida

# Inicia el programa
menu()