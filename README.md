# Butterfly Classification using CNN Project
Dataset:https://www.kaggle.com/datasets/phucthaiv02/butterfly-image-classification
## Overview
This repository contains code and resources for the Butterfly Classification project, which uses Convolutional Neural Networks (CNN) to classify butterfly species based on their images.

## Getting Started

### Prerequisites

- Python 3.x
- Tensorflow 2.x
- Keras
- Numpy, Pandas
- Matplotlib, Seaborn (for visualization)

### Setup

1. **Clone the Repository**:
   git clone <repository_link>

2. **Navigate to the Directory**:
  cd path_to_directory

3. **Install the Dependencies**:
   pip install -r requirements.txt

4. **Setup Dataset Path**:
Before running any script, make sure to change the dataset path in `your_script_name.py`:
```python
DATA_PATH = 'path_to_your_dataset'

Model Details
The CNN model implemented in this project uses multiple convolutional layers, followed by pooling layers and dense layers. The output layer uses a softmax function to classify butterfly species.

 
