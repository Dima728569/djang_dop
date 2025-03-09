from django.shortcuts import render, redirect
from pizza.models import PizzaModel, ToppingsModel
from order.models import OrderModel
from .forms import CreateForm, CreateOrderModelForm
from django.forms import modelformset_factory
# Create your views here.

def create_order(request, *args, **kwargs):
    qs = PizzaModel.objects.all()
    qs2 = PizzaModel.objects.all()
    order_form = CreateForm(request.POST or None)
    context = {'pizzas_list': qs, 'toppings_list': qs2, 'order_form': order_form}

    print(order_form.data)

    if order_form.is_valid():
        address = order_form.cleaned_data.get('address')
        order = dict(order_form.data).get('choice')
        pizza_objects = [PizzaModel.objects.get(id=i) for i in order]
        print(pizza_objects)
        new_order = OrderModel.objects.create(address=address)
        new_order.pizza_order.add(*pizza_objects)
        new_order.save()
        return redirect('createorder')

    # if order_form.is_valid():
    #     address = order_form.cleaned_data.get('address')
    #     order = order_form.cleaned_data.get('choice')
    #     new_order = OrderModel.objects.create(address=address)
    #     pizza = PizzaModel.objects.get(pk=order)
    #     new_order.pizza_order.add(pizza)
    #     new_order.save()
        
    
    return render(request, 'order/create_order.html', context=context)

def create_model_order(request, *args, **kwargs):
    pizzas = PizzaModel.objects.all()
    #order_object = OrderModel.objects.all()
    OrderFormSet = modelformset_factory(
        OrderModel,
        form=CreateOrderModelForm,
        extra=2
    )
    model_form = OrderFormSet(
        request.POST or None, 
        queryset=OrderModel.objects.none(),
        initial=[{
            'address': 'modelformset street'
        }]

    )

    # if model_form.is_valid():
    #     model_form.save()
    #     return redirect('createmodelorder')

    # model_form = CreateOrderModelForm(request.POST or None)
    context = {
        'pizzas': pizzas,
        'form_set': model_form,
    }

    # print(model_form.data)

    # if model_form.is_valid():
    #     model_form.save()
    #     return redirect('createmodelorder')
    return render(request, 'order/create_model_order.html', context=context)
