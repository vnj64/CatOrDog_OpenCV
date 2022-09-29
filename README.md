# CatOrDog_OpenCV

![cat-dog](https://user-images.githubusercontent.com/91592995/175183458-93b43007-43cc-4c5c-9644-51d57938b31f.gif)

### About

In this project, we are building an application that works with a deep learning model algorithm to classify whether images contain a dog or a cat. You will never go wrong again.

### Data

The dataset is available at Kaggle and has been provided officially by Microsoft Research.You can find it [here](https://www.kaggle.com/c/dogs-vs-cats/data).

### Requirements

We recommend to create a virtual environment using `python3 -m pip install --user virtualenv`  and `python3 -m venv env` then setup environment using `pip install -r requirements.txt` for setting up the environment. We have used **Python 3.8.0** for development.

```
Flask-SQLAlchemy==2.5.1
Werkzeug==2.0.1
Flask-Login==0.5.0
torch==1.11.0
torchvision==0.12.0
Flask==2.0.1
Pillow==8.2.0
numpy==1.21.3
pandas==1.3.4
matplotlib==3.4.3
requests==2.24.0
```

### Running The Server

To start you need to follow the path `OCRV_CatDog_FinalVersion/auth/` after enter the following commands

- export FLASK_APP=project.

- export FLASK_DEBUG=1.

- flask run.


### Team

- [Astan Pataraya](https://gitlab.com/pelmenin)
- [Kamil Khabibullin](https://gitlab.com/vnj644)

### Issues

Feel free to submit any issues.

### Contributions

Currently open to only issues and bug fix related PRs. Feel free to solve an issue and submit a PR.
