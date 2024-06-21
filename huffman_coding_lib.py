from priority_queue import PriorityQueue, Node

def calculateFrequencies(text: str) -> dict:
    frequencies = {}
    # Calculating the frequency of each character in the text
    for char in text:
        frequencies[char] = frequencies.get(char, 0) + 1
    
    return frequencies


def createHuffmanTree(frequencies: dict) -> Node:
    pq = PriorityQueue()

    # Creating a node for each character and adding it to the priority queue
    for char, freq in frequencies.items():
        pq.enqueue(Node(char, freq))
    
    while pq.getLength() > 1:       # last node remanining is the root of the Huffman tree
        first = pq.dequeue()
        second = pq.dequeue()
        internalNode = Node(value=None, priority=(first.getPriority() + second.getPriority()))
        internalNode.setLeft(first)
        internalNode.setRight(second)
        pq.enqueue(internalNode)
    
    return pq.dequeue()     # returns the root of the Huffman tree


def encodeHuffmanCodes(node: Node, huffmanCodes: dict, code:str = "") -> str:
    """
    Use DFS to traverse the tree and encode the value
    """

    if huffmanCodes.get(node.getValue(), -1) != -1:     # If the value is already encoded, memoization
        return None
    
    if node.getLeft() == None and node.getRight() == None:  # If the node is a leaf node, base case
        huffmanCodes[node.getValue()] = code
        return None

    encodeHuffmanCodes(node.getLeft(), huffmanCodes, code + "0")        # Traverse left
    encodeHuffmanCodes(node.getRight(), huffmanCodes, code + "1")       # Traverse right


def decodeHuffmanCodes(text: str, frequenices: dict) -> str:
    root = createHuffmanTree(frequenices)
    currentNode = root
    decodedText = ""
    for char in text:
        if char == "0":             # Traverse left when char is 0
            currentNode = currentNode.getLeft()
        elif char == "1":           # Traverse right when char is 1
            currentNode = currentNode.getRight()
        
        if currentNode.getLeft() == None and currentNode.getRight() == None:           # leaf node is reached or character is found
            decodedText += currentNode.getValue()
            currentNode = root          # reset current node to root once leaf is reached / character is found
    return decodedText