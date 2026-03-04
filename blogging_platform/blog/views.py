from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from django.http import JsonResponse
from .models import Post
from .forms import CommentForm, PostForm, UserRegisterForm
from .ai_service import get_ai_summary, get_ai_comment_suggestion, generate_ai_blog_post

def is_superuser(user):
    return user.is_superuser

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, id):
    post = get_object_or_404(Post, id=id)
    comments = post.comments.all()

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.post = post
            new_comment.save()
            return redirect('post_detail', id=post.id)
    else:
        form = CommentForm()

    return render(request, 'blog/post_detail.html', {
        'post': post,
        'comments': comments,
        'form': form
    })

@login_required
@user_passes_test(is_superuser)
def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.author = request.user
            new_post.save()
            return redirect('post_list')
    else:
        form = PostForm()

    return render(request, 'blog/post_create.html', {'form': form})

def signup(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account created successfully! You can now log in.")
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'blog/signup.html', {'form': form})

def ai_summary(request, post_id):
    """AJAX endpoint for AI summary generation"""
    post = get_object_or_404(Post, id=post_id)
    summary = get_ai_summary(post.content)
    return JsonResponse({'summary': summary})

def ai_comment_suggestion(request, post_id):
    """AJAX endpoint for AI comment suggestion"""
    post = get_object_or_404(Post, id=post_id)
    suggestion = get_ai_comment_suggestion(post.content)
    return JsonResponse({'suggestion': suggestion})

@login_required
@user_passes_test(is_superuser)
def ai_blog_writer(request):
    """AI blog writing page"""
    if request.method == 'POST':
        topic = request.POST.get('topic', '')
        tone = request.POST.get('tone', 'informative')
        length = request.POST.get('length', 'medium')
        
        if not topic:
            messages.error(request, "Please provide a topic for the blog post.")
            return render(request, 'blog/ai_blog_writer.html')
        
        generated_post = generate_ai_blog_post(topic, tone, length)
        
        # Create a form with the generated content for editing
        form = PostForm(initial={
            'title': generated_post['title'],
            'content': generated_post['content']
        })
        
        return render(request, 'blog/post_create.html', {
            'form': form,
            'ai_generated': True,
            'original_topic': topic
        })
    
    return render(request, 'blog/ai_blog_writer.html')

def ai_generate_post(request):
    """AJAX endpoint for AI post generation"""
    if request.method == 'POST':
        topic = request.POST.get('topic', '')
        tone = request.POST.get('tone', 'informative')
        length = request.POST.get('length', 'medium')
        
        if not topic:
            return JsonResponse({'error': 'Topic is required'}, status=400)
        
        generated_post = generate_ai_blog_post(topic, tone, length)
        return JsonResponse(generated_post)
    
    return JsonResponse({'error': 'Invalid request method'}, status=405)