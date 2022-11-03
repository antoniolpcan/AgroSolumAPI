from .config import routers_agrosolum
from models.request import ModelForm


@routers_agrosolum.post('/post_form')
def post_form(form: ModelForm):
    # https://www.embrapa.br/solos/sibcs/classificacao-de-solos/ordens/cambissolos
    return form