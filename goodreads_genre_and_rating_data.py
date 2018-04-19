import string
from goodreads import client


def main():
    gc = client.GoodreadsClient('V9bxgEm8ovI8ceia1uaLbA', 'H3ogn5JiQvVrYAwVBFsPnBCAuwQdi8dAo9cBQpAsP8')

    # genre files
    comedy_file = open('data/genre/comedy.txt', 'w')
    fantasy_file = open('data/genre/fantasy.txt', 'w')
    historical_file = open('data/genre/historical.txt', 'w')
    horror_file = open('data/genre/horror.txt', 'w')
    mystery_file = open('data/genre/mystery.txt', 'w')
    philosophy_file = open('data/genre/philosophy.txt', 'w')
    romance_file = open('data/genre/romance.txt', 'w')
    science_fiction_file = open('data/genre/science_fiction.txt', 'w')

    # rating files
    rating_01_file = open('data/rating/01.txt', 'w')
    rating_12_file = open('data/rating/12.txt', 'w')
    rating_23_file = open('data/rating/23.txt', 'w')
    rating_34_file = open('data/rating/34.txt', 'w')
    rating_45_file = open('data/rating/45.txt', 'w')

    count = 1
    index = 1
    while count <= 10000:
        try:
            book = gc.book(index)
            print('index:', index)
            print('count:', count)
            print('title:', book.title)
            print('rating:', book.average_rating)
            print('description:', book.description)
            print('filtered_description:', description_filter(book.description))
            print()

            # check language
            if book.language_code != 'eng':
                index += 1
                continue

            # filter description
            description = description_filter(book.description)
            if description == '':
                index += 1
                continue

            # check genre and write to file
            has_genre = False
            for shelf in book.popular_shelves:
                if 'comedy' == shelf.name:
                    comedy_file.write(description + '\n')
                    has_genre = True
                if 'fantasy' == shelf.name:
                    fantasy_file.write(description + '\n')
                    has_genre = True
                if 'historical' == shelf.name:
                    historical_file.write(description + '\n')
                    has_genre = True
                if 'horror' == shelf.name:
                    horror_file.write(description + '\n')
                    has_genre = True
                if 'mystery' == shelf.name:
                    mystery_file.write(description + '\n')
                    has_genre = True
                if 'philosophy' == shelf.name:
                    philosophy_file.write(description + '\n')
                    has_genre = True
                if 'romance' == shelf.name:
                    romance_file.write(description + '\n')
                    has_genre = True
                if 'science-fiction' == shelf.name:
                    science_fiction_file.write(description + '\n')
                    has_genre = True

            if has_genre:
                rating = float(book.average_rating)
                if 0 <= rating <= 1:
                    rating_01_file.write(description + '\n')
                elif 1 < rating <= 2:
                    rating_12_file.write(description + '\n')
                elif 2 < rating <= 3:
                    rating_23_file.write(description + '\n')
                elif 3 < rating <= 4:
                    rating_34_file.write(description + '\n')
                elif 4 < rating <= 5:
                    rating_45_file.write(description + '\n')
                count += 1
            index += 1
        except:
            index += 1
            pass

    # close files
    comedy_file.close()
    fantasy_file.close()
    historical_file.close()
    horror_file.close()
    mystery_file.close()
    philosophy_file.close()
    romance_file.close()
    science_fiction_file.close()
    rating_01_file.close()
    rating_12_file.close()
    rating_23_file.close()
    rating_34_file.close()
    rating_45_file.close()


def description_filter(description):
    # remove html
    filter_1 = ''
    is_open = False
    for i in range(len(description)):
        letter = description[i]
        if is_open:
            if letter == '>':
                is_open = False
                filter_1 += ' '
        else:
            if letter == '<':
                is_open = True
            else:
                filter_1 += letter

    # check for any crazy characters
    filter_2 = ''
    for i in range(len(filter_1)):
        letter = filter_1[i]
        if letter.isalpha():
            filter_2 += letter
        else:
            if letter in string.punctuation or letter == ' ':
                filter_2 += letter
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


if __name__ == "__main__":
    main()
