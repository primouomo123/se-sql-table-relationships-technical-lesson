import sqlite3
import pandas as pd
conn = sqlite3.connect('data.sqlite')

# Get the first name, last name, and email of all employees whose job title is 'Sales Rep'.
print('\n')
q = """
SELECT firstName, lastName, email
FROM employees
WHERE jobTitle = 'Sales Rep'
;
"""
df = pd.read_sql(q, conn)
print("Number of results:", len(df))
print('\n')
print(df.head())
print('\n')


# Get the first name, last name, email, and city of all employees whose job title is 'Sales Rep'.
q = """
SELECT firstName, lastName, email, city
FROM employees
JOIN offices
   USING(officeCode)
WHERE jobTitle = 'Sales Rep'
;
"""
df = pd.read_sql(q, conn)
print("Number of results:", len(df))
print('\n')
print(df.head())
print('\n')


# Get the product line and text description of all product lines.
q = """
SELECT productLine, textDescription
FROM productlines
;
"""
df = pd.read_sql(q, conn)
print("Number of results:", len(df))
print('\n')
print(df)
print('\n')


# Get the product line, text description, product vendor, and product description of all products.
q = """
SELECT productLine, textDescription, productVendor, productDescription
FROM productlines
JOIN products
    USING(productLine)
;
"""
df = pd.read_sql(q, conn)
print("Number of results:", len(df))
print('\n')
print(df.head())
print('\n')


# Get all columns for all offices.
q = """
SELECT *
FROM offices
;
"""
df = pd.read_sql(q, conn)
print('Number of results:', len(df))
print('\n')


# Get all columns for all customers.
q = """
SELECT *
FROM customers
;
"""
df = pd.read_sql(q, conn)
print('Number of results:', len(df))
print('\n')


# Get all columns for all offices and customers where the state is the same.
q = """
SELECT *
FROM offices
JOIN customers
    USING(state)
;
"""
df = pd.read_sql(q, conn)
print('Number of results:', len(df))
print('\n')
print(df.head())
print('\n')


conn.close()