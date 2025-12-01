# Importar librerías
import pandas as pd
import openpyxl

# Descargar el archivo de inventario, o crear uno nuevo
def gen_file():
  """
  Función para la descarga o creación de un archivo de inventario.
  """
  
  #Solicitar si se quiere descargar un archivo o crear uno nuevo
  soli = input("¿Descargar archivo o crear nuevo archivo? (D/N) ")
  soli = soli.upper()

  df = None

  #Verificar el resultado de la pregunta
  if soli == "D":
    #Ruta del archivo necesario en Google Drive
    file_path = input("Ingrese el nombre del archivo: ")

    #Se busca el archivo y se intenta acceder
    try:
      df = pd.read_excel(f"../Datos/{file_path}.xlsx")
      print("Archivo encontrado.")
    
    #En caso de no ser posible, se avisa al usuario
    except:
      print("No se pudo leer el archivo.")
    
  #Generar la tabla de datos
  elif soli == "N":
    #Ruta para guardar el archivo
    file_path = input("Ingrese el nombre del documento que se desea crear: ")

    #Solicitar la información del producto
    print("Introduzca los datos del primer producto que desea guardar.")
    code = input("Ingrese el código del producto: ")
    name = input("Ingrese el nombre del producto: ")
    buy = input("Ingrese la cantidad de productos comprados: ")
    sell = input("Ingrese la cantidad de productos vendidos: ")
    damage = input("Ingrese la cantidad de productos dañados: ")

    try:
      #Intentar convertir los datos de compra, venta y daño en números
      buy = int(buy)
      sell = int(sell)
      damage = int(damage)
      stock = buy - sell - damage

      #Mostrar los datos para verificación
      print("Verifique los datos")
      print(f"Código: {code}  ")
      print(f"Nombre: {name}  ")
      print(f"Compra: {buy}   ")
      print(f"Venta:  {sell}  ")
      print(f"Dañado: {damage}")

    except ValueError:
      #En caso de un error al intentar lo anterior
      print("Alguno de los datos no es válido.")

    cols = ["Código", "Nombre", "Compra", "Venta", "Dañado", "Stock"]
    df = [[code, name, buy, sell, damage, stock]]
    df = pd.DataFrame(df, columns=cols)

    #Guardar el documento
    df.to_excel(f"../Datos/{file_path}.xlsx", index=False, header=False)

  #En caso de que el dato ingresado no corresponda con las opciones
  else:
    print("Opción no reconocida.")

  return df, f"../Datos/{file_path}.xlsx"

df, file_path = gen_file()

# Funciones para editar la tabla

## Guardar cambios
def Save_Changes():
  global df, file_path
  print("Se han guardado los cambios.")
  return df.to_excel(file_path, index=False)

## Rehacer las tablas, para actualizar las celdas de "Stock"
def refresh():
  global df
  df['Stock'] = df['Compra'] - df['Venta'] - df['Dañado']
  return df["Stock"]

## Añadir nueva fila de producto
def new_product():
  global df

  #Solicitar datos del producto
  code = input("Ingrese el código del producto: ")
  name = input("Ingrese el nombre del producto: ")
  buy = input("Ingrese la cantidad de productos comprados: ")
  sell = input("Ingrese la cantidad de productos vendidos: ")
  damage = input("Ingrese la cantidad de productos dañados: ")

  try:
    #Convertir los datos de compra, venta y daño en números
    buy = int(buy)
    sell = int(sell)
    damage = int(damage)
    stock = buy - sell - damage

    #Generar la fila
    cols = ["Código", "Nombre", "Compra", "Venta", "Dañado", "Stock"]
    nuevo_producto = pd.DataFrame([[code, name, buy, sell, damage, stock]], columns=cols)
    
    #Agregar la fila a la tabla
    df = pd.concat([df, nuevo_producto], ignore_index=True)

  except:
    #En caso de que alguno de los datos no sea válido
    print("Alguno de los datos no es válido.")

  #Refrescar la tabla
  refresh()

  #Mostrar la tabla
  print(df)

## Eliminar producto
def delete():
  global df
  
  #Solicitar datos del producto
  code = input("Ingrese el código del producto: ")

  try:
    #Generar la tabla de nuevo, con los productos de código diferente
    df = df[df['Código'] != code]

  except:
    #Mostrar el error al buscar el código
    print("No se ha encontrado el código del producto.")

  #Refrescar la tabla
  refresh()

  #Mostrar la tabla
  print(df)

## Ingresar valores de compra
def Buy():
  global df

  cant = input("Ingrese la cantidad comprada: ")
  try:
    cant = int(cant)

  except:
    print("Cantidad no reconocida.")
    
  #Solicitud de código del producto comprado
  code = input("Ingrese el código del producto: ")
  code = code.upper()
  
  #Actualización de la cantidad del producto comprado
  try:
    df.loc[df['Código'] == code, 'Compra'] += cant

  except:
    print("Código no encontrado.")

  #Refrescar la tabla
  refresh()

  #Mostrar la tabla
  print(df)

## Ingresar valores de venta
def Sell():
  global df

  #Solicitud de la cantidad de producto comprado
  cant = input("Ingrese la cantidad vendida: ")
  try:
    cant = int(cant)

  except:
    print("Cantidad no reconocida.")

  #Solicitud de código del producto comprado
  code = input("Ingrese el código del producto: ")
  code = code.upper()

  #Actualización de la cantidad del producto comprado
  try:
    df.loc[df['Código'] == code, 'Venta'] += cant

  except:
    print("Código no encontrado.")

  #Refrescar la tabla
  refresh()

  #Mostrar la tabla
  print(df)

## Ingresar valores de producto dañado
def Damage():
  global df

  #Solicitud de la cantidad de producto comprado
  cant = input("Ingrese la cantidad dañada: ")
  try:
    cant = int(cant)

  except:
    print("Cantidad no reconocida.")

  #Solicitud de código del producto comprado
  code = input("Ingrese el código del producto: ")
  code = code.upper()

  #Actualización de la cantidad del producto comprado
  try:
    df.loc[df['Código'] == code, 'Dañado'] += cant

  except:
    print("Código no encontrado.")

  #Refrescar la tabla
  refresh()

  #Mostrar la tabla
  print(df)

# Mostrar y actualizar la tabla
def Inventory():
    try:
      print(df)
      while True:
          print("----------------------------------------")
          print("Opciones de edición del inventario: ")
          print("1. Añadir nuevo producto")
          print("2. Eliminar producto")
          print("3. Registrar compra")
          print("4. Registrar venta")
          print("5. Registrar daño")
          print("6. Guardar cambios")
          print("7. Salir")
          choice = input("Seleccione una opción (1-7): ")
          if choice == '1':
              new_product()
          elif choice == '2':
              delete()
          elif choice == '3':
              Buy()
          elif choice == '4':
              Sell()
          elif choice == '5':
              Damage()
          elif choice == '6':
              Save_Changes()
          elif choice == "7":
              break
          else:
              print(f"La opción {choice} no pudo ser reconocida.")

    except Exception as e:
      print(f"Ha ocurrido un error de tipo: {e}")

# Ejecutar
Inventory()