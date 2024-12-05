def from_null_to_none(x):
    return None if x=='null' else x

def from_None_to_null(x):
    return 'null' if x==None else x

def to_array(self)->list:
    '''from a TreeNode to array structure'''
    frontier=deque()#queue
    elements=[]
    frontier.append(self)
    while len(frontier)>0:
        node=frontier.pop()
        if node == None:
            elements.append('null')#the same format used by leet-code
        else:
            elements.append(node.val)
            frontier.appendleft(node.left)
            frontier.appendleft(node.right)
    
    
    while elements and elements[-1] == 'null':
        elements.pop()
    return elements

def to_standard(arr: list)->list:
    ''' if you need to have 'None' instead of 'null '''
    return list(map(from_null_to_none,arr))

def to_leetcode(arr: list)->list :
    ''' if you need to have 'null' instead of 'None' '''
    return list(map(from_None_to_null,arr))
