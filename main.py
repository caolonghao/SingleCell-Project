from scripts.data_reader import read_train_data,read_test_data
from scripts.model import base_model
from scripts.evaluate import evaluate
from config import config
import pandas as pd

def main():
    """
    This is the main function that loads data, trains a model, and evaluates the model.

    Returns:
        result: The evaluation result.
    """
    # Load data
    input_train_mod1, input_train_mod2 = read_train_data(config)
    input_test_mod1, input_test_mod2 = read_test_data(config)
    
    # Train model
    prediction=base_model(config,input_train_mod1,input_train_mod2,input_test_mod1)
    
    # Evaluate model
    if config["do_test"]:
        result = evaluate(prediction.X, input_test_mod2.X)
    
    if config["write_result"]:
        pd.DataFrame([result]).to_csv(config["output"].replace("h5ad","csv"))
    
    return result

if __name__ == "__main__":
    main()