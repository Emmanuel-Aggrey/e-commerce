from django.shortcuts import render, get_object_or_404
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db.models import Q
from .models import Category, Product, Gallary
from cart.forms import CartAddProductForm


def listAll(request):    
    gallary = Gallary.objects.all()
    
    # allproduct =Product.objects.all().order_by('-created_at')
    queryset_list  = Product.objects.filter(available=True) 

    # not paginating 
    paginator = Paginator(queryset_list, 2)
    page = request.GET.get('page')
    paginator_list = paginator.get_page(page)

    query = request.GET.get('keyword')
    if query:
        queryset_list =  queryset_list.filter(Q(name__icontains=query) | 
        Q(category__name__icontains=query)|
        Q(description__icontains=query)
        )
       
   

    context ={
        'allproduct':queryset_list,
        'gallarys':gallary
          
    }

    return render(request, 'shop/product/mylist.html', context)

def allCategory(request):
    queryset_list = Category.objects.all()

    query = request.GET.get('keyword')
    if query:
        queryset_list =  queryset_list.filter(name__icontains=query)
    notfound ='nothing much your search result'


    context ={
        'categorys': queryset_list,
      
    }

    return render(request, 'shop/product/allcategory.html', context)

def allRelated(request,p_id):
    # allrelated = Product.objects.select_related('category',id = c_id)
    # allRelated = Product.objects.get(id=p_id)
    # allrelated =Product.objects.select_related('category')
    category =Category.objects.all()
    if p_id:
        category = get_object_or_404(Category, id=p_id)
        products = Product.objects.filter(category=category)

    
    context ={
        'allrelated':products,
        
    }
    return render(request, 'shop/product/allrelatedproduct.html', context)
    
def unique_faqs(request):
    context ={
        
    }
    return render(request, 'shop/product/faq.html', context)


def product_list(request, category_slug=None):
   
    category = None
    categories = Category.objects.all()
    queryset_list = Product.objects.filter(available=True)
    query = request.GET.get('keyword')
    if query:
        queryset_list = queryset_list.filter(Q(name__icontains = query)|Q(price__lte=query))

    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=category)

    context = {
        'category': category,
        'categories': categories,
        'products': queryset_list,
        
    }
    return render(request, 'shop/product/list.html', context)


def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    cart_product_form = CartAddProductForm()
    context = {
        'product': product,
        'cart_product_form': cart_product_form
    }
    return render(request, 'shop/product/detail.html', context)


def search_product(request):
    # queryset_list = Product.objects.filter(available=True)
    queryset_list = Product.objects.order_by('-created_at')

    query = request.GET.get('keyword')
    if query:
        queryset_list = queryset_list.filter(Q(name__icontains = query)|Q(price__lte=query))
    size = len(queryset_list)

    context = {
        'search_result':queryset_list,
        'resultSize': size,
    }

    return render(request, 'shop/product/search.html',context)


def mygallery (request):

    gallary = Gallary.objects.all()

    context = {
        'gallary': gallary,
    }
    return render(request,'shop/partials/carousel.html', context )