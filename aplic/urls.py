from django.urls import path
from .views import IndexView, SobreView
from .views import ProfessoresView
from .views import CursoDetalheView
from .views import DadosGraficoAlunosView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('sobre/', SobreView.as_view(), name='sobre'),
    path('professores/', ProfessoresView.as_view(), name='professores'),
    path('curso-detalhe/<int:id>/', CursoDetalheView.as_view(), name='curso-detalhe'),
    path('dados-grafico-alunos/', DadosGraficoAlunosView.as_view(), name='dados-grafico-alunos'),
]
