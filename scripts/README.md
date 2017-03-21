# Scripts de Python para el análisis

* Instalar los requirements.txt

* En el script de extract.py es necesario agregar las credenciales para acceder a la API de Twitter. 

* El script test-naives-bayes.py es para crear un clasificador a partir de un dataset con una columna con textos y otra con su etiqueta. En la misma carpeta en el archivo pickle ya esta creado un clasificador y un diccionario necesario para el script load_classifier.py.

* Para el escript extract.py son necesarios treas argumentos:
..* El nombre del banco para búsqueda ej: Bancomer
..* Fecha de inicio de búsqueda ej: 2017-03-18
..* Fecha de termino de búsqueda ej: 2017-03-19

* El script subida_predi.py es para subir la información a la base de datos, necesita dos argumentos el primero es el doc_type, que para nuestro caso es el nombre del banco y el segundo es el id o el nombre del archivo json a subir.

* El script embed_test.py junta la parte de extracción(extract.py), análisis(load_classifier.py) y envio a la base de datos de Elasticsearch(subida_predi.py) tiene como argumentos el nombre del banco la fecha de inicio y fecha de término, como el script extract.py.


