# zoohackathon-ml
## _Decolgen-WildGogh_


WildGogh is a platform for investigation illegal selling wild animalr.

- We crawl use A.I (Deeplearning + Machine Learning) to detect and analyze the illegal on the internet.
- We provide dashboard for the users is the authority to check and analyze the illegal selling animal from social media.

## Features

- A.I detect the selling wild animal on images with accuracy ~90% (89.90%)
- Tracking caption have potential selling wild animal with accuracy ~ 86%
- Native Dashboard for the users 
- Help checking in cross social media platform
- Help authority to manage data relate to wild animal


## Tech

Full technology are used a number of open source projects to work properly:

- Tensorflow - Deep Learning platform!
- Numpy -  Vietnamese language preprocessing from scratch
- Flask - build A.I server
- TypeScript - build management portal
- node.js - evented I/O for the backend
- Reactjs - Frontend develope

And of course WildGogh itself is open source with public repo on GitHub.

## Installation

Install the dependencies and devDependencies and start the A.I server.
Dashboard server on the other repo that we have submitted.
```sh
virtualenv env
pip install -r requirements.txt
sudo apt install tmux
tmux -a test
sudo python3 main.py
```
Ctrl+B+D

```sh
sudo python3 crawler.py
```

## Plugins

Download the model and put in the ./animalProject/. Below model is the dataset link and Public Notebook that our team built.
| Plugin | Link |
| ------ | ------ |
| Google Drive | [https://drive.google.com/file/d/136iLxSuncyA7YG1jfwBRFYHuCH_OZKI-/view?usp=sharing][PlGd] |
|Dataset | [https://www.kaggle.com/navneetsurana/animaldataset]|
|Notebook| [https://www.kaggle.com/huyquoctrinh/fork-of-wildlife]|

## Training

For training process, using below notebook on Google Colab or Kaggle
```sh
train.ipynb
```

## Contribution
Thanks for consider our project. We hope we can help the wild animal have the better life on our earth.
