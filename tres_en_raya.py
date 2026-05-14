import random 
class Jugador:
  def __init__ (self, nombre, simbolo):
    self.nombre = nombre
    self.simbolo = simbolo

  def jugar(self,tablero):
    try:
      casilla = int(input(f"{self.nombre} ({self.simbolo}), elige una casilla del 1 al 9: "))
      if casilla < 1 or casilla > 9:
        print("Debes ingresar un número entre 1 a 9")
      elif tablero[casilla] != "":
        print ("La casilla ya esta ocupada. Elija otra casilla")
      else:
        tablero[casilla] = self.simbolo
    except ValueError:
      print ("Ingresar un valor entero")

class JuegoTresEnRaya:
  def __init__(self):
    self.tablero = {1:"", 2:"", 3:"", 4:"", 5:"", 6:"", 7:"", 8:"", 9:""}
    nombre1 = input ("Ingresar nombre jugador 1:")
    nombre2 = input ("Ingresar nombre jugador 2:")
    self.jugador1 = Jugador(nombre1, "X")
    self.jugador2 = Jugador(nombre2, "O")
    self.turno = self.jugador1

  def mostrar_tablero(self):
    print("JUEGO REAL")
    print(f"_{self.tablero [1]}_|_{self.tablero [2]}_|_{self.tablero [3]}")
    print(f"_{self.tablero [4]}_|_{self.tablero [5]}_|_{self.tablero [6]}")
    print(f"_{self.tablero [7]}_|_{self.tablero [8]}_|_{self.tablero [9]}")

  def verificar_ganador(self):
      combinaciones = [[1,2,3], [4,5,6], [7,8,9], [1,4,7], [2,5,8], [3,6,9], [1,5,9], [3,5,7]]
      for combinacion in combinaciones:
        if self.tablero [combinacion[0]] == self.tablero [combinacion[1]] == self.tablero [combinacion[2]] != "":
          return True
      return False

  def cambiar_turno(self):
      if self.turno == self.jugador1:
        self.turno = self.jugador2
      else:
        self.turno = self.jugador1

  def iniciar_juego(self):
      print("Juego inicializado. Bienvenido a Tres en Raya")
      print("Tablero referencia:")
      print("_1_|_2_|_3_")
      print("_4_|_5_|_6_")
      print("_7_|_8_|_9_")
      while True:
        self.mostrar_tablero()
        self.turno.jugar(self.tablero)
        if self.verificar_ganador():
          self.mostrar_tablero()
          print (f"Ganaste")
          break
        self.cambiar_turno()

juego = JuegoTresEnRaya()
juego.iniciar_juego()

