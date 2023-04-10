import pandas as pd
import matplotlib.pyplot as plt

# Generate random data for fungal genus relative abundance
sites =['Site 1','Site 2','Site 3','Site 4','Site 5','Site 6','Site 7','Site 8','Site 9','Site 10']
depths = ['Depth 1:0-10cm', 'Depth 2:10-20cm', 'Depth 3:20-30cm', 'Depth 4:30-40cm']

genera = ['Aspergillus','Penicillium','Trichoderma','Fusarium','Mucor','Rhizopus','Mortierella','Beauveria','Verticillium','Alternaria']
#load data
abundance = pd.read_csv('abundance.csv', header=0).values # header = None if there is no header
# normalize abundance to sum up to 1 for each depth level
abundance = (abundance.T / abundance.sum(axis=1)).T

# Create a pandas dataframe from the data
df = pd.DataFrame(abundance, index=pd.MultiIndex.from_product([depths, sites], names=['Depth', 'Site']), columns=genera)

# Plot stackbar chart with four subplots, one for each depth level
fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(12, 8))
for i, ax in enumerate(axes.flat):
    sub_df = df.loc[depths[i], :]
    sub_df.plot(kind='bar', stacked=True, ax=ax, width=0.9)
    ax.set_title(depths[i])
    ax.set_xlabel('Site')
    ax.set_ylabel('Relative Abundance (%)')
    ax.legend(title='Genus', bbox_to_anchor=(1.01, 1), loc='upper left')

plt.tight_layout()
plt.show()
