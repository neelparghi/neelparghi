import sys
import psycopg2 as ps
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn import tree
import logging
_logger = logging.getLogger(__name__)

column_names = ["mlwebsite_category", "mlwebsite_subcategory", "mlwebsite_navbar", "selected_theme"]
class Connection:
    df = None
    
    def setMlData(self,data_list):
        self.df = pd.DataFrame(data_list, columns=column_names)
        # return df
    def predict_theme(self, mlwebsite_category, mlwebsite_subcategory, mlwebsite_navbar):
        # Connect to the database
        
        d = self.df.head()
        print(d)
        inputs = self.df.drop('selected_theme', axis='columns')
        target = self.df['selected_theme']
        le_MainCat = LabelEncoder()
        le_Category = LabelEncoder()
        le_Subcat = LabelEncoder()
        inputs['Maincat_n'] = le_MainCat.fit_transform(inputs['mlwebsite_category'])
        inputs['Category_n'] = le_Category.fit_transform(inputs['mlwebsite_subcategory'])
        inputs['Subcat_n'] = le_Subcat.fit_transform(inputs['mlwebsite_navbar'])
        inputs.head()
        inputs_n = inputs.drop(['mlwebsite_category', 'mlwebsite_subcategory', 'mlwebsite_navbar'], axis="columns")
        _logger.info(inputs_n)
        model = tree.DecisionTreeClassifier()
        model.fit(inputs_n, target)
        _logger.info(model.score(inputs_n, target))
        
        theme_input = [mlwebsite_category, mlwebsite_subcategory, mlwebsite_navbar]
        result_theme = model.predict([theme_input])
        _logger.info(result_theme)
        
        return result_theme