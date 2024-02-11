
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
