from .models import Product, Cart
from django.core.urlresolvers import reverse_lazy
from django.views import generic
from django.contrib.auth import get_user_model
from django.contrib import auth
from braces import views as bracesviews
from . import forms

User = get_user_model()
class ProductCreateView(generic.CreateView):
    model = Product
    fields = ('name', 'price', 'stock', 'description',)

class ProductDetailView(generic.DetailView):
    model = Product

class ProductListView(generic.ListView):
    model = Product

class CartCreateView(generic.CreateView):
    model = Cart
    fields = ('product', 'quantity',)
    success_url = reverse_lazy('profiles:edit_self')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user= self.request.user
        print(self.object)
        self.object.save()
        return super(CartCreateView, self).form_valid(form)


class CartDetailView(generic.DetailView):
    model = Cart

class CartListView(generic.ListView):
    model = Cart

    def get_context_data(self, **kwargs):
        context = super(CartListView, self).get_context_data(**kwargs)
        context['cart_list'] = Cart.objects.all().filter(complete=False).filter(user=self.request.user)
        return context

class UserCreateView(bracesviews.AnonymousRequiredMixin,
                 bracesviews.FormValidMessageMixin,
                 generic.CreateView):
    form_class = forms.UserCreateForm
    model = User
    template_name = 'accounts/signup.html'
    success_url = reverse_lazy('home')
    form_valid_message = "You're signed up!"

    def form_valid(self, form):
        r = super(UserCreateView, self).form_valid(form)
        username = form.cleaned_data["email"]
        password = form.cleaned_data["password1"]
        user = auth.authenticate(email=username, password=password)
        auth.login(self.request, user)
        return r

class PendingOrders(generic.TemplateView):
    template_name = 'products/pending_orders.html'
    def get_context_data(self, **kwargs):
        context = super(PendingOrders, self).get_context_data(**kwargs)
        # context['user_list'] = User.objects.all().filter(email=None)
        context['cart_list'] = Cart.objects.all().order_by('user')
        return context