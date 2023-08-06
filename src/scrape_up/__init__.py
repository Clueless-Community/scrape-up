import pandas
df = pandas.DataFrame(list_rest)
df.to_csv("zomato_res.csv",index=False)
_all_=["zomato"]