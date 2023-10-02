# %%
## packages installed

import numpy as np
import pandas as pd
import sklearn
import seaborn
import keras
import mediapipe as mp 

# %% [markdown]
# ### Load Data 

# %%
## TO-DO: Load the ASL Alphabet dataset, using keras.preprocessing.image 

from keras.preprocessing.image import ImageDataGenerator



# %%


# %% [markdown]
# ### MediaPipe

# %% [markdown]
# ##### check https://developers.google.com/mediapipe/solutions/vision/hand_landmarker/python for guidance on this section

# %%
from mediapipe.tasks import python
from mediapipe.tasks.python import vision

# %%
## TO-DO: Download and Load Model Path

## Example model path given here 

model_path = '/absolute/path/to/gesture_recognizer.task'


# %%
## TO-DO: prepare image data, create task, and run the task

import mediapipe as mp

BaseOptions = mp.tasks.BaseOptions
HandLandmarker = mp.tasks.vision.HandLandmarker
HandLandmarkerOptions = mp.tasks.vision.HandLandmarkerOptions
VisionRunningMode = mp.tasks.vision.RunningMode



# %%
def process_output(landmarks):
    """
    extract and clean landmark coordinate data: including 
    - Removing depth (or z dimension)
    - Centralizing coordinates to center point of hand
    - Flattening to 1D array 
    - Normalization w.r.t. max value 
 
    Paramaters
    ---------
    landmakrs: output from Mediapipe model 
    """
    ##TO-DO: complete and use this function!

# %%

##TO-DO: generate the train and test set
X_train, y_train, X_test, y_test = ...

# %% [markdown]
# ### Model Training with ResNet / VGG

# %%
##TO-DO: train and evaluate model

# %%


# %% [markdown]
# ### Model Training with Mediapipe Landmarks (Random Forest, LSTM, etc.)

# %%
##TO-DO: train and evaluate model

# %%



