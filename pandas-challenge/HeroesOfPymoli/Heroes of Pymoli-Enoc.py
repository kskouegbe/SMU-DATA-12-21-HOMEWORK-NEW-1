#!/usr/bin/env python
# coding: utf-8

# # Observable Trends
# 
# * Most of the players are male; to be precise, 84% are male, and only 14% are female. The gender demographics have a repercussion on a Purchasing Analysis by gender. We can see that males spent $1967.64 compared to females $361.94.
# * Our peak age demographic is 20-24 years old with 44.79 %, with secondary groups of 15-19 years old with 18.58 % and 25-29 years old with 13.37 %.
# * The 20-24 age group spends the most money, with a total purchase value of $1,114.06 and an average purchase of $4.32. The demographic group with the greatest average order, with $4.76 and a total purchase value of $147.67, is the 35-39.
# 
# 

# In[3]:


# Dependencies and Setup
import pandas as pd

# Set CSV path to import data 
csv_path = "Resources/purchase_data.csv"

# Read the CSV into a Pandas DataFrame
data = pd.read_csv(csv_path)

# Display columns for easy reference 
data.head(0)


# ## Player Count

# * Display the total number of players
# 

# In[4]:


# Count the total number of players
player_count = len(data["SN"].unique())
player_count

# Display the total number of players in dataframe
total = pd.DataFrame({"Total Players" :[player_count]})
total


# ## Purchasing Analysis (Total)

# * Run basic calculations to obtain number of unique items, average price, etc.
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display the summary data frame
# 

# In[5]:


# Identify unique items and drop any duplicates 
items = data['Item ID'].drop_duplicates(keep='first')

# Count the total of unique items 
items_count = len(items)

# Calculate the average price 
average_price = round(data["Price"].mean(),2)

# Count the total number of purchases
number_purchases = data["Purchase ID"].count()

# Calculate the total revenue 
total_revenue = data["Price"].sum()

# Display results in dataframe 
purchasing_total = pd.DataFrame({"Number of Unique Items": [items_count],
                            "Average Price": [average_price],
                            "Number of Purchases": [number_purchases],
                            "Total Revenue": [total_revenue]})

# Change format of 'Average Price' and 'Total Revenue' to currency 
purchasing_total [["Average Price","Total Revenue"]] = purchasing_total [["Average Price","Total Revenue"]].applymap("${:,.2f}".format)

purchasing_total


# ## Gender Demographics

# * Percentage and Count of Male Players
# 
# 
# * Percentage and Count of Female Players
# 
# 
# * Percentage and Count of Other / Non-Disclosed
# 
# 
# 

# In[6]:


# Drop any duplicates 
players = data[["Gender", "SN"]].drop_duplicates(keep='first')

# Count the amount of players by gender
gender_count = players["Gender"].value_counts()

# Calculate the percentage of players by gender
gender_percent = (round(gender_count / players["Gender"].count() * 100, 2))

# Display the gender demographics in a table
gender_demo = pd.DataFrame({"Total Count": gender_count,
                          "Percentage of Players" : gender_percent})

# Change the format 'Percentage of Players' to percentage
gender_demo["Percentage of Players"] = gender_demo["Percentage of Players"].apply("{0:.2f}%".format)

# Rename the axis to show data label "Gender"
gender_demo.index.name = "Gender"

gender_demo


# 
# ## Purchasing Analysis (Gender)

# * Run basic calculations to obtain purchase count, avg. purchase price, avg. purchase total per person etc. by gender
# 
# 
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display the summary data frame

# In[7]:


# Count the amount of purchases by gender
purch_count_gender = data.groupby("Gender")['SN'].count()

# Calculate the average purchase price
avg_price_gender = data.groupby(["Gender"])["Price"].mean()

# Calculate the total purchase value 
purch_tot_gender = data.groupby(["Gender"])['Price'].sum()

# Drop any duplicates 
duplicates = data.drop_duplicates(subset='SN', keep="first")
grouped_dup = duplicates.groupby(["Gender"])

# Calculate the average purchase total per person by gender
avg_tot_gender = purch_tot_gender / grouped_dup["SN"].count()

# Display results in DataFrame 
purchasing_gender = pd.DataFrame({"Purchase Count": purch_count_gender,
                                  "Average Purchase Price": avg_price_gender,
                                  "Total Purchase Value": purch_tot_gender,
                                  "Avg Total Purchase per Person": avg_tot_gender})

# Format values 
purchasing_gender["Average Purchase Price"] = purchasing_gender["Average Purchase Price"].apply("${:.2f}".format)
purchasing_gender["Total Purchase Value"] = purchasing_gender["Total Purchase Value"].apply("${:.2f}".format)
purchasing_gender["Avg Total Purchase per Person"] = purchasing_gender["Avg Total Purchase per Person"].apply("${:.2f}".format)
purchasing_gender = purchasing_gender[["Purchase Count", "Average Purchase Price", "Total Purchase Value", "Avg Total Purchase per Person"]]

purchasing_gender


# ## Age Demographics

# * Establish bins for ages
# 
# 
# * Categorize the existing players using the age bins. Hint: use pd.cut()
# 
# 
# * Calculate the numbers and percentages by age group
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Optional: round the percentage column to two decimal points
# 
# 
# * Display Age Demographics Table
# 

# In[8]:


# Drop any duplicates 
players = data[["Age", "SN"]].drop_duplicates()

