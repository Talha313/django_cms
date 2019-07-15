from tempfile import template

from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render, redirect


# Create your views here.
from django.urls import reverse
from django.views.generic import TemplateView, ListView

from blogs.models import Blog, Comment


class BlogView(ListView):
    template_name = 'blogs.html'
    model = Blog
    paginate_by = 10

    queryset = model.objects.filter(is_active=True)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['blog'] = 'active'
        return context


class BlogDetailView(TemplateView):
    template_name = 'blog_detail.html'

    def get(self, request, slug):
        print(slug)
        blog = Blog.objects.get(is_active=True, slug=slug)
        comments = Comment.objects.filter(blog=blog)
        print(comments)
        return render(request, self.template_name, {'blog': blog, 'comments': comments})

    def post(self, request, slug):
        comment = request.POST.get('comment')

        print(comment)
        blog = Blog.objects.get(is_active=True, slug=slug)
        comment = Comment(blog=blog, user=self.request.user)
        comment.save()

        return render(request, self.template_name)

class BlogCommentView(LoginRequiredMixin, TemplateView):

    def post(self, request, slug):
        comment = request.POST.get('comment')
        blog = Blog.objects.get(is_active=True, slug=slug)
        Comment.objects.create(blog=blog, user=self.request.user, content=comment)
        return redirect(reverse('blogs:blog-detail', args=[slug]))