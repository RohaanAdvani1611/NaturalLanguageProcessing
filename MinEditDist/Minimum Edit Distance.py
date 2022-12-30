import pandas as pd
import warnings
warnings.filterwarnings("ignore")


def editDistance(str1, str2, m, n):
    if m == 0:
        return n
    if n == 0:
        return m
    if str1[m - 1] == str2[n - 1]:
        return editDistance(str1, str2, m - 1, n - 1)
    return 1 + min(editDistance(str1, str2, m, n-1), editDistance(str1, str2, m-1, n), editDistance(str1, str2, m-1, n-1))


df = pd.read_csv('dict.csv')
print('ENTER WORD:')
ip = input()
if ip != '':
    df['ED'] = 0
    for i in range(df.shape[0]):
        df['ED'][i] = editDistance(ip, df['Words'][i], len(ip), len(df['Words'][i]))
    result = []
    med = min(df['ED'])
    for i in range(df.shape[0]):
        if df['ED'][i] == med:
            result.append(df['Words'][i])
    print(result)
else:
    print('Empty String')
    exit(0)