# Establish bins for ages and age group
bins = [0,9,14,19,24,29,34,39,100]
age_group = ["<10","10-14","15-19","20-24","25-29","30-34","35-39","40+"]

# Categorize the existing players using the age bins. 
players['Age Range'] = pd.cut(players['Age'], bins, labels = age_group)

# Calculate the numbers and percentages by age group
age_count = players["Age Range"].value_counts()
age_percent = ((age_count/players["SN"].count()) * 100).round(2)

# Display results in DataFrame 
players = pd.DataFrame({'Total Count': age_count,
                        'Percentage of Players': age_percent})
#Rename index axis 
players.index.name = 'Age Ranges'
            
# Format Percentage of Players values to percent %
players['Percentage of Players'] = players['Percentage of Players'].apply('{:.2f}%'.format)

players.sort_index()


# ## Purchasing Analysis (Age)

# * Bin the purchase_data data frame by age
# 
# 
# * Run basic calculations to obtain purchase count, avg. purchase price, avg. purchase total per person etc. in the table below
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display the summary data frame

# In[9]:


# Categorize the players using the age bins. 
data['Age Ranges'] = pd.cut(data['Age'], bins, labels=age_group)
age_count = data["Age Ranges"].value_counts()

# Count the amount of purchases by age
purch_count_age = data.groupby("Age Ranges")['SN'].count()

# Calculate the average purchase price 
avg_price_age = data.groupby("Age Ranges")['Price'].mean()

# Calculate the total purchase value 
purch_tot_age = data.groupby("Age Ranges")['Price'].sum()

# Drop any duplicates
duplicates = data.drop_duplicates(subset='SN', keep="first")
age_dup = duplicates.groupby(["Age Ranges"])

# Calculate the average purchase total per person by gender
avg_tot_age = (purch_tot_age / age_dup["SN"].count())

# Display results in DataFrame 
purchasing_age = pd.DataFrame({'Purchase Count': purch_count_age,
                               'Average Purchase Price': avg_price_age,
                               'Total Purchase Value': purch_tot_age, 
                               'Avg Total Purchase per Person': avg_tot_age})


# Format values 
purchasing_age["Average Purchase Price"] = purchasing_age["Average Purchase Price"].apply("${:.2f}".format)
purchasing_age["Total Purchase Value"] = purchasing_age["Total Purchase Value"].apply("${:.2f}".format)
purchasing_age["Avg Total Purchase per Person"] = purchasing_age["Avg Total Purchase per Person"].apply("${:.2f}".format)
purchasing_age = purchasing_age[["Purchase Count", "Average Purchase Price", "Total Purchase Value", "Avg Total Purchase per Person"]]


purchasing_age.sort_index()


# ## Top Spenders

# * Run basic calculations to obtain the results in the table below
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Sort the total purchase value column in descending order
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display a preview of the summary data frame
# 
# 

# In[10]:


# Count the frequency of purchases by players
purch_count_sn = data.groupby("SN")["Price"].count()

# Caluculate average price spent by user
cal_purch_price_sn = data.groupby("SN")["Price"].mean()
purch_price_sn = cal_purch_price_sn.map("${:,.2f}".format)

# Calculate total price spent by user
purch_tot_sn = data.groupby("SN")["Price"].sum()

# Display in DataFrame
top_spenders = pd.DataFrame({"Purchase Count": purch_count_sn,
                             "Average Purchase Price": purch_price_sn,
                             "Total Purchase Value": purch_tot_sn})

# Sort by total purchase value (do this before changing the format to currency to avoid changing types to string)
top_spenders = top_spenders.sort_values(by = "Total Purchase Value",ascending = False)

# Change the format to currency
top_spenders["Total Purchase Value"] = top_spenders["Total Purchase Value"].map("${:.2f}".format)

top_spenders.head()


# ## Most Popular Items

# * Retrieve the Item ID, Item Name, and Item Price columns
# 
# 
# * Group by Item ID and Item Name. Perform calculations to obtain purchase count, average item price, and total purchase value
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Sort the purchase count column in descending order
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display a preview of the summary data frame
# 
# 

# In[11]:


# Identify the most popular items by 'Item ID' count
popular_item = data.groupby(["Item ID","Item Name"])["Price"].count()

# Calculate the total sales amount by 'Item ID' and 'Item Name'
sales_tot_item= data.groupby(["Item ID","Item Name"])["Price"].sum()

# Retrieve the item price
item_price = sales_tot_item / popular_item

# Display results in DataFrame
items = pd.DataFrame({"Purchase Count": popular_item,
                      "Item Price" : item_price,
                      "Total Purchase Value": sales_tot_item})

# Sort by purchase count in descending order
items = items.sort_values("Purchase Count", ascending = False)

# Change the format to currency
items[["Item Price", "Total Purchase Value"]] = items[["Item Price", "Total Purchase Value"]].applymap("${:.2f}".format)

items.head()


# ## Most Profitable Items

# * Sort the above table by total purchase value in descending order
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display a preview of the data frame
# 
# 

# In[12]:


# Remove formatting from Total Purchase Value and asign type float
items["Total Purchase Value"] = items["Total Purchase Value"].str.replace('$', '')
items["Total Purchase Value"] = pd.to_numeric(items["Total Purchase Value"])

# Sort the above table by total purchase value in descending order
items = items.sort_values("Total Purchase Value", ascending = False)

# Change the format to currency
items["Total Purchase Value"] = items["Total Purchase Value"].apply("${:.2f}".format)

items.head()


# In[ ]:




