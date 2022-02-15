from django.forms import ModelForm 
from main import models
class FeedbackForm(ModelForm):
    class Meta:
        model = models.Feedbacks
        exclude = []