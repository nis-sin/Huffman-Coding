from huffman_coding_lib import createHuffmanTree, encodeHuffmanCodes, decodeHuffmanCodes, calculateFrequencies
from argparse import ArgumentParser


def parse_args():
    parser = ArgumentParser(description = "Program to compress and decompress text files using Huffman Coding.", usage = "%(prog)s [options] <file>")
    parser.add_argument('file', type=str, help='File to compress or decompress')
    parser.add_argument('-c', "--compress", action = "store_true", help="Compress text file")
    parser.add_argument('-d', "--decompress", action = "store_true", help="Compress text file")
    return parser.parse_args()


def compressText(file: str) -> None:
    with open(file, 'r', encoding='utf-8') as f:
        text = f.read()

    frequencies = calculateFrequencies(text)    # Calculate the frequency of each character

    root = createHuffmanTree(frequencies)      # Create the Huffman tree

    huffmanCodes = {}
    encodeHuffmanCodes(root, huffmanCodes)  # Encode the Huffman codes

    compressedText = ""
    for char in text:
        compressedText += huffmanCodes[char]        # Replace each character with its Huffman code

    msg_len = str(len(compressedText))
    with open("compressed", 'wb') as f:
        f.write(str(frequencies).encode('utf-8'))
        f.write(b'\n')
        f.write(msg_len.encode('utf-8'))
        f.write(b'\n')
        f.write(int(compressedText, 2).to_bytes((len(compressedText) + 7) // 8, byteorder='big'))     # Write the compressed text to the file


def decompressText(file: str) -> str:
    with open(file, 'rb') as f:
        frequencies = eval(f.readline().decode('utf-8'))       # Read the frequencies from the compressed file
        msg_len = int(f.readline().decode('utf-8'))     # Read the length of the compressed text
        text = f.read()                 # Read the compressed text

    text = str(bin(int(text.hex(), 16))).replace("0b", "")

    if len(text) < msg_len:         # Add '0's to the beginning of the text since leading zeros are removed during conversion
        text = (msg_len-len(text))*"0" + text

    decodedText = decodeHuffmanCodes(text, frequencies)

    return decodedText
    

def main():
    args = parse_args()
    inputFile = args.file
    decodedText = ""
    if args.compress:
        print("Compressing")
        compressText(inputFile)
    if args.decompress:
        print("Decompressing")
        decodedText = decompressText(inputFile)
    
    print(decodedText)


if __name__ == '__main__':
    main()
