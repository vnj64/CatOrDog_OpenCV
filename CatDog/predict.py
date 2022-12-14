import torch
from .utils.helpers import *
import warnings
from PIL import Image
from torchvision import transforms
#from torchsummary import summary

def image_transform(imagepath):
    test_transforms = transforms.Compose([transforms.Resize(255),
                                      transforms.CenterCrop(224),
                                      transforms.ToTensor(),
                                      transforms.Normalize([0.485, 0.456, 0.406],
                                                           [0.229, 0.224, 0.225])])
    image = Image.open(imagepath)
    imagetensor = test_transforms(image)
    return imagetensor


def predict(imagepath, verbose=False):
    if not verbose:
        warnings.filterwarnings('ignore')
    model_path = './project/CatDog/models/catvdog.pth'
    #стандартно не находило модель, возможно связано с тем как запускается flask приложение
    try:
        checks_if_model_is_loaded = type(model)
    except:
        model = load_model(model_path)
    model.eval()
    #summary(model, input_size=(3,244,244))
    if verbose:
        print("Model Loaded..")
    image = image_transform(imagepath)
    image1 = image[None,:,:,:]
    ps=torch.exp(model(image1))
    topconf, topclass = ps.topk(1, dim=1)
    arg_dog = str(topconf.item())
    arg_cat = str(topconf.item())
    if topclass.item() == 1:
        return {'class':'собака','confidence':arg_dog[:4]}
    else:
        return {'class':'кошка','confidence':arg_cat[:4]}

#print(predict('data/dog1.jpeg'))
#print(predict('data/cat1.jpeg'))
#print(predict('data/dog2.jpeg'))
#print(predict('data/cat2.jpeg'))
