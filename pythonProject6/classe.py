import pandas as pd

cliente = {'Nome': ['Marcelo', 'Ana', 'Maria'],
           'Idade': [33,26,45]}

print(cliente)
print('\n\n')
dataframe = pd.DataFrame(cliente)

print(dataframe)
