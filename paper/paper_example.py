import string
from goodreads import client

valid_lower = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'}
valid_upper = {'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'}
valid_number = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}


def main():
    gc = client.GoodreadsClient('V9bxgEm8ovI8ceia1uaLbA', 'H3ogn5JiQvVrYAwVBFsPnBCAuwQdi8dAo9cBQpAsP8')
    try:
        index = 5
        book = gc.book(index)
        print('index:', index)
        print('title:', book.title)
        print('rating:', book.average_rating)
        print('description:', book.description)

        print(book.popular_shelves)

        # filter description
        description = description_filter(book.description)
    except:
        pass


def description_filter(description):
    # remove html
    filter_1 = ''
    is_open = False
    for i in range(len(description)):
        character = description[i]
        if is_open:
            if character == '>':
                is_open = False
                filter_1 += ' '
        else:
            if character == '<':
                is_open = True
            else:
                filter_1 += character

    # check for any crazy characters
    filter_2 = ''
    for i in range(len(filter_1)):
        character = filter_1[i]
        if is_valid(character):
            filter_2 += character
        else:
            if character in string.punctuation or character == ' ':
                filter_2 += character
            else:
                filter_2 += ' '

    # remove multiple white space and .com's
    word_split = filter_2.split()
    word_filter = []
    for word in word_split:
        if '.com' in word:
            continue
        else:
            word_filter.append(word)
    filter_3 = ' '.join(word_filter)

    print('filter 1:', filter_1)
    print('filter 2:', filter_2)
    print('filter 3:', filter_3)
    print(string.punctuation)

    return filter_3


def is_valid(character):
    if character in valid_lower:
        return True
    elif character in valid_upper:
        return True
    elif character in valid_number:
        return True
    return False


if __name__ == "__main__":
    main()
