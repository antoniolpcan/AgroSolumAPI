from .config import routers_agrosolum
from models.request import ModelForm
from models.database import json_solos

@routers_agrosolum.post('/post_form')
def post_form(form: ModelForm):
    
    lista_resultado = []

    for solo in json_solos:
        if form.cor in solo['cor']:
            if form.textura in solo['textura']:
                if form.umidade == solo['umidade']:
                    lista_resultado.append(solo['nome_solo'])

    for solo in json_solos:    
        if len(lista_resultado) == 0:
            if form.imagem == solo['imagem'] and ((form.umidade + 1 == solo['umidade']) or form.umidade - 1 == solo['umidade']):
                lista_resultado.append(solo['nome_solo'])

    resultados = []
    for solo in json_solos:
        if len(lista_resultado) > 1:
            if form.regiao == json_solos['regiao']['predominancia']:
                resultados.append(solo['nome_solo'])
        if len(resultados > 1):
            #if solo['regiao']
            pass
    return form