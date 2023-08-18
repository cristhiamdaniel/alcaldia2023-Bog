from youtube_transcript_api import YouTubeTranscriptApi

# Reemplaza 'video_id' con la ID del video que quieres transcribir.
video_id = 'uLC0dJhQ1d0'


# Obtén la lista de transcripciones para este video.
transcript_list = YouTubeTranscriptApi.list_transcripts(video_id)

# Obtén la transcripción en el idioma que prefieras. En este caso, español.
transcript = transcript_list.find_transcript(['es'])

# Obtén la transcripción como una lista de diccionarios y luego conviértela en texto.
transcript_text = ' '.join([d['text'] for d in transcript.fetch()])

# Guardar transcripción en un archivo de texto.
with open('transcript.txt', 'w', encoding='utf-8') as f:
    f.write(transcript_text)

# nube de palabras
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Crea la nube de palabras a partir del archivo de texto.






