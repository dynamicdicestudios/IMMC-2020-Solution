# IMMC-2020-Solution
The IMMC (International Mathematical Modeling Challenge) is a team challenge that asks participants to write a 20-page description of how they solved an assigned problem using mathematical modelling and other techniques. 

**Challenge Requirements**
For the 2020 challenge, teams were required to write a 20-page report on how to handle a flash sale event at a brick-and mortar location. The main goals were to reorganize the layout of the store to allow the slash sale to go a s smoothly as possible (via minimizing the time customers spend in the store, the amount of fighting and the damage to the goods in the store). 

**My role**
My teammates and I received data about the store, and I was responsible for processing and concluding the data. I then had to create a rating system for products, create a rough layout of the store from my conclusions, and write about my findings.

**My process**
During flash sale events, there are always items that the majority of customers will find desirable. By determining which products these are, it will not only positively affect the decision making in regards to the layout of the store, but also in determining which products are at a greater risk to be damaged. I went about finding the most desirable products (MDPs) by assinging each product an "Attractiveness Score." The Attractiveness Score consists of the sum of the rating score and discount score. The formulas for the rating and discount scores are as follows:

Rating score formula 
Let x be the rating of the product and y be the weight of the product rating 
f(x, y) = y[5 * (x − (x mod 1)) + 0.5 * (x mod 1)]
Discount score formula 
Let x be the discount on the product and y be the weight of the discount 
f(x, y) = y(x/10)

Studies have found that for every star rating, the attractiveness of a merchandise increases by a minimum of 5%. We applied this principle in our formula by multiplying the ones place (digit) in the rating of the product by 5. For example, if the rating was 4.7, we would multiply 4 by 5 giving us a product of 20. Since there are ten tenths of a rating (.1 ratings) between each star rating, we divided 5% by 10 giving us a 0.5% increase per .1 star rating. For example, if the rating was 4.2, we would multiply .2 by 0.5 giving a product of 0.1. Studies have shown that the attractiveness of a product steadily increases per .1 rating. But as the rating approaches 5 stars, the attractiveness decreases due to customers believing that the merchandise may be too good to be true and is possibly overrated. Thus, we assigned each rating a weight to better determine how significant the rating of the merchandise is. The weighting was derived from the percentage of merchandise with the same rating.
![Rating_Distribution](https://user-images.githubusercontent.com/60636495/127366906-b1335823-6b66-4152-9fae-6bfd476b2121.png)

