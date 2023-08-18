import matplotlib.pyplot as plt
from wordcloud import WordCloud
from collections import defaultdict


# Función para generar una nube de palabras a partir de un texto
def generate_word_cloud(filename):
    # Leer el archivo de texto
    with open(filename, 'r') as f:
        text = f.read()

    # Crear un WordCloud
    wordcloud = WordCloud(background_color='white', max_words=200, width=800, height=400).generate(text)

    # Mostrar la nube de palabras
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.show()


# Usa la función con tu archivo .txt
generate_word_cloud('transcript.txt')
