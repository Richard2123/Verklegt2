from django.shortcuts import render
from django.views import View
from django.http.response import HttpResponse
from django.middleware.csrf import get_token
from .models import Upload


# Create your views here.
def index(request):
    return render(request, 'sellitem/index.html')


class UploadImage(View):
    def get(self, request):
        html = """
            <form method="post" enctype="multipart/form-data">
              <input type='text' style='display:none;' value='%s' name='csrfmiddlewaretoken'/>
              <input type="file" name="image" accept="image/*">
              <button type="submit">Upload Image</button>
            </form>
        """ % (get_token(request))
        return HttpResponse(html)

    def post(self, request):
        image = request.FILES['image']
        image_url = Upload.upload_item_image(image, image.name)
        return HttpResponse("<img src='%s'/>" % image_url)
