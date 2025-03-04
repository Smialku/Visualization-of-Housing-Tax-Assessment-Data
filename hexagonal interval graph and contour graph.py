import matplotlib.pyplot as plt
import pandas as pd
from scipy.stats import alpha
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
#plt.show()

ax = sb.kdeplot(x = kc_sample.SqFtTotLiving, y = kc_sample.TaxAssessedValue, ax=ax, bw_adjust=0.5)
plt.show()


