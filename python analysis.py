import pandas as pd
import  numpy as np

raw_data = {
    'Order_ID':[101,102,103,104,105,106],
    'Customer':  ['ahmed','mona','ali','sara','omr','sama'],
    'Product':['LAPTOP','PHONE','WATCH','HEADPHONES','TABLET','PHONE'],
    'Price':[45000,10000,2000,1000,10000,1000],
    'Quantity':[2,1,3,1,1,1],
    'City':['cairo','giza','cairo','giza','giza','cairo'],
}
df = pd.DataFrame(raw_data)
print("---البيانات الخام قبل التنظيف---")
print(df)
print("\n"+'='*40 +'\n')

df = df.drop_duplicates()

df['Price'] = df['Price'].fillna(df['Price'].median())

df['Price'] = df['Price'].abs()

df['total_sales'] =  df['Price'] * df['Quantity']
print("--البينات بعد التنظيف وايضافه جمالي المبيعات--")
print(df)
print("\n"+'='*40 +'\n')


print("---اجمالي المبيعات حسب المدينه---")
City_sales= df.groupby('City')['total_sales'].sum()

print('City_sales')


input(" Enter close")