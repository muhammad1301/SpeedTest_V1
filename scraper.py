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
            self.wait.until(EC.presence_of_element_located((By.XPATH, '//div[@id="speed-value"]')))
            speed = self.text(By.XPATH,'//div[@id="speed-value"]')
            speed_unit = self.text(By.XPATH,'//div[@id="speed-units"]')
            if speed == 0:
                print("Try again..")
                self.scrape()
            else:
                print(speed,speed_unit)
        except:
            print("Your internet is too Slow..")
