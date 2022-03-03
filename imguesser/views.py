from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from django.conf import settings
from .models import imageInfo
# Create your views here.

import numpy
from keras.models import load_model
from keras.preprocessing.image import load_img, img_to_array



def imguess(imagePath):
    model = load_model('models/my_model.h5')
    image = load_img(imagePath, target_size=(32, 32))
    image = img_to_array(image)
    image = image.reshape(1, 32, 32, 3)
    image = image.astype('float32') / 255.0
    result = numpy.argmax(model.predict(image), axis=1)
    guesses = ['Airplane', 'Automobile', 'Bird', 'Cat', 'Deer', 'Dog', 'Frog', 'Horse', 'Ship', 'Truck']
    return guesses[result[0]]



def index(request):
    if request.method == 'POST':
        imageObject = request.FILES['imagePath']
        fss = FileSystemStorage()
        imagePathName = fss.save(imageObject.name, imageObject)
        imagePath = settings.MEDIA_ROOT.replace('\\', '/') + '/' + imagePathName
        res = imguess(imagePath);
        context = {'imagePathName' : fss.url(imagePathName), 'res' : res}
        imageInfo.save(imageInfo.objects.create(imagePath=imagePath, res=res))
        return render(request, 'index.html', context)
    return render(request, 'index.html')

