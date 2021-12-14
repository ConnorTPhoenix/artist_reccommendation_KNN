from __future__ import print_function
from sklearn.neighbors import NearestNeighbors
import argparse
import os
import pandas as pd
import numpy as np
import scipy
import joblib

def model_fn(model_dir):
    """Load model from the model_dir. This is the same model that is saved
    in the main if statement.
    """
    print("Loading model.")
    
    # load using joblib
    model = joblib.load(os.path.join(model_dir, "model.joblib"))
    print("Done loading model.")
    
    return model

if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument('--output-data-dir', type=str, default=os.environ['SM_OUTPUT_DATA_DIR'])
    parser.add_argument('--model-dir', type=str, default=os.environ['SM_MODEL_DIR'])
    parser.add_argument('--data-dir', type=str, default=os.environ['SM_CHANNEL_TRAIN'])

    parser.add_argument('--n_neighbors', type=int, default=10)
    parser.add_argument('--metric', type=str, default='cosine')
    parser.add_argument('--algorithm', type=str, default='brute')

    args = parser.parse_args()

    training_dir = args.data_dir
    train_data = scipy.sparse.load_npz(os.path.join(training_dir, "artist_user_mtrx.npz"))
    train_data = np.array(train_data.todense())

    model = NearestNeighbors(n_neighbors=args.n_neighbors,
                             metric=args.metric,
                             algorithm=args.algorithm)
    
    model.fit(train_data)

    joblib.dump(model, os.path.join(args.model_dir, "model.joblib"))