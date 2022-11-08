from django.views.generic import TemplateView, ListView
from .models import Professor, Disciplina
from .models import Curso
from django.db.models import Count
from chartjs.views.lines import BaseLineChartView


class IndexView(TemplateView):
    template_name = 'index.html'

class SobreView(TemplateView):
    template_name = 'about-us.html'

class ProfessoresView(TemplateView):
    template_name = 'teachers.html'

    def get_context_data(self, **kwargs):
        context = super(ProfessoresView, self).get_context_data(**kwargs)
        context['professores'] = Professor.objects.order_by('nome').all()
        return context
class IndexView(TemplateView):
    template_name = 'index.html'
    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['cursos'] = Curso.objects.order_by('?').all()
        return context

class CursoDetalheView(ListView):
    template_name = 'course-detail.html'
    paginate_by = 5
    ordering = 'nome'
    model = Disciplina

    def get_context_data(self, **kwargs):
        context = super(CursoDetalheView, self).get_context_data(**kwargs)
        id = self.kwargs['id']
        context['curso'] = Curso.objects.filter(id=id).first
        return context

    def get_queryset(self, **kwargs):
        id = self.kwargs['id']
        return Disciplina.objects.filter(curso_id=id)

class DadosGraficoAlunosView(BaseLineChartView):
    def get_labels(self):
        labels = []
        queryset = Curso.objects.order_by('id')
        for curso in queryset:
            labels.append(curso.nome)
        return labels

    def get_data(self):
        resultado = []
        dados = []
        queryset = Curso.objects.order_by('id').annotate(total=Count('aluno'))
        for linha in queryset:
            dados.append(int(linha.total))
        resultado.append(dados)
        return resultado
