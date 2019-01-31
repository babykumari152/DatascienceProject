import numpy as np
def get_power_set(s):

    empty_set = set()
    power_set = [empty_set]

    for elem in s:
        # Need this temporary list because we can't change the power_set list while iterating it. Or so I think.
        new_sets = [] 
        for power_set_item in power_set:
            new_set = set().union(power_set_item) # Is this the best way to copy set?
            new_set.add(elem)
            new_sets.append(new_set)
        power_set.extend(new_sets)

    return power_set
def Knapsacks(lists,wgt):
    ps=get_power_set(lists)
    ws=get_power_set(wgt)
    m=[]
    for each in range(len(ws)):
        print(ps[each])
        if np.array(list(ws[each])).sum()==w:
             m.append(each)
         sums=[]
    for i in m:
        sums.append(np.array(list(ps[i])).sum())
    return np.array(sums).max()
    
            
