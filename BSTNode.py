class BSTNode:
    '''
    properties
        info  : info stored in current node. must be comparable
        left  : left node
        right : right node
    '''

    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None

    def setInfo(self, info):
        self.info = info
    
    def getInfo(self):
        return self.info
 
    def setLeft(self, link):
        self.left = link

    def setRight(self, link):
        self.right = link

    def getLeft(self):
        return self.left


    def getRight(self):
        return self.right