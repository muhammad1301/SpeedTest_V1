import time
from driver import *

class Speedtest(Selenium):
    def open_web(self):
        self.get("https://fast.com/")
        self.scrape()

    def scrape(self):
        print("Loading,Please Wait")
        time.sleep(15)
        try:
            speed = self.text(By.XPATH,'//div[@id="speed-value"]')
            speed_unit = self.text(By.XPATH,'//div[@id="speed-units"]')
            print(speed,speed_unit)
        except NoSuchElementException:
            print("Your internet is too Slow")


