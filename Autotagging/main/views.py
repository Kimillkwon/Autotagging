from django.shortcuts import render
# View에 Model(Post 게시글) 가져오기
from .models import Post
from . import models
import subprocess

from django.shortcuts import render, HttpResponse, redirect
from django.views.decorators.csrf import csrf_exempt
import os

# Create your views here.
'''
def index(request):
    subprocess.run(['detect.py'], shell=True)
    return render(request,'main/index.html')
'''
def index(request):
    article = '''
    <head>
        <title>Blog List</title>
    </head>
    <body>
        <h1>detection complete</h1>
	<a href='/upload'>back</a>
    </body>
    '''
    subprocess.run(['detect.py'], shell=True)
    return HttpResponse(article)

# blog.html 페이지를 부르는 blog 함수
def blog(request):
    # 모든 Post를 가져와 postlist에 저장합니다
    postlist = Post.objects.all()
    # blog.html 페이지를 열 때, 모든 Post인 postlist도 같이 가져옵니다 
    return render(request, 'main/blog.html', {'postlist':postlist})

def uploadFile(request):
    if request.method == "POST":
        # Fetching the form data
        fileTitle = request.POST["fileTitle"]
        uploadedFile = request.FILES["uploadedFile"]

        # Saving the information in the database
        document = models.Document(
            title = fileTitle,
            uploadedFile = uploadedFile
        )
        document.save()

    documents = models.Document.objects.all()

    return render(request, "main/uploadFile.html", context = {
        "files": documents
    })

from django import forms

class UploadFileForm(forms.Form):
    name = forms.CharField(max_length = 15)
    # files = forms.FileField()
    files = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))


def test(request):
    article = '''
    <form action="" method="post" enctype="multipart/form-data">

        <input type='file' name='files' multiple/>
	<input type='submit' value='Upload'/>
	<button type="button" onclick="location.href='../result/' ">제출하기</button>
    </form>
    
    '''
  
    for count, x in enumerate(request.FILES.getlist("files")):
        def process(f):
            with open('/Users/user/speech/web_test/static/' +str(x), 'wb+') as destination:
                for chunk in f.chunks():
                    destination.write(chunk)
        process(x)
    return HttpResponse(article)

def result(request):

    file_list = os.listdir('/Users/user/speech/web_test/static')

    img_names = []
    

    return render(request, "main/result.html",{'file_list': file_list})
