AMOUNT = 999


def main():
    raw_fantasy_file = open('data/raw/fantasy_raw.txt', 'r')
    raw_mystery_file = open('data/raw/mystery_raw.txt', 'r')
    raw_philosophy_file = open('data/raw/philosophy_raw.txt', 'r')
    raw_romance_file = open('data/raw/romance_raw.txt', 'r')
    raw_science_fiction_file = open('data/raw/science_fiction_raw.txt', 'r')

    final_fantasy_file = open('data/final/fantasy.txt', 'w')
    final_mystery_file = open('data/final/mystery.txt', 'w')
    final_philosophy_file = open('data/final/philosophy.txt', 'w')
    final_romance_file = open('data/final/romance.txt', 'w')
    final_science_fiction_file = open('data/final/science_fiction.txt', 'w')

    fantasy_set = set()
    mystery_set = set()
    philosophy_set = set()
    romance_set = set()
    science_fiction_set = set()

    # fantasy
    for description in raw_fantasy_file:
        if description in fantasy_set:
            continue
        else:
            fantasy_set.add(description)

    count = 0
    for description in fantasy_set:
        final_fantasy_file.write(description)
        if count < AMOUNT:
            count += 1
            continue
        else:
            break

    # mystery
    for description in raw_mystery_file:
        if description in mystery_set:
            continue
        else:
            mystery_set.add(description)

    count = 0
    for description in mystery_set:
        final_mystery_file.write(description)
        if count < AMOUNT:
            count += 1
            continue
        else:
            break

    # philosophy
    for description in raw_philosophy_file:
        if description in philosophy_set:
            continue
        else:
            philosophy_set.add(description)

    count = 0
    for description in philosophy_set:
        final_philosophy_file.write(description)
        if count < AMOUNT:
            count += 1
            continue
        else:
            break

    # romance
    for description in raw_romance_file:
        if description in romance_set:
            continue
        else:
            romance_set.add(description)

    count = 0
    for description in romance_set:
        final_romance_file.write(description)
        if count < AMOUNT:
            count += 1
            continue
        else:
            break

    # science_fiction
    for description in raw_science_fiction_file:
        if description in science_fiction_set:
            continue
        else:
            science_fiction_set.add(description)

    count = 0
    for description in science_fiction_set:
        final_science_fiction_file.write(description)
        if count < AMOUNT:
            count += 1
            continue
        else:
            break


if __name__ == "__main__":
    main()
