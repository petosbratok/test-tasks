from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.db.models import Count
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
    RedirectView,
)
from .models import Table
from users.models import Profile, Subdivision
from rest_framework.response import Response
from rest_framework import authentication, permissions

class PostListView(ListView):
    model = Table
    order_by = 'title'
    context_object_name = 'tables'
    template_name = 'blog/home.html'

def table_detail(request, pk):
    table = Table.objects.get(id=pk)
    workers = [worker.split(',') for worker in table.data.split(';')]
    context = {
        'table': table,
        'workers': workers,
    }
    if request.method == 'POST':
        print(request.POST.get('data'))
        table.data = request.POST.get('data')
        table.save()
        return redirect(request.META['HTTP_REFERER'])
    return render(request, 'blog/table_detail.html', context)


def subdivision_detail(request, pk):
    subdivision = Subdivision.objects.get(id=pk)
    context = {
        'subdivision': subdivision,
    }
    return render(request, 'blog/subdivision_detail.html', context)


class TableCreateView(LoginRequiredMixin, CreateView):
    model = Table
    fields = ['title', 'length']
    def form_valid(self, form):
        profile = Profile.objects.get(user=self.request.user)
        if not profile.tablemaster:
            messages.error(self.request, 'Вы не можете создавать табели')
            return HttpResponseRedirect(self.request.path_info)
        form.instance.author = self.request.user
        users = Profile.objects.filter(subdivision=profile.subdivision)
        # print(self.request)
        length = int(self.request.POST.get('length'))
        data = ''
        for user in users:
            data += user.full_name + ',0' * length + ';'

        form.instance.data = data[:-1]

        return super().form_valid(form)

    def get_success_url(self):
        return reverse('table-detail', kwargs={'pk': self.object.pk})


class SubdivisionCreateView(LoginRequiredMixin, CreateView):
    model = Subdivision
    fields = ['title']
    def form_valid(self, form):
        form.instance.data = self.request.POST.get('title')

        return super().form_valid(form)

    def get_success_url(self):
        return reverse('subdivision-detail', kwargs={'pk': self.object.pk})
