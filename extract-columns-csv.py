import csv
import os
import glob

# Define la ruta a la carpeta que contiene los archivos CSV
# Reemplaza con la ruta real
directory_path = '/Users/sdcarr/Documents/python_documents/annotations-citynet/5882242'

# Define el nombre de la columna que deseas extraer
column_name = 'Label'  # Reemplaza con el nombre real de la columna

# Crea una lista para almacenar los datos extraídos
extracted_data = []

# Usa glob para encontrar todos los archivos CSV en la carpeta
csv_files = glob.glob(os.path.join(directory_path, '*.csv'))

# Itera a través de cada archivo CSV
for file_path in csv_files:
    with open(file_path, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        # Extrae los datos de la columna deseada
        for row in reader:
            extracted_data.append(row[column_name])

# Escribe los datos extraídos en un nuevo archivo CSV
with open('extracted_column_data2.csv', mode='w', encoding='utf-8', newline='') as output_file:
    writer = csv.writer(output_file)
    writer.writerow([column_name])  # Escribe la cabecera
    for data in extracted_data:
        writer.writerow([data])  # Escribe los datos extraídos

# Imprime un mensaje de éxito
print(f"La columna '{
      column_name}' se ha extraído de todos los archivos CSV y se ha guardado en 'extracted_column_data.csv'.")
