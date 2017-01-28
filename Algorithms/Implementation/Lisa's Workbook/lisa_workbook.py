def special_problems(k, chapters):
    count, offset = 0, 1

    for chapter in chapters:
        problems = range(1, (chapter + 1))
        pages = [tuple(problems[i:(i + k)]) for i in xrange(0, chapter, k)]
        for index, page in enumerate(pages):
            if offset in page:
                count += 1
            offset += 1

    return count


def main():
    n, k = map(int, raw_input().split())
    chapters = map(int, raw_input().split())

    print special_problems(k, chapters)


if __name__ == '__main__':
    main()

