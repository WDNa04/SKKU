birth = float(input('Birthday: '))
year = birth//10000
month = birth%10000//100
day = birth%100
print('Year - Month - Day: %0.3f'%((year-month-day)))
print('Year * Month - Day: %0.3f'%((year*month-day)))
print('(Year + Month) / Day: %0.3f'%(((year+month)/day)))
print('Year - Month * Day: %0.3f'%((year-month*day)))
