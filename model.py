import pickle

PATH_TO_MODELS = 'models/'
filename = 'engine_model_new.pkl'

model = PATH_TO_MODELS + filename

def load_model():
    loaded_model = pickle.load(open(model, 'rb'))
    return loaded_model