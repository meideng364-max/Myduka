import psycopg2

# Connecting SQL Database and Python using Psycopg2

conn=psycopg2.connect(host='localhost', port=5432 , user='postgres', password='1234', database='myduka_db')


cur=conn.cursor()


# Function to fetch data from the products table database, bring them to python, and output them on the Python Terminal
# def get_products():
#     cur.execute("select * from products")
#     products_data= cur.fetchall()
#     return products_data

# products_data=get_products()
# print(products_data)


# Function for inserting data into the products table in the SQL Database
# def insert_products(prods_details):
#     cur.execute("insert into products(name, buying_price, selling_price) values(%s, %s, %s)", prods_details)
#     conn.commit()

# # prod1=('Wireless Board', 3000, 4000)
# # prod2=('Headphones', 2000, 3000)
# prod3=('Macbook', 50000, 60000)
# # insert_products(prod1)
# # insert_products(prod2)
# insert_products(prod3)
# products_data=get_products()
# print(products_data)





# Function to fetch sales data from sales tabele from the database, bring them to python, and output them on the Python Terminal
# def get_sales():
#     cur.execute("select * from sales")
#     sales_data=cur.fetchall()
#     return  sales_data
# sales_data=get_sales()
# print(sales_data)



# # # Function to insert data into sales table in the Database
# def insert_sales(sales_data):
#     cur.execute("insert into sales (pid, quantity) values(%s, %s)",sales_data)
#     conn.commit()

# sale1=(1,5)
# sale2=(2,7)
# sale3=(3,4)
# sale3=(4, 10)
# insert_sales(sale1)
# insert_sales(sale2)
# insert_sales(sale3)


# sales_data=get_sales()
# print(sales_data)



#  Function for inserting into the stocks table on my SQL Database
# def get_stock():
#     cur.execute("select * from stock")
#     stock_data=cur.fetchall()
#     return stock_data
# stock_data= get_stock()
# print(stock_data)


# def insert_stock(stock_details):
#     cur.execute("insert into stock(pid, stock_quantity) values (%s,%s)",stock_details)
#     conn.commit()

# stock1=(1, 40)
# stock2=(2,50)
# stock3=(3, 20)

# insert_stock(stock1)
# insert_stock(stock2)
# insert_stock(stock3)

# stock_data= get_stock()
# print(stock_data)


#  A function that computes sales per day

def get_sales_per_day ():

    cur.execute("select sum(products.selling_price*sales.quantity) as sales_per_day from products left join sales on products.id = sales.pid")

    sales_per_day= cur.fetchall()

    return sales_per_day


sales_per_day=get_sales_per_day()
print(sales_per_day)





# A function that calculates profit per product

def get_profit_per_product():
    cur.execute("select products.name as  p_name, sum(products.selling_price-products.buying_price) as profit_per_product from products group by p_name")
    profit_per_product=cur.fetchall()

    return profit_per_product

profit_per_product=get_profit_per_product()
print(profit_per_product)



# A function that computes the profit per day


def get_profit_day():
    cur.execute("select sum(products.selling_price - products.buying_price) as profit_per_day from products")
    profit_per_day=cur.fetchall()
    return profit_per_day

profit_per_day=get_profit_day()
print(profit_per_day)














# sales_day

# select  sum(products.selling_price*sales.quantity) as sales_per_day from products left join sales on products.id = sales.pid


# profit per day
# select products.name as  p_name, sum(products.selling_price-products.buying_price) as profit_per_day from products group by p_name;

# profit per day

# select sum(products.selling_price - products.buying_price) as profit_per_day from products;