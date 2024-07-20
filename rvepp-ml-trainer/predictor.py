import lightgbm as lgb
from numpy import array

model = lgb.Booster(model_file='elf.mdl')

input_vector = array([[4000, 1]])

prediction = model.predict(input_vector)
print("Prediction:", prediction)
