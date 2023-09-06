import whisperx

def detect_lyrics(audio_path:str):
    device = "cuda" 
    audio_file = audio_path
    batch_size = 16
    compute_type = "float16" 

    # 1. Transcribe with original whisper (batched)
    model = whisperx.load_model("large-v2", device, compute_type=compute_type)

    audio = whisperx.load_audio(audio_file)
    result = model.transcribe(audio, batch_size=batch_size)

    return result

# return [dic["text"] for dic in result["segments"]]