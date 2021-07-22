import pandas as pd

a = {
    "a":1,
    "b":2
}
g=pd.Series(data=a,index=["a","b"])
print(g)