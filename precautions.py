class NeverDo:
    "things one should never do in python"
    def __init__(self,var=[]):
        self.var = var
    def removing_items_from_current_iterator(self):
        "removing items form current iterator confuses compiler resulting in wrong output"
        do=[[number for number in range(19,88,8)],[number for number in range(10) if number%2!=0],[number for number in range(33,55) if number%3==0],[number for number in range(10,20) if number%2==0]]
        merged, m = [],[]
        for sublist in do:
            merged.extend(_ for _ in sublist)
        for sublist in do:
            m.extend(element for element in sublist)
            do.remove(sublist)
        return merged, m #see m skips sublists
nd = NeverDo()
        
        



