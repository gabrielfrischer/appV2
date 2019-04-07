from django.urls import path, include, re_path
from .views import EvaluationDetailView, EvaluationDetailView, EvaluationDetailPDFView
from . import views

urlpatterns = [
    re_path(r'^evaluations/$', views.EvaluationListView.as_view(), name='efab-home'),
    path('evaluation/<int:pk>/', views.EvaluationDetailView.as_view(), name='evaluation_details'),
    path('evaluationpdf/<int:pk>/', views.EvaluationDetailPDFView.as_view(), name='evaluation_details')
]