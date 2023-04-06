import crawlingtools
import datetime as dt


def main():
    """
    main of program
    """
    wod_contents = crawlingtools.get_wod_by_date(dt.datetime.now())


if __name__ == '__main__':
    main()
