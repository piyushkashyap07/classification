# Image Classification Project

This project is designed to automate the process of downloading images from the AJIO website using Selenium, and then training a classifier using TensorFlow to predict the gender and type (sleeve or sleeveless) of clothing items.

## Table of Contents
- [Introduction](#introduction)
- [Installation](#installation)
- [Usage](#usage)
- [Data Collection](#data-collection)
- [Model Training](#model-training)
- [Model Evaluation](#model-evaluation)
- [Contributing](#contributing)
- [License](#license)

## Introduction
This project involves two main components:
1. **Image Collection:** Using Selenium WebDriver to scrape images of clothing items from the AJIO website.
2. **Image Classification:** Training a TensorFlow model to classify the downloaded images into categories based on gender (male or female) and type (sleeve or sleeveless).

## Installation

### Prerequisites
- Python 3.6 or higher
- TensorFlow
- Selenium
- Chrome WebDriver


### Setup

1. **Clone the repository:**
    ```bash
    git clone https://github.com/piyushkashyap07/classification.git
    ```

2. **Install the required packages:**
    ```bash
    pip install -r requirements.txt
    ```

## Usage

### Data Collection

To scrape images from AJIO, run the following script:

```bash
python ajio-git.py

After collecting the images create a neural network for training the classifier which will provide the Checkpoint.
using that checkpoint we will get the prediction done.
