import sys
from Broll_generator.StoreImage import StoreB_roll


def main():
    args = sys.argv[1:]
    text_file = args[0]
    number_of_images = args[1]
    
    if type(number_of_images) == str:
        try:
            int(number_of_images)
        except:
            print("Enter a numerical value, It cannot be a string")
            return
    if '.txt' in text_file and int(number_of_images) <= 5:
        StoreB_roll(text_file, int(args[1])).store_images()
    elif '.txt' not in text_file:
        print("Pass a .txt file as the first argument")
    else:
        print("Only 5 images per Keyword can be downloaded")


if __name__ == '__main__':
    main()
