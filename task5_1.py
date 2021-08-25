"""There we build stacks with four elements in.
If there is more than 4 elements, we build another stack"""


class StackClass:
    """This class is used to build stacks"""
    def __init__(self):
        """ Typical construction method"""
        self.elems = []
        self.stack_save = []

    def is_empty(self):
        """Checking class for empty space"""
        return self.elems == []

    def push_in(self, el):
        """Inserting elements in stack-list"""
        if len(self.elems) < 4:
            self.elems.insert(0, el)

    def new_stack(self):
        """Popping out elements from stack_list, putting them in another stack_list.
        Than printing the new stack-list and popping out elements from it for putting new values in it in the future
        """
        for parts in range(len(self.elems)):
            a = self.elems.pop(0)
            self.stack_save.append(a)

        print(self.stack_save)

        for parts_new_stack in range(len(self.stack_save)):
            self.stack_save.pop(0)

    def pop_out(self):
        "Popping out elements from stack"
        return self.elems.pop()

    def get_val(self):
        "Getting value from stack"
        return self.elems[len(self.elems) - 1]

    def stack_size(self):
        "Getting stack size"
        return len(self.elems)


stack = StackClass()

stack.push_in(5)
stack.push_in(6)
stack.push_in(7)
stack.push_in(8)
stack.push_in(8)
stack.push_in(8)

stack.new_stack()

stack.push_in(9)
stack.push_in(10)
stack.push_in(11)
stack.push_in(12)

stack.new_stack()
