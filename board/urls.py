from django.urls import path

from . import views

app_name = 'board'

urlpatterns = [
    path('index/', views.index, name='index'),
    path('<int:question_id>/', views.detail, name='detail'),
    path('answer/create/<int:question_id>/', views.answer_create, name='answer_create'),
    path('question/create/', views.question_create, name='question_create'),
    path('question/modify/<int:question_id>/', views.question_modify, name='question_modify'),
    path('question/delete/<int:question_id>/', views.question_delete, name='question_delete'),
    
    # path('comment/create/question/<int:question_id>/', views.comment_create_question,
    #      name='comment_create_question'),
    # path('comment/modify/question/<int:comment_id>/', views.comment_modify_question',
    #      name='comment_modify_question'),
    # path('comment/delete/question/<int:comment_id>', views.comment_delete_question,
    #      name='comment_delete_question'),
]