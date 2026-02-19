from django.db import models


class Supplier(models.Model):
    name = models.CharField(max_length=100)
    contact = models.CharField(max_length=50)
    email = models.EmailField()

    def __str__(self):
        return self.name
    

class Product(models.Model):
    name = models.CharField(max_length=100)
    stock_quantity = models.IntegerField(default=0)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)


class Sale(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    sale_date = models.DateTimeField(auto_now_add=True)
    total_value = models.DecimalField(max_digits=10, decimal_places=2, editable=False)

    def save(self, *args, **kwargs):
        self.valor_total = self.quantity * self.product.unit_price
        super().save(*args, **kwargs)

    
    def __str__(self):
        return f"Venda de {self.product.name} - {self.sale_date.strftime('%d/%m/%Y')}"