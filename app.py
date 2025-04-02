import yt_dlp 
import os
import sys
from datetime import datetime

#Usuário digita o nome do arquivo onde estão os nomes das músicas com a sua extensão '.txt'
print("Python music Download v1.0 🎶📥")
file_path = input("📝 file name: ")

#Se o programa não encontrar o nome do arquivo, a execução é encerrada
if not os.path.isfile(file_path):
    print(f"'{file_path}' was not found ❌")
    exit()

#Caso o arquivo esteja vazio, a execução é encerrada
if os.path.getsize(file_path) == 0:
    print(f"'{file_path}' must to have a music ❗")
    exit()

#O terminal é limpo caso o arquivo seja encontrado e não esteja vazio
os.system('cls' if sys.platform == 'win32' else 'clear')

# Para cada música inserida no arquivo de texto, seu nome será adicionado ao array 'musicNameList'
musicNameList = []
with open(file_path,'r') as file:
        for music in file:
            if(len(music.strip()) > 0):
                musicNameList.append(music.strip())

#Caputurando data e hora atual
timestamp = datetime.now().strftime("%Y-%m-%d_%Hh%M")

#Iterando sobre os itens do array criado
for music in musicNameList:
    index = musicNameList.index(music) + 1
    print(f'({index}/{len(musicNameList)}) Searching: {music}...')
    
    search_options = {
        'quiet': True,
        'extract_flat': True,
        'logtostderr': False,
        'no_warnings': True,
        'noprogress': True
    }
    
    #Busca o nome da música no youtube e captura sua url
    with yt_dlp.YoutubeDL(search_options) as ydl:
        result = ydl.extract_info(f"ytsearch:{music}", download=False)
        url = result['entries'][0]['url'] if result['entries'] else None
    
    #Caso a url exista realiza o download
    if url:
        with yt_dlp.YoutubeDL({
            'format': 'bestaudio/best',
            'extractaudio': True,
            'audioformat': 'mp3',
            'outtmpl': f'./music/{timestamp}/{index}-%(title)s.mp3',
            'quiet': True,
            'no_warnings': True,
            'logtostderr': False,
            'noprogress': True,
            'verbose': False
        }) as ydl:
            ydl.download([url])
            print(f'{music} - successfully downloaded ✔')
    else:
        print(f"No results found for {music} ❌")

#Mensagem final
print(f"Musicas foram baixadas no caminho 'music/{timestamp}/' ✨")