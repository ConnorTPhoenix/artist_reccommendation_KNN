import joblib
import os

def model_fn(model_dir):
    """Load model from the model_dir. This is the same model that is saved
    in the main if statement.
    """
    print("Loading model.")
    
    # load using joblib
    model = joblib.load(os.path.join(model_dir, "model.joblib"))
    print("Done loading model.")
    
    return model

def predict_fn(input_data, model):
    distances, indices=model.kneighbors(input_data)
    return indices[0]