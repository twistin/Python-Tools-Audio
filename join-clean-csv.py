import pandas as pd

# Función para unir dos archivos CSV y limpiar los datos
def unir_y_limpiar_csv(archivo1, archivo2, archivo_salida):
    # Leer los archivos CSV
    df1 = pd.read_csv("data1.csv")
    df2 = pd.read_csv("data2.csv")
    
    # Unir los DataFrames
    df_unido = pd.concat([df1, df2], ignore_index=True)
    
    # Eliminar filas con 'Unknown sound' o 'Unknown'
    df_unido = df_unido[~df_unido.isin(['Unknown sound', 'unknown',0]).any(axis=1)]
     # Eliminar casillas vacías (NaN)
    df_unido = df_unido.dropna()
    
    # Eliminar filas duplicadas
    df_unido = df_unido.drop_duplicates()
    
    # Guardar el DataFrame limpio en un nuevo archivo CSV
    df_unido.to_csv(archivo_salida, index=False)

# Reemplaza 'archivo1.csv' y 'archivo2.csv' con los nombres de tus archivos
unir_y_limpiar_csv('data1.csv', 'data2.csv', 'archivo_unido_limpio.csv')

# Imprime un mensaje de éxito
print("Los archivos CSV han sido unidos y limpiados de datos 'Unknown sound' y 'Unknown'.")
