import os
from pydub import AudioSegment


def convert_mp3_to_wav(directory):
    # Lista para almacenar los nombres de los archivos WAV generados
    wav_files = []

    # Recorre todos los archivos en el directorio
    for filename in os.listdir(directory):
        if filename.endswith(".mp3"):
            # Ruta completa del archivo MP3
            mp3_path = os.path.join(directory, filename)

            # Leer el archivo MP3
            audio = AudioSegment.from_mp3(mp3_path)

            # Convertir a mono
            audio = audio.set_channels(1)

            # Generar el nombre del archivo WAV
            wav_filename = os.path.splitext(filename)[0] + ".wav"
            wav_path = os.path.join(directory, wav_filename)

            # Exportar el archivo WAV
            audio.export(wav_path, format="wav")

            # Agregar el archivo WAV a la lista
            wav_files.append(wav_path)

            # Eliminar el archivo MP3 original
            os.remove(mp3_path)

    # Renombrar los archivos WAV de 1 a x
    for index, wav_path in enumerate(wav_files, start=1):
        new_name = f"{index}.wav"
        new_path = os.path.join(directory, new_name)
        os.rename(wav_path, new_path)


if __name__ == "__main__":
    # Cambia 'your_directory_path' por la ruta de tu carpeta
    directory = "your_directory_path"
    convert_mp3_to_wav(directory)
