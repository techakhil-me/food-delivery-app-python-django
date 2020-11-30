from django.shortcuts import render,redirect,HttpResponse
import mysql.connector
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from .models import tomato_user,cart
import sqlite3


# Create your views here.
#super user anika anika@07

def mysql_db():
    mydb = mysql.connector.connect(
      host="localhost",
      user="root", # default user="root"
      password="",  # default password=""
      database="fooddb"
    )
    mycursor = mydb.cursor()
    row = []
    types = ['STARTER','MAINCOURSE','DESSERT']
    for type in types:
        mycursor.execute(f"SELECT * FROM {type}")
        result = mycursor.fetchall()
        print(result)
        row.append([type,result])
    return row
    # print(row)
def sqlite_db():
    mycursor = sqlite3.connect('menu.db')
    row = []
    types = ['STARTER','MAINCOURSE','DESSERT']
    for type in types:
        result = mycursor.execute(f"SELECT * FROM {type}")
        # print(list(result))
        result = list(result)
        row.append([type,result])
    return row

row = sqlite_db()
print(row)
def signin(request):
    context={'case':True}
    if not request.user.is_anonymous:
        return redirect('/')
        
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        username_new = request.POST.get('username_new')
        password_new = request.POST.get('password_new')
        # print(username,username_new)
        if username_new is None:
            user = authenticate(username=username, password=password)
            if user is not None:
                # A backend authenticated the credentials
                login(request,user)
                return redirect('/')
            else:
                context['case'] = False
                return render(request,"login.html",context=context)

        else:
            if (username_new,) in User.objects.values_list("username",) :
                context['case'] = False
                return render(request,'login.html',context)
            
            tomato_user.objects.create(username=username_new)
            new_user = User.objects.create_user(username_new,"tomato_user@gmail.com",password_new)
            new_user.save()
            login(request,new_user)
            return redirect('/')
    return render(request,"login.html",context=context)


def logout_auth(request):
    logout(request)
    return redirect('/login')

def home(request):
    if request.user.is_anonymous:
        return redirect('/login')
    main = {}

    if request.method == 'POST':
        product = request.POST.get('product').strip()
        quantity = request.POST.get('quantity').strip()
        price = request.POST.get('price').strip()
        # print(product,quantity,price)
        cur_user = tomato_user.objects.get(username = request.user)
        if (product,) in cur_user.cart_set.values_list("product",):
            update = cur_user.cart_set.get(product=product)
            if quantity != '0':
                update.quantity = quantity
                update.save()
            else:
                update.delete()

        else:
            cur_user.cart_set.create(product=product,quantity=quantity,price=price  )
        return HttpResponse("")

    cur_user = tomato_user.objects.get(username = request.user)
    products = cur_user.cart_set.values_list("product")
    product_lst = list(i[0] for i in [ k for k in products])
    items_dict = {i:cur_user.cart_set.get(product=i).quantity for i in product_lst}

    cart_items = list(cur_user.cart_set.all())
    cart_total = sum([int(item.quantity) for item in cart_items])

    return render(request,"home.html",context={'data':row, 'cart_total': cart_total,'items_dict':items_dict})



def cart(request):
    if request.user.is_anonymous:
        return redirect('/login')
    cur_user = tomato_user.objects.get(username = request.user)
    if request.method == 'POST':
        case = request.POST.get('clear')

        if case == 'True':
            cur_user.cart_set.all().delete()
        return HttpResponse("")
    
    cart_items = list(cur_user.cart_set.all())
    cart_total = sum([int(item.quantity) for item in cart_items])
    return render(request,"cart.html",context={'cart_items':cart_items,'cart_total': cart_total,})
