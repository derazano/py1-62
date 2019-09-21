import csv
data = [['a','b','c',],['d','e','f'],['Shingeki no kyojin','Vinland saga','Kore ga sombie desu ka']]
ff = open("sameple.csv",'w')
writefcsv = csv.writer(ff)
writefcsv.writerows(data)
ff.close()
