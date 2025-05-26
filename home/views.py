from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from django.core.paginator import Paginator
from django.views.generic import TemplateView, View
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from home.models import Blog, Main, AboutUs, Gallery, ContactUs, Comments, PhotoGallery
from  home.forms import ContactUsForm, CommentsForm
from django.http import HttpResponse
from django.views.generic.detail import DetailView




class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        blogs_list = Blog.objects.order_by('-id')  # Правильно

        paginator = Paginator(blogs_list, 3)
        page_number = self.request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        context['blogs'] = page_obj
        context['site'] = Main.objects.first()
        return context


class BlogDetail(View):
    def get(self, request, pk):
        post = get_object_or_404(Blog, id=pk)
        comments = post.comments.all()
        form = CommentsForm()
        return render(request, 'single-post.html', {
            'post': post,
            'comments': comments,
            'form': form,
        })

    def post(self, request, pk):
        blog = get_object_or_404(Blog, id=pk)
        form = CommentsForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = blog
            comment.save()
            return redirect('single_post', pk=blog.id)  # Имя URL, проверь в urls.py
        comments = blog.comments.all()
        return render(request, 'single-post.html', {
            'blog': blog,
            'comments': comments,
            'form': form,
        })



class AboutUsView(TemplateView):
        template_name = 'about.html'

        def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)  # Сначала создаём context
            context['abouts'] = AboutUs.objects.all()  # Потом используем
            return context


        def get_object(self):
            return get_object_or_404(AboutUs, id=self.kwargs.get("id"))


class ContactUsView(View):
    template_name = 'contact.html'

    def get(self, request):
        form = ContactUsForm()
        contact = ContactUs.objects.order_by('-id').first()  # безопасно вернёт None, если нет записей
        return render(request, self.template_name, {'form': form, 'contact': contact})

    def post(self, request,*args,**kwargs):
        form = ContactUsForm(request.POST)
        if form.is_valid():
            contact_message = form.save()
            send_mail(
                subject ='Спасибо за ваше сообшение!',
                message ='Мы получили ваше сообшение и ответим в ближайшее время.',
                from_email = settings.EMAIL_HOST_USER,
                recipient_list = [contact_message.email],
                fail_silently = False
            )
            messages.success(request, "Ваше сообщение отправлено!")
            return redirect('contact')
        messages.error(request, 'Пожалуйста исправьте ошибку в форме!')
        return render(request, self.template_name, {'form':form})


class GalleryView(TemplateView):
      template_name = 'gallery.html'
      def get_context_data(self, **kwargs):
          context = super().get_context_data(**kwargs)
          context['gallerys'] = Gallery.objects.all()
          context['photos'] = PhotoGallery.objects.all()
          return context






