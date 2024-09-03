
def main():
    with open("frankenstein.txt") as f:
        file_contents = f.read()
        file_contents = file_contents.lower().replace(" ", "")
        count_dict = {}
        for letter in file_contents:
            if letter in count_dict:
                count_dict[letter] += 1
            else:
                count_dict[letter] = 1
        print(count_dict)


if __name__ == "__main__":
    main()