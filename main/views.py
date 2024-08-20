from django.shortcuts import render, redirect, get_object_or_404
from .models import Customer, Product, Order, OrderItem, User, Role
from django.http import HttpResponse, JsonResponse
from datetime import date
from django.contrib import messages
from django.utils import timezone

# Create your views here.


def home(request):
    if request.session.has_key('logged'):
        if request.session['logged-user'] == 'Sales Representive':
            return redirect('/sales-representative/')
        elif request.session['logged-user'] == 'Head Manager':
            return redirect('/head-manager/')
        elif request.session['logged-user'] == 'Packaging Manager':
            return redirect('/packaging-manager/')
        elif request.session['logged-user'] == 'Production Manager':
            return redirect('/production-manager/')
        elif request.session['logged-user'] == 'Dispatcher':
            return redirect('/dispatcher/')
    else:
        return redirect('/login/')


def login(request):
    if request.session.has_key('logged'):
        return redirect('/')
    else:
        if request.method == 'POST':

            user_name = request.POST.get('login-name')
            password = request.POST.get('login-password')
            logged_user = User.objects.filter(
                user_name=user_name, password=password).first()
            if (logged_user):
                request.session['logged-name'] = logged_user.name
                request.session['logged-user'] = logged_user.role.name
                request.session['logged'] = True
                # print(request.session['logged-name'], request.session['logged-user'])
                return redirect('/')
            else:
                messages.error(request, "Incorrect User Name or Password")
                return render(request, 'HTML/login.html')

        else:
            return render(request, 'HTML/login.html')


def logout(request):
    if request.session.has_key('logged'):
        del request.session['logged-name']
        del request.session['logged-user']
        del request.session['logged']

    return redirect('/login/')


def sales_rep(request):
    if request.session.has_key('logged') and request.session['logged-user'] == 'Sales Representive':
        user_name = request.session['logged-name']
        user_role = request.session['logged-user']
        orders = Order.objects.filter(status__contains='active').all()
        order_ids = []
        for order in orders:
            order_ids.append(order.id)
        order_items = OrderItem.objects.filter(order__id__in=order_ids)
        data = {
            'user_name': user_name,
            'user_role': user_role,
            'orders': orders,
            'order_items': order_items,
        }
        return render(request, 'HTML/sr-home.html', data)

    else:
        return redirect('/login/')


def head_mng(request):
    if request.session.has_key('logged') and request.session['logged-user'] == 'Head Manager':
        user_name = request.session['logged-name']
        data = {
            'user_name': user_name,
        }
        return render(request, 'HTML/hm-home.html', data)

    else:
        return redirect('/login/')


def packng_mng(request):
    if request.session.has_key('logged') and request.session['logged-user'] == 'Packaging Manager':
        user_name = request.session['logged-name']
        data = {
            'user_name': user_name,
        }
        return render(request, 'HTML/pckmng-home.html', data)

    else:
        return redirect('/login/')


def prdctn_mng(request):
    if request.session.has_key('logged') and request.session['logged-user'] == 'Production Manager':
        user_name = request.session['logged-name']
        data = {
            'user_name': user_name,
        }
        return render(request, 'HTML/prdmng-home.html', data)

    else:
        return redirect('/login/')


def dispatcher(request):
    if request.session.has_key('logged') and request.session['logged-user'] == 'Dispatcher':
        user_name = request.session['logged-name']
        user_role = request.session['logged-user']
        orders = Order.objects.filter(status__contains='active').all()
        order_ids = []
        for order in orders:
            order_ids.append(order.id)
        order_items = OrderItem.objects.filter(order__id__in=order_ids)
        data = {
            'user_name': user_name,
            'user_role': user_role,
            'orders': orders,
            'order_items': order_items,
        }
        return render(request, 'HTML/disp-home.html', data)

    else:
        return redirect('/login/')


def create_order(request):
    customers = Customer.objects.all()
    products = Product.objects.all()
    data = {
        'customers': customers,
        'products': products
    }
    return render(request, 'HTML/create_order.html', data)


def complete_order(request, id):
    if request.method == 'POST':
        return redirect('/dispatcher')

    else:
        if request.session.has_key('logged') and request.session['logged-user'] == 'Dispatcher':
            user_name = request.session['logged-name']
            user_role = request.session['logged-user']
            order = get_object_or_404(Order, id=id)
            order_items = OrderItem.objects.filter(order=order)
            data = {
                'user_name': user_name,
                'user_role': user_role,
                'order': order,
                'order_items': order_items,
            }
            return render(request, 'HTML/complete-order.html', data)

        else:
            return redirect('/dispatcher')


