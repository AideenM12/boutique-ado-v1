from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm

# Create your views here.


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request,"There's nothing in your bag")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51JIZpiGhtM7L4fxBn2FylnN18TiiW0Z3cj4Ejgn5N6n0hqoFrI8QlQBP7aVA5SYNTFsW4Mkf4JMqrjSWoxvhz5P800HIgU95D2',
        'client_secret': 'test client secret',
    }
    return render(request, template, context)

