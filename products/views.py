from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from unicodedata import category
from .models import Products, Cart

# Create your views here.
@login_required
def products(request, category=None):
    if Products.objects.count() == 0:

        # Electronics (6)
        Products.objects.create(name='Laptop', price=50000, category='electronics', image='images/laptop.jpeg')
        Products.objects.create(name='Mobile', price=20000, category='electronics', image='images/mobile.jpg')
        Products.objects.create(name='Tablet', price=15000, category='electronics', image='images/tablet.jpg')
        Products.objects.create(name='Headphones', price=3000, category='electronics', image='images/headphones.jpg')
        Products.objects.create(name='Smartwatch', price=8000, category='electronics', image='images/smartwatch.jpg')
        Products.objects.create(name='Camera', price=25000, category='electronics', image='images/camera.jpg')

        # Clothing (6)
        Products.objects.create(name='T-Shirt', price=800, category='clothing', image='images/tshirt.jpg')
        Products.objects.create(name='Jeans', price=1500, category='clothing', image='images/jeans.jpg')
        Products.objects.create(name='Jacket', price=2500, category='clothing', image='images/jacket.jpg')
        Products.objects.create(name='Shirt', price=1200, category='clothing', image='images/shirt.jpg')
        Products.objects.create(name='Kurta', price=1000, category='clothing', image='images/kurta.jpg')
        Products.objects.create(name='Sweater', price=1800, category='clothing', image='images/sweater.jpg')

        # Footwear (6)
        Products.objects.create(name='Sneakers', price=2500, category='footwear', image='images/sneakers.jpg')
        Products.objects.create(name='Sandals', price=1200, category='footwear', image='images/sandals.jpg')
        Products.objects.create(name='Boots', price=3500, category='footwear', image='images/boots.jpg')
        Products.objects.create(name='Formal Shoes', price=3000, category='footwear', image='images/formal.jpg')
        Products.objects.create(name='Slippers', price=500, category='footwear', image='images/slippers.jpg')
        Products.objects.create(name='Sports Shoes', price=2800, category='footwear', image='images/sports.jpg')

        # Books (6)
        Products.objects.create(name='Python Programming', price=600, category='books', image='images/python.jpg')
        Products.objects.create(name='Django Guide', price=700, category='books', image='images/django.jpg')
        Products.objects.create(name='Data Science Basics', price=900, category='books', image='images/datascience.jpg')
        Products.objects.create(name='Machine Learning', price=1000, category='books', image='images/ml.jpg')
        Products.objects.create(name='AI Fundamentals', price=1100, category='books', image='images/ai.jpg')
        Products.objects.create(name='Web Development', price=650, category='books', image='images/web.jpg')

    # Default category
    if category is None:
        category = "electronics"

    pr = Products.objects.filter(category=category)

    return render(request, 'products.html', {'pr': pr, 'selected_category': category})

@login_required
def addcart(request):
    if request.method=='POST':
        u_id=request.user.id
        p_id=request.POST['product_id']
        qty=request.POST['product_qty']
        Cart.objects.create(u_id=u_id, p_id=p_id, qty=qty, status=0, address=None)
        return redirect('/user_dash')

@login_required
def viewcart(request):
    cart_items = Cart.objects.filter(u_id=request.user.id, status=0)
    cart_data = []

    for item in cart_items:
            product = Products.objects.get(id=item.p_id)
            total = product.price * item.qty

            cart_data.append({
                'id':item.id,
                'name': product.name,
                'price': product.price,
                'qty': item.qty,
                'total': total
            })

    return render(request, 'viewcart.html', context={'cart_data': cart_data})

@login_required
def deletecart(request, id):
    Cart.objects.filter(id=id).delete()
    return redirect('/viewcart')

@login_required
def checkout(request):
    if request.method=='POST':
        address=request.POST['address']
        Cart.objects.filter().update(status=1, address=address)
        return redirect('/user_dash')

@login_required
def orders(request):
    cart_items = Cart.objects.filter(u_id=request.user.id, status=1)
    cart_data = []

    for item in cart_items:
            product = Products.objects.get(id=item.p_id)
            total = product.price * item.qty

            cart_data.append({
                'name': product.name,
                'price': product.price,
                'qty': item.qty,
                'total': total,
                'address': item.address
            })
    return render(request, 'orders.html', context={'cart_data':cart_data})