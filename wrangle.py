# For visualization
import matplotlib.pyplot as plt
import seaborn as sns

# Standar imports
import numpy as np
import pandas as pd

from datetime import datetime

from env import user, password, host

from sklearn import metrics

#------------------------------------------------------

##-- Functions --##
query = '''
select * from cohorts 
'''

def get_db_url(user, host, password, database):
    '''This function acquires data from the Codeup MYSQL server while using the credentials from env.py'''
    url = f'mysql+pymysql://{user}:{password}@{host}/{database}'
    return url


def ds_pop(df):
    ''' This function prints the top 10 pages all Data Science cohort visit'''  
    for pro in df.program_id.value_counts().index.sort_values():
        print(f'Program: {pro}')
        # Printing the 10 most visited pages by all Data Science Cohorts
        print(df[df.program_id == 3][['program_id','page']].groupby('page').count().sort_values('program_id', ascending=False).head(10))
        print('---')
    
def most_pop(df):
    ''' This function prints all program types and the top 10 pages they visit'''
    for pro in df.program_id.value_counts().index.sort_values():
        print(f'Program: {pro}')
        # Printing the 10 most visited pages by program
        print(df[df.program_id == pro][['program_id','page']].groupby('page').count().sort_values('program_id', ascending=False).head(10))
        print('---')
        
def prep_cohort(df):
    # Program 1: Full-Stack Java PHP
    # Program 2: Full-Stack Java
    # Program 3: Data Science
    # Program 4: Front-End, no longer exists
    df = df.drop(columns={'deleted_at', 'slack', 'created_at','updated_at'})
    df.start_date = pd.to_datetime(df.start_date)
    df.end_date = pd.to_datetime(df.end_date)
    # Renaming id so merging is easier
    df = df.rename(columns={'id':'cohort'})
    return df