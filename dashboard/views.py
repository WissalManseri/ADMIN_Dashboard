import json
from django.contrib.auth.models import User
from django.views.generic import TemplateView
from .models import Signup, Order
# Create your views here.


class DashboardView(TemplateView):
    template_name = 'dashboard.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        signup_data = Signup.objects.all()
        context['signup_data_json'] = json.dumps(list(signup_data.values()))
        return context

class UserListView(TemplateView):
    template_name = 'user_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        users = User.objects.all()
        context['users'] = users
        return context

class OrderListView(TemplateView):
    template_name = 'order_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        orders = Order.objects.all()
        context['orders'] = orders
        return context