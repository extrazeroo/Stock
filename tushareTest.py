import tushare as ts
import pandas as pd
import numpy as np

#np.random.randint(1,9,size=(2,3))
#df1 = pd.DataFrame(np.random.randn(3,3), index = list('ABC'), columns=list('msn'))
df = ts.get_today_all()
print(df.values[0])