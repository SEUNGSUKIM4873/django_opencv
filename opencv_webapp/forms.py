from django import forms
from .models import ImageUploadModel

class SimpleUploadForm(forms.Form):

    title = forms.CharField(max_length=50)
    image = forms.ImageField()
    # file = forms.FileField() # 파일을 받을 때 사용

class ImageUploadForm(forms.ModelForm):

    class Meta:
        model = ImageUploadModel
        fields = ('description', 'document')
