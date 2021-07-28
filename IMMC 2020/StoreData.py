"""
Author: Team 2020038
Date: May 18, 2020
This class is in charge of retrieving data from the excel file, StoreData_IMMC,
 and performing all of the necessary calculations to process and return useful
 information to help us make layout decisions.
"""
import xlrd #library used to read data from an excel file

class StoreData():
    """
    This method instantiates the class and accepts a string which is
     the path location of the excel file that is to be read.
    """
    def __init__(self, loc: str):
        self.loc = loc

    """
    This method opens the excel file allowing information to be read from it
     and returns a variable used fro retrieving that information.
    """
    def get_excel_info(self):          
        wb = xlrd.open_workbook(self.loc) #opens the excel file
        sheet = wb.sheet_by_index(0)

        return sheet
    
    """
    This method goes through the excel file and retrieves the name and
     rating of every product and stores it in a dictionary where the keys
     of the dictionary are the names of the products and the values are
     the ratings.
    """
    def product_ratings(self):
        sheet = self.get_excel_info()
        sheet.cell_value(0, 0)
        products = {}

        for i in range(2, sheet.nrows):
            product = sheet.row_values(i)[4] #retrieves the name of the product
            rating = sheet.row_values(i)[8] #retrieves the rating of the product

            #if the index where the name is located is empty
            #that means there are no more products so exit the for loop
            if sheet.row_values(i)[4] == "":
                break
            #stores the name and rating of the product into a dictionary
            products[product] = rating
    
        return products #return the dictionary
    
    """
    This method goes through the excel file finding the sum of the ratings of
     the products in each department and stores the department name and total
     rating of the department's products in a dictionary.
    """
    def total_department_ratings(self):
        sheet = self.get_excel_info()
        sheet.cell_value(0, 0)
        departments = {}

        for i in range(2, sheet.nrows):
            #the name of the department the product is in
            name = sheet.row_values(i)[0] 
            rating = sheet.row_values(i)[8] #the rating of the product  

            #if the index where the name is located is empty
            #that means there are no more products so exit the for loop
            if sheet.row_values(i)[4] == "":
                break
            #add the rating to the department total as long as
            #the department key exists
            try:
                departments[name] += rating #add the rating to the total
                #rounds the total in case the number has more than 1 decimal place 
                departments[name] = round(departments[name], 1)
            #if we have not yet added a rating to this department
            #we create the department key and then add the rating
            except:
                #create the department key and set the total to zero
                departments[name] = 0
                departments[name] += rating #add the rating
                
        return departments #return the dictionary

    """
    This method gets the amount of products ina department by
     going through the excel file and keeping track of the number
     in a dictionary.
    """
    def num_of_department_products(self):
        sheet = self.get_excel_info()
        sheet.cell_value(0, 0)
        amounts = {}

        for i in range(2, sheet.nrows):
            name = sheet.row_values(i)[0] #name of the department

            #if the index where the name is located is empty
            #that means there are no more products so exit the for loop
            if sheet.row_values(i)[4] == "":
                break
            #add one to the product count as long as
            #the department key exists
            try:
                amounts[name] += 1
            #if we have not yet started counting this department
            #we create the department key and then add the first product
            except:
                amounts[name] = 0
                amounts[name] += 1

        return amounts #return the dictionary
    
    """
    This method takes the total department rating and divides it by
     the number of products in the department to create an average
     rating for the department to determine the popularity of the department.
    """
    def average_department_ratings(self):
        #dictionary containing the number of products in each department
        amounts = self.num_of_department_products()
        #dictionary containing the total rating of each department
        departments = self.total_department_ratings()

        department_amounts = amounts.values() #list with the number of products
        department_names = amounts.keys() #list with the department names
        #list with the total department ratings
        department_ratings = departments.values() 

        average_ratings = {}

        #goes through each list at the same time to calculate the average
        #and assign it to the department in a new dictionary
        for amount, rating, name in zip(department_amounts, department_ratings, department_names):
            average_ratings[name] = rating/amount

        return average_ratings #return the dictionary
        
    """
    This method gets the product name, regular price and current sale price.
    """
    def product_prices(self):
        products = []
        sheet = self.get_excel_info()
        
        for i in range(2, sheet.nrows):
            #if the index where the name is located is empty
            #that means there are no more products so exit the for loop
            if sheet.row_values(i)[4] == "":
                break
            #add the name and the prices to a list
            products.append(sheet.row_values(i)[4:7])

        return products #return the list
    
    """
    This method determines how many products shre the same rating.
    """
    def rating_distribution(self):
        #dictionary containing the product name and rating
        products = self.product_ratings()

        ratings = list(products.values()) #list containg the product ratings
        ratings.sort() #sort the ratings from lowest to highest
        dist = {}
        
        for rating in ratings:
            #add one to the rating count as long as
            #the rating key exists
            try:
                dist[rating] += 1
            #if we have not yet started counting this rating
            #we create the rating key and then add the first count
            except:
                dist[rating] = 0
                dist[rating] += 1
                
        return dist #return the dictionary

    """
    This method calculates the discount on a product by dividing the
     current sale price by the regular price.
    """
    def calc_discount(self, regular_price, sale_price):
        return 1.0 - (float(sale_price)/float(regular_price))

    """
    This method calculates the weights that will be used in determing
     the 'attractiveness score' by finding what percent of products
     have the same rating and keeping that percent in a dictionary for
     later calculations.
    """
    def calc_rating_weights(self):
        #dictionary containg ratings and how many products have the same rating
        rating_dist = self.rating_distribution()
        #dictionary containing the ratings of each product
        products = self.product_ratings()

        #the number of products in the store
        total = len(list(products.values()))

        ratings = rating_dist.keys() #list of the ratings there are
        weights = {}


        for rating in ratings:
            #assigns the percent of products that have the same rating
            #to another dictionary
            weights[rating] = rating_dist[rating] / total

        return weights
        
    """
    This method calculates the rating score which is used for
     determining the attractiveness score.
    """
    def calc_rating_score(self, rating):
        return 5*(rating-(round(rating%1, 1)))+0.5*(round(rating%1, 1))

    """
    This method calculates the discount score which is used for
     determining the attractiveness score.
    """
    def calc_discount_score(self, discount):
        return round(discount/10)

    """
    This method calculates the attractiveness score for a particular
     product which is used for determining the popular products in the store.
    """
    def calc_product_attractiveness(self, rating, discount):
        #dictionary containing the ratings and weights for those ratings
        rating_weights = self.calc_rating_weights() 
        weight = rating_weights[rating] #the weight for a particular rating

        #calculates the rating score
        rating_score = self.calc_rating_score(rating)
        #calculates the discount score
        discount_score = self.calc_discount_score(discount)

        #calculates and returns the attractiveness score
        return ((weight*rating_score) + (discount_score*(1-weight)))/2
    
    """
    This method goes through the list of products and prints the most
     popular products to the console
    """
    def popular_products(self):
        sheet = self.get_excel_info()
        sheet.cell_value(0, 0)

        for i in range(2, sheet.nrows):
            #if the index where the name is located is empty
            #that means there are no more products so exit the for loop
            if sheet.row_values(i)[4] == "":
                break
            else:
                regular_price = sheet.row_values(i)[5] #regular price of the product
                sale_price = sheet.row_values(i)[6] #sale price of the product
                
                rating = sheet.row_values(i)[8] #rating of the product
                #calculates the discount on the product from the regular price
                #and sale price
                discount = self.calc_discount(regular_price, sale_price)

                #2.54375 was found to be the highest attractiveness score when using
                #the data so any product with this score is considered popular and
                #the name of the product will be printed to the console
                if self.calc_product_attractiveness(rating, discount) == 2.54375:
                    print(sheet.row_values(i)[4])
    
#if this file is being run, the method that prints
#the popular products to the console will be called
if __name__ == "__main__":
    self.popular_products()
