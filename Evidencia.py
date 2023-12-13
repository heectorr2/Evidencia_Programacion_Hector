from datetime import datetime
import matplotlib.pyplot as plt
import random
import time
from colorama import Fore, Style, init
"""Ejercicio 1"""
def ejercicio1():
    while True:
            ciudad_destino = input(Style.BRIGHT + Fore.CYAN +"Introduce una ciudad de destino Madrid, Sevilla o Valencia (o 0 para salir): ").lower()

            if ciudad_destino == '0':
                print(Fore.GREEN +"Gracias por visitarnos")
                break
            elif ciudad_destino in ['madrid', 'sevilla', 'valencia']:
                try:
                    noches_hotel = int(input(Fore.CYAN +"¿Cuántas noches de hotel necesitas?: "))
                    print(Fore.GREEN +f"Has elegido {ciudad_destino.capitalize()} y {noches_hotel} noches de hotel.")
                except ValueError:
                    print(Fore.RED +"Error: Debes introducir un número válido para las noches de hotel.")
            else:
                print(Fore.RED +"Error: Ciudad no válida. Por favor, elige Madrid, Sevilla o Valencia.")

"""Ejercicio 2"""
class Cliente:
    def __init__(self, nombre, direccion):
        self.nombre = nombre
        self.direccion = direccion
class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio
class Pedido:
    lista_pedidos = []

    def __init__(self, cliente, productos):
        self.cliente = cliente
        self.productos = productos
        self.fecha_pedido = datetime.now()
        self.total = sum(producto.precio for producto in productos)
        Pedido.lista_pedidos.append(self)
    @classmethod
    def ordenar_por_fecha(cls):
        return sorted(cls.lista_pedidos, key=lambda x: x.fecha_pedido)
    @classmethod
    def mostrar_resumen(cls):
        for pedido in cls.lista_pedidos:
            print(f"Cliente: {pedido.cliente.nombre}, Total: {pedido.total} euros")
    @staticmethod
    def mostrar_productos_con_iva():
        for pedido in Pedido.lista_pedidos:
            print(Fore.CYAN +f"Productos del pedido realizado por {pedido.cliente.nombre}:")
            for producto in pedido.productos:
                precio_sin_iva = producto.precio
                precio_con_iva = precio_sin_iva * 1.21  # IVA del 21%
                print(Fore.GREEN +f"  {producto.nombre}: Sin IVA {precio_sin_iva} euros, Con IVA {precio_con_iva} euros")
def agregar_pedido():
    nombre_cliente = input(Fore.GREEN +"Nombre del cliente: ")
    direccion_cliente = input(Fore.GREEN +"Dirección del cliente: ")

    cliente = Cliente(nombre_cliente, direccion_cliente)

    productos_pedido = []
    while True:
        nombre_producto = input(Fore.GREEN +"Nombre del producto (o '0' para finalizar): ")
        if nombre_producto == '0':
            break

        precio_producto = float(input(Fore.GREEN +"Precio del producto: "))
        producto = Producto(nombre_producto, precio_producto)
        productos_pedido.append(producto)

    if productos_pedido:
        Pedido(cliente, productos_pedido)
        print(Fore.GREEN +"Pedido agregado con éxito.")
    else:
        print(Fore.RED +"Error: El pedido debe contener al menos un producto.")
def ejercicio2():
    while True:
        print(Style.BRIGHT + Fore.CYAN +"\n--- Menú ---")
        print("1. Agregar Pedido")
        print("2. Mostrar Resumen de Pedidos")
        print("3. Mostrar Productos con IVA")
        print("4. Salir")

        opcion = input("Selecciona una opción (1-4): "+ Style.RESET_ALL)

        if opcion == '1':
            agregar_pedido()
        elif opcion == '2':
            print(Style.BRIGHT + Fore.CYAN +"\nResumen de Pedidos:")
            Pedido.mostrar_resumen()
        elif opcion == '3':
            print(Style.BRIGHT + Fore.CYAN +"\nProductos con IVA:")
            Pedido.mostrar_productos_con_iva()
        elif opcion == '4':
            print(Fore.GREEN +"Gracias por visitar en nuestra tienda")
            break
        else:
            print(Fore.RED+"Opción no válida. Por favor, elige una opción válida.")
