from json.decoder import JSONDecodeError
from flask import flash, render_template, request, redirect
from app import app
from app.forms import SearchForm
import requests
import json

#rotas simples do projeto:
@app.route('/', methods=['GET', 'POST'])
def search():
    search = SearchForm(request.form)
    if request.method == 'POST':
        return search_results(search)
    return render_template('cep.html', form=search)

@app.route('/results')
def search_results(search):
    endereco_dict = {}
    endereco_f = ""
    search = search.data['search']
    url = requests.get(f"https://viacep.com.br/ws/{search}/json/")
    endereco = url.json()
    #As exceções ainda não estão funcionando. É preciso tratar esse erro.
    try:
        if url.status_code == 200:
            for keys in endereco:
                endereco_dict[keys] = endereco[keys]
        elif url.status_code == 500:
            redirect('/')
            flash("Cep inserido desconhecido.")
    except JSONDecodeError:
        flash("Cep inserido desconhecido.")
        redirect('/')

    for keys in endereco_dict:
        endereco_f += "\n" + keys + " : " + endereco_dict[keys] + " |" +  "\n"

    return render_template('/results.html', endereco_f=endereco_f)

        
    


    
