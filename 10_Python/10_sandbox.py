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
