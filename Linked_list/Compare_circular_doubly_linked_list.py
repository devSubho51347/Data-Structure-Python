class Solution:
    def compareCLL(self,head1,head2):
        #code here
        curr1 = head1
        curr2 = head2
        
        while True:
            if head1.data != head2.data:
                return False
            head1= head1.next
            head2 = head2.next
            
            completed1 = curr1 is head1
            completed2 = curr2 is head2
            
            if completed1 and completed2:
                return True
            
            if completed1 or completed2:
                return False