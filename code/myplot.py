"""
This is my plotting obj/feature
"""
import matplotlib.pyplot as plt

class myplot():
    def __init__(self):

        pass

    def plot2y1x(self,x,y1,y2):
        """
        This function is to plot 2 data with the same x variable in the same figurse
        :param x:
        :param y1:
        :param y2:
        :return: a plot
        """

        plt.figure()
        plt.scatter(x,y1)
        plt.plot(x,y2)

        plt.show()





