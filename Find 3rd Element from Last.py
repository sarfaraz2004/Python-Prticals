def third_from_last(self):
    first = self.head
    second = self.head

    for _ in range(3):
        if not first:
            return None
        first = first.next

    while first:
        first = first.next
        second = second.next

    return second.data
