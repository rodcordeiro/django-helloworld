# Importamos a função index() definida no arquivo views.py
from . import views

app_name = 'website'

# urlpatterns a lista de roteamentos de URLs para funções/Views
urlpatterns = [
    # GET /
    path('funcionarios/<int:ano>/', views.funcionarios_por_ano),
]
