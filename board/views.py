from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Question, Answer#, Comment
from django.utils import timezone
from .forms import QuestionForm, AnswerForm#, CommentForm
from django.core.paginator import Paginator

def index(request):
    """
    board 목록 출력
    """
    # 입력 인자
    page = request.GET.get('page', 1)   # 페이지

    # 조회
    question_list = Question.objects.order_by('-create_date')
    print(len(question_list))

    # 페이징 처리
    paginator = Paginator(question_list, 10)    # 페이지당 10개씩 보여주기
    page_obj = paginator.get_page(page)

    context = {'question_list': page_obj}
    return render(request, 'board/question_list.html', context)

def detail(request, question_id):
    """
    board 내용 출력
    """
    question = get_object_or_404(Question, pk=question_id)
    context = {'question': question}
    return render(request, 'board/question_detail.html', context)

def answer_create(request, question_id):
    """
    board 답변 등록
    """
    question = get_object_or_404(Question, pk=question_id)
    if request.method =="POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.create_date = timezone.now()
            answer.question = question
            answer.save()
            return redirect('board:detail', question_id=question.id)
        
    else:
        form = AnswerForm()
    context = {'question': question, 'form': form}
    return render(request, 'board/question_detail.html', context)

def question_create(request):
    """
    질문 등록
    """ 
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.create_date = timezone.now()
            question.save()
            return redirect('board:index')
        
    else:
        form = QuestionForm()
    context = {'form': form}
    return render(request, 'board/question_form.html', context)

# @login_required(login_url='common:login')

# def comment_create_question(request, question_id):
#     """
#     board 질문 등록
#     """
#     question = get_object_or_404(Question, pk=question_id)
#     if request.method == 'POST':
#         form = CommentForm(request.POST)
#         if form.is_valid():
#             comment = form.save(commit=False)
#             comment.author = request.user
#             comment.create_date = timezone.now()
#             comment.question = question
#             comment.save()
#             return redirect('board:detail', question_id=question_id)
#         else:
#             form = CommentForm()
#         context = {'form': form}
#         return render(request, 'board/comment_form.html', context)