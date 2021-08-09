import pandas as pd

def lambda_handler(event, context):
    d = {'sampel1': [1,2], 'sample2': [3,4]}
    df = pd.DataFrame(data=d)
    print(df)
    print('Done x1.1')
