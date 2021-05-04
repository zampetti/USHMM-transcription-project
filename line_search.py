import speech_recognition as sr
import os
from fuzzysearch import find_near_matches_in_file, find_near_matches
import Levenshtein
import re

r = sr.Recognizer()

whole_text = []
def audio_to_text_list(path):
    filepath = path.split('wav-files/')[1]
    filename = filepath.split('.wav')[0]
    for i in range(1, 11):
        try:
            chunk_filename = filename+f"_chunk{i}.wav"
            with sr.AudioFile('audio-chunks/'+chunk_filename) as source:
                audio_listened = r.record(source)
                try:
                    text = r.recognize_google(audio_listened)
                except sr.UnknownValueError as e:
                    print(e)
                    print(f'{chunk_filename}: UNRECOGNIZED PATTERN')
                else:
                    text = f"{text}. "
                    print(chunk_filename, ":", text)
                    whole_text.append(text)
        except Exception as e:
            # print(e)
            print("----END OF CHUNK FILES----")
            break

for file in reversed(os.listdir("./wav-files")):
    print("----WAV FILE BEING ANALYZED----> ", file)
    if file.endswith(".wav"):
        audio_to_text_list('wav-files/'+file)
        print("RECOGNIZABLE ENTRIES: ", whole_text)

        for filename in os.listdir('USHMM_GaborToth/USHMM'):
            wav_file = file
            txt_list = wav_file.split('.')[0:3]
            clip_file = wav_file.split('.wav')[0]+'.txt'
            txt_file = '.'.join(txt_list)+'.txt'
            if filename != txt_file:
                continue
            else:
                with open('USHMM_GaborToth/USHMM/'+filename, "r") as f:
                    lines = f.readlines()
                    positions = []
                    for i, line in enumerate(lines):
                        for wt in whole_text:
                            pattern = re.sub(r'[^\w\s]','',wt).lower()
                            text = re.sub(r'[^\w\s]','',line).lower()
                            # if pattern in text and len(wt) > 12:
                            #     print('SUBSTRING FOUND IN TEXT: ', i, pattern)
                            #     break
                            Lratio = Levenshtein.ratio(pattern, text)
                            if Lratio > 0.5 and len(wt) > 12:
                                # print(f'ELEVATED LEVENSHTEIN RATIO {Lratio} found at line {i} : {pattern}')
                                r_dict = {"ratio": Lratio, "position": i, "pattern": pattern, "text": text}
                                positions.append(r_dict)
                                break

                    # max_pos = max(positions, key=lambda x:x['ratio'])
                    # print("MAX RATIO POSITION: ", max_pos)
                    for position in positions:
                        print()
                        print('-----------------------------------------------')
                        print("LEVENSHTEIN RATIO: ", position['ratio'])
                        print("POSITION IN TEXT: ", position['position'])
                        print("PATTERN FROM AUDIO: ", position['pattern'])
                        print("POSSIBLE MATCH IN TEXT: ", position['text'])
                        print('-----------------------------------------------')
                        print()

                #     with open('clip-files/'+clip_file, 'w') as txtClip:
                #         for l in lines[start_position:]:
                #             txtClip.write(l + '\n')
            
                # with open('USHMM_GaborToth/USHMM/'+filename, "w") as f:
                #     for l in lines[:start_position]:
                #         f.write(l + '\n')

                whole_text = []
                break