'''
file has below dataset:
no,name,age,sal
1,swapnil,28,3000
2,nmv,40,12321
3,dsadsa,30,31313
4,dasd,10,111
5,sasa,30,12412412'''

''' generate file having top 3 salary '''
''' output should be
no,name,age,sal
2,nmv,40,12321
3,dsadsa,30,31313
5,sasa,30,12412412 '''

import pandas as pd

def main():
    df = pd.read_csv("/Users/swbh/Downloads/google_File.csv")
    #df_first_col = df.iloc[:,0]
    #print(df_first_col)
    df_last_column = sorted(df.iloc[:,-1],reverse=True)
    df_top_3 = df_last_column[:3]
    print(df)
    print(df_last_column)
    print(df_top_3)
    get_min_sal = min(df_top_3)
    print(get_min_sal)
    df1 = df[df.sal.isin(df_top_3)]
    print(df1)
    
    #print data in sorted form of Salary:
    print(df1.sortlevel(df1.sal,ascending=False))





if __name__ == "__main__":
    main();
