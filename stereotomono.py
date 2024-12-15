from pydub import AudioSegment
import os


def convert_stereo_to_mono(input_path, output_path):
    # Cargar el archivo de audio
    audio = AudioSegment.from_wav(input_path)

    # Convertir a mono
    mono_audio = audio.set_channels(1)

    # Exportar el archivo de audio en mono
    mono_audio.export(output_path, format="wav")


def batch_convert(directory):
    for filename in os.listdir(directory):
        if filename.endswith(".wav"):
            input_path = os.path.join(directory, filename)
            output_path = os.path.join(directory, f"mono_{filename}")
            convert_stereo_to_mono(input_path, output_path)
            print(f"Convertido: {input_path} a {output_path}")


if __name__ == "__main__":
    # Directorio que contiene los archivos WAV
    directory =

    # Convertir todos los archivos WAV estéreo a mono en el directorio
    batch_convert(directory)
