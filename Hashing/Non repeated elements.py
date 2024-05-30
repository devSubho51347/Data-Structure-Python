# User function Template for python3
class Solution:

    # Complete this function
    # Function to return non-repeated elements in the array.
    def printNonRepeated(self, arr, n):
        # Your code here

        dict = {

        }

        for ele in arr:
            dict[ele] = dict.get(ele, 0) + 1

        for key in dict.keys():
            if dict[key] == 1:
                val = key
                print(val)