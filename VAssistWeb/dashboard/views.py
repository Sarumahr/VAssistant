from django.shortcuts import render
from django.views.generic import FormView

from .forms import DashboardModelForm
# Create your views here.
class Dashboard(FormView):
    form_class = DashboardModelForm
    template_name = 'dashboard/forms.html'