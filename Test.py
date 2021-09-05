
from NanDealer import nanDealer as nd
import pandas as pd
df=pd.read_csv("C://Users//atulkumarrai//Batsmen_data.csv")
nd=nd()
test=nd.fillNanWithMeanColumnWise(df)
print(f' The updated dataframe is {test}')