# linked list

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new_node

    def insert_after(self, prev_node: Node, data):
        if prev_node is None:
            print("Попереднього вузла не існує.")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def delete_node(self, key: int):
        cur = self.head
        if cur and cur.data == key:
            self.head = cur.next
            cur = None
            return
        prev = None
        while cur and cur.data != key:
            prev = cur
            cur = cur.next
        if cur is None:
            return
        prev.next = cur.next
        cur = None

    def search_element(self, data: int) -> Node | None:
        cur = self.head
        while cur:
            if cur.data == data:
                return cur
            cur = cur.next
        return None

    def print_list(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next
    
    def reverse_linked_list(self):
        prev = None
        current = self.head
        while current is not None:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev
    
    def insertion_sort(self):
        if self.head is None:
            return
        
        sorted_head = None  # Початково відсортований список порожній
        cur = self.head
        
        while cur:
            next_node = cur.next  # Зберігаємо наступний вузол перед переміщенням cur
            
            # Вставка поточного вузла в відсортований список
            if sorted_head is None or cur.data <= sorted_head.data:
                cur.next = sorted_head
                sorted_head = cur
            else:
                temp = sorted_head
                while temp.next and temp.next.data < cur.data:
                    temp = temp.next
                cur.next = temp.next
                temp.next = cur
                
            cur = next_node  # Переміщення cur до наступного вузла
        
        self.head = sorted_head  # Оновлюємо початок списку на відсортований


# Функція, що об'єднує два відсортовані однозв'язні списки в один відсортований список
def merge_sorted_lists(list1, list2):
    # Створюємо новий пустий список для зберігання об'єднаного списку
    merged_list = LinkedList()  
    cur1 = list1.head
    cur2 = list2.head
    
    # Проходимо обидва списки, порівнюючи значення вузлів і додаючи їх у злитий список
    while cur1 is not None and cur2 is not None:
        if cur1.data <= cur2.data:
            merged_list.insert_at_end(cur1.data)
            cur1 = cur1.next
        else:
            merged_list.insert_at_end(cur2.data)
            cur2 = cur2.next
    
    # Додаємо залишок першого списку, якщо такий є
    while cur1 is not None:
        merged_list.insert_at_end(cur1.data)
        cur1 = cur1.next
    
    # Додаємо залишок другого списку, якщо такий є
    while cur2 is not None:
        merged_list.insert_at_end(cur2.data)
        cur2 = cur2.next
    
    # Сортування вставками після об'єднання списків
    merged_list.insertion_sort() 

    return merged_list


llist = LinkedList()

# Вставляємо вузли в початок
llist.insert_at_beginning(5)
llist.insert_at_beginning(10)
llist.insert_at_beginning(15)

# Вставляємо вузли в кінець
llist.insert_at_end(20)
llist.insert_at_end(25)

# Друк зв'язного списку
print("Зв'язний список:")
llist.print_list()

# Видаляємо вузол
llist.delete_node(10)

print("\nЗв'язний список після видалення вузла з даними 10:")
llist.print_list()

# Пошук елемента у зв'язному списку
print("\nШукаємо елемент 15:")
element = llist.search_element(15)
if element:
    print(element.data)

# Pеверсування однозв'язного списку
llist.reverse_linked_list()
print("\nРеверс список:")
llist.print_list()

# Відсортований список після сортування вставками
llist.insertion_sort()
print("\nПісля сортування вставками:")
llist.print_list()  

llist2 = LinkedList()

# Вставляємо вузли в початок
llist2.insert_at_beginning(0)
llist2.insert_at_beginning(9)
llist2.insert_at_beginning(19)

# Вставляємо вузли в кінець
llist2.insert_at_end(29)
llist2.insert_at_end(39)

# Об'єднанаємо 2 списки та виведемо отриманий відсортований список
merged_list = merge_sorted_lists(llist, llist2)
print("\nПісля об'єднання двох відсортованих однозв'язних списків в один відсортований список:")
merged_list.print_list()  
