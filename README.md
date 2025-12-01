Hasta el momento, la emprese de mi mamá (Meilí) no cuenta con un sistema de inventario automatizado, requiriendo la realización deun conteo de productos manual. Este proceso no sería un problema, si la cantidad de productos que trabaja la empresa fuera pequeña, pero ese no es el caso. Actualmente, la empresa cuenta con 126 productos diferentes, cada uno de los cuales tiene un mínimo de 2 cajas llenas de diversas unidades, por lo que el proceso de conteo puede llegar a ser tedioso y durar varias horas. Con el fin de simplificar este procedimiento, se propone crear un sistema de inventario basado en Python, haciendo uso de la librería Pandas para el tratamiento de datos y tablas, así como de la librería Openpyxl para permitir el acceso y editado de documentos en formato excel, los cuales funcionarán como la fuente de datos del código.

El repositorio contiene el código python utilizado para el proceso, así como los archivos .xlsx utilizados para probar las operaciones del mismo. El código permite tanto el acceso a un documento .xlsx previamente creado, como la generación de uno nuevo, así como la edición de los datos presentes en la tabla de datos. Entre las ediciones posibles, se encuentran:
1. Guardado de cambios en el archivo.
2. Cálculo automático de las cantidades en Stock
3. Añadir un nuevo producto
4. Eliminar un producto
5. Añadir compra de productos ya existentes
6. Añadir venta de productos ya existentes
7. Añadir elementos de productos ya existentes que se han dañado

También, se tiene una funcionalidad básica de interfaz de usuario (Se planea expandir esta funcionalidad a futuro, con uso de elementos html, javascript y demás).

(La presencia de un segundo colaborador fue un error al momento de subir cambios. No estuve pendiente de las credenciales y los datos del computador, y subí unos cambios con los datos de otra persona.)
