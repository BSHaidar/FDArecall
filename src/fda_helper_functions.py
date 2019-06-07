# import libraries
import pandas as pd
from datetime import datetime
import json
from statsmodels.stats.proportion import proportions_ztest
import matplotlib.pyplot as plt
import sqlite3


def setup_load():
    ''' Setup display options
        Load dataset in dataframe
        Drop uneeded columns
        Convert to csv'''
    #Set max columns and rows
    pd.set_option('display.max_columns',30)
    pd.set_option('display.max_rows',1000)

    #Open and load JSON file
    f=open('/Users/bhaidar/Desktop/food-enforcement-0001-of-0001.json', 'r')
    data=json.load(f)
    #Create dataframe
    df = pd.DataFrame(fda_dict)
    #Drop unwanted columns
    df.drop(['more_code_info'],axis=1,inplace=True)
    df.drop(['openfda'], axis=1, inplace=True)
    #Create csv file from dataframe
    df.to_csv('FDArecall.csv', index=False)

def sql_connect_query():
    '''Connect to SQL database and select relevant columns'''
    #Assign q with the sql query with the needed columns
    q="""SELECT event_id, recall_number, classification, recall_initiation_date, state, country, voluntary_mandated
        FROM fdarecall
        WHERE country='United States'
        ;"""
    #Connect to the sqlite database
    conn = sqlite3.connect('fdarecall.db')
    #Create dataframe by executing the sql query
    df = pd.read_sql_query(q, conn)
    return df

def states_won_clinton():
    '''Get states won by Hillary Clinton in the 2016 Presidential Elections'''
    # Assign blue_states with the states won by Hillary Clinton in the 2016 Presidential Elections
    blue_states = (['WA', 'OR', 'CA', 'NV', 'CO', 'NM', 'MN', 'IL', 'VA', 'MD',
    'NJ', 'CT', 'MA', 'NY', 'DE', 'VT', 'NH', 'ME', 'HI', 'RI'])
    return blue_states

def feature_engineering(df, blue_states):
    #Assign 0 to red_states if state was won by Clinton and 1 if state was won by Trump
    df['red_states'] = [0 if state in blue_states else 1 for state in df.state]
    #Assign date from recall_initiation_date to initiation_date
    df['initiation_date'] = [datetime.strptime(str(i),'%Y%m%d').date() for i in df.recall_initiation_date]
    #Assingn 1 to Class-1 if it is equal to Class I otherwise(meaning Class II or Class III) assign 0
    df['Class_1'] = [1 if c == 'Class I' else 0 for c in df.classification]
    #Create FDA_initiated columns and assingn 0 if it is voluntary otherwise assign 1 if it was FDA mandated
    df['FDA_initiated'] = [0 if i == 'Voluntary: Firm Initiated' else 1 for i in df.voluntary_mandated]
    #Slice off the first 4 characters (the year) of recall_initiation_date and assign it to initiation_year
    df['initiation_year'] = [str(i)[:4] for i in df.recall_initiation_date]
    #Drop rows with years not needed for hypothesis tesing
    df = (df.drop(df[(df.initiation_year == '2008') | (df.initiation_year == '2009') | (df.initiation_year == '2010')
    | (df.initiation_year == '2011') | (df.initiation_year == '2121')].index, inplace=True))


def set_df_mask(df):
    '''Create two dataframes with a 2 year window for pre-Trump election
    and post-Trump election. set_df_mask(df) takes a dataframe as an argument'''
    pre_trump = (df[(df['country'] == 'United States')
                       & (df['initiation_date'] >= datetime.strptime('20150120','%Y%m%d').date())
                       & (df['initiation_date'] < datetime.strptime('20170120','%Y%m%d').date())])
    post_trump = (df[(df['country'] == 'United States')
                       & (df['initiation_date'] >= datetime.strptime('20170120','%Y%m%d').date())
                       & (df['initiation_date'] < datetime.strptime('20190120','%Y%m%d').date())])
    return pre_trump, post_trump

def set_df_new_mask(df1, df2):
    '''Create 4 dataframes:
    pre_trump_class_1: 2 years pre-Trump election with FDA recall Class I severity
    post_trump_class_1: 2 years post-Trump election with FDA recall Class I severity
    pre_trump_vol: 2 years pre-Trump election with FDA voluntatry recall
    post_trump_vol: 2 years post-Trump election with FDA mandatory recall
    set_df_new_mask(df1, df2) takes two dataframes as arguments'''
    #Create datafrane by Class I severity filter 2 years prior to the 2016 Presidential Elections
    pre_trump_class_1 = df1[df1['Class_1'] == 1]
    #Create datafrane by Class I severity filter 2 years post the 2016 Presidential Elections
    post_trump_class_1 = df2[df2['Class_1'] == 1]
    #Create datafrane by non-FDA mandate 2 years prior to the 2016 Presidential Elections
    pre_trump_vol = df1[df1['FDA_initiated'] == 0]
    #Create datafrane by non-FDA mandate 2 years post the 2016 Presidential Elections
    post_trump_vol = df2[df2['FDA_initiated'] == 0]
    return pre_trump_class_1, post_trump_class_1, pre_trump_vol, post_trump_vol

def plot_recalls(df, col1, col2, title, ylim=0):
    ''' Plot 2 variables based on proportion'''
    df_plot = df.groupby([col1]).sum()[col2]
    df_plot_total=df[col1].value_counts()
    df_plot=pd.concat([df_plot,df_plot_total],axis=1)
    # df_plot.drop(drop_years, inplace=True)
    df_plot['year']= df_plot.index
    plt.figure(figsize=(10,8))
    plt.ylim(ylim)
    plt.title(title, fontsize=14)
    plt.xlabel('Years', fontsize=12)
    plt.ylabel('Proportion', fontsize=12)
    plt.plot(df_plot.index, df_plot[col2]/df_plot[col1]);

def plot_red_blue_states_recalls(df, col1, col2):
    df_plot3 = df[df.Class_1==1].groupby([col1]).sum()[col2]
    df_plot3_total=df[df.Class_1==1][col1].value_counts()
    df_plot3=pd.concat([df_plot3,df_plot3_total],axis=1)
    df_plot3['percentage']= df_plot3[col2]/df_plot3[col1]
    df_plot3['blue_state_per'] = 1-df_plot3[col2]/df_plot3[col1]
    df_plot3['year']= df_plot3.index


     #plt.xlim(2012,2018)
    plt.figure(figsize=(10,8))
    plt.ylim(0)
    plt.title("Proportion of Class 1 Recalls in Red and Blue States", fontsize=14)
    plt.xlabel('Years', fontsize=12)
    plt.ylabel('Proportion', fontsize=12)
    # df_plot3.drop(['2008','2009','2010','2011', '2121'], inplace=True)
    plt.plot(df_plot3['year'], df_plot3['percentage'], label='Red States', color='red')
    plt.plot(df_plot3['year'], df_plot3['blue_state_per'], label='Blue States', color='blue')
    plt.legend()
    plt.show();

def get_ztest(data1,data2, g_var,hyp_type):
    '''Get the z_test and p_values scores'''
    c1 = data1[data1[g_var]==1][g_var].sum()
    c2 = data2[data2[g_var]==1][g_var].sum()
    count = [c1,c2]
    nobs = [len(data1), len(data2)]
    stat,pval = proportions_ztest(count,nobs,value=0,alternative=hyp_type)
    print('p-value: {0:0.3f}'.format(pval))
    print('z-statistic: {}'.format(round(stat,2)))
