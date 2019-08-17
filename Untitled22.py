import pandas as pd
df1 = pd.read_excel('denemeler-1.xlsx')
df2 = pd.read_excel('notalar_ve_freq_comma.xlsx')

results = df1.merge(df2, on='Koma53')
sort_by_time = results.sort_values('Sira')
pd.DataFrame(sort_by_time).to_excel('denemeler-12.xlsx')

directory = input("Path to directory: ")
files_dir =  os.listdir(directory)
newlist = []
for names in files_dir:
    if names.endswith(".xlsx"):
        newlist.append(names)
print(newlist)



