from django.shortcuts import render,redirect
from .models import *
from .forms import orderForm,CreateUSerForm
from django.contrib import messages
from django.contrib.auth import authenticate , login , logout
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='login')
def home(request):
    orders = order.objects.all()
    customers = Customer.objects.all()
    tot_customers = customers.count()
    tot_orders = orders.count()
    delivered = orders.filter(status='Delivered').count()
    pending = orders.filter(status='Pending').count()
    context = {'orders':orders, 'customers':customers, 'tot_customers':tot_customers, 'tot_orders':tot_orders, 'delivered':delivered, 'pending':pending}
    return render(request, 'dashboard.html', context)

@login_required(login_url='login')
def products(request):
    products = product.objects.all()
    return render(request, 'products.html',{'prod':products})

@login_required(login_url='login')
def customer(request,pk):
    customers = Customer.objects.get(id=pk)
    orders = customers.order_set.all()
    tot_orders = orders.count()
    context = {'customers':customers, 'orders':orders, 'tot_orders':tot_orders}
    return render(request, 'customer.html',context)

@login_required(login_url='login')
def createOrder(request,pk):
    customer = Customer.objects.get(id=pk)
    form = orderForm(initial={'customer':customer})
    context = {'form':form}
    if request.method == 'POST':
        #print("printing ",request.POST)
        form = orderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request,'order_form.html',context)

@login_required(login_url='login')
def updateOrder(request,pk):
    orders = order.objects.get(id=pk)
    form = orderForm(instance=orders)
    context = {'form':form}
    if request.method == 'POST':
        form = orderForm(request.POST,instance = orders)
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request,'order_form.html',context)

@login_required(login_url='login')
def deleteOrder(request,pk):
    orders = order.objects.get(id=pk)
    context = {'item':orders}
    if request.method == 'POST':
        orders.delete()
        return redirect('/')
    
    return render(request,'delete.html',context)

def register(request):
    form= CreateUSerForm()
    if request.method=="POST":
        form=CreateUSerForm(request.POST)
        if form.is_valid():
            user=form.save()
            Username=form.cleaned_data.get('username')
            messages.success(request,"profile was created for"+ Username)
            return render(request,'login.html')
    context={'form':form}
    return render(request,'register.html',context)

def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('/')
        else:
            messages.info(request,"Username or password may be incorrect")
    context = {}
    return render(request,'login.html',context)

def logoutUser(request):
    logout(request)
    return redirect('login')