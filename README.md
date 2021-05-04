# USHMM Transcription Project

## HTML Parsing
<p>The htmlTranscriptions.py file parses all the HTML files in the USHMM_GaborToth directory.</p>

## WAV File Conversion
<p>The wav_file_convert.py file uses ffmpeg to convert mp4 files to mp3 and finally to wav files.</p>
<p>Some changes need to be added to loop through mp4 files in the mp4-files directory, then to loop through all subsequent mp3 files in the mp3-files directory.</p>

## Audio Segmenting
<p>The audio_segmenting.py file loops through the wav files and creates audio clips based on silences lasting two and a half seconds. These audio-chunks are written to the audio-chunks directory and given the same name as the parent file.</p>

## Line Search
<p>The line_search.py file conducts speech recognition of the audio-chunks and attempts to find matching patterns in the text.</p>
<p>There is some code commented out at the bottom that was made to clip everything following the matching pattern and writing the results to text files in the clip-files directory. Unfortunately, the pattern matching technique wasn't reliable enough to create accurate clips of the text files.<p>
<p>Running the file logs the results of the Levenshtein ratio higher than 0.5, along with the pattern and the matching text.</p>