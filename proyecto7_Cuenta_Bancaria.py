
class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

class Cliente(Persona):
    def __init__(self, nombre, apellido, cuenta, balance = 0):
        super().__init__(nombre,apellido)
        self.cuenta = cuenta
        self.balance = balance
    def __str__(self):
        return f'Cliente: {self.nombre} {self.apellido} \nNumero de cuenta: {self.cuenta} \nSaldo: ${self.balance}'
    def depositar(self, monto_deposito):
        self.balance += monto_deposito
        print("Deposito acptado")
    def retirar(self,monto_retiro):
        if self.balance >= monto_retiro:
            self.balance -= monto_retiro
            print("Retiro realizado")
        else:
            print("Fondos insuficientes")

def crear_cliente():
    nombre_cl = input("Ingrese su nombre: ")
    apellido_cl =  input("Ingresa su apellido: ")
    numero_cuenta = input("Ingrese su numero de cuenta: ")
    cliente = Cliente(nombre_cl, apellido_cl, numero_cuenta)
    return cliente

def inicio():
    mi_cliente = crear_cliente()
    print(mi_cliente)
    opccion = 0

    while opccion != 'S':
        print("Elije: Depositar (D), Retirar (R), o Salir (S)")
        opccion = input()

        if opccion == 'D':
            monto_deposito = int(input("Monto a depositar: "))
            mi_cliente.depositar(monto_deposito)
        elif opccion == 'R':
            monto_retirar = int(input("Monto a retirar: "))
            mi_cliente.retirar(monto_retirar)
        print(mi_cliente)

    print("Gracias por operar en Banco Python")

inicio()

