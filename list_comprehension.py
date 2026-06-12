words='python example programming leetocde'.split()
print(words)
stuff=map(lambda w:[w.upper(),w.lower(),len(w)],words)
for i in stuff:
    print(i)

print("Second code:")
sem1=['english','maths','science','chemistry']
sem2=['science','physics','maths','social']
s1=set(sem1)
s2=set(sem2)
s3=s1.intersection(s2)
common=list(s3)
print(common)
