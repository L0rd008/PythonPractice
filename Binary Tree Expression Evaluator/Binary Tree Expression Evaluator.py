class Node:
    def __init__(self, data):
        #initialize the node with left and right children set to None and store the provided data
        self.left = None
        self.right = None
        self.data = data

    def get_output(self):
        """
        print the output depending on the evaluated value
        if the value is between 0 and 999, print the value
        if the value is less than 0, print UNDERFLOW
        if the value is greater than 999, print OVERFLOW
        """
        value = self.evaluate()
        #check if the evaluation resulted in an error
        if value is None:
            print('Error in evaluation.')
        #check if the evaluated value exceeds 999
        elif value > 999:
            print('OVERFLOW')
        #check if the evaluated value is less than 0
        elif value < 0:
            print('UNDERFLOW')
        #otherwise, print the evaluated value
        else:
            print(value)

    def insert(self, data, bracketed):
        """
        insert data into the binary tree
        :param data: tuple containing ('TYPE', value) where TYPE is 'OPERATOR' or 'OPERAND'
        :param bracketed: boolean indicating if the operator is within brackets
        :return: the new root node after insertion
        """
        try:
            #check if the data is an operator or operand
            if data[0] == 'OPERATOR':
                return self._insert_operator(data, bracketed)
            else:
                return self._insert_operand(data)
        except Exception as e:
            print(f"Error while inserting\n{e}")
            return None

    def _insert_operator(self, data, bracketed):
        #handle insertion of operator nodes
        #check if the operator is not within brackets
        if not bracketed:
            #create a new root node and assign the current node as its left child
            new_root = Node(data)
            new_root.left = self
            return new_root
        else:
            #create a sub-root node and assign the current right child as its left child
            sub_root = Node(data)
            sub_root.left = self.right
            self.right = sub_root
            return self

    def _insert_operand(self, data):
        #handle insertion of operand nodes
        #check if the right child of the current node is None
        if self.right is None:
            #assign the operand as the right child of the current node
            self.right = Node(data)
        else:
            #if the right child is already an operator, insert the operand as its right child
            self.right.right = Node(data)
        return self

    def evaluate(self):
        """
        recursively evaluate the expression represented by the binary tree
        :return: the evaluated value or None if an error occurs
        """
        try:
            #check if the current node is an operand and return its value
            if self.data[0] == 'OPERAND':
                return self.data[1]

            #evaluate the left and right subtrees
            left_val = self.left.evaluate()
            right_val = self.right.evaluate()

            #define the operations based on the operator
            operations = {
                '+': lambda x, y: x + y,
                '-': lambda x, y: x - y,
                '*': lambda x, y: x * y,
                '^': lambda x, y: x ** y,
            }

            #get the operator from the current node and apply the corresponding operation
            operator = self.data[1]
            return operations.get(operator, lambda x, y: None)(left_val, right_val)

        except Exception as e:
            print(f"Error while evaluating\n{e}")
            return None
