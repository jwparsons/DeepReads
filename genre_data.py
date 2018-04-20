import string
from goodreads import client

valid_lower = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'}
valid_upper = {'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'}
valid_number = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}


def main():
    gc = client.GoodreadsClient('V9bxgEm8ovI8ceia1uaLbA', 'H3ogn5JiQvVrYAwVBFsPnBCAuwQdi8dAo9cBQpAsP8')

    # genre files
    fantasy_file = open('data/genre/fantasy1.txt', 'w')
    mystery_file = open('data/genre/mystery1.txt', 'w')
    philosophy_file = open('data/genre/philosophy1.txt', 'w')
    romance_file = open('data/genre/romance1.txt', 'w')
    science_fiction_file = open('data/genre/science_fiction1.txt', 'w')

    genre_count = {'fantasy': 4545, 'mystery': 3640, 'philosophy': 2525, 'romance': 3377, 'science-fiction': 2678}
    fantasy = False
    mystery = False
    philosophy = False
    romance = False
    science_fiction = False

    index = 101236
    while True:
        try:
            book = gc.book(index)
            print('index:', index)
            print('title:', book.title)
            print('rating:', book.average_rating)
            print('description:', book.description)

            # check language
            if book.language_code != 'eng' and book.language_code != 'en-US':
                index += 1
                print('skip: language:', book.language_code)
                print()
                continue

            # filter description
            description = description_filter(book.description)
            if len(description) < 10:
                index += 1
                print('skip: description length')
                print()
                continue

            # check genre and write to file
            for shelf in book.popular_shelves:
                if 'fantasy' == shelf.name and not fantasy:
                    fantasy_file.write(description + '\n')
                    genre_count['fantasy'] += 1
                    if genre_count['fantasy'] == 5000:
                        fantasy = True

                if 'mystery' == shelf.name and not mystery:
                    mystery_file.write(description + '\n')
                    genre_count['mystery'] += 1
                    if genre_count['mystery'] == 5000:
                        mystery = True

                if 'philosophy' == shelf.name and not philosophy:
                    philosophy_file.write(description + '\n')
                    genre_count['philosophy'] += 1
                    if genre_count['philosophy'] == 5000:
                        philosophy = True

                if 'romance' == shelf.name and not romance:
                    romance_file.write(description + '\n')
                    genre_count['romance'] += 1
                    if genre_count['romance'] == 5000:
                        romance = True

                if 'science-fiction' == shelf.name and not science_fiction:
                    science_fiction_file.write(description + '\n')
                    genre_count['science-fiction'] += 1
                    if genre_count['science-fiction'] == 5000:
                        science_fiction = True

            print('fantasy: ', genre_count['fantasy'])
            print('mystery: ', genre_count['mystery'])
            print('philosophy: ', genre_count['philosophy'])
            print('romance: ', genre_count['romance'])
            print('science-fiction: ', genre_count['science-fiction'])
            print()

            if fantasy and mystery and philosophy and romance and science_fiction:
                break
            index += 1
        except:
            print('skip: exception')
            print()
            index += 1
            pass

    # close files
    fantasy_file.close()
    mystery_file.close()
    philosophy_file.close()
    romance_file.close()
    science_fiction_file.close()


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
