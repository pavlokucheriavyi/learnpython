
from django.urls import path
from . import views
from django.contrib.auth import views as authViews

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login, name='login'),
    path('exit/', authViews.LogoutView.as_view(template_name='products/exit.html'), name='exit'),
    path('more/<int:pk>', views.more_product, name='more'),
    path('more/<int:pk>/update', views.UpdateProduct.as_view(), name='update'),
    path('more/<int:pk>/delete', views.DeleteProduct.as_view(), name='delete')
]