def confirm_order(request):
    if request.method == 'POST':
        if request.session.has_key('logged') and request.session['logged-user'] == 'Dispatcher':
            order_id = request.POST.get('con_order_id')
            order = get_object_or_404(Order, id=order_id)
            for key in request.POST:
                if key.startswith('delivered_quantity_'):
                    item_id = key.split('delivered_quantity_')[1]
                    delivered_quantity = int(request.POST[key])
                    order_item = get_object_or_404(OrderItem, id=item_id)
                    order_item.delivered_quantity = delivered_quantity
                    order_item.save()

            order.status = 'DELIVERED'
            order.delivered_date = timezone.now()
            order.save()
            messages.success(
                request, "Orders has been Mark Completed Sucessfully !")
            return redirect('/dispatcher')
    else:
        return render(request, 'HTML/error-page.html')


def delete_order(request):
    if request.method == 'POST':
        order_id = request.POST['order_id']
        if order_id:
            order = get_object_or_404(Order, id=order_id)
            customer_id = order.order_by.id
            customer = get_object_or_404(Customer, id=customer_id)
            customer.total_orders = customer.total_orders - 1
            customer.save()
            order.delete()
            messages.success(request, "Orders has been Deleted Sucessfully !")
        return redirect('/dispatcher/')

    else:
        return render(request, 'HTML/error-page.html')


def change_schedule(request):
    if request.method == 'POST':
        schedule_date = request.POST['schedule_date']
        order_id = request.POST['date_id']
        if order_id and schedule_date:
            order = get_object_or_404(Order, id=order_id)
            order.scheduled_date = schedule_date
            order.save()
            messages.success(
                request, "Orders Schedule has been Updated Sucessfully !")
        return redirect('/dispatcher/')

    else:
        return render(request, 'HTML/error-page.html')


def submit_data(request):
    if request.method == 'POST':
        customer = request.POST['customer-id']
        item_count = int(request.POST['item-count'])

        items = []
        quantities = []
        for i in range(item_count):
            id = i + 1
            item = request.POST.get(f"product-id-{id}")
            items.append(item)
            quantiy = request.POST.get(f"quantity-{id}")
            quantities.append(quantiy)

        customer_instance = Customer.objects.get(id=int(customer))
        customer_instance.last_order = date.today()
        customer_instance.total_orders = customer_instance.total_orders + 1
        customer_instance.save()
        new_order = Order(order_by=customer_instance)
        new_order.save()

        for i in range(item_count):
            item_instance = Product.objects.get(id=int(items[i]))
            new_item = OrderItem(
                order=new_order, item=item_instance, ordered_quantity=quantities[i])
            new_item.save()

        return HttpResponse("Chal Gaya!")
    else:
        return render(request, 'HTML/error-page.html')


def show_customers(request):
    if request.session.has_key('logged') and request.session['logged-user'] in ['Dispatcher', 'Sales Representive']:
        user_name = request.session['logged-name']
        user_role = request.session['logged-user']
        if request.method == 'POST':
            name = request.POST.get('name-filter', '')
            city = request.POST.get('city-filter', '')
            state = request.POST.get('state-filter', '')
            print(name + ' ' + city + ' ' + state)
            customers = Customer.objects.filter(
                name__contains=name, city__contains=city, state__contains=state)
            data = {
                'customers': customers,
                'name': name,
                'city': city,
                'state': state,
                'user_name': user_name,
                'user_role': user_role,
            }
            return render(request, 'HTML/customers.html', data)

        else:
            customers = Customer.objects.all()
            return render(request, 'HTML/customers.html',
                          {
                              'customers': customers,
                              'user_name': user_name,
                              'user_role': user_role,
                          })
    else:
        return render(request, 'HTML/error-page.html')


def create_customer(request):
    if request.method == 'POST':
        cust_name = request.POST.get('new-Name')
        cust_num = request.POST.get('phone_no')
        cust_addr = request.POST.get('address')
        cust_city = request.POST.get('new-city')
        cust_state = request.POST.get('new-state')
        new_customer = Customer(
            name=cust_name,
            phone=cust_num,
            address=cust_addr,
            city=cust_city,
            state=cust_state,
        )
        new_customer.save()

        return redirect('show_customers')

    else:
        return render(request, 'HTML/error-page.html')


def customer_detail(request, id):
    try:
        customer = Customer.objects.get(id=id)
    except Customer.DoesNotExist:
        return render(request, 'HTML/error-page.html')
    user_name = request.session['logged-name']
    user_role = request.session['logged-user']
    orders = Order.objects.filter(order_by__id=customer.id)
    active_orders = Order.objects.filter(
        status='ACTIVE', order_by__id=customer.id)
    past_orders = Order.objects.filter(
        status='DELIVERED', order_by__id=customer.id)
    order_ids = orders.values_list('id', flat=True)
    order_items = OrderItem.objects.filter(order__id__in=order_ids)

    return render(request, 'HTML/customer_detail.html', {
        'customer': customer,
        'active_orders': active_orders,
        'past_orders': past_orders,
        'order_items': order_items,
        'user_name': user_name,
        'user_role': user_role,
    })
