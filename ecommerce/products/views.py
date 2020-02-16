from django.shortcuts import render, get_object_or_404
from django.http import Http404
from .models import Product
from carts.models import Cart
from django.views.generic import ListView, DetailView
# Create your views here.


class ProductView(ListView):
    queryset = Product.objects.all()


class product_details_slug_view(DetailView):
    queryset = Product.objects.all()
    template_name = "products/details.html"

    def get_context_data(self, *args, **kwargs):
        context = super(product_details_slug_view, self).get_context_data(*args, **kwargs)
        cart_obj, new_obj = Cart.objects.new_or_get(self.request)
        context['cart'] = cart_obj
        return context

    def get_object(self, *args, **kwargs):
        request = self.request
        slug = self.kwargs.get('slug')
        # queryset = get_object_or_404(Product, slug=slug)
        try:
            queryset = Product.objects.get(slug=slug, active=True)
        except Product.DoesNotExist:
            raise Http404("Not Found")
        except Product.MultipleObjectsReturned:
            qs=Product.objects.filter(slug=slug, active=True)
            queryset = qs.first()
        except:
            raise Http404("Hmmm")
        return queryset

#
# class product_Details_slug_view(DetailView):
#     queryset = Product.objects.all()
#     template_name = "products/details.html"
#

def product_details_view(request,pk=None, *args, **kwargs):
    # queryset = Product.objects.get(pk = pk)

    # qs = Product.objects.filter(id = pk)
    queryset = Product.objects.get_by_id(id=pk)
    if queryset is None:
        raise Http404('Product Does not exits')
    mydict = {
        'object':queryset
    }
    return render(request, 'products/details.html', mydict)
