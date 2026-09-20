# Assignment 1

## Getting Started with Pandas and Data Visualization

This assignment introduces core data analysis workflows using **Python**, **pandas**, and plotting tools. You will work with the UCI Heart Disease dataset and practice loading, exploring, transforming, aggregating, and visualizing real-world data.

---

## Table of Contents

* [Description](#description)
* [Learning Objectives](#learning-objectives)
* [Dataset](#dataset)
* [Dataset Setup](#dataset-setup)
* [Repository Structure](#repository-structure)
* [How to Work on This Assignment](#how-to-work-on-this-assignment)
* [Running the Notebook](#running-the-notebook)
* [Questions](#questions)

---

## Description

In this assignment, you will practice fundamental data analysis techniques using the **pandas** library.

The assignment focuses on:

* Loading and inspecting datasets
* Filtering rows and columns
* Handling and preparing data
* Grouping data
* Performing aggregate operations
* Working with pandas input/output operations
* Combining and manipulating data
* Exploring relationships between variables
* Creating plots and visualizations with pandas
* Interpreting results from exploratory data analysis

---

## Learning Objectives

By completing this assignment, you should be able to:

* Import datasets into pandas DataFrames
* Inspect the structure and characteristics of a dataset
* Select and filter data using pandas
* Perform grouping and aggregation operations
* Identify and handle missing or irregular values
* Manipulate columns and DataFrames
* Generate summary statistics
* Create basic visualizations
* Interpret patterns found within a real-world dataset

---

## Dataset

This assignment uses the **Heart Disease Dataset** from the **UCI Machine Learning Repository**.

The dataset is retrieved using the official `ucimlrepo` Python package and UCI dataset ID:

```text
45
```

The dataset can be fetched directly with:

```python
from ucimlrepo import fetch_ucirepo

heart_disease = fetch_ucirepo(id=45)

X = heart_disease.data.features
y = heart_disease.data.targets
```

Where:

* `X` contains the feature variables
* `y` contains the target variable
* `heart_disease.metadata` contains information about the dataset
* `heart_disease.variables` contains information about the individual variables

You **do not need to manually download the dataset from UCI**.

---

## Dataset Setup

A helper script named `data_preparation.py` is included in this repository.

The script retrieves the Heart Disease dataset from the UCI Machine Learning Repository and stores local copies inside the `data/` directory.

To download and prepare the dataset from Python, run:

```python
from data_preparation import get_heart_disease_content

get_heart_disease_content()
```

You can also execute the script directly from the command line:

```bash
python data_preparation.py
```

After the script executes successfully, the following files will be created:

```text
  data/
  ├── heart_disease.csv
  ├── heart_disease_features.csv
  ├── heart_disease_targets.csv
  └── heart_disease_variables.csv
```

### Generated Files

**`heart_disease.csv`**

Contains the complete dataset, including both the feature variables and target variable.

**`heart_disease_features.csv`**

Contains the predictor or feature variables.

**`heart_disease_targets.csv`**

Contains the target variable representing the heart disease diagnosis.

**`heart_disease_variables.csv`**

Contains descriptive information about the dataset variables provided by the UCI repository.

If the dataset has already been prepared, the helper script will reuse the existing local files rather than retrieving them again unless otherwise specified.

---

## Repository Structure

Your repository should have a structure similar to the following:

```text
  assignment-1/
  │
  ├── data/
  │   ├── heart_disease.csv
  │   ├── heart_disease_features.csv
  │   ├── heart_disease_targets.csv
  │   └── heart_disease_variables.csv
  │
  ├── data_preparation.py
  ├── requirements.txt
  ├── README.md
  └── assignment-1.ipynb
```

The exact notebook filename may differ depending on the version of the assignment provided.

---

## How to Work on This Assignment

### 1. Clone the Repository

Open a terminal and clone the assignment repository:

```bash
git clone https://github.com/SPU-F1-2026/assignment-1.git
```

Navigate into the repository:

```bash
cd assignment-1
```

---

### 2. Create a Virtual Environment

Create a dedicated Python virtual environment:

```bash
python -m venv .venv
```

Activate it on **Windows**:

```bash
.venv\Scripts\activate
```

Activate it on **macOS or Linux**:

```bash
source .venv/bin/activate
```

Remember to activate the virtual environment whenever you return to work on the assignment.

---

### 3. Install the Required Packages

Install the required Python packages using:

```bash
pip install -r requirements.txt
```

The project requires packages including:

```text
pandas
matplotlib
ucimlrepo
```

Additional packages may also be included in `requirements.txt`.

---

### 4. Prepare the Dataset

The notebook may automatically prepare the dataset.

If necessary, you can prepare it manually by running:

```bash
python data_preparation.py
```

Alternatively, from Python or a Jupyter Notebook:

```python
from data_preparation import get_heart_disease_content

get_heart_disease_content()
```

Once completed, verify that the `data/` directory contains the generated CSV files.

---

## Running the Notebook

Start Jupyter Notebook or JupyterLab from the repository directory.

For Jupyter Notebook:

```bash
jupyter notebook
```

For JupyterLab:

```bash
jupyter lab
```

Open the assignment notebook and complete the exercises in the order presented.

Read each question carefully and place your Python code in the appropriate cells.

When requested to provide an explanation or interpretation, include your answer in a **Markdown cell** rather than only displaying Python output.

---

## Important Guidelines

Before submitting your work:

* Make sure every notebook cell runs successfully.
* Run the notebook from beginning to end.
* Verify that there are no unresolved Python errors.
* Do not hard-code results that should be calculated using pandas.
* Use meaningful variable names.
* Keep your code readable and properly formatted.
* Include plots where requested.
* Label plots appropriately.
* Include written interpretations where required.
* Make sure your repository contains your completed notebook.
* Do not modify the original dataset unnecessarily.

A useful final check is to restart the notebook kernel and select:

```text
Restart Kernel and Run All Cells
```

Your notebook should execute successfully from the first cell to the last.

---

## Questions

The repository and notebook are designed to guide you through the assignment step by step.

Before asking for assistance, verify that:

1. Your virtual environment is activated.
2. The required packages are installed.
3. `data_preparation.py` runs successfully.
4. The dataset exists inside the `data/` directory.
5. You are running the notebook from the correct repository.

If you still have questions regarding the assignment, please contact your instructor.
