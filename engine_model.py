import json
import pandas as pd
import model as EngineModel

model = EngineModel.load_model()

targets = ['Normal', 'Failure']

def get_pred(rpm, temperature, pressure, vibration, fuel, speed, load):
    
    all_columns = ['RPM', 'EngineTemperature', 'EnginePressure', 'EngineVibration', 'Fuel',
                   'Speed', 'Load']
    lst = [rpm, temperature, pressure, vibration, fuel, speed, load]
    df = pd.DataFrame([lst], columns = all_columns)
    
    df = df.astype(float)
    result = model.predict_proba(df)
    predx = ['%.3f' % elem for elem in result[0]]
    preds_concat = pd.concat([pd.Series(targets), pd.Series(predx)], axis=1)
    preds = pd.DataFrame(data=preds_concat)
    preds.columns = ["class", "probability"]
    return preds.reset_index(drop=True)

def launch_task(rpm, temperature, pressure, vibration, fuel, speed, load, api):
    
    pred_model = get_pred(rpm, temperature, pressure, vibration, fuel, speed, load)

    if api == 'v1.0':
        res_dict = {'result':  json.loads(pd.DataFrame(pred_model).to_json(orient='records'))}
        return res_dict
    else:
        res_dict = {'error': 'API doesnt exist'}
        return res_dict