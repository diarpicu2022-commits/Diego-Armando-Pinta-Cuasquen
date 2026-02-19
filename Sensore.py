class Pila:
    def __init__(self):
        self.elementos = []

    def push(self, item):
        self.elementos.append(item)

    def pop(self):
        if self.elementos:
            return self.elementos.pop()
        return None

    def esta_vacia(self):
        return len(self.elementos) == 0


# Clase base
class Menu:
    def __init__(self, sistema):
        self.sistema = sistema


# Menú Principal
class MenuPrincipal(Menu):
    def mostrar(self):
        print("\n===== MENÚ PRINCIPAL =====")
        print("1. Configuración")
        print("2. Calibración")
        print("0. Salir del programa")

    def ejecutar(self, opcion):
        if opcion == "1":
            self.sistema.cambiar_menu(MenuConfiguracion(self.sistema))
        elif opcion == "2":
            self.sistema.cambiar_menu(MenuCalibracion(self.sistema))
        elif opcion == "0":
            print("Apagando sistema...")
            exit()
        else:
            print("Opción inválida")


# Configuración
class MenuConfiguracion(Menu):
    def mostrar(self):
        print("\n===== CONFIGURACIÓN =====")
        print("1. Ajustar Voltaje")
        print("2. Regresar")
        print("3. Salir al Principal")

    def ejecutar(self, opcion):
        if opcion == "1":
            print("Voltaje ajustado ✔")
        elif opcion == "2":
            self.sistema.regresar()
        elif opcion == "3":
            self.sistema.ir_principal()
        else:
            print("Opción inválida")


# Calibración
class MenuCalibracion(Menu):
    def mostrar(self):
        print("\n===== CALIBRACIÓN =====")
        print("1. Calibrar Sensor")
        print("2. Regresar")
        print("3. Salir al Principal")

    def ejecutar(self, opcion):
        if opcion == "1":
            print("Sensor calibrado ✔")
        elif opcion == "2":
            self.sistema.regresar()
        elif opcion == "3":
            self.sistema.ir_principal()
        else:
            print("Opción inválida")


# Sistema
class Sistema:
    def __init__(self):
        self.historial = Pila()
        self.menu_actual = MenuPrincipal(self)

    def cambiar_menu(self, nuevo_menu):
        self.historial.push(self.menu_actual)
        self.menu_actual = nuevo_menu

    def regresar(self):
        if not self.historial.esta_vacia():
            self.menu_actual = self.historial.pop()
        else:
            print("Ya estás en el menú principal")

    def ir_principal(self):
        self.historial = Pila()  # limpia historial
        self.menu_actual = MenuPrincipal(self)


# Simulación principal
sistema = Sistema()

while True:
    sistema.menu_actual.mostrar()
    opcion = input("Selecciona una opción: ")
    sistema.menu_actual.ejecutar(opcion)
