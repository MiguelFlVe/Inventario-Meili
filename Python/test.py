## Importación de librerías
# pandas permite la manipulación y tratamiento de tablas de datos
import pandas as pd
# openpyxl permite el uso de documentos de excel
import openpyxl

## Determinación del tamaño de las tablas de datos, al momento de mostrarlas en pantalla
# Se elimina el límite máximo de la cantidad de columnas mostradas en pantalla
pd.set_option('display.max_columns', None)
# Se elimina el límite máximo de la cantidad de filas mostradas en pantalla
pd.set_option('display.max_rows', None)

## Definición de la clase "Inventario"
class Inventario:

  # Se inicializa la clase "Inventario", utilizando como atributos el objeto creado y la ruta del archivo excel donde se guarda la información
  def __init__(self, file_path):
    self.file_path = file_path
    # Se intenta buscar el archivo en la ruta otorgada
    try:
      self.df = pd.read_excel(file_path)
      print("Archivo cargado correctamente.")
    # En caso de que no se encuentre un archivo en dicha ruta, se procede a generar un archivo nuevo, y se le asigna la ruta previamente otorgada
    except FileNotFoundError:
      print("No se encontró el archivo. Se creará uno nuevo.")
      self.df = pd.DataFrame(columns=["Código", "Nombre", "Compra", "Venta", "Dañado", "Stock"])

  # Cálculo automático de la cantidad de productos en stock, a partir de los datos ya dispuestos en el DataFrame
  def refresh(self):
    self.df["Stock"] = self.df["Compra"] - self.df["Venta"] - self.df["Dañado"]

  # Guardado de las modificaciones realizadas al archivo
  def save(self):
    self.df.to_excel(self.file_path, index=False)
    print("Cambios guardados.")

  # Ingreso de un producto nuevo al DataFrame. Se solicita el código de identificación del mismo, así como su nombre y las cantidades que se han comprado, vendido y dañado. Se ingresan los datos al DataFrame, y se calcula el stock del producto
  def add_product(self, code, name, buy, sell, damage):
    code = code.upper()
    stock = buy - sell - damage
    nuevo = pd.DataFrame([[code, name, buy, sell, damage, stock]], columns=self.df.columns)
    self.df = pd.concat([self.df, nuevo], ignore_index=True)
    self.refresh()
    print("Producto añadido.")

  # Eliminación de un producto del DataFrame. Se solicita el código de identificación del mismo, y se rehace el DataFrame sin la fila correspondiente a dicho código
  def delete_product(self, code):
    code = code.upper()
    self.df = self.df[self.df['Código'] != code]
    self.refresh()
    print("Producto eliminado.")

  # Ingreso de existencias nuevas de un producto (compra). Se solicita el código de identificación del mismo, y la cantidad comprada. Se realiza la modificación de la cantidad del producto en la sección de compra, y se hace el cálculo del stock
  def buy(self, code, cantidad):
    code = code.upper()
    self.df.loc[self.df['Código'] == code, 'Compra'] += cantidad
    self.refresh()
    print("Compra registrada.")

  # Ingreso de ventas nuevas de un producto. Se solicita el código de identificación del mismo, y la cantidad vendida. Se realiza la modificación de la cantidad del producto en la sección de venta, y se hace el cálculo del stock
  def sell(self, code, cantidad):
    code = code.upper()
    self.df.loc[self.df['Código'] == code, 'Venta'] += cantidad
    self.refresh()
    print("Venta registrada.")

  # Ingreso de existencias dañadas de un producto. Se solicita el código de identificación del mismo, y la cantidad dañada. Se realiza la modificación de la cantidad del producto en la sección de dañado, y se hace el cálculo del stock
  def damage(self, code, cantidad):
    code = code.upper()
    self.df.loc[self.df['Código'] == code, 'Dañado'] += cantidad
    self.refresh()
    print("Daño registrado.")

  # Muestra la tabla
  def mostrar(self):
    print(self.df)

  # Muestra el menú. Permite la interacción con la tabla, por medio de los métodos previamente explicados
  def menu(self):
    while True:
      print("----------------------------------------")
      self.mostrar()
      print("----------------------------------------")
      print("Opciones de edición del inventario: ")
      print("1. Añadir nuevo producto")
      print("2. Eliminar producto")
      print("3. Registrar compra")
      print("4. Registrar venta")
      print("5. Registrar daño")
      print("6. Guardar cambios")
      print("7. Mostrar inventario")
      print("8. Salir")
      choice = input("Seleccione una opción (1-7): ")

      # Ejecución del método para nuevo producto
      if choice == '1':
        code = input("Código: ")
        name = input("Nombre: ")
        buy = int(input("Comprados: "))
        sell = int(input("Vendidos: "))
        damage = int(input("Dañados: "))
        self.add_product(code, name, buy, sell, damage)
      # Ejecución del método para eliminar producto
      elif choice == '2':
        code = input("Código: ")
        self.delete_product(code)
      # Ejecución del método para compra de producto
      elif choice == '3':
        code = input("Código: ")
        cantidad = int(input("Cantidad comprada: "))
        self.buy(code, cantidad)
      # Ejecución del método para venta de producto
      elif choice == '4':
        code = input("Código: ")
        cantidad = int(input("Cantidad vendida: "))
        self.sell(code, cantidad)
      # Ejecución del método para producto dañado
      elif choice == '5':
        code = input("Código: ")
        cantidad = int(input("Cantidad dañada: "))
        self.damage(code, cantidad)
      # Ejecución del método para guardar los cambios
      elif choice == '6':
        self.save()
      # Interrupción del proceso
      elif choice == '7':
        break
      # Aviso del ingreso de un valor erróneo
      else:
        print("Opción no reconocida.")

# Ejecución
file_path = "../Data/Inv.xlsx"
inv = Inventario(file_path)
inv.menu()