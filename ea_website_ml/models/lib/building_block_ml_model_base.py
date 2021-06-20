import sys
import psycopg2 as ps
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn import tree
import logging
column_names = ["mlwebsite_subcategory","pos1","pos2","pos3","pos4","pos5"]


class Buildingblocks:
    df = None

    def setMlDatasub_category(self, data_list):
        self.df = pd.DataFrame(data_list, columns=column_names)

    def predict_blocks(self,mlwebsite_subcategory):
        
        d = self.df.head()
        print(d)
        inputs = self.df.drop(['pos1', 'pos2', 'pos3', 'pos4', 'pos5'], axis='columns')
        print(inputs)
        target1 = self.df[['pos1']]
        target2 = self.df[['pos2']]
        target3 = self.df[['pos3']]
        target4 = self.df[['pos4']]
        target5 = self.df[['pos5']]
        le_Category = LabelEncoder()
        inputs['Category_n'] = le_Category.fit_transform(inputs['mlwebsite_subcategory'])
        print(inputs.head())
        inputs_n = inputs.drop('mlwebsite_subcategory', axis="columns")
        print(inputs_n)
        model1 = tree.DecisionTreeClassifier()
        model2 = tree.DecisionTreeClassifier()
        model3 = tree.DecisionTreeClassifier()
        model4 = tree.DecisionTreeClassifier()
        model5 = tree.DecisionTreeClassifier()
        model1.fit(inputs_n, target1)
        model2.fit(inputs_n, target2)
        model3.fit(inputs_n, target3)
        model4.fit(inputs_n, target4)
        model5.fit(inputs_n, target5)
        theme_input = [mlwebsite_subcategory]
        result_block1 = model1.predict([theme_input])
        result_block2 = model2.predict([theme_input])
        result_block3 = model3.predict([theme_input])
        result_block4 = model4.predict([theme_input])
        result_block5 = model5.predict([theme_input])

        return (result_block1,result_block2,result_block3,result_block4,result_block5)