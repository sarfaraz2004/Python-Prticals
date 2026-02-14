def search(self, key):
    temp = self.head
    while temp:
        if temp.data == key:
            return "Found"
        temp = temp.next
    return "Not Found"
