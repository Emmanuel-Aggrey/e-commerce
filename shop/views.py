from django.shortcuts import render, get_object_or_404
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Category, Product, Gallary
from cart.forms import CartAddProductForm
from datetime import date, timedelta
from django.utils import timezone


def product_list(request, category_slug=None):

    category = None
    categories = Category.objects.all()
    # categories = categories.products.all()
    queryset_list = Product.objects.filter(available=True)
    query = request.GET.get('keyword')
    if query:
        queryset_list = queryset_list.filter(
            Q(name__icontains=query) | Q(category__name__icontains=query))

    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=category)

    context = {
        'category': category,
        'categories': categories,
        'products': queryset_list,
        'latest_product': queryset_list.filter(available=True).order_by('?', '-updated_at'),
        'all_category': Category.objects.all(),


    }
    return render(request, 'shop/product/list.html', context)


def allCategory(request):
    queryset_list = Category.objects.all()
    sugest = Product.objects.order_by('-updated_at')
    best_buy = sugest.order_by('created_at')

    query = request.GET.get('keyword')
    if query:
        queryset_list = queryset_list.filter(name__icontains=query)
    notfound = 'nothing much your search result'

    context = {
        'categorys': queryset_list,
        'sugest': sugest,
        'best_buy': best_buy,

    }

    return render(request, 'shop/product/allcategory.html', context)


def allRelated(request, slug):
    # allrelated = Product.objects.select_related('category',id = c_id)
    # allRelated = Product.objects.get(id=p_id)
    # allrelated =Product.objects.select_related('category')
    # category =Category.objects.all()

    # if slug:
    category = get_object_or_404(Category, slug=slug)
    products = category.products.all()
    # product = Product.objects.filter(category=category)

    paginator = Paginator(products, 10)
    page = request.GET.get('page')

    try:
        product = paginator.page(page)
    except PageNotAnInteger:
        product = paginator.page(1)
    except EmptyPage:
        product = paginator.page(paginator.num_pages)

    affordable = products.filter(available=True)
    value = request.GET.get('value')
    if value:
        affordable = products.filter(price__lte=value)

    context = {
        'allrelated': product,
        'category': category,
        'affordable': affordable,

    }
    return render(request, 'shop/product/allrelatedproduct.html', context)


def unique_faqs(request):
    context = {

    }
    return render(request, 'shop/product/faq.html', context)


def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    cart_product_form = CartAddProductForm()

    recomendation = Product.objects.filter(name__icontains=product.name)

    may_like = Product.objects.filter(price__lte=product.price)
    context = {
        'product': product,
        'cart_product_form': cart_product_form,
        'recomendation': recomendation,
        'may_like': may_like,
    }
    return render(request, 'shop/product/detail.html', context)


def search_product(request):
    # queryset_list = Product.objects.filter(available=True)
    queryset_list = Product.objects.order_by('-created_at')

    query = request.GET.get('keyword')
    if query:
        queryset_list = queryset_list.filter(
            Q(name__icontains=query) | Q(price__lte=query))
    size = len(queryset_list)

    context = {
        'search_result': queryset_list,
        'resultSize': size,
    }

    return render(request, 'shop/product/search.html', context)


def mygallery(request):

    gallary = Gallary.objects.all()

    context = {
        'gallary': gallary,
    }
    return render(request, 'shop/partials/carousel.html', context)
