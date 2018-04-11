from django.views.generic import ListView, View , DetailView, CreateView
from django.shortcuts import render , redirect , render_to_response, HttpResponseRedirect
from .blog_form import blogForm
from .comment_form import CommentForm
from django.utils import timezone
from myapp.models import BlogModel, CommentModel

class BlogListView(ListView):
	template_name = 'blog.html'
	model = BlogModel
	context_object_name = 'blog_data'


class BlogDetailView(DetailView):
	template_name = 'blog_detail.html'
	model = BlogModel
	queryset = BlogModel.objects.all()
	pk_url_kwarg = 'slug'
	slug_field ='slug'
	# BlogModel = get_object_or_404(id='pk')
	#context_object_name = 'blog_data'
	
	# def Post_object(self, request, **kwargs):
	# 	comment = request.POST.get('comment')
	# 	context = {comment:'comment',form:'comment_form'}
	# 	return render(self.get(request,'blog_detail.html',context))



	def get_object(self):
		slug = self.kwargs.get('slug')
		#import ipdb;ipdb.set_trace()
		return BlogModel.objects.get(slug=slug)

	def get_context_data(self,**kwargs):
		context = super(BlogDetailView,self).get_context_data(**kwargs)
		print kwargs
		context['now'] = timezone.now()
		context['data'] = BlogModel.objects.exclude( slug = self.kwargs.get('slug'))
		context['comment_form'] = CommentForm()
		context['comment'] = CommentModel.objects.filter(comment_F__slug=self.kwargs.get('slug')) #foreign key funda

		#context['comments'] = BlogModel.objects.include(comment=self.comment)
		return context


	# def Post_object(self):
	# 	comment = self.kwargs.get('comment')
	# 	return BlogModel.object.get(slug=slug)
class BlogCommentCreateView(CreateView):
	form_class = CommentForm
	model = CommentModel
	template_name = 'blog_comment.html'
	redirect_url = '/'

	def get_success_url(self):
		return '/'

	def form_valid(self, form):
		#import ipdb ; ipdb.set_trace()
		return super(BlogCommentCreateView, self).form_valid(form)

	