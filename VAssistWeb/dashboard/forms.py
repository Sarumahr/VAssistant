from django import forms
from .models import DashboardModel

class DashboardModelForm(forms.ModelForm):
    class Meta:
        model = DashboardModel
        fields = '__all__'