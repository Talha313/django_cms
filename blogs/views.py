from tempfile import template

from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse
from django.views.generic import TemplateView, ListView

from blogs.forms import CommentForm
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


class BlogCommentView(TemplateView):
    template_name = 'blog_detail.html'

    def post(self, request, slug):
        if request.user.is_authenticated:
            comment = request.POST.get('comment')
            blog = Blog.objects.filter(is_active=True, slug=slug).first()
            comment_json = {'content': comment, 'blog': blog, 'user': request.user}
            form = CommentForm(comment_json)
            if form.is_valid() and request.recaptcha_is_valid:
                form.save()
                messages.success(request, 'Comment added successfully.', extra_tags='comment')
            return redirect(reverse('blogs:blog-detail', args=[slug]))

        return redirect('{}?next={}'.format(reverse('login'), reverse('blogs:blog-detail', args=[slug])))
