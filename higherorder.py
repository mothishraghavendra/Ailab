def count(task,lis):
    val = 0;
    n = len(lis)
    for i in range(n):
        x = lis[i]
        if task(x):
            val+= 1;
    print("Number of values higher than 2 = ",val);

lis = [1,2,3,4,5]
count(lambda x:x>2,lis)