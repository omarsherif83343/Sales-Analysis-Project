import mysql.connector as sql
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

connect = sql.connect(host='localhost', user='root',password='omarahmed123@',database='company')
cursor = connect.cursor()
#statement = "select * from products"
#statement2 = "select * from products where price > 2000"
#statement3 = "select * from products order by price desc"
#statement4 = ("select max(price) as max_price,min(price) as min_price,round(avg(price)) as avg_price , price * stock as total_price from products group by total_price")
#statement5 = "select count(product_id) as number_of_products ,category from products group by category"
#statement6 = "select avg(price) as avg_price,category from products group by category"
#statement7 = "select avg(price) as avg_price,category from products group by category having avg(price) > 3000"
#statement8 = "select s.sale_id,p.product_name,s.quantity from products p inner join sales s on p.product_id = s.product_id"
#statement9 = "select sum(s.quantity) as sum_of_quantity,p.product_name from products p join sales s on p.product_id = s.product_id group by p.product_name"
#statement10 = "select sum(s.quantity) as total_quantity,p.product_name from products p join sales s on p.product_id = s.product_id group by p.product_name order by total_quantity desc limit 1 "
#statement11 = "select sum(p.price * s.quantity) as revenue , p.product_name from products p join sales s on p.product_id = s.product_id group by p.product_name"
#statement12 = "select sum(p.price * s.quantity) as revenue,p.product_name from products p join sales s on p.product_id = s.product_id group by p.product_name order by revenue desc limit 3"
statement13 = "select p.product_name,p.price,s.quantity from products p inner join sales s on p.product_id = s.product_id"
cursor.execute(statement13)

results = cursor.fetchall()

columns = [col[0] for col in cursor.description]

df = pd.DataFrame(results, columns=columns)
df["price"] = pd.to_numeric(df["price"])
df["quantity"] = pd.to_numeric(df["quantity"])
df["revenue"] = df["price"] * df["quantity"]

"""
df["inventory_value"] = df["price"] * df["stock"]
print(df.head(5))

count_of_product = df.groupby("category")["product_name"].count()
count_of_product.plot(kind="line")
plt.title("Count By Category")
plt.xlabel("Category")
plt.ylabel("Count Of Products")
plt.show()
avg_of_price_by_category = df.groupby("category")["price"].mean()
avg_of_price_by_category.plot(kind="bar")
plt.title("Average Price By Category")
plt.xlabel("Category")
plt.xticks(rotation=0,fontsize=12)
plt.ylabel("Average Price")
plt.show()

"""

revenue_by_product = df.groupby("product_name")["revenue"].sum()
plt.figure(figsize=(10,6))
ax = revenue_by_product.plot(kind="bar")
ax.yaxis.set_major_formatter(ticker.StrMethodFormatter('{x:,.0f}'))
plt.title("Revenue by Product")
plt.xlabel("Product Name")
plt.xticks(rotation=0)
plt.ylabel("Revenue")
plt.show()

top_selling_products = df.groupby("product_name")["quantity"].sum().nlargest(5)
plt.figure(figsize=(10,6))
top_selling_products.plot(kind="bar")
plt.title("Top 5 Products By Quantity Sold")
plt.xlabel("Product Name")
plt.xticks(rotation=0)
plt.ylabel("Quantity Sold")
plt.show()


