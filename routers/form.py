from .config import routers_agrosolum
from models.request import ModelForm


@routers_agrosolum.post('/post_form')
def post_form(form: ModelForm):
    # https://www.embrapa.br/solos/sibcs/classificacao-de-solos/ordens/cambissolos

    """
    1 – Cambissolos
        - Formado por material mineral. Presença de argila e, em alguns casos, elementos da decomposição de riodacitos (rocha de origem vulcânica). Possui textura média ou mais fina.

    2 – Argissolos
        - Formado, principalmente, por material de origem mineral. Apresenta acentuada diferenciação entre as camadas ou horizontes. Podem ser argilosos ou arenosos. Apresentam coloração avermelhada, amarelada ou brunada.

    3 – Espodossolos
        - Composto por material mineral. É predominantemente arenoso.

    4 – Chernossolos
        - Composto por material mineral. Presença de sedimentos argilosos.

    5 – Gleissolos
        - Formado por material mineral. Presença de sedimentos orgânicos e argilosos do período Quaternário (Era Cenozoica). São formados, principalmente, em condições de saturação com água. Por isso, são encontrados, principalmente, em regiões de várzeas e planícies que sofrem inundações. Possui, geralmente, cor cinza claro.
    
    6 – Luvissolos
        - Presentes, principalmente, no agreste e no sertão do Nordeste. Rico em magnésio, sódios, cálcio e argila.
    
    7 – Latossolos
        - Composto, principalmente, por material mineral. Presença de sedimentos argilosos na parta superior. São homogêneos, apresentando baixa diferenciação entre horizontes e camadas. Sua textura é argilosa. As cores mais comuns são: vermelho e vermelho-amarelo.
    
    8 – Neossolos
        - Tipos de solo que apresenta pouco desenvolvimento (azonal). Presença de material mineral e orgânico (materiais de decomposição), além de areias quartsozas. São solos rasos (pouca profundidade).
    
    9 – Nitossolos
        - Formado por material mineral com presença de argila. São homogêneos, apresentando pouca diferenciação de cor com a variação da profundidade.
    
    10 – Organossolos
        - Solo formado basicamente por materiais orgânicos, principalmente carbono orgânico. Possui coloração escura (cinza escuro, chumbo). São formados em condições de saturação hídrica.
    
    11 – Planossolos
        - Formado principalmente por material mineral. Apresenta baixa presença de argila em camadas superiores. Possui permeabilidade reduzida.
    
    12 – Plintossolos
        - Solo composto basicamente por material mineral. Presença de sedimentos argilo-arenosos.
    
    13 – Vertissolos
        - Solo composto por material mineral. Solo encontrado no Brasil no bioma da Caatinga.
    
    """
    return form