from pyzbar.pyzbar import decode
from PIL import Image
import sys
def main():
    for file in sys.argv[1:]:
        try:
            result = decode(Image.open(file))
            for r in result:
                print("%s - %s"%(file, r.data.decode("ascii")))
        except:
            print("Errore decodifica %s"%file, file=sys.stderr)
    if len(sys.argv) <= 1:
        print("Usage: barcode_indexing_tool file1.jpg file2.jpg > index.txt\nbarcode_indexing_tool file1.jpg file2.jpg | grep lookingfor", file=sys.stderr)