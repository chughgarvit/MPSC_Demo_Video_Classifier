
# MPSC Demo Video Classifier

Welcome to the MPSC Demo Video Classifier! This Flask web application is designed to demonstrate our machine learning models for video classification, providing an intuitive interface for users to upload videos and view predictions.

## Repository

[GitHub Repository](https://github.com/chughgarvit/MPSC_Demo_Video_Classifier.git)

## Project Structure

Below is the structure of the project, highlighting key directories and files:

```
MPSC_Demo_Video_Classifier/
├── Data/
│   └── Pickle_files/
│       ├── Ajagi_8_26_21_2_300_300-001.pkl
│       └── Trial2_7_27_300_300-003.pkl
├── My_net_r2+1D_good_model.pth
├── My_net_r2+1D_good_model_signle_.pth
├── README.md
├── animation2500.gif
├── codes/
│   ├── __pycache__/
│   │   ├── r2plus1d_ptv.cpython-311.pyc
│   │   └── r2plus1d_ptv.cpython-38.pyc
│   ├── animation2500.gif
│   ├── animation3500.gif
│   ├── chekc.py
│   ├── r2plus1d_ptv.py
│   ├── test_demo.ipynb
│   └── test_demo.py
└── zahid_demo/
    ├── __pycache__/
    │   ├── prediction_logic.cpython-311.pyc
    │   └── r2plus1d_ptv.cpython-311.pyc
    ├── app copy.py
    ├── app.py
    ├── prediction_logic.py
    ├── r2plus1d_ptv.py
    ├── static/
    │   ├── css/
    │   │   └── style.css
    │   ├── images/
    │   │   ├── green_check.png
    │   │   └── red_cross.png
    │   ├── js/
    │   │   └── app.js
    │   └── videos/
    │       ├── video1.mp4
    │       ├── video2.mp4
    │       └── video3.MP4
    └── templates/
        ├── index copy.html
        └── index.html
```

## Getting Started

### Prerequisites

- Python 3.6 or higher
- Flask
- Necessary Python packages listed in `requirements.txt`

### Installation

1. **Clone the Repository**

    ```sh
    git clone https://github.com/chughgarvit/MPSC_Demo_Video_Classifier.git
    cd MPSC_Demo_Video_Classifier
    ```

2. **Install Requirements**

    ```sh
    pip install -r requirements.txt
    ```

3. **Download Necessary Files**

    - **Model and Data Pickle Files**: Download from [this link](https://drive.google.com/drive/folders/1nZrDrLvX8En8fphpek0C4QsmDk2UxNC8?usp=sharing) and place in `Data/Pickle_files`.
    - **Model Files**: Download from [here](https://drive.google.com/drive/folders/1WCsTCIwEWJaCbjSwblpOa-nPHldjdnMI?usp=sharing) and place in the root directory.

### Running the Application

1. **Environment Setup**

    Linux/macOS:
    ```sh
    export FLASK_APP=app.py
    ```
    Windows:
    ```cmd
    set FLASK_APP=app.py
    ```

2. **Start the Application**

    ```sh
    flask run
    ```

    Access the web app at `http://127.0.0.1:5000/`.

# MPSC_Demo_Video_Classifier


## Install instruction
- Clone this git clone https://github.com/chughgarvit/mpsc_video_classifier_demo.git
- Install all the dependencies
- Go to the directory cd mpsc_video_classifier_demo
- Run the py file python app.py
- Open the web browser
- Go to the following address localhost:8080

## Storyline
Welcome to our interactive demo on self-supervised learning from multiview video data for activity recognition and pose detection. In this demo, we'll showcase two approaches to classifying activities in video data: using a single-view model trained in a supervised manner and our innovative multi-view model trained through self-supervised learning.

Imagine a scenario where we can access multiview data captured from cameras placed on the ground and drones flying overhead. This setup gives us rich, multi-perspective views of the environment and the activities taking place within it.

Let's dive into our demo. We have 12 examples of different activities that can be selected from the dropdown menu. When we click "Classify using single-view model," we'll see the results based on a model trained from only one view in a supervised way. This model might struggle with variations in viewpoint and occlusions, typical challenges in single-view activity recognition.

Now, let's try "Classify using the multi-view model." This time, we're leveraging our innovative approach, where we've developed a view-invariant model using partially labeled data. By exploiting optimal losses given partially labeled video, we've built a machine learning architecture to recognize activities across different views and handle occlusions more effectively.

As we switch between the single-view and multi-view models, pay attention to how each model performs on the selected examples. You'll notice that the multi-view model offers more robust and accurate predictions, thanks to its ability to leverage information from multiple perspectives.

Our objectives in developing this system were clear: to design a view/occlusion-invariant human activity and pose detection model, to create scalable video frame classification techniques using unlabeled multiview video data, and to validate the performance of our system using both public and in-house multiview data streams.

Through self-supervised and adversarial learning methods, we've learned to separate video frames in low-dimensional spaces, allowing us to extract meaningful features and representations that generalize well across different views.

In conclusion, our interactive demo showcases the power of self-supervised learning and multiview data in activity recognition and pose detection. By harnessing the richness of multiview data and developing innovative learning techniques, we're pushing the boundaries of what's possible in understanding and analyzing human activities in complex environments.

Thank you for exploring our demo, and we hope you enjoyed witnessing the capabilities of our approach firsthand.
