class MaxHeap:
    #TODO

    # implemented using just one array
    # index starts from 1
    # indices of two left and right child nodes of a root node at index k: 2*k and 2*k+1
    # indices of a parent node of two child nodes: k // 2


    def __init__(self) -> None:
        self.length = 0
        self.the_array = [0]

    def __len__(self) -> int:
        return self.length

    def get_max(self):
        if len(self) == 0:
            raise NoElementError("no element in the heap")

        oup = self.the_array[1]
        self.the_array[1] = self.the_array[len(self)]
        self.length -= 1
        self.sink(1)

        return oup

    def peak_max(self):
        return self.the_array[1]

    def put(self, element):
        """
        Swaps elements while rising
        """

        self.length += 1
        self.the_array.append(element)
        self.rise(self.length)

    # lower-level codes
    def rise(self, k: int) -> None:
        """
        Rise element at index k to its correct position
        :pre: 1<= k <= self.length
        """
        while k > 1 and self.the_array[k] > self.the_array[k // 2]:
            self.swap(k, k // 2)
            k = k // 2

    def largest_child(self, k: int) -> int:
        """
        Returns the index of the largest child of k.
        pre: 2*k <= self.length (at least one child)
        """
        if 2 * k == self.length or self.the_array[2 * k] > self.the_array[2 * k + 1]:
            return 2*k
        else:
            return 2*k+1

    def sink(self, k: int) -> None:
        """ Make the element at index k sink to the correct position """
        while 2*k <= self.length:
            child = self.largest_child(k)
            if self.the_array[k] >= self.the_array[child]:
                break
            self.swap(child, k)
            k = child

    def swap(self, a, b):
        self.the_array[a], self.the_array[b] = self.the_array[b], self.the_array[a]

    def __str__(self):
        return str(self.the_array)

# def put(self, element) -> None:
    #     """
    #     Combined into one method
    #     More efficient but less readable
    #
    #     find the hole and swap (rising)
    #     """
    #
    #     if self.length == 0:
    #         self.length += 1
    #         self.the_array.append(element)
    #     else:
    #         self.length += 1
    #         k = self.length
    #         while k > 1 and element > self.the_array[k // 2]:
    #             print("pass here")
    #             self.the_array[k] = self.the_array[k // 2]
    #             k = k // 2
    #
    #         self.the_array[k] = element

class NoElementError(Exception):
    pass