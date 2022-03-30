import pandas as pd
import random

class nanDealer:
    def fillNanWithMeanColumnWise(self,dataframe):
        """
        This option will fill the Nan values present in your dataframe with the mean of its column.
         """
        try:
           ## store the categorical columns so that they can be merged at end of the
            cat = dataframe.select_dtypes(include='object').columns.to_list()
            index_of_cat = [dataframe.columns.get_loc(col) for col in cat]
            
            cat_cols = []             ## to store the categorical columns series
            for i in range(len(cat)):
                cat_cols.append(dataframe[cat[i]])
            
             ## We exclude the categorical data here
            dataframe_numerical = dataframe.select_dtypes(exclude='object')

            ## Finding the mean of the each feature/column
            df = dataframe_numerical.columns[dataframe_numerical.isnull().any()]

            ## Replacing nan values with their column mean
            for i in df:
                mean=dataframe_numerical[i].mean()
                dataframe_numerical[i].fillna(mean,inplace=True)

            ## merging the categorical columns again to the updated dataframe
            for i in range(len(index_of_cat)):
                dataframe_numerical.insert(index_of_cat[i],cat[i], cat_cols[i])

            return dataframe_numerical
        except Exception as e:
            raise Exception("Error occured while filling Nan values with mean of the data\n",str(e))

    def fillNanWithMedianColumnWise(self,dataframe):
        """
        This option will fill the Nan values present in your dataframe with the median of its column.
         """
        try:
            ## store the categorical columns so that they can be merged at end of the
            cat = dataframe.select_dtypes(include='object').columns.to_list()
            index_of_cat = [dataframe.columns.get_loc(col) for col in cat]
            
            cat_cols = []             ## to store the categorical columns series
            for i in range(len(cat)):
                cat_cols.append(dataframe[cat[i]])


            ## We exclude the categorical data here
            dataframe_numerical = dataframe.select_dtypes(exclude='object')

            ## Finding the median of the each feature/column
            df = dataframe_numerical.columns[dataframe_numerical.isnull().any()]

            ## Replacing nan values with their column median
            for i in df:
                median = dataframe_numerical[i].median()
                dataframe_numerical[i].fillna(median, inplace=True)


            ## merging the categorical columns again to the updated dataframe
            for i in range(len(index_of_cat)):
                dataframe_numerical.insert(index_of_cat[i],cat[i], cat_cols[i])

            return dataframe_numerical

        except Exception as e:
            raise Exception("Error occured while filling Nan values with mean of the data\n", str(e))



    def fillNanWithRandomValuesFromColumn(self, dataframe):
        """
        This option will fill the Nan values present in your dataframe with the Random values from its column.
         """
        try:

            ## store the categorical columns so that they can be merged at end of the
            cat = dataframe.select_dtypes(include='object').columns.to_list()
            index_of_cat = [dataframe.columns.get_loc(col) for col in cat]
            
            cat_cols = []             ## to store the categorical columns series
            for i in range(len(cat)):
                cat_cols.append(dataframe[cat[i]])

            ## We exclude the categorical data here
            dataframe_numerical = dataframe.select_dtypes(exclude='object')

            ## Finding the median of the each feature/column
            df = dataframe_numerical.columns[dataframe_numerical.isnull().any()]

            ## Replacing nan values with their column median
            for i in df:
                random_num = random.randrange(dataframe_numerical[i].min(),dataframe_numerical[i].max())
                dataframe_numerical[i].fillna(random_num, inplace=True)

            ## merging the categorical columns again to the updated dataframe
            for i in range(len(index_of_cat)):
                dataframe_numerical.insert(index_of_cat[i],cat[i], cat_cols[i])

            return dataframe_numerical
        except Exception as e:
            raise Exception("Error occured while filling Nan values with random value from the column\n", str(e))

    def fillNanWithMeanRowWise(self,dataframe):
        """
        This option will fill the Nan values present in your dataframe with the mean of the respective row.
         """
        try:

             ## store the categorical columns so that they can be merged at end of the
            cat = dataframe.select_dtypes(include='object').columns.to_list()
            index_of_cat = [dataframe.columns.get_loc(col) for col in cat]
            
            cat_cols = []             ## to store the categorical columns series
            for i in range(len(cat)):
                cat_cols.append(dataframe[cat[i]])

            ## We exclude the categorical data here
            dataframe_numerical = dataframe.select_dtypes(exclude='object')

            ##Finding the mean row wise
            mean=dataframe_numerical.mean(axis=1)

            ##Enumertating the dataframe and filling the mean value in the Nan values
            for i,column in enumerate(dataframe_numerical):
                dataframe_numerical.iloc[:,i].fillna(mean,inplace=True)

            ## merging the categorical columns again to the updated dataframe
            for i in range(len(index_of_cat)):
                dataframe_numerical.insert(index_of_cat[i],cat[i], cat_cols[i])


            return dataframe_numerical
        except Exception as e:
            raise Exception("Error occured while filling the Nan values with mean of their respective rows\n,str(e)")


    def fillNanWithMedianRowWise(self,dataframe):
        """
        This option will fill the Nan values present in your dataframe with the median of the respective row.
         """
        try:

             ## store the categorical columns so that they can be merged at end of the
            cat = dataframe.select_dtypes(include='object').columns.to_list()
            index_of_cat = [dataframe.columns.get_loc(col) for col in cat]
            
            cat_cols = []             ## to store the categorical columns series
            for i in range(len(cat)):
                cat_cols.append(dataframe[cat[i]])

            ## We exclude the categorical data here
            dataframe_numerical = dataframe.select_dtypes(exclude='object')

            ##Finding the mean row wise
            median=dataframe_numerical.median(axis=1)

            ##Enumertating the dataframe and filling the mean value in the Nan values
            for i,column in enumerate(dataframe_numerical):
                dataframe_numerical.iloc[:,i].fillna(median,inplace=True)

            
            ## merging the categorical columns again to the updated dataframe
            for i in range(len(index_of_cat)):
                dataframe_numerical.insert(index_of_cat[i],cat[i], cat_cols[i])


            return dataframe_numerical
        except Exception as e:
            raise Exception("Error occured while filling the Nan values with mean of their respective rows\n,str(e)")


    def fillNanwithoutCategoricalRemoval(self, dataframe):
        try:
            ## store the categorical columns so that they can be merged at end of the
            cat = dataframe.select_dtypes(include='object').columns.to_list()
            index_of_cat = [dataframe.columns.get_loc(col) for col in cat]
            
            cat_cols = []             ## to store the categorical columns series
            for i in range(len(cat)):
                cat_cols.append(dataframe[cat[i]])
            
             ## We exclude the categorical data here
            dataframe_numerical = dataframe.select_dtypes(exclude='object')

            ## Finding the mean of the each feature/column
            df = dataframe_numerical.columns[dataframe_numerical.isnull().any()]

            ## Replacing nan values with their column mean
            for i in df:
                mean=dataframe_numerical[i].mean()
                dataframe_numerical[i].fillna(mean,inplace=True)

            ## merging the categorical columns again to the updated dataframe
            for i in range(len(index_of_cat)):
                dataframe_numerical.insert(index_of_cat[i],cat[i], cat_cols[i])

            return dataframe_numerical

        except Exception as e:
            raise Exception(f"Error occured while filling the Nan values with mean {str(e)} ")


    def fillModeinCategoricalMeanInNumerical(self,dataframe):
        try:
            dataframe.fillna(dataframe.select_dtypes(include='object').mode().iloc[0], inplace=True)
            
            dataframe.fillna(dataframe.select_dtypes(include='number').mode().iloc[0], inplace=True)
        except Exception as e:
            raise Exception(f"Error occured while filling the Nan values of numerical columns with Mean and categorical with Mode {str(e)} ")

    
    def fillModeinCategoricalMedianInNumerical(self,dataframe):
        try:
            dataframe.fillna(dataframe.select_dtypes(include='object').mode().iloc[0], inplace=True)
            
            dataframe.fillna(dataframe.select_dtypes(include='number').median().iloc[0], inplace=True)
        except Exception as e:
            raise Exception(f"Error occured while filling the Nan values of numerical columns with median and categorical column with mode {str(e)} ")


################################################################################
# work on clustering algorithm to fill the Nan values with
################################################################################





if __name__=="__main__":
    test = nanDealer()
    t = pd.read_csv("C://Users//atulkumarrai//Batsmen_data.csv")

    df = test.fillNanWithMeanColumnWise(t)
    df1 = test.fillNanWithMedianColumnWise(t)
    df2 = test.fillNanWithRandomValuesFromColumn(t)
    df3 = test.fillNanWithMeanRowWise(t)
    df4 = test.fillNanWithMedianRowWise(t)
    print(df)
    print(df1)
    print(df2)
    print(df3)
    print(df4)
