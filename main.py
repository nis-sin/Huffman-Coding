from priority_queue import PriorityQueue, Node
from huffman_coding_lib import createHuffmanTree, encodeHuffmanCodes, decodeHuffmanCodes


def compressText(file: str) -> Node:
    with open(file, 'r') as f:
        text = f.read()

    root = createHuffmanTree(text)      # Create the Huffman tree

    huffmanCodes = {}
    encodeHuffmanCodes(root, huffmanCodes)  # Encode the Huffman codes

    compressedText = ""
    for char in text:
        compressedText += huffmanCodes[char]        # Replace each character with its Huffman code

    with open("compressed.txt", 'w') as f:
        f.write(compressedText)
    
    return root         # Return the root of the Huffman tree for decompression


def decompressText(file: str, root: Node) -> None:
    with open(file, 'r') as f:
        text = f.read()

    decodedText = decodeHuffmanCodes(text, root)

    return decodedText
    

def main():
    print("Compression using Huffman Coding")
    root = compressText("test.txt")
    print("Compression done")
    print("Decompressing")
    decodedText = decompressText("compressed.txt", root)
    print(decodedText)
    print("Decompression done")

if __name__ == '__main__':
    main()