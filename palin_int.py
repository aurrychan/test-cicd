class Solution(object):

    def is_palindrome(self, x):

            result = False
            arr = []

            #Check if number is positive. If not, discard as number will never be a palindrome

            if (x>=0):

                if(x==0):

                    return False
                
                #Number is now positive. Use modulus to get its digits.

                while(x>0):
                    arr.append(x%10)
                    x=int(x/10)             

                index_arr = len(arr)-1            

                for val in arr:
                    if(val!=arr[index_arr]):
                        return result
                    else:
                        index_arr=index_arr-1	

                return True

            return result    






    			






        
        