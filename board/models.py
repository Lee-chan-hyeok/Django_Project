from django.db import models

# Create your models here.

class Question(models.Model):
    subject = models.CharField(max_length=100)
    content = models.TextField()
    create_date = models.DateTimeField()

    def __str__(self):
        return self.subject

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()

# class Comment(models.Model):
#     author = models.ForeignKey(User, on_delete=models.CASCADE)
#     content = models.TextField()
#     create_date = models.DateTimeField()
#     modify_date = models.DateField(null=True, black=True)
#     question = models.ForeignKey(Question, null=True, blank=True, on_delete=models.CASCADE)
#     answer = models.ForeignKey(Answer, nuull=True, blank=True, on_delete=models.CASCADE)