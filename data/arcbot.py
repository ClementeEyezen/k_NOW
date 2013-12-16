###############################################################
# Test class for python code
# the arcbot looks at nothing, as is just a test class/library
# for academic interest of sorts, it has an implementation of
#   quicksort
# it also has implementations of binary search and a different
#   type of sort that has a name I'm forgetting that is better
###############################################################

import random
import time

def main():
    #the method called if arcbot is run on its own
    test1()
    exit()
#    print "not doing nothing, lol"
def test1():
    pass


def test():
    #a method for quickly testing code
#    print local_binarysearch(simple_test_quicksort(True),7,0,10)
    print "starting sort"
    sorttime = time.time()*1000
    testsize = 10000
    list_test = test_quicksort(testsize)
#    list_test = [0,1,2,3,4,5,6,7,8,9,10]
    print "quicksort ran "
    index = random.randint(0,testsize)
    target = list_test[index]
    print "target = "+str(target)
    print "index  = "+str(index)
    timestart_w = time.time()*1000
    print weighted_binarysearch(list_test,target,0,testsize)
    timeend_w = time.time()*1000-timestart_w
    timestart_b = time.time()*1000
    print local_binarysearch(list_test,target,0,testsize)
    timeend_b = time.time()*1000-timestart_w
    print "expected = "+str(index)
    print "Bsearch time = "+str(timeend_b)+" ms"
    print "Wsearch time = "+str(timeend_w)+" ms"
    print "sort time =   "+str(timestart_w-sorttime)+" ms"
    
    

def test_quicksort(list_size=100):
    simple_test_quicksort(False)
    start_time = time.time()
    i=0
    global test_list
    test_list = []
    while (i < list_size):
        test_list.append(random.random()*list_size*list_size//1)
        i = i+1
#    print "pre-sort :"+str(test_list)
    end_value = len(test_list)
    local_quicksort(test_list,0,end_value)
#    print "post-sort:"+str(test_list)
    print "run time " + str((time.time()*1000-start_time*1000))
    return test_list
    
    
    
def simple_test_quicksort(print_results):
    #generate a random list of integers, and have quicksort test it
    if print_results:
        print "quicksort is running a self check"
    i=0
    global test_list
    test_list = [7,4,1,5,9,3,8,2,0,6]
#    while (i < 10):
#        test_list.append(random.random()*100//1)
#        i = i+1
    if print_results:
        print "0 "+str(test_list)
    end_value = len(test_list)
    local_quicksort(test_list,0,end_value)
    if print_results:
        print "1 "+str(test_list)
        return test_list
    i=0
    while (i <10):
        if test_list[i]!=i:
            print "ERROR in QUICKSORT"
        i=i+1
    
def local_binarysearch(list,target,start_index,end_index):
    #a binary search algorithm
    list_length = min(len(list),end_index-start_index)
    list_length = max(0,list_length)
    if list_length < 2:
        print "testing index "+str(start_index)
        if list[start_index]==target:
            return start_index
        else:
            return -1

    elif list_length == 2:
        print "testing index "+str(start_index)+","+str(end_index)
        if list[start_index]==target:
            return start_index
        elif list[end_index-1]==target:
            return end_index-1
        else:
            return -1
#        print list
    else:
        pivot_index = list_length//2+start_index
        print "pivot_index = "+str(pivot_index)
        pivot_value = list[pivot_index]
        print "pivot value = "+str(pivot_value)
        if pivot_value==target:
            print "pivot value is a match"
            return pivot_index
        elif pivot_value>target:
            print "pivot "+str(pivot_value)+" greater than target"
            return local_binarysearch(list,target,start_index,pivot_index)
        else:
            print "pivot "+str(pivot_value)+" less than target"
            return local_binarysearch(list,target,pivot_index+1,end_index)
    
def weighted_binarysearch(list,target,start_index,end_index):
    #a binary search algorithm
    list_length = min(len(list),end_index-start_index)
    list_length = max(0,list_length)
    if list_length < 2:
        print "testing index "+str(start_index)
        if list[start_index]==target:
            return start_index
        else:
            return -1

    elif list_length == 2:
        print "testing index "+str(start_index)+","+str(end_index)
        if list[start_index]==target:
            return start_index
        elif list[end_index-1]==target:
            return end_index-1
        else:
            return -1
#        print list
    else:
        slope = (list[end_index-1]-list[start_index])/(end_index-start_index)+1
        print "slope "+str(slope)
        pivot_index = int(round((target-list[start_index])/slope))+start_index
        print "pivot_index = "+str(pivot_index)
        pivot_value = list[pivot_index]
        print "pivot value = "+str(pivot_value)
        if pivot_value==target:
            print "pivot value is a match"
            return pivot_index
        elif pivot_value>target:
            print "pivot "+str(pivot_value)+" greater than target"
            print list[start_index:pivot_index]
            return weighted_binarysearch(list,target,start_index,pivot_index)
        else:
            print "pivot "+str(pivot_value)+" less than target"
            print list[pivot_index+1:end_index]
            return weighted_binarysearch(list,target,pivot_index+1,end_index)

    
    
def local_quicksort(list,start_index,end_index):
    #run a quicksort on the list
#    print "accepted list"
#    print "starting at:"+str(start_index)
#    print "end at:     "+str(end_index) 
#    print list
    list_length = min(len(list),end_index-start_index)
    list_length = max(0,list_length)
#    print "list length "+str(list_length)
    if list_length < 2:
        #do nothing
        a=1
    elif list_length == 2:
#        print "list length at 2"
        if list[start_index]>list[end_index-1]:
            list.insert(start_index,list.pop(end_index-1))
#        print list
    else:
        pivot_index = list_length//2+start_index
        pivot_value = list[pivot_index]
#        print "pivot "+str(pivot_value)+" at "+str(pivot_index)
        i = start_index
        while (i<pivot_index):
            if list[i] > pivot_value:
#                print "swap forward "+str(list[i])+" over "+str(pivot_value)
#                print "pivot_index"
                list.insert(pivot_index,list.pop(i))
#                print list
                pivot_index = pivot_index-1
                i=i-1
                if i<-1:
                    i=0
            i = i+1
        i = end_index-1
        while (i>pivot_index):
            if list[i] < pivot_value:
#                print "swap backward "+str(list[i])+" over "+str(pivot_value)
#                print "pivot_index "+str(pivot_index)
                list.insert(pivot_index,list.pop(i))
#                print list
                pivot_index = pivot_index+1
                i=i+1
            i = i-1
#        print "list after sort"
#        print list
#        print "start index for pre-pivot sort " + str(start_index)
#        print "end index for pre-pivot sort " + str(pivot_index)
        local_quicksort(list,start_index,pivot_index)
#        print "start index for post-pivot sort "+str(pivot_index+1)
#        print "end index for post-pivot sort "+str(end_index)
        local_quicksort(list,pivot_index+1,end_index)
#    return list



if __name__ == "__main__":
    main()