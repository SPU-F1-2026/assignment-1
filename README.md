# assignment-1

Getting started with pandas and plotting.

## Table of Contents

- [assignment-1](#assignment-1)
  - [Table of Contents](#table-of-contents)
  - [Description](#description)
  - [Dataset](#dataset)
  - [How to work on this Assignment?](#how-to-work-on-this-assignment)
  - [Questions](#questions)

## Description

In this assignment, you will be practicing pandas library, in the following ways:

- filtering
- group by and aggregate operations
- pandas io operations
- data mingling
- plotting with pandas

## Dataset

We will be using [Heart Disease Data Set](https://archive.ics.uci.edu/ml/datasets/Heart+Disease) from UCI.

- [processed.cleveland.data](https://archive.ics.uci.edu/ml/machine-learning-databases/heart-disease/processed.cleveland.data)
- [processed.hungarian.data](https://archive.ics.uci.edu/ml/machine-learning-databases/heart-disease/processed.hungarian.data)
- [processed.switzerland.data](https://archive.ics.uci.edu/ml/machine-learning-databases/heart-disease/processed.switzerland.data)
- [processed.va.data](https://archive.ics.uci.edu/ml/machine-learning-databases/heart-disease/processed.va.data)

You **do not** need to download dataset. When the notebook runs, it will download the dataset into `data` folder. You may also use following code to download the dataset.

``` py
from data_prep import get_heart_disease_content
get_heart_disease_content()
```

## How to work on this Assignment?

1. Download this repository with `git clone https://github.com/SPU-F1-2026/assignment-1.git`.
2. [Create a virtual environment](#how-to-create-a-new-virtual-environment) and activate this environment everytime you need to use it.
3. Install [requirements.txt](requirements.txt) file using `pip install -r requirements.txt`.
4. Run the notebook.

## Questions

The repository should be self descriptive and it should guide you through assignment. Let me know if you have any questions.
