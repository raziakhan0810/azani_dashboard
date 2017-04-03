from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from models import *


def home_page(request):
    return render(request, 'homepage.html')


def register(request):
    if request.method == 'GET':
        return render(request, 'register.html')

    else:
        username = request.POST.get('username', None)
        full_name = request.POST.get('first_name', None)
        address = request.POST.get('address', None)
        password = request.POST.get('password', None)

        try:
            user = User.objects.create_user(username, None, password)
            user.save()

            Profile.objects.create(
                user=user,
                name=full_name,
                address=address
            )

        except Exception as exc:
            print exc
        return redirect('/login/')


def user_login(request):
    if request.method == 'GET':
        return render(request, 'login.html')

    else:
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)

        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return redirect('/dashboard/')
            else:
                return HttpResponse('User disabled')
        else:
            return HttpResponse('Invalid username/password')


@login_required(login_url='/login/')
def logout_view(request):
    logout(request)
    return redirect('/')


@login_required(login_url='/login/')
def dashboard(request):
    return render(request, 'table.html', {'orders': Order.objects.all().order_by('-id')})


@login_required(login_url='/login/')
def create_order(request):
    if request.method == 'GET':
        return render(request, 'create_order.html')

    else:
        order_id = request.POST.get('order_id', None)
        product_name = request.POST.get('product_name', None)
        status = request.POST.get('status', None)
        cost_price = request.POST.get('cost_price', None)
        product_url = request.POST.get('product_url', None)

        print 'status', status

        try:

            Order.objects.create(
                order_id=order_id,
                product_name=product_name,
                status=status,
                cost_price=cost_price,
                product_url=product_url
            )

        except Exception as exc:
            print exc
        return redirect('/dashboard/')
