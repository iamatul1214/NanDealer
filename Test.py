
from NanDealer.NanHandler import nanDealer as nd
import pandas as pd
df=pd.read_csv("C://Users//atulkumarrai//Desktop//NanDealer_Testing.csv")
nd=nd()
dataframe_numerical = df.select_dtypes(exclude='number')

updated_df = nd.fillModeinCategoricalMeanInNumerical(dataframe=dataframe_numerical)


# test=nd.fillNanWithMeanColumnWise(df)
print(f"The updated dataframe without categorical is \n\n{updated_df}")

