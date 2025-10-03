from django.shortcuts import render
from django.views.generic import FormView
from django.urls import reverse_lazy
from django.contrib import messages

from core.forms import ContatoForm
from core.models import Funcionario


class IndexView(FormView):
    template_name = 'index.html'
    form_class = ContatoForm
    success_url = reverse_lazy('nome')

    def get_context_date(self, **kwargs):
        contexto = super().get_context_data(**kwargs)
        contexto['funcionarios'] = Funcionario.objects.order_by('?').all()
        return contexto

    def form_valid(self, form):
        form.send_mail()
        messages.success(self.request,
                         'Email enviado com sucesso!')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request,
                       'Não foi possível enviar o email')
        return super(IndexView, self).form_invalid(form)
