class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = []
        self.head = 0

    def append(self, item):
        if len(self.storage) < self.capacity:
            self.storage.append(item)
        
        else:
            self.storage[self.head] = item
            if self.head < len(self.storage) -1:
                self.head += 1
                
            else:
                self.head = 0

    def get(self):
        return self.storage