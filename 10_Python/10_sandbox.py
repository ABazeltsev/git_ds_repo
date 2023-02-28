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