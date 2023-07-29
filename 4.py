import ds_operations

#seta&setb #check if dictionaries are equal#group anagrams#subarray with maximum sum#bidirectional search

dso = ds_operations.DSOperations()
def nextsublists(t=(1,2,3)):
    sublists = []
    for i in range(len(t)+1):    
        for j in range(1,len(t)+1):
            print(i,j)
            #if j>i:
            #sublists.extend(t[i:j]) [[1, 1, 2, 2], [1, 1, 2, 2], [1, 1, 2, 2], [1, 1, 2, 2], [1, 1, 2, 2], [1, 1, 2, 2]]
            sublists.append(t[i:j])
            yield sublists

l = iter(nextsublists())    #now you can do next(l) to see items one by one, useful when you want to see how a loop is running        


l = [temperature for temperature     
