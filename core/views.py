from django.shortcuts import render
import pandas as pd
from django.http import HttpResponse
from .models import Product


def export_products_to_excel(request):
    products = Product.objects.all().values(
        'name', 'sku', 'category__name', 'stock_quantity', 'price_cost', 'price_sell'
    )


    if not products:
        return HttpResponse('Nenhum produto cadastrado para exportar.')
    df = pd.DataFrame(list(products))
    df.columns = ['Nome', 'SKU', 'Categoria', 'Estoque', 'Preço Custo', 'Preço Venda']
    df['Valor Total Estoque'] = df['Estoque'] * df['Preço Venda']
    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename="relatorio_estoque.xlsx"'

    with pd.ExcelWriter(response, engine='openpyxl') as writer:
        df.to_excel(writer, index=False, sheet_name='Products')

    return response