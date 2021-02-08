from django.shortcuts import render
from .forms import SimpleUploadForm, ImageUploadForm
from django.core.files.storage import FileSystemStorage
from django.conf import settings
from .cv_functions import cv_detect_face

# Create your views here.
def first_view(request):
    return render(request,'opencv_webapp/first_view.html', {})

def simple_upload(request):

    if request.method == 'POST':


        # print('***')
        # print(request.FILES) #FILES로 들어가야 이미지로 받은 것이 있음.
        # print('***')

        form = SimpleUploadForm(request.POST, request.FILES) #filled forms

        if form.is_valid():

            myfile = request.FILES['image']
            fs = FileSystemStorage()
            filename = fs.save(myfile.name, myfile)
            # myfile.name <- "ses.jpg"
            # myfile <- ses.jpg
            uploaded_file_url = fs.url(filename) #"/media/ses.jpg"





        context = {'form':form, 'uploaded_file_url':uploaded_file_url}
        return render(request,'opencv_webapp/simple_upload.html', context)

    else : #GET 요청일 때

        form = SimpleUploadForm() # empty forms


        context = {'form':form}
        return render(request,'opencv_webapp/simple_upload.html', context)





def detect_face(request):

    if request.method == 'POST' :
        form = ImageUploadForm(request.POST, request.FILES)

        if form.is_valid():
            post = form.save(commit=False) #바로 저장하지 않을 경우에는 False로 넣음
            post.save()

            imageURL = settings.MEDIA_URL + form.instance.document.name
            # '/media/' + 'ses.jpg'. document.name은 'ses.jpg'

            cv_detect_face(settings.MEDIA_ROOT_URL + imageURL)
            # Root directory ./의 의미

            context = {'form':form, 'post':post}
            return render(request, 'opencv_webapp/detect_face.html', context)

    else :
        form = ImageUploadForm() #empty forms

        return render(request, 'opencv_webapp/detect_face.html', {'form':form})
