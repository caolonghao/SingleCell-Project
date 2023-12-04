# evaluate.py

# evaluate using RMSE and MAE
import numpy as np

def evaluate(prediction, ground_truth):
    """
    Evaluate the prediction against the ground truth and calculate the score.

    Parameters:
    prediction (numpy.ndarray): The predicted values.
    ground_truth (numpy.ndarray): The ground truth values.

    Returns:
    float: The calculated score.
    """
    tmp = prediction - ground_truth
    rmse = np.sqrt(tmp.power(2).mean())
    mae = np.abs(tmp).mean()
    print(f"RMSE: {rmse}\nMAE: {mae}")
    return {"RMSE":rmse, "MAE":mae}