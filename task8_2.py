"""Бинарное дерево"""


class BinaryTree:
    """Класс бинарного дерева"""

    def __init__(self, root_obj):

        self.root = root_obj

        self.left_child = None

        self.right_child = None

    # добавить левого потомка
    def insert_left(self, new_node):
        """Функция вставки левого потомка"""
        if new_node > self.root or new_node == self.root:
            raise Exception("Left child должен быть меньше root")
        else:
            # если у узла нет левого потомка
            if self.left_child is None:
                # тогда узел просто вставляется в дерево
                # формируется новое поддерево
                self.left_child = BinaryTree(new_node)
            # если у узла есть левый потомок
            else:
                # тогда вставляем новый узел
                tree_obj = BinaryTree(new_node)
                # и спускаем имеющегося потомка на один уровень ниже
                tree_obj.left_child = self.left_child
                self.left_child = tree_obj

    # добавить правого потомка
    def insert_right(self, new_node):
        """Функция вставки правого потомка"""
        if new_node < self.root or new_node == self.root:
            raise Exception("Right child должен быть меньше root")
        else:
            # если у узла нет правого потомка
            if self.right_child is None:
                # тогда узел просто вставляется в дерево
                # формируется новое поддерево
                self.right_child = BinaryTree(new_node)
            # если у узла есть правый потомок
            else:
                # тогда вставляем новый узел
                tree_obj = BinaryTree(new_node)
                # и спускаем имеющегося потомка на один уровень ниже
                tree_obj.right_child = self.right_child
                self.right_child = tree_obj

    # метод доступа к правому потомку
    def get_right_child(self):
        """Получить правого потомка"""
        return self.right_child

    # метод доступа к левому потомку
    def get_left_child(self):
        """Получить левого потомка"""
        return self.left_child

    # метод установки корня
    def set_root_val(self, obj):
        """Установить значение корня"""
        self.root = obj

    # метод доступа к корню
    def get_root_val(self):
        """Получить доступ к корню"""
        return self.root


r = BinaryTree(8)
print(r.get_root_val())
print(r.get_left_child())
r.insert_left(6)
print(r.get_left_child())
print(r.get_left_child().get_root_val())
r.insert_right(10)
print(r.get_right_child())
print(r.get_right_child().get_root_val())
r.get_right_child().set_root_val(16)
print(r.get_right_child())
