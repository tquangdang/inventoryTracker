from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from store.models import Product, Supplier, Buyer, Order

@login_required(login_url='login')
def dashboard(request):
    # Retrieve counts of all products, suppliers, buyers, and orders from the database.
    total_product = Product.objects.count()
    total_supplier = Supplier.objects.count()
    total_buyer = Buyer.objects.count()
    total_oder = Order.objects.count()
    
    # Retrieve all orders 
    orders = Order.objects.all().order_by('-id')
    
    # Context dictionary to pass the counts and orders to the template.
    context = {
        'product': total_product,
        'supplier': total_supplier,
        'buyer': total_buyer,
        'order': total_oder,
        'orders': orders
    }
    
    # Render the dashboard template with the provided context.
    return render(request, 'dashboard.html', context)
