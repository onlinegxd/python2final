# Image Classifier using Django and Keras

### Installation
Copy from source
```bash
git clone https://github.com/onlinegxd/python2final
```

### Usage

```python
# Used for image classification
from tensorflow.keras.preprocessing.image import load_img, img_to_array
from tensorflow.keras.models import load_model

# Used for image save
from django.core.files.storage import FileSystemStorage
from django.conf import settings 

from tensorflow.keras.utils import to_categorical
from tensorflow.keras.models import load_model
from tensorflow.keras.models import Sequential

```

### Examples

Start an application webserver/visit https://imguesserpy.herokuapp.com/

After successful run home page will be available     

PostgreSQL DataBase used

Usage examples:

(/) - The only route available
![image](https://user-images.githubusercontent.com/80266425/156709933-bd402393-9a3e-43a0-abe7-06b8ca3c06ca.png) - Heroku
![image](https://user-images.githubusercontent.com/80266425/156709992-137d1694-d3aa-4d72-8a15-cde006bd5155.png) - localhost



