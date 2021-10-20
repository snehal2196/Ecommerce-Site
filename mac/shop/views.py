from django.shortcuts import render
from django.http import HttpResponse, response
from .models import OrderUpdate, Product,Contact,Order
from math import ceil
import json
# Create your views here.

def index(request):
    allProds = []
    catprods = Product.objects.values('category')
    cats = { item['category'] for item in catprods }
    for cat in cats:
        prods = Product.objects.filter(category=cat)
        n = len(prods)
        nSlide = n // 4 + ceil((n / 4) - (n // 4))
        allProds.append([prods, range(1, nSlide), nSlide])

    params = {'allProds':allProds}
    return render(request, 'shop/index.html', params)

def searchMatch(query, item):
    if query in item.product_name.lower() or query in item.product_desc.lower() or query in item.category.lower():
        return True
    else:
        return False

def search(request):
    query= request.GET.get('search')
    allProds = []
    catprods = Product.objects.values('category', 'id')
    cats = {item['category'] for item in catprods}
    for cat in cats:
        prodtemp = Product.objects.filter(category=cat)
        prod=[item for item in prodtemp if searchMatch(query, item)]
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        if len(prod)!= 0:
            allProds.append([prod, range(1, nSlides), nSlides])
    params = {'allProds': allProds, 'msg':""}
    if len(allProds)==0 or len(query)<4:
        params={'msg':"Please make sure to enter relevant search query"}
    return render(request, 'shop/search.html', params)

def about(request):
    return render(request, 'shop/about.html')


def contact(request):
    if request.method == 'POST':
        name= request.POST.get('name')
        email= request.POST.get('email')
        phone= request.POST.get('phone')
        desc= request.POST.get('desc')

        contact = Contact(name=name, email=email, phone=phone, desc=desc)
        contact.save()
    return render(request, 'shop/contact.html')


def tracker(request):
    if request.method == 'POST':
        orderId= request.POST.get('orderId')
        email= request.POST.get('email')
        #return HttpResponse(f"{orderId} and {email}")
        try:
            order = Order.objects.filter(id=orderId,email=email)
            if len(order)>0:
                update = OrderUpdate.objects.filter(order_id = orderId)
                updates = []
                for item in update:
                    updates.append({'text':item.update_desc, 'time':item.datetime})
                    response = json.dumps({'status':'success', 'updates':updates, 'itemJson': order[0].itemJson},default=str)
                return HttpResponse(response)
            else:
                return HttpResponse('{}')
        except Exception as e:
            return HttpResponse(e)

    return render(request, 'shop/tracker.html')





def productView(request, pid):
    product = Product.objects.filter(id=pid)
    return render(request, 'shop/prodView.html',{'product':product[0]})


def checkout(request):
    if request.method == 'POST':
        itemJson= request.POST.get('itemJson')
        name= request.POST.get('name')
        email= request.POST.get('email')
        address1= request.POST.get('address1')
        address2= request.POST.get('address2')
        state= request.POST.get('state')
        city= request.POST.get('city')
        zip_code= request.POST.get('zip_code')
        phone= request.POST.get('phone')
        
        order = Order(itemJson=itemJson,name=name, email=email, address1=address1,address2=address2,state=state,city=city,zip_code=zip_code,phone=phone)
        order.save()
        update = OrderUpdate(order_id = order.id, update_desc = "The order has been placed.")
        update.save()
        thank = True
        id = order.id
        return render(request, 'shop/checkout.html',{'thank':thank, 'id':id})
    return render(request, 'shop/checkout.html')
    