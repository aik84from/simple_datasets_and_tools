from selenium import webdriver


class SimpleSelenium:
    def get_text(self, url, selector):
        driver = webdriver.Firefox()
        driver.get(url)
        result = []
        for element in driver.find_elements_by_css_selector(selector):
            result.append(element.text)
        driver.close()
        return result
