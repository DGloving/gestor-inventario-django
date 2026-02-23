from django.urls import path
from .views import export_products_to_excel


urlpatterns = [
    path('exportar-excel/', export_products_to_excel, name='export_excel')
]