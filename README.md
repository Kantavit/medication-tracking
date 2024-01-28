# Medication Tracking System of Morphine Tablets For Palliative Care

Follow the patient taking medicine is an important problem because a doctor can’t follow how many pill that patient might have taken. We must develop pill box that contain an image processing system that will distinguish which pill have been taken with the deep learning algorithm. We also develop web application that use to track the amount of pill in each patient’s pill box. web application can make a communication between caregiver resident’s doctor and attending staff. They can monitor the patient’s pill intake and evaluate the patient’s health through online form up close.

## Windows10 Installation

> [!IMPORTANT]
> You need to install these things first.
> Python3: [Link](https://www.python.org/downloads/)
> NodeJS: [Link](https://nodejs.org/en/download/)

Clone repository and cd into folder

```
git clone https://github.com/Kantavit/medication-tracking.git
cd medication-tracking
```

Create an enviroments

```
py -3 -m venv env
```

Activate the environment

```
env\Scripts\activate
```

Install NPM packages

```
cd med_track/static
npm install
cd ../..
```

Install pip packages

```
pip install -r requirements.txt
```

Run Web Application

```
run-web-win10.bat
```

## Linux Installation

> [!IMPORTANT]
> You need to install these things first.
> Python3: [Link](https://docs.python-guide.org/starting/install3/linux/)
> NodeJS: [Link](https://github.com/nodesource/distributions)

Clone repository and cd into folder

```
git clone https://github.com/Kantavit/medication-tracking.git
cd medication-tracking
```

Create an enviroments

```
python3 -m venv env
```

Activate the environment

```
env/bin/activate
```

Install NPM packages

```
cd med_track/static
npm install
cd ../..
```

Install pip packages

```
pip install -r requirements.txt
```

Run Web Application

```
run-web-win10.bat
```
