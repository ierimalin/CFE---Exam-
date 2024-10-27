
import os 
import pandas as pd

base_directory = "C:\\Users\\Alin\\Documents\\GitHub\\CFE---Exam-\\ierima_exam" 
#CHANGE THIS TO THE DESIRED PATH!


#5., 6. and 2. Reading the TJET data in Python and cleaning it, and subsetting/transforming data.

tjet = pd.read_csv("https://raw.githubusercontent.com/ierimalin/CFE---Exam-/main/ierima_exam/raw/tjet_cy.csv")
print(tjet.head())

#show me all the columns (I use this instead of the more simple list(tjet.columns) because it offers each variable on a different row
for column in tjet: print(column)

tjet_clean = tjet[["country", "year", "amnesties_sample", "tcs_sample"]]
tjet_clean = tjet_clean[tjet_clean["year"] == 2021]

#Using for loop again for the sake of exemplifying
tjet_clean_2021 = pd.DataFrame()
for year in tjet_clean["year"].unique():
    if year == 2021:
      tjet_clean_2021 = tjet_clean[tjet_clean["year"] == year]
      break
    else:
      tjet_clean_2021 = tjet_clean
      
#Transformation: creating a new variable
tjet_clean_2021["has_mechanisms"] = ((tjet_clean_2021["amnesties_sample"] == 1) | (tjet_clean_2021["tcs_sample"] == 1)).astype(int)
    
    
#7. saving cleaned data. 

clean_folder = os.path.join(base_directory, "clean")
tjet_clean_2021.to_csv(os.path.join(clean_folder, "tjet_clean_2021.csv"),index=False)

#3. Using lists and dictionaries
#Lists
list_countries = list(tjet_clean_2021["country"].unique())
print("This is a list of the included countries", list_countries)

#Dictionaries. This code creates an empty dictionary, which will be used to store the counts of occurences of each country. Then a loop iterates over each country and counts the occurences. All countries should only appear once.
  country_count = {}

for country in tjet_clean_2021["country"]:
    if country in country_count:
        country_count[country] += 1
    else:
        country_count[country] = 1
  
print(country_count)


#8. Creating summary statistics

print(tjet_clean_2021.describe())


#9. Create graph

import matplotlib.pyplot as plt

has_mechanisms_counts = tjet_clean_2021['has_mechanisms'].value_counts()

plt.figure(figsize=(6, 5))
has_mechanisms_counts.plot(kind='bar', color=['navy', 'red'])
plt.title('Count of Has Mechanisms (0 and 1)')
plt.xlabel('Has Mechanisms (1 = Yes, 0 = No)')
plt.ylabel('Count')
plt.xticks(rotation=0)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()

plt.savefig(os.path.join(os.path.join(base_directory, "graphs"), 'TJ mechanisms.png'), bbox_inches='tight')

