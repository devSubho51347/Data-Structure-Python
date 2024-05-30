# Implememnt search insertion and deletion operation closed addressing


class myHash:
    def __init__(self,buckets):
        self.size = buckets
        self.table = [[] for i in range(self.size)]


    ### Method to insert an element into hash table
    def insert(self,x):
        index = x % self.size
        self.table[index].append(x)

    ## Method to delete an element from hash table

    def delete_ele(self,x):
        index = x % self.size
        if x in self.table[index]:
            self.table[index].remove(x)

    ## Method to search an element

    def search(self,x):
        index = x % self.size
        if x in self.table[index]:
            return True
        return False




ob = myHash(5)

ob.insert(10)

print(ob.search(10))
ob.delete_ele(10)
print(ob.search(10))
print(ob.table)