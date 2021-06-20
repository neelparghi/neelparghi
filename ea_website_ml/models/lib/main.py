"""
Base code without class and function
"""
import sys
import psycopg2
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn import tree

param_dic = {
    "host"      : "127.0.0.1",
    "database"  : "test",
    "user"      : "odoo",
    "password"  : "odoo",
    "port"      : "8070",
}


def connect(param_dic):
    conn = None
    try:
        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(**param_dic)
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        sys.exit(1)
    print("Connection successful")
    return conn


def postgresql_to_dataframe(conn, select_query, column_names):
    cursor = conn.cursor()
    try:
        cursor.execute(select_query)
    except (Exception, psycopg2.DatabaseError) as error:
        print("Error: %s" % error)
        # cursor.close()
        # return 1

    # Naturally we get a list of tupples
    tupples = cursor.fetchall()
    # cursor.close()

    # We just need to turn it into a pandas dataframe
    df = pd.DataFrame(tupples, columns=column_names)
    return df


# Connect to the database
conn = connect(param_dic)

column_names = ["mlwebsite_category", "mlwebsite_subcategory", "mlwebsite_navbar", "selected_theme"]
# Execute the "SELECT *" query
df = postgresql_to_dataframe(conn, "select mlwebsite_category,mlwebsite_subcategory,mlwebsite_navbar,selected_theme from mldata", column_names)
d=df.head()
print(d)

inputs = df.drop('selected_theme', axis='columns')
target = df['selected_theme']

le_MainCat = LabelEncoder()
le_Category = LabelEncoder()
le_Subcat = LabelEncoder()

inputs['Maincat_n'] = le_MainCat.fit_transform(inputs['mlwebsite_category'])
inputs['Category_n'] = le_Category.fit_transform(inputs['mlwebsite_subcategory'])
inputs['Subcat_n'] = le_Subcat.fit_transform(inputs['mlwebsite_navbar'])
inputs.head()

inputs_n = inputs.drop(['mlwebsite_category', 'mlwebsite_subcategory', 'mlwebsite_navbar'], axis="columns")
print(inputs_n)

model = tree.DecisionTreeClassifier()
model.fit(inputs_n, target)

model.score(inputs_n, target)
theme_input = [int(input("Enter Main Category:")), int(input("Enter sub_Category:")), int(input("Enter NavBar option:"))]
result_theme = model.predict([theme_input])
print(result_theme)
