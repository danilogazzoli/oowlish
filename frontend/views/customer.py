from django.views.generic import TemplateView
from customers.models import Customer


class CustomerTemplateView(TemplateView):
    template_name = "customer/customers.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context["customer_list"] = Customer.objects.all()
        return context


