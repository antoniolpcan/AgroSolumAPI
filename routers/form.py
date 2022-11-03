from .config import routers_agrosolum
from models.request import ModelForm


@routers_agrosolum.post('/post_form')
def post_form(form: ModelForm):
    return form