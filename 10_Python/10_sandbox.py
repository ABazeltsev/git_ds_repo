import pandas as pd
#--------------------------------------------------------------2.4
names=['chlorhexidine', 'cyntomycin', 'afobazol']
counts=[15, 18, 7]
def create_medications(names, counts):
    result = pd.Series(
    data = counts,
    index = names#,
    #name = 'meds'
    )
    return result
medications = create_medications(names, counts)
#print(medications)

def get_percent(meds, name):
    result = (meds.loc[name]/sum(meds))*100
    return result
med_cnt = get_percent(medications, 'afobazol')
#print(med_cnt)
#--------------------------------------------------------------2.4

countries_df = pd.DataFrame({
    'country': ['Англия', 'Канада', 'США', 'Россия', 'Украина', 'Беларусь', 'Казахстан'],
    'population': [56.29, 38.05, 322.28, 146.24, 45.5, 9.5, 17.04],
    'square': [133396, 9984670, 9826630, 17125191, 603628, 207600, 2724902],
    'boolean':[0, 0, 0, 0, 0, 0, 1]
}
)
ind = 0
#print(countries_df.loc[ind])

#--------------------------------------------------------------3.5
income = [478, 512, 196]
expenses = [156, 130, 270]
years = [2018, 2019, 2020]

def create_companyDF(inc, exp, yrs):
    result = pd.DataFrame(
        {
        'Income':inc,
        'Expenses':exp
        },
        index=yrs        
    )
    return result
#print(create_companyDF(income, expenses, years))

def get_profit(df, yr):
    if yr in df.index:
        profit = df.loc[yr, 'Income'] - df.loc[yr, 'Expenses']
        return profit
    else: return None
    
get_profit(create_companyDF(income, expenses, years), 2018)

countries_df.to_csv(path_or_buf='10_Python/data/cntrs.csv', index='False', sep=';')

#--------------------------------------------------------------11.2.3
customer_df = pd.DataFrame({
            'number': [0, 1, 2, 3, 4],
            'cust_id': [128, 1201, 9832, 4392, 7472],
            'cust_age': [13, 21, 19, 21, 60],
            'cust_sale': [0, 0, 0.2, 0.15, 0.3],
            'cust_year_birth': [2008, 2000, 2002, 2000, 1961],
            'cust_order': [1400, 14142, 900, 1240, 8430]
        })
def delete_columns(df, col=[]):
    for cc in col:
        if cc not in df.columns:
            return None
    df.drop(col, axis=1, inplace=True)
    return df
#print(delete_columns(customer_df, ['number', 'cust_year_birth', 'err']))
#--------------------------------------------------------------11.2.3
#melb_df.drop(['index', 'Coordinates'], axis=1, inplace=True)

#--------------------------------------------------------------11.2.4
countries_df = pd.DataFrame({
    'country': ['Англия', 'Канада', 'США', 'Россия', 'Украина', 'Беларусь', 'Казахстан'],
    'population': [56.29, 38.05, 322.28, 146.24, 45.5, 9.5, 17.04],
    'square': [133396, 9984670, 9826630, 17125191, 603628, 207600, 2724902]
})
men_per_mile = 1000000*countries_df['population'] / countries_df['square']
print(men_per_mile.mean())
#--------------------------------------------------------------11.2.4