"""Ejercicio 3"""
class TemperaturasSemanales:
    def __init__(self):
        self.temperaturas = {
            'Lunes': {'max': 25, 'min': 10},
            'Martes': {'max': 28, 'min': 12},
            'Miércoles': {'max': 30, 'min': 15},
            'Jueves': {'max': 26, 'min': 11},
            'Viernes': {'max': 24, 'min': 9},
            'Sábado': {'max': 22, 'min': 8},
            'Domingo': {'max': 23, 'min': 10},
        }
    def actualizar_temperatura(self, dia, maxima, minima):
        temperaturas_max = [temp['max'] for temp in self.temperaturas.values()]
        temperaturas_min = [temp['min'] for temp in self.temperaturas.values()]

        if maxima not in temperaturas_max and minima not in temperaturas_min:
            self.temperaturas[dia]['max'] = maxima
            self.temperaturas[dia]['min'] = minima
        else:
            print(Fore.RED +"Error: Las temperaturas máximas y mínimas no pueden repetirse.")
    def mostrar_media_temperaturas(self):
        medias = {dia: (temp['max'] + temp['min']) / 2 for dia, temp in self.temperaturas.items()}
        medias_ordenadas = sorted(medias.items(), key=lambda x: x[1], reverse=True)

        print(Fore.CYAN +"Media de temperaturas por día (de mayor a menor):")
        for dia, media in medias_ordenadas:
            print(f"{dia}: {media} grados")
    def dibujar_grafico(self):
        dias = list(self.temperaturas.keys())
        temperaturas_max = [temp['max'] for temp in self.temperaturas.values()]
        temperaturas_min = [temp['min'] for temp in self.temperaturas.values()]

        plt.figure(figsize=(10, 6))

        # Graficar líneas suaves para temperaturas máximas y mínimas
        plt.plot(dias, temperaturas_max, marker='o', label='Temperatura Máxima', color='#FF5733', alpha=0.8,
                 linewidth=2)
        plt.plot(dias, temperaturas_min, marker='o', label='Temperatura Mínima', color='#33B5FF', alpha=0.8,
                 linewidth=2)

        # Rellenar el área entre las líneas con una sombra
        plt.fill_between(dias, temperaturas_max, temperaturas_min, color='#D3D3D3', alpha=0.2)

        # Estilo general del gráfico
        plt.title('Temperaturas Semanales', fontsize=16)
        plt.xlabel('Día de la Semana', fontsize=14)
        plt.ylabel('Temperatura (°C)', fontsize=14)
        plt.legend()
        plt.grid(True, linestyle='--', alpha=0.5)

        # Añadir etiquetas a los puntos de máximas y mínimas
        for i, txt in enumerate(temperaturas_max):
            plt.annotate(f'{txt}°C', (dias[i], temperaturas_max[i]), textcoords="offset points", xytext=(0, 10),ha='center')

        for i, txt in enumerate(temperaturas_min):
            plt.annotate(f'{txt}°C', (dias[i], temperaturas_min[i]), textcoords="offset points", xytext=(0, -15), ha='center')

        plt.show()
def ejercicio3():
    temperaturas_semana = TemperaturasSemanales()

    # Mostrar la media de temperaturas
    temperaturas_semana.mostrar_media_temperaturas()

    # Dibujar el gráfico inicial
    temperaturas_semana.dibujar_grafico()

    # Modificar la temperatura mínima del Miércoles
    temperaturas_semana.actualizar_temperatura('Miércoles', 30, 18)

    # Mostrar la media de temperaturas después de la modificación
    temperaturas_semana.mostrar_media_temperaturas()

    # Dibujar el gráfico después de la modificación
    temperaturas_semana.dibujar_grafico()
"""Ejercicio 4"""
def ejercicio4():

    numero_aleatorio = random.randint(1, 9)

    intentos = 0
    numeros_adivinados = set()

    inicio_tiempo = time.time()

    print(Style.BRIGHT + Fore.CYAN +"¡Bienvenido al Juego de Adivinanza!")
    while True:
        try:
            intento = int(input(Fore.CYAN +"Adivina el número entre 1 y 9: "))
        except ValueError:
            print(Fore.RED +"Error: Por favor, ingresa un número entero.")
            continue
        if intento in numeros_adivinados:
            print(Fore.RED +"¡Ya has intentado ese número! Inténtalo de nuevo.")
            continue

        intentos += 1

        numeros_adivinados.add(intento)

        if intento == numero_aleatorio:
            fin_tiempo = time.time()
            tiempo_transcurrido = fin_tiempo - inicio_tiempo
            print(Fore.GREEN +f"¡Felicidades! Adivinaste el número {numero_aleatorio} en {intentos} intentos.")
            print(Fore.GREEN +f"Tiempo de ejecución: {tiempo_transcurrido:.2f} segundos.")
            break
        else:
            print(Fore.RED +"Intenta de nuevo.")

    if intentos > 3:
        print(Fore.RED +"Prueba no superada. Has necesitado más de 3 intentos.")