"""login_reg URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.urls import path, include

from app import views
from app.views import MarketerApiView

urlpatterns = [
    path('login/', views.login, name="login"),
    path('logout/', views.logout, name="logout"),
    # path('add-marketer/',views.add_marketer, name="addMarketer"),

    path('add-marketer/',views.Index.as_view(template_name='signup_marketer.html'), name="addMarketer"),
    path('buyer-signup/', views.buyer_signup, name="signup"),
    path('shared-url/<str:uu_id>', views.shared_url, name="shared-ur"),
    path('marketerUuid', MarketerApiView.as_view(), name='marketerUuid'),
    path('buyItem', views.BuyItem.as_view(), name='buyItem'),
    path('test/<str:uu_id>', views.ProductSharedUrl.as_view(), name='test'),

]
