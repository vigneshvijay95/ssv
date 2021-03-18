import pandas
df = pandas.read_csv('vignesh1.txt')
index_col='Employee name',
header = 0,
Name = ['Employee name']
df.to_csv('vignesh3.txt')
print(df)

