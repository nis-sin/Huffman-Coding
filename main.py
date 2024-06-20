from huffman_coding_lib import createHuffmanTree, encodeHuffmanCodes, decodeHuffmanCodes, calculateFrequencies
from json import dumps, loads
from codecs import decode

def compressText(file: str) -> None:
    with open(file, 'r', encoding='utf-8') as f:
        text = f.read()

    frequencies = calculateFrequencies(text)    # Calculate the frequency of each character

    root = createHuffmanTree(frequencies)      # Create the Huffman tree

    huffmanCodes = {}
    encodeHuffmanCodes(root, huffmanCodes)  # Encode the Huffman codes

    header = dumps(frequencies)        # Store the frequencies of characters in a JSON format

    compressedText = ""
    for char in text:
        compressedText += huffmanCodes[char]        # Replace each character with its Huffman code

    msg_len = str(len(compressedText))
    with open("compressed", 'wb') as f:
        f.write(header.encode('utf-8'))
        f.write(b'\n')
        f.write(msg_len.encode('utf-8'))
        f.write(b'\n')
        f.write(int(compressedText, 2).to_bytes((len(compressedText) + 7) // 8, byteorder='big'))     # Write the compressed text to the file


def decompressText(file: str) -> str:
    with open(file, 'rb') as f:
        header = f.readline().decode('utf-8')       # Read the frequencies from the compressed file
        msg_len = int(f.readline().decode('utf-8'))     # Read the length of the compressed text
        text = f.readline()

    frequencies = loads(header)        # Load the frequencies from the JSON format
    text = str(bin(int(text.hex(), 16))).replace("0b", "")       # Convert the compressed text to binary
    if len(text) < msg_len:
        text = (msg_len-len(text))*"0" + text
    print(text)
    decodedText = decodeHuffmanCodes(text, frequencies)

    return decodedText
    

def main():
    compressText("test2.txt")
    decodedText = decompressText("compressed")

    with open('test2.txt', 'r') as f:
        text = f.read()
    
    
#    for i,word in enumerate(text.split()):
#        if word != decodedText.split()[i]:
#            print("Compression and Decompression unsuccessful")

    print(decodedText)
    if text == decodedText:
        print("Compression and Decompression successful")

if __name__ == '__main__':
    main()
