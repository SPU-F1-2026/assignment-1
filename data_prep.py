"""
Data Download Helper.
----------------------
Download heart-disease dataset to data folder.

Usage:
----------------------
From python.

>>> from data_prep import get_heart_disease_content
>>> get_heart_disease_content()

From command line.

``` sh
python data_prep.py
```
"""

from logging import basicConfig, getLogger
from pathlib import Path

import requests

DATA_FOLDER = Path(__file__).parent.joinpath('data')
logger = getLogger(__name__)


def download_data(url, filename) -> bool:
    """ Download to data folder. """
    if DATA_FOLDER.joinpath(filename).exists():
        logger.info(f'File `{filename}` already exists.')
        return True

    logger.info(f'Downloading {filename}...')
    response = requests.get(url)
    with open(DATA_FOLDER.joinpath(filename), 'wb') as stream:
        stream.write(response.content)


def get_heart_disease_content() -> None:
    """ Download Heart Disease data files. """
    base_url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/heart-disease'
    files = [
        'processed.cleveland.data',
        'processed.hungarian.data',
        'processed.switzerland.data',
        'processed.va.data',
        'heart-disease.names',
    ]

    for file in files:
        download_data(f'{base_url}/{file}', file)
    logger.info('Done!')


if __name__ == '__main__':
    """ Entry point. """
    basicConfig(level=20, format='%(asctime)8s %(levelname)s %(message)s')
    get_heart_disease_content()
