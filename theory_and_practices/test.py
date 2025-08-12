import pandas as pd

test = pd.Series({'accuracy': 0.8, 'precision': 0.7})
test2 = pd.Series({'accuracy': 0.8, 'precision': 0.7})

frame = pd.DataFrame([test, test2], index=['DecisionTree', 'RandomForest'])

print(frame.T)
