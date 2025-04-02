# Python Music Download
Este é um script em Python que permite **baixar músicas do YouTube** com base nos nomes listados em um arquivo externo (`.txt`). Ele automatiza a busca e o download de áudio, evitando a necessidade de inserir os nomes manualmente no código.

## 📌 Conheça o fluxo do script
- Solicita que o usuário digite o nome do arquivo que contenha as músicas.
- Localiza o arquivo _.txt_ e salva o nome das músicas em um array. 
- Pesquisa automaticamente os nomes das músicas no YouTube retornando seu link na plataforma.
- Faz o download a partir desse link com a melhor versão de áudio disponível, convertendo para MP3.
- Todas músicas baixadas são armazenadas em uma pasta nomeada com a data e hora que o script foi executado, organizando da melhor forma
- Nomeia os arquivos numericamente, seguido do título original da música.

## 📋 Pré-requisitos
Antes de usar o script, certifique-se de ter instalado:

- **Python 3** 
- **yt-dlp** (biblioteca usada para pesquisar e baixar músicas)

## 🚀 Como Usar
1. **Crie ou edite um arquivo no formato `.txt`** no mesmo diretório do script e adicione os nomes das músicas uma por linha. Exemplo:
   ```
   Na fé Firmão - Racionais MC
   Primavara - Tim Maia
   Ouro de Tolo - Raul seixas
   ```

2. **Execute o script** no terminal ou prompt de comando:
   ```sh
   python app.py
   ```

3. **Informe o arquivo** que as músicas estão escritas. Lembre-se de **_passar sua extensão_** para que o script o encontre corretamente.

4. **Aguarde o download**, você pode acompanhar qual música está sendo instalada a partir do terminal em que o programa foi executado.

## Créditos
Para esse projeto, utilizei [yt-dlp](https://github.com/yt-dlp/yt-dlp) para realizar as pesquisas das músicas e realizar o seu download.