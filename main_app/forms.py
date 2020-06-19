from django.forms import ModelForm
from .models import Feeding, Bath

class FeedingForm(ModelForm):
    class Meta:
        model = Feeding
        fields = ['date', 'meal']
  
class BathForm(ModelForm):
    class Meta:
        model = Bath
        fields = ['date']      