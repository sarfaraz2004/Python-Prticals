def delete_begin(self):
    if self.head:
        self.head = self.head.next
    def delete_end(self):
        temp=self.head
        if not temp:
            return
        if not temp.next:
            self.head=None
            return
        while temp.next.next:
            temp=temp.next
        temp.next=None
