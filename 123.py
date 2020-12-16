Python 03.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927
64 bit (AMD64)] on win32 Type "help", "copyright", "credits" or
"license()" for more information. >>> print('The price of one kg rice is
    Rs 16.75') printe('The price of one kg sugar is Rs 15')
rice_amount=float(input('write the amount of rice you want in kg:'))
sugar_amont=float(input('write the amount of sugar you want in kg:'))
rice_price = rice_amount*16.75 sugae_price = sugar_amount*15 total_bill
= rice_price+sugar_price print('Item  Price  Qty  Total')
print('__________________________________') print('rice  16.75  %.2f
%.2f'%(rice_amount,rice_price)) print('sugar  15  %.2f
%.2f'%(sugar_amount,sugar_price)) print('total bill = %.2f'%total_bill')
