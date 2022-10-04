import pandas as pd

squirrel_data = pd.read_csv("squirrel_data.csv")
squirrel_data = squirrel_data.rename(columns={'Primary Fur Color': 'fur_color'})
print(squirrel_data.fur_color.value_counts().reset_index())
# print(squirrel_data.groupby('fur_color').fur_color.count())

fur_color = pd.DataFrame(squirrel_data.fur_color.value_counts()).reset_index()
fur_color = fur_color.rename(columns={"index":"Fur Color", "fur_color":"Count"})
fur_color.to_csv("fur_color.csv")

