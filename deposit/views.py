from django.shortcuts import render
from deposit.models import Deposit
from django.views.generic import View, ListView, DetailView, FormView
from deposit.forms import DepositForm
from django.urls import reverse_lazy


def interest(deposit, term, rate):
    sum_int = float(deposit)
    for i in range(0, int(term)):
        sum_int = sum_int * (1+float(rate))
    return sum_int - float(deposit)


class DepositListView(ListView):

    model = Deposit
    template_name = 'deposit/index.html'


class AddDeposit(FormView):
    form_class = DepositForm
    Template_name = 'deposit/new_deposit.html'
    success_url = reverse_lazy('deposit_list')

    def form_valid(self, form):
        form.save()

        response = super().form_valid(form)
        return response


class DepositDetail(DetailView):

    model = Deposit
    template_name = 'deposit/deposit_detail.html'
    context_object_name: 'deposit'
