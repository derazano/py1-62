sports = {1:'Football',2:'Tennis',3:'Basketball'}

print("The original sport table",sports)
sports.update({4:"Badminton"})
sports.update({1:"Racing"})
sports.update({3:"Basketball"})

print("The new sport table")

for key,s in sports.items():
    print("   ",key ,")", s)
