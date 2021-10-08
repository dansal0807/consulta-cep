import requests
from flask import Flask

endereco_dict = {}
endereco_f = ''
def consultacep(cep):
    url = requests.get(f'https://viacep.com.br/ws/{cep}/json/')
    endereco = url.json()
    if url.status_code == 200:
        print("Conexão feita com sucesso")
        for keys in endereco:
            if keys == 'erro':
                return ("Seu CEP é inválido.")
            else:
                endereco_dict[keys] = endereco[keys]
    elif url.status_code == 400:
        return ("Não foi possível conectar com o servidor. Verifique se o CEP está correto.")
   

cep_input = input("Diga-me o seu CEP que eu direi o seu endereço:\n")
consultacep(cep_input)

for keys in endereco_dict:
    endereco_f += "\n" + keys + " : " + endereco_dict[keys] + " |" +  "\n"

print(endereco_f)

app = Flask(__name__)

@app.get('/')
def return_cep():
    return endereco_f