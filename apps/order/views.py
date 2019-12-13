from django.views.generic import View, TemplateView, RedirectView
from django.shortcuts import get_object_or_404, redirect
from django.http import JsonResponse

from ..core.models import Book
from ..order.cart import Cart
from ..order.models import OrderBook
from ..order.forms import OrderForm


class CartView(TemplateView):
    template_name = 'order/cart.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cart'] = Cart(self.request)
        return context


class AddCartView(View):

    def post(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        book = get_object_or_404(Book, pk=pk)
        cart = Cart(request)
        cart.add(book)
        return redirect('core:index')


class RemoveCartView(View):

    def post(self, request, *args, **kwargs):
        cart = Cart(request)
        pk = self.kwargs.get('pk')
        book = get_object_or_404(Book, pk=pk)
        cart.remove(book)
        return redirect('order:cart')


class ClearCartView(RedirectView):
    pattern_name = 'core:index'

    def get_redirect_url(self, *args, **kwargs):
        Cart(self.request).clear()
        return super().get_redirect_url(*args, **kwargs)


class CheckoutView(TemplateView):
    template_name = 'order/checkout.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cart'] = Cart(self.request)
        return context

    def post(self, request):

        if request.user.is_authenticated:
            address = request.POST.get('address')
            comment = request.POST.get('comment')
            form = OrderForm({
                'user': request.user.id,
                'name': request.user.name,
                'surname': request.user.surname,
                'email': request.user.email,
                'phone': request.user.phone,
                'address': address,
                'comment': comment,
            })
            if form.is_valid():
                order = form.save()
                cart = Cart(request)
                for item in cart:
                    print(item)
                    OrderBook.objects.create(
                        order=order,
                        book=item['book'],
                        quantity=item['quantity']
                    )
                cart.clear()
            else:
                return JsonResponse(form.errors)
        else:
            print('else')
        return redirect('users:profile')
