import numpy as np 
import matplotlib.pyplot as plt

class PandasComputations:

    """Useful pandas computations not in pandas"""


    def __init__(self, data_frame):
        self.dataframe = data_frame

    
    def interesting_metrics_to_compute(self):
        """Prints interesting metrics to compute"""
        print("ECDF")
        print("")
        print("CDF")
        print("")
        print("PDF")
        



    def check_df(self):
        print(self.dataframe.head())

    def cumulative_subtraction_across_column(self, column_name):
        """Title is self-explantory"""
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


    def ECDF(self, column_name, x_label):
        """Computes a graph that shows the percentage of data that has that specific value"""
        x = np.sort(self.dataframe[column_name])
        y = np.arange(1, len(x)+1) / len(x)
        _ = plt.plot(x,y, marker='.', linestyle='none')
        _ = plt.xlabel(x_label)
        _ = plt.ylabel("ECDF")
        plt.margins(0.02)
        plt.show()

    




        

        









