score=list(map(int,input("Enter the scores: ").split()))
min=score[0]
max=score[0]
min_count=0
max_count=0
for i in range(1,len(score)):
    if min<score[i]:
        min=score[i]
        min_count+=1
    elif max>score[i]:
        max=score[i]
        max_count+=1
print(min_count,min)
print(max_count,max)

                    