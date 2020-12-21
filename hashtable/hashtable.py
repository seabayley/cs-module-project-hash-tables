class HashTableEntry:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next_node = None

    def get_value(self):
        return self.value

    def set_value(self, new_value):
        self.value = new_value
        return self.value

    def get_key(self):
        return self.key

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next
        return self.next_node.value

    def delete(self, previous_node):
        previous_node.set_next(self.get_next())
        return self


class HTLinkedList:
    def __init__(self):
        self.head = None

    def add_to_head(self, key, value):
        node = HashTableEntry(key, value)

        if self.head is not None:
            node.set_next(self.head)

        self.head = node

    def contains(self, key):
        if not self.head:
            return False

        current = self.head

        while current:
            if current.get_key() == key:
                return True

            current = current.get_next()

        return False

    def get_node(self, key):
        if not self.head:
            return None

        current = self.head

        while current:
            if current.get_key() == key:
                return current

            current = current.get_next()

        return None

    def delete(self, value):
        current = self.head
        previous = current

        if current.value == value:
            self.head = self.head.next_node
            return current

        current = current.next_node

        while current is not None:
            if current.value == value:
                previous.next_node = current.next_node
                return current
            else:
                previous = previous.next_node
                current = current.next_node
        return None


# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8


class HashTable:

    def __init__(self, capacity):
        self.capacity = capacity
        self.load = 0
        self.data = [HTLinkedList()] * capacity

    def update_load(self, value):
        self.load += value
        lf = self.get_load_factor()
        if lf > 0.7:
            self.resize(self.capacity*2)
        elif lf < 0.2:
            self.resize(int(self.capacity/2))

    def get_num_slots(self):

        return self.capacity

    def get_load_factor(self):

        return self.load / self.capacity

    def hash_index(self, key):
        hash = 5381
        for x in key:
            hash = ((hash << 5) + hash) + ord(x)

        return hash & 0xFFFFFFFF % self.capacity

    def put(self, key, value):
        slot = self.hash_index(key)
        node = self.data[slot].get_node(key)
        if node is not None:
            node.set_value(value)
            return node
        else:
            self.data[slot].add_to_head(key, value)

        self.update_load(1)

    def delete(self, key):
        self.put(key, None)
        self.update_load(-1)

    def get(self, key):
        slot = self.hash_index(key)
        node = self.data[slot].get_node(key)

        return None if node is None else node.get_value()

    def resize(self, new_capacity):
        self.capacity = new_capacity
        old_data = self.data
        self.data = [HTLinkedList()] * new_capacity

        for slot in old_data:
            node = slot.head
            while node is not None:
                self.put(node.key, node.value)
                node = node.get_next()


if __name__ == "__main__":
    ht = HashTable(8)

    ht.put("line_1", "'Twas brillig, and the slithy toves")
    ht.put("line_2", "Did gyre and gimble in the wabe:")
    ht.put("line_3", "All mimsy were the borogoves,")
    ht.put("line_4", "And the mome raths outgrabe.")
    ht.put("line_5", '"Beware the Jabberwock, my son!')
    ht.put("line_6", "The jaws that bite, the claws that catch!")
    ht.put("line_7", "Beware the Jubjub bird, and shun")
    ht.put("line_8", 'The frumious Bandersnatch!"')
    ht.put("line_9", "He took his vorpal sword in hand;")
    ht.put("line_10", "Long time the manxome foe he sought--")
    ht.put("line_11", "So rested he by the Tumtum tree")
    ht.put("line_12", "And stood awhile in thought.")

    print("")

    # Test storing beyond capacity
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    # Test resizing
    old_capacity = ht.get_num_slots()
    ht.resize(ht.capacity * 2)
    new_capacity = ht.get_num_slots()

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    print("")
