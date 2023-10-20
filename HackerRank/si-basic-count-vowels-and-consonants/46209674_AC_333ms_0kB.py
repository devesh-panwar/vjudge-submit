st=input()
#st.lower()
#l=list(st)
# vo=['a','e','i','o','u']
vowel=0
con=0
for x in st:
    if(x=='a' or x=='e' or x=='i' or x=='o' or x=='u' or x=='A' or x=='E' or x=='I' or x=='O' or x=='U'):
        vowel+=1
    else:
        con+=1
print(vowel,con)