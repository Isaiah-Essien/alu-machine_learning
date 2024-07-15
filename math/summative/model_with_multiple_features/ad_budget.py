'''
This file will uses scikit learn to create a Linear regression model on the The advertising dataset, dataset which captures the sales revenue generated with respect to advertisement costs across multiple channels like radio, tv, and newspapers.

It is required to understand the impact of ad budgets on the overall sales.

Dataset Features:
    -Id: The Id table listed in ascending order
    -TV ad Budget: Amonut spent on TV advertisments
    -Radio ad Budget Amount spent on radio advertisment
    -Newspaper ad Budget column: Amount to be spent on Newespaper advert
    -Sales column: The target Feature of the dataset, showing a relationship between the different advertisment budgets and their expected reveue on Sales

'''
# Neccsasry imports for traainig a linear regression Model 
import pandas as pd

# Import necessary libraries

# For data manipulation and analysis
import pandas as pd


# For linear regression
from sklearn.linear_model import LinearRegression

# For splitting the dataset
from sklearn.model_selection import train_test_split

# For evaluation metrics
from sklearn.metrics import mean_squared_error

# for saving pickle file import joblib
import joblib


# Load the data set
data = pd.read_csv('../data/advertising_budget _and_sales.csv')
#display the first 10 rows
print(data.head(10))
#check the description of the dataset to ensure there is no data to be cleaned or null cells
print(data.describe())
#check the number of rows and columns of the dataset
print(data.shape)

'''This dataset has spaces and dolar signs in the columns, so it has to be cleaned and columns renamed'''
# creating a copy of the dataset for cleaning and model training
data_copy=data.copy()
# Rename the columns of the copy
data_copy.columns = ['Id','TV_ad_budget', 'Radio_ad_budget', 'Newspaper_ad_budget', 'Sales']

#Display first 10 rows of the copy and cleaned data
print(data_copy.head(10))

'''On to the traninig process'''
# Select features and target from the modified dataset
features = ['TV_ad_budget', 'Radio_ad_budget', 'Newspaper_ad_budget']
target='Sales'

x=data_copy[features]
y=data_copy[target]

#Split the data for training and testing with an 80% for training
x_train,x_test,y_train,y_test = train_test_split(x,y,random_state=42,test_size=0.2)

#create and train the linear regression model
ad_budgets_sales_model=LinearRegression()
ad_budgets_sales_model.fit(x_train,y_train)

'''Predictions'''
# Make predictions using the testing sets
y_predict=ad_budgets_sales_model.predict(x_test)
print(f'The test predictions are: \n{y_predict}')

'''Evaluate the model to get the Mean Squared error and Root mean Squared error'''
MSE=mean_squared_error(y_test,y_predict)

RMSE=mean_squared_error(y_test,y_predict, squared=False)


print(f'The Mean squared error is: {MSE}\nThe Root Mean squared Error is: {RMSE}')


'''Let's get some values from the dataset and try to map to the predicted sales'''
some_ad_budgets=x.head()
print(f'some advert budgets are: \n{some_ad_budgets}')
y_predict = ad_budgets_sales_model.predict(some_ad_budgets)
print(f'Their  predicted sales are: \n{y_predict}')

print(data_copy.head())#comparing

#Check the score of the model
model_score=ad_budgets_sales_model.score(x_test,y_test)*100
print(f'The Score of the model is: {model_score}')

# Save the model to a file using joblib
# joblib.dump(ad_budgets_sales_model, 'ad_budgets_sales_model.joblib')

# print("Model saved as ad_budgets_sales_model.joblib")
