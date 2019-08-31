month = input("Input the name of Month : ")
M_31 = ['January','March','May','July','August','October','December']
M_30 = ['April','June','September','November']

if(month in M_31):
    print("No. of days: 31 days" )
elif(month in M_30):
    print("No. of days: 30 days")
elif(month == 'February'):
    print("No. of days: 28/29 days")
else:
    print("not a month")
