from django.db import models
from django.utils import timezone

class Question1(models.Model):
	question_text = models.CharField(max_length=255, null=False)
	closed = models.BooleanField(default=False)
	pub_date = models.DateTimeField()

	def __str__(self):
		return self.question_text

class Choice(models.Model):

	question = models.ForeignKey(Question1, on_delete=models.CASCADE, related_name="questions")
	choice_text = models.CharField(max_length=255,null=False)
	votes = models.CharField(max_length=10)

	def __str__(self):
		return self.question