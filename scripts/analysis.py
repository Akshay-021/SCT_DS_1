import pandas as pd
import matplotlib.pyplot as plt

population = pd.read_csv(r"D:\SCT_DS_1\data\raw\API_SP.POP.TOTL_DS2_en_csv_v2_1122588.csv", skiprows=4)
country=pd.read_csv(r"D:\SCT_DS_1\data\raw\Metadata_Country_API_SP.POP.TOTL_DS2_en_csv_v2_1122588.csv")

population=population[['Country Name', 'Country Code', '2020']]
merged=pd.merge(population, country, left_on='Country Name', right_on='TableName')
region_pop = merged.groupby('Region')['2020'].sum().sort_values(ascending=False)

plt.figure(figsize=(10, 6))
region_pop.plot(kind='bar', color='skyblue', edgecolor='black')
plt.xlabel('Region')
plt.ylabel('Total Population (2020)')
plt.title('Total Population by Region in 2020')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
