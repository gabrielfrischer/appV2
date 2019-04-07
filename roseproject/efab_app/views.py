from django.shortcuts import render
from django.http import HttpResponse
from .models import Evaluation
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, View
from django.contrib.auth.mixins import LoginRequiredMixin
from easy_pdf.views import PDFTemplateResponseMixin




# Create your views here.

tests = [
    {'Step 1': 0,
     'Step 2': 1}   
]


# @login_required
# def home(request):
#     countOfEvaluations = Evaluation.objects.all().count()
#     listOfCount = [countOfEvaluations]
#     strCount = str(listOfCount[0])
#     context = {
#         'title':'Home',
#         'countofevals':strCount,
#         'evaluations': Evaluation.objects.all(),
#         "home_page":"active"
#     }
#     return render(request, 'efab_app/home.html', context)



class EvaluationListView(LoginRequiredMixin, ListView):
    model = Evaluation
    template_name = 'efab_app/home.html'
    context_object_name = 'evaluations'
    ordering = ['-startOfTestDatetime']

class EvaluationDetailView(LoginRequiredMixin, DetailView):
    model = Evaluation
    template_name = 'efab_app/evaluation_details.html'
   

class EvaluationDetailPDFView(LoginRequiredMixin, PDFTemplateResponseMixin, DetailView):
    model = Evaluation
    template_name = 'efab_app/evaluation_details_pdf.html'
   
