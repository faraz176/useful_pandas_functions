import numpy as np 
import matplotlib.pyplot as plt

class PandasComputations:

    """Useful pandas computations not in pandas"""


    def __init__(self, data_frame):
        self.dataframe = data_frame



    def check_df(self):
        print(self.dataframe.head())

    def cumulative_subtraction_across_column(self, column_name):
        list_of_cases = []
        series_items = list(self.dataframe[column_name])
        
        for i in range(len(series_items)):
            count = 0 
            try:
                    
                count = count + series_items[i+1] - series_items[i]
                    
            except IndexError:
                print('completed')

            
            final_count = count
            list_of_cases.append(final_count)


    def ECDF(self, column_name, x_label, y_label):
        x = np.sort(self.dataframe[column_name])
        y = np.arange(1, len(x)+1) / len(x)
        _ = plt.plot(x,y, marker='.', linestyle='none')
        _ = plt.xlabel(x_label)
        _ = plt.ylabel(y_label)
        plt.margins(0.02)
        plt.show()




        

        









