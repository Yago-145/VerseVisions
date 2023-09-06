import os
from pydub import AudioSegment
from pydub.utils import make_chunks
import requests

def split_audio(file_path, output_folder):

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    audio = AudioSegment.from_file(file_path)

    chunk_length = len(audio) // 20
    chunks = make_chunks(audio, chunk_length)

    for i, chunk in enumerate(chunks):
        output_path = os.path.join(output_folder, f"part_{i}.wav")
        chunk.export(output_path, format="wav")