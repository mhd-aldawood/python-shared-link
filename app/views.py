import uuid

from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.views.generic import ListView
from rest_framework import permissions
from rest_framework.views import APIView

from app.models import Marketer, Product, MarketerProduct, BuyerProduct, Buyer
from app.serializer import MarketerSerializer, ProductSerializer

User = get_user_model()


def buyer_signup(request):
    if request.method == "POST":
        if request.POST['password1'] == request.POST['password2']:
            try:
                User.objects.get(username=request.POST['username'])
                return render(request, 'signup.html', {'error': 'Username is already taken!'})
            except User.DoesNotExist:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'],
                                                balance=request.POST['balance'])
                auth.login(request, user)
                return redirect('home')
        else:
            return render(request, 'signup.html', {'error': 'Password does not match!'})
    else:
        return render(request, 'signup.html')


# @login_required(login_url='login')
# def add_marketer(request):
#     return render(request, 'signup_marketer.html')


def login(request):
    if request.method == 'POST':
        user = auth.authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            auth.login(request, user)
            if user.is_staff:
                return redirect('addMarketer');
            else:
                return redirect('home')
        else:
            return render(request, 'login.html', {'error': 'Username or password is incorrect!'})
    else:
        return render(request, 'login.html')


def logout(request):
    # if request.method == 'POST':
    auth.logout(request)
    return redirect('home')


def shared_url(request, uu_id: str):
    try:
        user = User.objects.get(uu_id=uu_id)
        user.total_used = user.total_used + 1
        user.save()
        msg = "increased successfully"
    except:
        msg = "not found"
    return JsonResponse({"msg": msg})


class ProductSharedUrl(APIView):
    # model=MarketerProduct
    # template_name = 'index.html'
    # context_object_name = 'productList'

    def get(self, request, uu_id):
        marketer_uuid = uu_id  # self.kwargs['lab']
        # Marketer.objects.filter(marketer__uuid=marketer_uuid)
        result = MarketerProduct.objects.filter(marketer_id=marketer_uuid).select_related('product').all()
        list = {}
        for item in result:
            list.update({item.product})


class BuyItem(APIView):
    def get(self, request):
        pass

    def post(self, request):
        if request.user.is_staff:
            pass
        # marketer_uuid=request.data['marketerUuid']
        # marketer=Marketer.objects.get(uuid=marketer_uuid)

        else:
            # product operation
            product_id = request.data['productId']
            product = Product.objects.get(pk=product_id)
            product.quantity -= 1
            product.save()

            # user operation
            # user_id=request.user.id
            user = request.user
            user = Buyer.objects.get(pk=user.id)
            user.balance -= product.price
            user.save()

            # save this transaction for this user
            BuyerProduct.objects.create(buyer=user, product=product)

            data = ProductSerializer(product).data
            return JsonResponse(data)


class Index(ListView):
    model = Product
    # template_name = 'index.html'
    context_object_name = 'productList'


class MarketerApiView(APIView):
    permission_classes = [
        permissions.AllowAny
    ]

    @staticmethod
    def get(self, request, username):
        marketers = Marketer.objects.get(username=username)
        data = MarketerSerializer(marketers).data
        return JsonResponse(data)

    @staticmethod
    def post(request):
        try:
            Marketer.objects.get(username=request.data['username'])
            return JsonResponse(request, 'add_marketer.html', {'error': 'Username is already taken!'})

        except Marketer.DoesNotExist:

            uu_id = uuid.uuid4()
            marketer = Marketer.objects.create(username=request.data['username']
                                               , gender=request.data['gender']
                                               , percentage_in_marketing=request.data['percentage_in_marketing']
                                               , minimum_to_receive=request.data['minimum_to_receive']
                                               , uu_id=uu_id)

            products = request.data['products']
            products_list = Product.objects.filter(name__in=products)

            for product in products_list:
                MarketerProduct.objects.create(marketer=marketer, product=product)

            return JsonResponse({"marketer": uu_id}, safe=False)
