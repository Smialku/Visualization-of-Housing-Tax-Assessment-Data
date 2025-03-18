import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sb

kc_tax = pd.read_csv("kc_tax.csv")

kc_tax0 = kc_tax.loc[(kc_tax.TaxAssessedValue<750000) &
                 (kc_tax.SqFtTotLiving >100)&
                 (kc_tax.SqFtTotLiving<3500), :]
kc_tax0.shape
(432693, 3)

kc_sample = kc_tax0.sample(5000, random_state=42)

ax = kc_tax0.plot.hexbin(x = 'SqFtTotLiving', y = 'TaxAssessedValue',gridsize=30,sharex=False, figsize =(5, 4))
ax.set_xlabel('House Area')
ax.set_ylabel('Tax Value')


ax = sb.kdeplot(x = kc_sample.SqFtTotLiving, y = kc_sample.TaxAssessedValue, ax=ax, bw_adjust=0.5)


zip_codes = [98188,98105,98108, 98126]
kc_tax_zip = kc_tax0.loc[kc_tax0.ZipCode.isin(zip_codes),:]
kc_tax_zip

def hexbin(x,y, color, **kwargs):
    cmap = sb.light_palette(color, as_cmap=True)
    plt.hexbin(x, y, gridsize=25, cmap=cmap, **kwargs)

g = sb.FacetGrid(kc_tax_zip, col= 'ZipCode', col_wrap=2)
g.map(hexbin, 'SqFtTotLiving','TaxAssessedValue',
      extent = [0, 3500, 0, 700000])
g.set_axis_labels('SqFtTotLiving','TaxAssessedValue')
g.set_titles('Zip code {col_name:.0f}')
plt.show()


