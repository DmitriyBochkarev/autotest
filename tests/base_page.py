class BasePage:

    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    def maximize_window(self):
        self.driver.maximize_window()

    def get_url(self):
        self.driver.get(self.url)

    def implicitly_wait(self, time):
        self.driver.implicitly_wait(time)

    def new_window(self):
        """Переключиться на новую вкладку"""
        new_window = self.driver.window_handles[1]
        return self.driver.switch_to.window(new_window)

    def get_current_url(self):
        get_current_url = self.driver.current_url
        return get_current_url
