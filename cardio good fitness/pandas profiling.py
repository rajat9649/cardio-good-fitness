import pandas as pd 
from pandas_profiling import ProfileReport

df=pd.read_csv('CardioGoodFitness.csv')

result=ProfileReport(df,title='pandas profiling report')
result.to_file('CardioGoodFitness.html')