from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
import json
from .analytics_spell_check import check_spelling
# from .forms import UploadFileForm
from django.conf import settings
from django.core.files.storage import default_storage
import os
from .models import AnalyticsDocument as ADocument, Document

def validate_content(request):
    if request.method == "POST":
        request_data = json.loads(str(request.body, encoding='utf-8'))
        content = request_data["content"]
        response = check_spelling(content)
        print("response",response)
        return JsonResponse(response)
 
def upload_file(request):
    if request.user.is_authenticated and request.method == "POST":
        print("files",request.FILES)
        upload_file = request.FILES['file']
        print(type(upload_file),upload_file.name,upload_file.content_type)
        save_path = os.path.join(settings.MEDIA_ROOT, 'uploads/',upload_file.name)
        path = default_storage.save(save_path, upload_file)
        document = Document.objects.create(document=path, upload_by=request.user)
        analytic_document = ADocument.objects.create(document=document, title="test")
        # return JsonResponse({'document': analytic_document.id})
        return render(request, "upload_docs.html", {})
    elif request.user.is_authenticated and request.method == "GET":
        return render(request, "upload_docs.html", {})        
    else:
        return redirect("/accounts/login")
