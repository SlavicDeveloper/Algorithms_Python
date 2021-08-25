"""TЗдесь мы составляем стек из 4-х элементов.
Если элементов больше, чем 4, то мы делаем новый стек"""


class StackClass:
    """Класс используется для построения стека"""
    def __init__(self):
        """ Конструктор"""
        self.elements = [[], [], [], []]


    def is_empty(self):
        """Проверка стека на отсутствие элементов"""
        return self.elems == []

    def push_in(self, el):
        """Вставка элемента в стопку при условии, что длина стопки будет меньше 4"""
        for list_parts in range(len(self.elements)):
            if len(self.elements[list_parts]) < 4:
                self.elements[list_parts].append(el)
                break

    def show_stacks(self):
        """Метод, выводящий стек на экран"""
        print(self.elements)

    def pop_out(self):
        """Popping out elements from stack"""
        return self.elems.pop()

    def get_val(self):
        "Getting value from stack"
        return self.elems[len(self.elems) - 1]

    def stack_size(self):
        "Getting stack size"
        return len(self.elems)


stack = StackClass()

stack.push_in(1)
stack.push_in(2)
stack.push_in(3)
stack.push_in(4)
stack.push_in(5)
stack.push_in(6)
stack.push_in(7)
stack.push_in(8)
stack.push_in(9)
stack.push_in(10)
stack.push_in(11)
stack.push_in(12)
stack.push_in(13)
stack.push_in(14)
stack.push_in(15)
stack.push_in(16)







stack.show_stacks()
