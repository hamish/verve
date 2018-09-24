import sys


def main(version_label, output_directory):
    print("Would generate version {} and place them into directory {}".format(version_label, output_directory))
  
if __name__== "__main__":
    if len(sys.argv) != 3: 
        print "usage: python {} version_label output_directory".format(sys.argv[0])
        exit()

    version_label = sys.argv[1]
    output_directory = sys.argv[2]
    main(version_label, output_directory)
