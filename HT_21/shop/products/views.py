from django.shortcuts import render, redirect
from .models import Products
from .forms import LoginForm
from django.contrib import messages
from django.views.generic import UpdateView, DeleteView
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin
from cart.forms import CartAddProductForm
from rest_framework import viewsets
from .serializers import ProductsSerializer, CategoriesSerializer, UsersSerializer
from .models import Products, Categories
from django.contrib.auth.models import User


def home(request):
    all_objects_list = Products.objects.all()

    response_phones = request.POST.get('submit_phones')
    response_headphones = request.POST.get('submit_headphones')
    response_notebooks = request.POST.get('submit_notebooks')
    response_keys = request.POST.get('submit_keys')

    midlle_list = [response_phones, response_headphones, response_notebooks, response_keys]
    result_list = [i for i in midlle_list if i != None]

    data_export = []

    data = {
        'products_list': all_objects_list
    }

    if len(result_list) != 0:
        for i in all_objects_list:
            if str(i.category) == result_list[0]:
                data_export.append(i)
        data['products_list'] = data_export

    return render(request, 'products/home.html', data)


def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(
                username=data['username'],
                password=data['password']
            )
            if user:
                auth_login(request, user)
                messages.success(request, f'Welcome, {user}')
                return redirect('home')
            else:
                messages.success(request, 'Wrong login or password, please try again')
                return redirect('login')
    else:
        form = LoginForm()
    context = {'form': form}

    return render(request, 'products/user_in.html', context)


def more_product(request, pk):
    all_objects_list = Products.objects.all()
    result_list = []

    for i in all_objects_list:
        if i.id == pk:
            result_list.append(i)

    cart_product_form = CartAddProductForm()

    data = {
        'result_list': result_list,
        'cart_product_form': cart_product_form
    }

    return render(request, 'products/more_product.html', data)


class UpdateProduct(SuccessMessageMixin, UserPassesTestMixin, UpdateView):
    model = Products
    template_name = 'products/update_product.html'
    fields = ['name', 'description', 'price', 'category']
    success_message = "Product information has been successfully changed"

    def get_success_message(self, cleaned_data):
        return self.success_message

    def test_func(self):
        return self.request.user.is_superuser

    def handle_no_permission(self):
        messages.error(self.request, 'You do not have rights to edit this product, please contact the site administrator')
        return redirect('home')


class DeleteProduct(SuccessMessageMixin, UserPassesTestMixin, DeleteView):
    model = Products
    success_url = '/'
    template_name = 'products/delete.html'
    success_message = "The product page has been deleted"

    def test_func(self):
        return self.request.user.is_superuser


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer


class CategoriesViewSet(viewsets.ModelViewSet):
    queryset = Categories.objects.all()
    serializer_class = CategoriesSerializer


class UsersViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UsersSerializer
