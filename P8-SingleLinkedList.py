class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
class SLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data_in):
        NewNode = Node(data_in)
        NewNode.next = self.head
        self.head = NewNode

# Function to remove node
    def remove(self, Removekey):
        HeadVal = self.head
         
        if (HeadVal is not None):
            if (HeadVal.data == Removekey):
                self.head = HeadVal.next
                HeadVal = None
                return
        while (HeadVal is not None):
            if HeadVal.data == Removekey:
                break
            prev = HeadVal
            HeadVal = HeadVal.next

        if (HeadVal == None):
            return

        if (prev.next == HeadVal.next):
            HeadVal = None

    def LListprint(self):
        printval = self.head
        while (printval):
            print(printval.data),
            printval = printval.next

# llist = SLinkedList()
# llist.append("Mon")
# llist.append("Tue")
# llist.append("Wed")
# llist.append("Thu")
# llist.remove("Tue")
# llist.LListprint()

print('')
Head1, Head2 = SLinkedList(), SLinkedList()
array1 = [6,5,3,2]
array2 = [10,4,1]
for el in array1:
    Head1.append(el)
for el in array2:
    Head2.append(el)

def merge_sorted(head1, head2):
  # if both lists are empty then merged list is also empty
  # if one of the lists is empty then other is the merged list
    if head1 == None:
        return head2
    elif head2 == None:
        return head1
    mergedHead = None
    if head1.data < head2.data:
        mergedHead = head1
        mergedHead.next = merge_sorted(head1.next, head2)
    else:
        mergedHead = head2
        mergedHead.next = merge_sorted(head1, head2.next)
    return mergedHead

merged_list = SLinkedList()
merged_list.head = merge_sorted(Head1.head, Head2.head)
merged_list.LListprint()
