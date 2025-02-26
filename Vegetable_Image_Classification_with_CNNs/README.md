# Vegetable Image Classification Project

This project implements a Convolutional Neural Network (CNN) for classifying images of vegetables. It uses TensorFlow/Keras for model development and training, and includes data preprocessing steps to ensure optimal performance. The project aims to accurately classify images into three categories: Broccoli, Carrot, and Radish.

## Project Overview

This project demonstrates the process of building and training a CNN model for image classification. It encompasses all stages of a typical machine learning workflow, from data loading and preprocessing to model training, evaluation, and optimization. The ultimate goal is to create a robust model capable of accurately classifying images of three common vegetables: Broccoli, Carrot, and Radish.

## Dataset

The dataset used in this project consists of images of Broccoli, Carrot, and Radish. The original dataset can be downloaded from [Kaggle Dataset](https://www.kaggle.com/datasets/misrakahmed/vegetable-image-dataset).

Before using the dataset, ensure to:

*   Download the `vegetable-image-dataset.zip` file.
*   Extract the contents into a directory named `/content/Vegetable Images`. This will create the following structure:

    ```
    /content/Vegetable Images/
    ├── train/
    │   ├── Broccoli/
    │   ├── Carrot/
    │   └── Radish/
    ├── validation/
    │   ├── Broccoli/
    │   ├── Carrot/
    │   └── Radish/
    └── test/
        ├── Broccoli/
        ├── Carrot/
        └── Radish/
    ```

## Libraries Used

The following Python libraries are utilized in this project:

*   **TensorFlow (2.15.0):** Deep learning framework for model development and training.
*   **Keras:** High-level API for building neural networks.
*   **NumPy:** Library for numerical computations.
*   **Pandas:** Library for data manipulation and analysis.
*   **Matplotlib:** Library for creating visualizations.
*   **Scikit-learn:** Library for classification report.
*  **tensorflowjs:** To convert keras model into tensorflow js model

## Data Processing

The data processing steps include:

*   **Loading Data:** The dataset is loaded using `ImageDataGenerator` from the specified directories, with separate generators for training and validation data, both using augmentations.
*   **Rescaling:** Pixel values are rescaled to the range of 0-1.
*   **Data Augmentation:** For both the training and validation data, the following augmentations are applied:
    *   `rotation_range=20` (40 for training)
    *   `width_shift_range=0.2` (0.4 for training)
    *   `height_shift_range=0.2` (0.4 for training)
    *   `shear_range=0.2` (0.4 for training)
    *   `zoom_range=0.2` (0.4 for training)
    *   `horizontal_flip=True`
    *    `vertical_flip=True (only for training)`
    *   `fill_mode='nearest'`
*   **Color Mode:** Ensure that color mode is in `rgb`.
*   **Data Splitting:** The data is separated into training (80%) and validation (20%) data based on folder.
*   **Shuffle:** Training data is shuffled during the loading process.

## Model Architecture

The CNN model architecture is as follows:

*   **Input Shape:** (224, 224, 3)
*   **Convolutional Layer 1:** 16 filters, 3x3 kernel, ReLU activation, MaxPooling2D, Dropout (0.2)
*   **Convolutional Layer 2:** 32 filters, 3x3 kernel, ReLU activation, MaxPooling2D, Dropout (0.2)
*   **Flatten Layer**
*   **Dense Layer:** 64 neurons, ReLU activation, Dropout (0.3)
*   **Output Layer:** 3 neurons (for the 3 classes), Softmax activation
*   **Regularization:** L2 regularization is applied on convolutional and dense layers.

## Model Training

The model training process involves:

*   **Optimizer:** Adam optimizer with learning rate 0.0001
*   **Loss Function:** Categorical crossentropy
*   **Metrics:** Accuracy
*   **Callbacks:**
    *   `EarlyStoppingAtAccuracy`: Stop training when a target accuracy of 95% is reached on both training and validation sets or when the validation accuracy does not improve for 10 consecutive epochs.
*   **Batch Size:** 32
*   **Epochs:** 40

## Model Evaluation

The model performance is evaluated using:

*   **Accuracy:** Metrics used during training.
*   **Classification Report:** Reports precision, recall, f1-score, and support for each class.
*   **Visualizations:** Training and validation accuracy are plotted over epochs, also one sample is displayed for each class.

## Model Optimization

The following techniques have been used to optimize the model and prevent overfitting:

*   **L2 Regularization:** To control the complexity of the network.
*   **Dropout:** Regularization technique to prevent overfitting.
*   **Data Augmentation:** To increase variation in the training data.

## Usage

To use the code:

1.  Ensure that you have all necessary libraries installed.
2.  Create the directories and populate with images from the Kaggle dataset (or your own).
3.  Upload the `kaggle.json` file to the `.kaggle` directory to access the dataset through Kaggle API.
4. Open the notebook.
5. Run each cell sequentially.
6. The script will output the model as `.h5`, `savedmodel`, and `.tflite` in respective folders and as TFJS Model.
7.  To run the inference code, update the `image_path` variable to point to an image that you would like to test.

## Future Work

*   Experiment with different model architectures (e.g., adding more layers, changing filter sizes).
*   Perform more extensive hyperparameter tuning.
*   Evaluate using more evaluation metrics (e.g., precision, recall, F1-score).
*   Explore other data augmentation techniques.

## Author

**Name:** Rahadian Muhammad Sutandar

**Email:** rahadiansutandar@gmail.com

**ID Dicoding:** rahadian_ms
