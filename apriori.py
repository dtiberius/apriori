# install apyori library if not already installed

!pip install apyori

# import new library and Pandas (for dataframes)

import pandas as pd
from apyori import apriori

# make a function to clean the results that apyori gives us

def clean_rules(rules):

  results = list(rules)

  li = []

  for RelationRecord in results:
    support = RelationRecord[1]
    ordered_stats = RelationRecord[2]
    for ordered_stat in ordered_stats:
      li.append([set(ordered_stat[0]), set(ordered_stat[1]), support, ordered_stat[2], ordered_stat[3]])

  df = pd.DataFrame(li, columns =['If', 'Then', 'Support', 'Confidence', 'Lift']) 
  df = df[(df.If != set())]
  
  return df

# create hypothetical list of transactions

baskets = [  
  ['beer', 'oats', 'broccoli', 'nappies'],
  ['beer', 'broccoli', 'bin bags'],
  ['bananas', 'kippers'],
  ['beer', 'bananas', 'oats', 'nappies'],
  ['bananas', 'kippers', 'broccoli', 'bin bags']
]

# use the apyori library's aprioi algorithm

rules = apriori(baskets, min_lift = 1.01)

df = clean_rules(rules)

df.sort_values(['Confidence']).head()