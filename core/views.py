from django.shortcuts import render
from django.views.generic import TemplateView

from core.models import Funcionario


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_date(self, **kwargs):
        contexto = super().get_context_data(**kwargs)
        contexto['funcionarios'] = Funcionario.objects.order_by('?').all()
        return contexto
