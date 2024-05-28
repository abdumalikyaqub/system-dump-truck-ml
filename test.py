import pandas as pd
import model as EngineModel

all_columns = ['RPM', 'EngineTemperature', 'EnginePressure', 'EngineVibration', 'Fuel',
                   'Speed', 'Load']
lst = [900, -34, 2, 0.02, 0, 130, 100]

df = pd.DataFrame([lst], columns = all_columns)

targets = ['Normal', 'Failure']

model = EngineModel.load_model()

result = model.predict_proba(df)
predx = ['%.3f' % elem for elem in result[0]]
preds_concat = pd.concat([pd.Series(targets), pd.Series(predx)], axis=1)
preds = pd.DataFrame(data=preds_concat)
preds.columns = ["class", "probability"]
preds.reset_index(drop=True)
# print(result)
# print(predx)
# print(preds_concat)
print(preds)