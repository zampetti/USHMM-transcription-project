import os
from pydub import AudioSegment
from pydub.silence import split_on_silence

def get_large_audio_transcription(path):
    """
    Splitting the large audio file into chunks
    and apply speech recognition on each of these chunks
    """
    sound = AudioSegment.from_wav(path) 

    chunks = split_on_silence(sound,
        min_silence_len = 2500,
        silence_thresh = sound.dBFS-14,
        keep_silence=2500,
    )
    folder_name = "audio-chunks"
    if not os.path.isdir(folder_name):
        os.mkdir(folder_name)
    for i, audio_chunk in enumerate(chunks, start=1):
        if i <= 10:
            filepath = path.split('wav-files/')[1]
            filename = filepath.split('.wav')[0]
            chunk_filename = os.path.join(folder_name, filename+f"_chunk{i}.wav")
            audio_chunk.export(chunk_filename, format="wav")
        else:
            break

for file in os.listdir("./wav-files"):
    if file.endswith(".wav"):
        get_large_audio_transcription('wav-files/'+file)

