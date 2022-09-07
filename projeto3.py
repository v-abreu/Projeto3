"""
Projeto 3
Escreva um programa em python que colete dados de noticias na página do G1 e salve em um arquivo no
formato html
versão: 0.0.1
data:06/09/2022
"""

#importando arquivos
import requests

#lendo a página de política do g1
def page_reader(endereco:str) -> requests.models.Response:
    pagina=requests.get(endereco)
    return pagina
    
#gravando o arquivo com as informações da variável página
def grava_pagina_web(resposta: requests.models.Response)->None:
    arquivo=open('pagina.html','wb')
    for texto in resposta.iter_content():
        arquivo.write(texto)
    arquivo.close()
    
def main():
    endereco="https://g1.globo.com/politica/"
    politica=page_reader(endereco)
    grava_pagina_web(politica)
    print(f"A página {endereco} foi gravada com sucesso no arquivo 'pagina.html'.")
    
if __name__=="__main__":
    main()