from matplotlib import pyplot as plt
from StoreData import StoreData
import numpy as np

loc = (r"C:\Users\Josiah\Desktop\IMMC 2020\StoreData_IMMC.xlsx")
sd = StoreData(loc)

def deals_table():
    fig = plt.figure(dpi=80)
    ax = fig.add_subplot(1,1,1)
    front, mid, back = sd.deal_sort(0.25, 0.4)

    table_data=[
        ["Front", front],
        ["Middle", mid],
        ["Back", back]
    ]
    table = ax.table(cellText=table_data, loc='center')

    table.set_fontsize(14)
    table.scale(1,4)

    ax.axis('off')
    plt.show()

def calc_xvalues(n, t, d, w):
    """
    n = Which dataset this is  
    t = Number of datasets (in this case there are 3)
    d = Number of sets of bars
    w = Width of each bar
    """
    xvalues = [t*element + w*n for element
                 in range(d)]
    return xvalues

def discount_bars():
    placement = ["Front", "Middle", "Back"]
    
    front, mid, back = sd.deal_sort(0.25, 0.4)
    deals1 = [len(front), len(mid), len(back)]
    deals1_x = calc_xvalues(1, 3, 3, 0.8)
    plt.bar(deals1_x, deals1)

    front, mid, back = sd.deal_sort(0.3, 0.4)
    deals2 = [len(front), len(mid), len(back)]
    deals2_x = calc_xvalues(2, 3, 3, 0.8)
    plt.bar(deals2_x, deals2)

    front, mid, back = sd.deal_sort(0.25, 0.35)
    deals3 = [len(front), len(mid), len(back)]
    deals3_x = calc_xvalues(3, 3, 3, 0.8)
    plt.bar(deals3_x, deals3)
    
    ax = plt.subplot()
    middle_x = [(a + b + c) / 3.0 for a, b, c in zip(deals1_x, deals2_x, deals3_x)]
    ax.set_xticks(middle_x)
    ax.set_xticklabels(placement)
    
    plt.xlabel("Placement in the store")
    plt.ylabel("Number of products that would be there")
    plt.title("Placement of products based on percent off")
    plt.legend(["<=25%, 25-40%, >40%", "<=30%, 30-40%, >40%", "<=25%, 25-35%, >35%"], loc=1)
    
    plt.show()

def department_bars():
    departments = sd.average_department_ratings()

    names = departments.keys()
    yvalues = departments.values()

    spaced_labels = [3*i for i in range(len(names))]

    print(yvalues)
    names = [name[0:7]+"." for name in names]

    plt.bar(spaced_labels, yvalues)

    ax1 = plt.subplot(1, 1, 1)
    ax1.set_xticks(spaced_labels)
    ax1.set_xticklabels(names)
    
    plt.xlabel("Departments")
    plt.ylabel("Average rating")
    plt.title("Department popularity based on average ratings")

    plt.show()

def department_table():
    amounts = sd.num_of_department_products()
    departments = sd.total_department_ratings()

    department_amounts = amounts.values()
    department_names = amounts.keys()
    department_ratings = departments.values()

    table_data = []
    headers = ["Department", "Number of products", "Average rating"]

    for amount, rating, name in zip(department_amounts, department_ratings, department_names):
        table_data.append([name, amount, round(rating/amount, 1)])
    
    fig = plt.figure(dpi=80)
    ax = fig.add_subplot(1,1,1)
    
    table = ax.table(cellText=table_data, colLabels=headers, loc='center')

    table.set_fontsize(14)
    table.scale(1,3)

    ax.axis('off')
    plt.show()

def popular_bars():
    popular_products = sd.popular_products()

    names = popular_products.keys()
    yvalues = popular_products.values()
    
    spaced_labels = [3*i for i in range(len(names))]

    print(yvalues)
    names = [name[0:7]+"." for name in names]

    plt.bar(spaced_labels, yvalues)

    ax1 = plt.subplot(1, 1, 1)
    ax1.set_xticks(spaced_labels)
    ax1.set_xticklabels(names)
    
    plt.xlabel("Departments")
    plt.ylabel("Average rating")
    plt.title("Department popularity based on average ratings")

    plt.show()
    
def popular_table():
    popular_products = sd.popular_products()

    names = popular_products.keys()
    yvalues = popular_products.values()

    table_data = []
    headers = ["Product", "Rating"]
    
    spaced_labels = [3*i for i in range(len(names))]

    print(yvalues)
    names = [name[0:7]+"." for name in names]

    plt.bar(spaced_labels, yvalues)

    ax1 = plt.subplot(1, 1, 1)
    ax1.set_xticks(spaced_labels)
    ax1.set_xticklabels(names)
    
    plt.xlabel("Departments")
    plt.ylabel("Average rating")
    plt.title("Department popularity based on average ratings")

    plt.show()
def rating_bars():
    ratings = sd.rating_distribution()

    rating = ratings.keys()
    yvalues = ratings.values()
    print(yvalues)

    spaced_labels = [3*i for i in range(len(rating))]

    plt.bar(spaced_labels, yvalues)

    ax1 = plt.subplot(1, 1, 1)
    ax1.set_xticks(spaced_labels)
    ax1.set_xticklabels(rating)
    
    plt.xlabel("Ratings")
    plt.ylabel("How many products have the same rating")
    plt.title("Rating distribution")

    plt.show()

def rating_lines():
    ratings = sd.rating_distribution()

    rating = np.array(list(ratings.keys()))
    yvalues = np.array(list(ratings.values()))
    
    m, b = np.polyfit(rating, yvalues, 1)

    spaced_labels = [3*i for i in range(len(rating))]

    plt.plot(range(len(rating)), yvalues, color='gray', marker = 'o')
    plt.plot(range(len(rating)), m*rating + b, color='red')

    ax1 = plt.subplot(1, 1, 1)
    ax1.set_xticks(rating)
    ax1.set_xticklabels(rating)
    
    plt.xlabel("Ratings")
    plt.ylabel("How many products have the same rating")
    plt.title("Rating distribution")

    plt.show()

def weights_table():
    rating_weights = sd.calc_rating_weights()

    ratings = rating_weights.keys()
    weights = rating_weights.values()

    table_data = []
    headers = ["Rating", "Weight for the rating"]

    for rating, weight in zip(ratings, weights):
        table_data.append([rating, weight])

    fig = plt.figure(dpi=80)
    ax = fig.add_subplot(1,1,1)
    
    table = ax.table(cellText=table_data, colLabels=headers, loc='center')

    table.set_fontsize(12)
    table.scale(1,2)

    ax.axis('off')
    plt.show()    

sd.popular_products()
