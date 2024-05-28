import pickle

PATH_TO_MODELS = 'models/'

eng_model = PATH_TO_MODELS + 'engine_model_new.pkl'
tire_model = PATH_TO_MODELS + 'tire_model.pkl'

def load_engine_model():
    loaded_model = pickle.load(open(eng_model, 'rb'))
    return loaded_model

def load_tire_model():
    loaded_model = pickle.load(open(tire_model, 'rb'))
    return loaded_model