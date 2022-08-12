from django.http import HttpResponse
from django.template import loader

# Create your views here.
def dashboard(request):
    template = loader.get_template('dashboard/dashboard.html')
    context = {}
    return HttpResponse(template.render(context, request))