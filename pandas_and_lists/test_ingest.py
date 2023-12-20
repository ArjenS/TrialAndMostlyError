import pandas as pd


salt_dict = {"date": "2023-12-20", "salt": "2f6afe25bbca95bf4f6b971b73c1a484"}
salt_df = pd.DataFrame(salt_dict.values(), columns=['date','salt'])

print(salt_dict["date"])
print(salt_df)


