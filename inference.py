import os
import json
import joblib
import numpy as np

# Load the scikit-learn model
def model_fn(model_dir):
    clf = joblib.load(os.path.join(model_dir, "pretrained_model.joblib"))
    return clf


from scipy.sparse import coo_matrix

def predict_fn(input_data, model):
    # Preprocess input data if necessary
    # For example, convert JSON input to COO sparse matrix
    features_data = input_data['features']
    num_rows = features_data['num_rows']
    num_cols = features_data['num_cols']
    data = features_data['data']
    row = features_data['row']
    col = features_data['col']
    
    features = coo_matrix((data, (row, col)), shape=(num_rows, num_cols))
    
    # Convert sparse matrix to dense representation
   # dense_features = features.toarray()
    
    # Generate predictions
    predictions = model.predict(features)
    
    # Postprocess predictions if necessary
    
    return predictions.tolist()

# # Example usage:
# # Assuming input_data is a dictionary containing features in JSON format and model is the trained scikit-learn model
# input_data = {
#     'features': {
#         'num_rows': 2,
#         'num_cols': 3,
#         'data': [1, 2],
# #         'row': [0, 1],
# #         'col': [0, 2]
#     }
# }

# Assuming model is already loaded
# predictions = predict_fn(input_data, model)




def input_fn(serialized_input_data, content_type):
    # Parse input data
    if content_type == 'application/json':
        input_data = json.loads(serialized_input_data)
        return input_data
    else:
        raise ValueError(f'Unsupported content type: {content_type}')

def output_fn(prediction_output, accept):
    # Serialize predictions
    if accept == 'application/json':
        return json.dumps(prediction_output), accept
    else:
        raise ValueError(f'Unsupported accept type: {accept}')
