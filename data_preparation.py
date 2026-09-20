"""
Data Download Helper.
---------------------
Fetch the UCI Heart Disease dataset using the `ucimlrepo` package
and save it to the local data folder.

Dataset:
UCI Machine Learning Repository - Heart Disease
Dataset ID: 45

Installation:
-------------
pip install ucimlrepo pandas

Usage:
------
From Python:

>>> from data_prep import get_heart_disease_content
>>> get_heart_disease_content()

From command line:

    python data_prep.py
"""

from logging import basicConfig, getLogger
from pathlib import Path

import pandas as pd
from ucimlrepo import fetch_ucirepo


# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

DATA_FOLDER = Path(__file__).parent / "data"

HEART_DISEASE_DATASET_ID = 45

logger = getLogger(__name__)


def get_heart_disease_content(force_download: bool = False) -> None:
    """
    Fetch the UCI Heart Disease dataset and save it locally.

    Files created:
        data/
        ├── heart_disease.csv
        ├── heart_disease_features.csv
        ├── heart_disease_targets.csv
        └── heart_disease_variables.csv

    Parameters
    ----------
    force_download : bool, optional
        If True, fetch and overwrite existing files.
        Default is False.
    """

    DATA_FOLDER.mkdir(parents=True, exist_ok=True)

    combined_file = DATA_FOLDER / "heart_disease.csv"
    features_file = DATA_FOLDER / "heart_disease_features.csv"
    targets_file = DATA_FOLDER / "heart_disease_targets.csv"
    variables_file = DATA_FOLDER / "heart_disease_variables.csv"

    # Avoid fetching again if the dataset already exists.
    if combined_file.exists() and not force_download:
        logger.info(
            "Heart Disease dataset already exists at `%s`.",
            combined_file,
        )
        return

    logger.info(
        "Fetching UCI Heart Disease dataset (ID=%s)...",
        HEART_DISEASE_DATASET_ID,
    )

    try:
        # Fetch dataset from UCI Machine Learning Repository.
        heart_disease = fetch_ucirepo(id=HEART_DISEASE_DATASET_ID)

        # -------------------------------------------------------------------
        # Extract dataset components
        # -------------------------------------------------------------------

        # Feature columns
        X = heart_disease.data.features

        # Target column(s)
        y = heart_disease.data.targets

        # Variable / schema information
        variables = heart_disease.variables

        # -------------------------------------------------------------------
        # Save individual components
        # -------------------------------------------------------------------

        X.to_csv(features_file, index=False)
        logger.info("Saved features to `%s`.", features_file)

        y.to_csv(targets_file, index=False)
        logger.info("Saved targets to `%s`.", targets_file)

        variables.to_csv(variables_file, index=False)
        logger.info("Saved variable information to `%s`.", variables_file)

        # -------------------------------------------------------------------
        # Save combined dataset
        # -------------------------------------------------------------------

        heart_disease_df = pd.concat([X, y], axis=1)
        heart_disease_df.to_csv(combined_file, index=False)

        logger.info("Saved complete dataset to `%s`.", combined_file)

        # -------------------------------------------------------------------
        # Basic dataset information
        # -------------------------------------------------------------------

        logger.info(
            "Dataset loaded successfully: %s rows, %s columns.",
            heart_disease_df.shape[0],
            heart_disease_df.shape[1],
        )

        logger.info("Done!")

    except Exception:
        logger.exception("Unable to fetch the UCI Heart Disease dataset.")
        raise


if __name__ == "__main__":
    basicConfig(
        level=20,
        format="%(asctime)s %(levelname)s %(message)s",
    )

    get_heart_disease_content()