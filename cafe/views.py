from django.shortcuts import render, redirect
from django.views.generic import TemplateView, DetailView
from .models import Dish, DishCategory, Gallery, Event, ContactInfoItem
from .forms import ContactForm, BookTableForm
from django.core.mail import send_mail
from django.contrib import messages
from django.utils import timezone
from django.db import models


class CafeHome(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)

        context['title'] = 'Yummy'

        context['dish_categories'] = DishCategory.objects.filter(is_visible=True)
        context['gallery'] = Gallery.objects.filter(is_visible=True)
        context['events'] = Event.objects.filter(models.Q(is_visible=True) &
                                                 (models.Q(date_time__isnull=True) |
                                                  models.Q(date_time__date__gte=timezone.now())))
        context['contacts_info'] = ContactInfoItem.objects.all()
        context['contact_form'] = ContactForm()
        context['booking_form'] = BookTableForm()
        return context

    def post(self, request, *args, **kwargs):
        contact_form = ContactForm(request.POST)
        booking_form = BookTableForm(request.POST)

        if contact_form.is_valid():
            name = contact_form.cleaned_data['name']
            email = contact_form.cleaned_data['email']
            message = contact_form.cleaned_data['message']

            send_mail(
                'Сообщение с контактной формы',
                f'Имя: {name}\nEmail: {email}\nСообщение: {message}',
                f'{email}',
                ['oleg.s.tymchuk@gmail.com'],
                fail_silently=False,
            )

            messages.success(request, 'Сообщение успешно отправлено')
            return redirect('cafe:home')

        if booking_form.is_valid():
            booking_form.save()
            messages.success(request, 'Ваш заказ принят')
            return redirect('cafe:home')

        context = self.get_context_data()
        context['contact_form'] = contact_form
        context['booking_form'] = booking_form
        return render(request, self.template_name, context)


class ShowDish(DetailView):
    template_name = 'dish.html'
    model = Dish
    context_object_name = 'dish'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Yummy'
        context['inner_title'] = f'Yummy - {self.object.name}'
        return context
