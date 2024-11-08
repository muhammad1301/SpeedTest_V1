from scraper import Speedtest

HEADLESS = True


def main():

    S = Speedtest('uc', headless2=HEADLESS, start=True)
    S.open_web()


if __name__ == '__main__':
    main()
