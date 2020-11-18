from django.shortcuts import render ,get_object_or_404
from django.core.paginator import Paginator
from contact.models import Elec_semlali_info
from .models import Product ,Tags ,Category
# Create your views here.
def home_page (request):
    if len(request.GET) != 0:
        data = request.GET['product']
        products = Product.objects.filter(PRD_Name__startswith=f'{data}')
        paginator = Paginator(products,12)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
    else:
        products = Product.objects.all()
        paginator = Paginator(products,12)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
    Web_site  = Elec_semlali_info.objects.first()
    Catregorys = Category.objects.all()
    context ={
    'products':page_obj,
    'info':Web_site,
    'Catregorys':Catregorys,
                    }                
    return render(request,'project\home_page.html',context)



def One_pruduct(request,slug):
    obj = get_object_or_404(Product,slug=slug)
    Web_site  = Elec_semlali_info.objects.first()

    context = {
        "obj":obj,
        'info':Web_site

    }
    return render(request,'project/product-page.html',context)

def Categorys_handeling(request , slug):
    object_self = Category.objects.get(slug=slug)
    categorys = Product.objects.filter(PRD_Ctegory=object_self)
    Catregorys = Category.objects.all()
    context ={
        'categorys_1':categorys,
        'Catregorys_bar':Catregorys,
    }
    return render(request,'project\Category_page.html', context)