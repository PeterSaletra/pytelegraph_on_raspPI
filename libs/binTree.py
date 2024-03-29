class Node:
    def __init__(self, letter: str, left=None, right=None):
        self.letter = letter
        self.left = left
        self.right = right


def findLetter(node: Node, code: str, i: int) -> str:
    '''
    Finds letter in binary tree based on morse code entered by user.

    :param Node node: Head of binary tree
    :param str code: Morse code entered by user
    :param int i: should by 0, it is the counter of length of code
    :return str: Returns correct letter or empty string if letter was not found
    '''
    if not node:
        return ""
    elif i == len(code):
        return node.letter
    elif code[i] == '.':
        return findLetter(node.left, code, i+1)
    elif code[i] == '-':
        return findLetter(node.right, code, i+1)


def makeMorseTree() -> Node:
    '''
    Makes whole binary tree for easier translation.

    :retrun Node: Head of the binary tree
    '''
    tree = Node("Start")
    tree.left = Node('E')
    tree.right = Node('T')
    
    tree.left.left = Node('I')
    tree.left.right = Node('A')
    tree.right.left = Node('N')
    tree.right.right = Node('M')
    
    tree.left.left.left = Node('S')
    tree.left.left.right = Node('U')
    tree.left.right.left = Node('R')
    tree.left.right.right = Node('W')
    tree.right.left.left = Node('D')
    tree.right.left.right = Node('K')
    tree.right.right.left = Node('G')
    tree.right.right.right = Node('O')

    tree.left.left.left.left = Node('H')
    tree.left.left.left.right = Node('V')
    tree.left.left.right.left = Node('F')
    tree.left.right.left.left = Node('L')
    tree.left.right.right.left = Node ('P')
    tree.left.right.right.right = Node('J')
    tree.right.left.left.left = Node('B')
    tree.right.left.left.right = Node('X')
    tree.right.left.right.left = Node('C')
    tree.right.left.right.right = Node('Y')
    tree.right.right.left.left = Node('Z')
    tree.right.right.left.right = Node('Q')
    
    return tree


