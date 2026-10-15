class EmployeeNode:

    '''
    A class to represent a node in the binary tree.
    Attributes:
        name (str): The name of the employee.
        left (EmployeeNode): The left child node, representing the left subordinate.
        right (EmployeeNode): The right child node, representing the right subordinate.
    '''

    def __init__(self, name):
        self.name = name
        self.left = None
        self.right = None

class TeamTree:
    '''
    A class to represent a binary tree for managing a team structure.
    Attributes:
        root (EmployeeNode): The root node of the tree, representing the team lead.
    Methods:
        insert(manager_name, employee_name, side, current_node=None): Inserts a new employee under the specified manager.
        print_tree(node=None, level=0): Prints the tree structure starting from the given node.

    '''
    
    def __init__(self, root_name=None):
        if root_name is None:
            self.root = None
        else:
            self.root = EmployeeNode(root_name)

    def insert(self, manager_name, employee_name, side, current_node=None):
        if current_node is None: 
          current_node = self.root
        if current_node.name == manager_name:
          if side.lower() == "left":
              if current_node.left is None:
                  current_node.left = EmployeeNode(employee_name)
                  print(f"{employee_name} added as LEFT subordinate of {manager_name}.")
              else:
                  print(f"{manager_name} already has a LEFT subordinate.")
          elif side.lower() == "right":
              if current_node.right is None:
                    current_node.right = EmployeeNode(employee_name)
                    print(f"{employee_name} added as RIGHT subordinate of {manager_name}.")
              else:
                    print(f"{manager_name} already has a RIGHT subordinate.")
          return True
      
        if current_node.left:
            if self.insert(manager_name, employee_name, side, current_node.left):
              return True
        if current_node.right:
            if self.insert(manager_name, employee_name, side, current_node.right):
              return True
        return False

    def print_tree(self, node=None, level=0):
        if self.root is None:
            print("no employees in directory")
            return
        if node is None:
            node = self.root

        print("  " * (level * 4) + node.name)
        if node.left:
          self.print_tree(node.left, level + 1)
        if node.right:
          self.print_tree(node.right, level + 1)

employee_1 = EmployeeNode("Alice")
print(employee_1.name)
print(employee_1.left)
print(employee_1.right)

company_directory = TeamTree("Mr. Manager")
company_directory.insert("Mr. Manager", "Alice", "left")
company_directory.insert("Mr. Manager", "Bob", "right")
company_directory.insert("Alice", "Charlie", "left")
company_directory.insert("Alice", "Diana", "right")
print(company_directory.root)
print(company_directory.root.left.name)
print(company_directory.root.right.name)
company_directory.print_tree()
# Test your code here









# CLI functionality
def company_directory():
    tree = TeamTree()

    while True:
        print("\n📋 Team Management Menu")
        print("1. Add Team Lead (root)")
        print("2. Add Employee")
        print("3. Print Team Structure")
        print("4. Exit")
        choice = input("Choose an option (1–4): ")

        if choice == "1":
            if tree.root:
                print("⚠️ Team lead already exists.")
            else:
                name = input("Enter team lead's name: ")
                tree.root = EmployeeNode(name)
                print(f"✅ {name} added as the team lead.")

        elif choice == "2":
            manager = input("Enter the manager's name: ")
            employee = input("Enter the new employee's name: ")
            side = input("Should this employee be on the LEFT or RIGHT of the manager? ")
            side = side.lower()
            tree.insert(manager, employee, side)

        elif choice == "3":
            print("\n🌳  Current Team Structure:")
            tree.print_tree()

        elif choice == "4":
            print("Good Bye!")
            break
        else:
            print("❌ Invalid option. Try again.")

company_directory()
