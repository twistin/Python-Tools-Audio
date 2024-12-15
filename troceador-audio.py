from pydub import AudioSegment
import os


def split_audio(file_path, segment_length_ms, output_folder):
    # Cargar el archivo de audio
    audio = AudioSegment.from_file(file_path)

    # Crear la carpeta de salida si no existe
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Obtener la duración del audio en milisegundos
    duration_ms = len(audio)

    # Dividir el audio en segmentos
    for i in range(0, duration_ms, segment_length_ms):
        segment = audio[i:i+segment_length_ms]

        # Generar un nombre de archivo para el segmento
        segment_filename = os.path.join(output_folder, f"davisInterview{
                                        i // segment_length_ms}.wav")

        # Exportar el segmento a un archivo
        segment.export(segment_filename, format="wav")

        print(f"Guardado: {segment_filename}")


# Ejemplo de uso
# Ruta al archivo de audio
file_path = "/Volumes/Nexus/carpeta sin título/Miles Davis interview about Bill Evans_VXhmvOa5Xjo.mp3"
# Longitud de cada segmento en milisegundos (30 segundos)
segment_length_ms = 5000
# Carpeta donde se guardarán los segmentos
output_folder = "/Volumes/Nexus/carpeta sin título/"

split_audio(file_path, segment_length_ms, output_folder)
