# ATUALIZADOR

>Script criado para atualizar o sistema na empresa em que trabalho.

## O que ele faz?
Ele faz uma leitura nos 2 diretórios (origem e destino), os arquivos que estiverem em ambos ele vai verificar a data, se na origem a data estiver diferente do destino, ele vai fazer uma cópia da origem para o destino.

## Config.ini

\# | Nome  | Descrição
------------- | ------------- | -------------
:house: | origem  | Onde ele vai pegar os arquivos
:computer: | destino | Para onde ele vai copiar os arquivos

## Exemplo

	[Default]
	origem = \\192.168.1.1\repositorio\
	destino = C:\Sistema
## Gerando .exe
- [pyinstaller](https://www.pyinstaller.org/ "pyinstaller")

`pip install pyinstaller`

`pyinstaller -n Atualizador --icon=icon.ico -F atualizador.py`
