"""
Author: Team 2020038
Date: May 18, 2020
This file contains all of the methods that visualize the data
 processed by the StoreData class.
"""

from matplotlib import pyplot as plt
from StoreData import StoreData
import numpy as np

loc = (r"Location of the StoreData_IMMC.xlsx file") #must be a raw string
sd = StoreData(loc) #instantiates a StoreData object

"""
This method fills a table with the list of departments, number of products
 in those departments and the average rating of those departments.
"""
def department_table():
    #dictionary containing the names of the departments
    #and the number of products in those departments
    amounts = sd.num_of_department_products()
    #dictionary containing the names of the departments
    #and the total rating of those departments
    departments = sd.total_department_ratings()

    #list containing number of products in the departments
    department_amounts = amounts.values()
    #list containing the names of the departments
    department_names = amounts.keys()
    #list containing the total rating of the departments
    department_ratings = departments.values()

    table_data = []
    #headers of the table
    headers = ["Department", "Number of products", "Average rating"]

    #goes through the three lists and adds the name of the department, number
    #of products in the department and the average rating of the department by
    #dividing the total rating by the amount of products
    for amount, rating, name in zip(department_amounts, department_ratings, department_names):
        table_data.append([name, amount, round(rating/amount, 1)])
    
    fig = plt.figure(dpi=80)
    #determines how many diagrams will be shown (which is one)
    ax = fig.add_subplot(1,1,1)
    
    #creates the table
    table = ax.table(cellText=table_data, colLabels=headers, loc='center')

    table.set_fontsize(14) #fontsize of the table
    table.scale(1,3) #scale of the table

    ax.axis('off')
    plt.show() #shows the table

"""
This method creates a bar graph showing how many products
 have the same rating.
"""
def rating_bars():
    #dictionary containg ratings and how many products have the same rating
    ratings = sd.rating_distribution()

    #seperates the ratings data from the number of products
    #that have the same rating data
    rating = ratings.keys()
    yvalues = ratings.values()

    #triples the normal spacing between bars to make the graph look better
    spaced_labels = [3*i for i in range(len(rating))]

    #creates the bar graph
    plt.bar(spaced_labels, yvalues)

    #adds labels to the x ticks that are the different ratings
    ax = plt.subplot(1, 1, 1)
    ax.set_xticks(spaced_labels)
    ax.set_xticklabels(rating)
    
    plt.xlabel("Ratings") #label on the x axis
    plt.ylabel("How many products have the same rating") #label on the y axis
    plt.title("Rating distribution") #title of the graph

    plt.show() #shows the diagram

"""
This method creates a table that shows the weights that
 apply to each rating.
"""
def weights_table():
    #dictionary containing the ratings and weights for those ratings
    rating_weights = sd.calc_rating_weights()

    #seperates the ratings and weights for those ratings into seperate lists
    ratings = rating_weights.keys()
    weights = rating_weights.values()

    table_data = []
    headers = ["Rating", "Weight for the rating"] #headers for the table

    #goes through the 2 list and adds the information to another list that
    #will be used to fill the table
    for rating, weight in zip(ratings, weights):
        table_data.append([rating, weight])
    
    fig = plt.figure(dpi=80)
    #determines how many diagrams will be shown (which is one)
    ax = fig.add_subplot(1,1,1)

    #creates the table
    table = ax.table(cellText=table_data, colLabels=headers, loc='center')

    table.set_fontsize(12) #fontsize of the table
    table.scale(1,2)#scale of the table

    ax.axis('off')
    plt.show() #shows the table

#if this file is being run, the method that shows
#rating weights table will be called
if __name__ == "__main__":
    weights_table()
