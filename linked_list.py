# import pdb


class node(object):
    def __init__(self, val, next):
        self.val = val
        self.next = next

    def remove(self, rm_node):
        if self.next is rm_node:
            self.next = self.next.next
        else:
            self.next.remove(rm_node)

    def print_nodes(self):
        str_val = str(self.val)
        if self.next is not None:
            return str_val + ', ' + self.next.print_nodes()
        else:
            return str_val

    def search_nodes(self, val):
        if self.val is val:
            return self
        elif self.next is not None:
            return self.next.search_nodes(val)
        else:
            return None


class l_list(object):

    def __init__(self):
        self.length = 0
        self.header_node = node(None, None)

    def insert(self, val):
        new_node = node(val, self.header_node.next)
        self.header_node.next = new_node
        self.length += 1

    def size(self):
        return self.length

    def pop(self):
        if self.header_node.next is not None:
            val = self.header_node.next.val
            self.header_node.next = self.header_node.next.next
            self.length -= 1
            return val
        else:
            return None

    def _print(self):
        str = ""
        if self.header_node.next is not None:
            str = self.header_node.next.print_nodes()
        return '(' + str + ')'

    def search(self, val):
        return self.header_node.search_nodes(val)

    def remove(self, rm_node):
        current_node = self.header_node
        while current_node.next is not None:
            if current_node.next is rm_node:
                current_node.next = current_node.next.next
                break
            else:
                current_node = current_node.next
