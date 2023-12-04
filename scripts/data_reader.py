# data_reader.py

# Load data from train and test `h5ad` files.
# Path can be changed in the configuration file.

import anndata as ad
import numpy as np
import logging

def read_train_data(config):
    """
    Read training data from `h5ad` files.

    Args:
        config (dict): A dictionary containing the file paths for input_train_mod1, input_train_mod2, and input_train_sol.

    Returns:
        tuple: A tuple containing input_train_mod1, input_train_mod2, and input_train_sol.
    """
    logging.info('Reading `h5ad` files for training...')
    input_train_mod1 = ad.read_h5ad(config['input_train_mod1'])
    input_train_mod2 = ad.read_h5ad(config['input_train_mod2'])
    
    return input_train_mod1, input_train_mod2


def read_test_data(config):
    """
    Read test data from `h5ad` files based on the provided configuration.

    Args:
        config (dict): Configuration dictionary containing file paths.

    Returns:
        tuple: A tuple containing the loaded `h5ad` files for testing.
            - input_test_mod1: The first test `h5ad` file.
            - input_test_mod2: The second test `h5ad` file.
            - input_test_sol: The solution `h5ad` file.

    """
    if config["do_test"]:
        logging.info('Reading `h5ad` files for testing...')
        input_test_mod1 = ad.read_h5ad(config['input_test_mod1'])
        input_test_mod2 = ad.read_h5ad(config['input_test_mod2'])
    else:
        logging.info('Reading `h5ad` files for testing...')
        input_test_mod1 = ad.read_h5ad(config['input_test_mod1'])
        input_test_mod2 = ad.read_h5ad(config['input_test_mod2'])
    
    return input_test_mod1, input_test_mod2