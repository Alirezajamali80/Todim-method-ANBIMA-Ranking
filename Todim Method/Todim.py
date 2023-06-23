import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings("ignore")

# Read the Excel file and convert it into a DataFrame
df = pd.read_excel('Todim.xlsx')


# Extract the decision matrix (alternatives and criteria) & save data that we want later in vars
alternatives = df.iloc[:, 1].values.tolist()
criteria = df.columns[2:-1].tolist()
decision_matrix = df.iloc[:, 2:-1]


#Define the weights of each criterion & standardize weights
weight_df = []
weight_df = decision_matrix[['Fixed income','Stock','Multi-market','Exchange','Pension','ETF','FIDC','FIP','FII','OffShore']].sum().values
decision_matrix['weight_df'] = weight_df
decision_matrix['weight_df'] /= weight_df.sum()
decision_matrix['weight_df'].sum()



#Standardize the decision matrix
column_sums = decision_matrix.sum(axis=0).values[:]
decision_matrix.iloc[:, :] /= column_sums

# Calculate wcr
#wr = decision_matrix['weight_df'].sum()
#decision_matrix['wcr'] = decision_matrix['weight_df'] / wr

decision_matrix.rename(columns={'weight_df': 'wcr'}, inplace=True)

wcr_c = decision_matrix["wcr"]


# Calculate the dominance matrix
phi_matrix = []

theta = 1
temp = list()

for i in range(10):
    for j in range(10):
        for c in range(10):    
            P_i_c = decision_matrix.iloc[i, c]
            P_j_c = decision_matrix.iloc[j, c]
            wcr_c = decision_matrix["wcr"][c]
           # print(P_i_c,P_j_c,wcr_c)

            if P_i_c > P_j_c:
                phi_c = np.sqrt((wcr_c * (P_i_c - P_j_c)))
            elif P_i_c < P_j_c:
                phi_c = np.sqrt((-1 / theta) * (P_i_c - P_j_c) / wcr_c)
            else:
                phi_c = 0
                
            temp.append(phi_c)

            
        phi_matrix.append(temp)
        temp = list() 



delta_list = []
for k in range (100):
    delta_list.append(sum(phi_matrix[k]))
#delta_matrix = pd.DataFrame(delta_matrix)
delta_matrix = [[0] * 10 for _ in range(10)]
for i in range(10):
    for j in range(10):
        delta_matrix[j][i] = delta_list[i * 10 + j]


row_sums = []
for row in delta_matrix:
    row_sum = sum(row)
    row_sums.append(row_sum)
max_sum_rows = max(row_sums)
min_sum_rows = min(row_sums)



zeta = list()
for i in range (10):
    temp = (row_sums[i]-min_sum_rows)/(max_sum_rows - min_sum_rows)
    zeta.append(temp)

final_result = pd.DataFrame(df.iloc[:,:2])
final_result['global dominance'] = zeta


sorted_result = final_result.sort_values(by='global dominance', ascending=False)
temp = list()
for i in range (10):
    temp.append(i+1)
sorted_result['new_rank']=temp
print(sorted_result)





