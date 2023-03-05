from parserLab.parser import AnnouncementParser


def main():
    page = 1
    while True:
        print(f'Cтраница {page} парсится ...')
        url = f'https://www.kijiji.ca/b-apartments-condos/city-of-toronto/page-{page}/c37l1700273'
        parser = AnnouncementParser(url)
        parser.get_data()
        print(f'{page} страница спарcена ...')
        if not parser.find_button_next():
            break
        page += 1


if __name__ == '__main__':
    main()