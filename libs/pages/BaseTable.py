
from assertpy import assert_that
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait

from libs.helpers.exceptions import NoSuchElement
from libs.pages.BasePage import BasePage
from selenium.webdriver.support import expected_conditions as EC

from libs.pages.WalletsPage import WalletsPage


class BaseTable(BasePage):

    def __init__(self, browser: WebDriver, table_number=1):
        super().__init__(browser)
        self.parent_xpath = f"//*[contains(@class, 'chakra-table')][1]"
        self.table_number = table_number

    def get_all_tables(self, delay=2):
        self.wait_page_loaded(delay=delay)
        return self.browser.find_elements(by=By.XPATH, value=f"{self.parent_xpath}")

    # TODO: doesn't work for table_number!=1
    def wait_page_loaded(self, delay=3):
        self.wh.wait_page_loaded(by=By.XPATH, value=f"{self.parent_xpath}", delay=delay)
        # table = self.browser.find_element(by=By.XPATH, value="//*[contains(@class, \"chakra-table\")]")
        self.wh.wait_page_loaded(by=By.XPATH, value=f"{self.parent_xpath}//tbody/tr", delay=delay)
        # rows = table.find_elements(by=By.XPATH, value="//tbody/tr")
        self.wh.wait_element_invisible(by=By.XPATH,
                                       value=f"{self.parent_xpath}//*[contains(@class, \"chakra-skeleton\")]", delay=delay)

    def get_headers(self, delay=2):
        self.wait_page_loaded(delay=delay)
        table = self.browser.find_elements(by=By.XPATH, value=f"{self.parent_xpath}")[self.table_number-1]
        # return table.find_elements(by=By.XPATH, value=".//tr/th")[0].text.split("\n")
        return [el.text for el in table.find_elements(by=By.XPATH, value=".//tr/th")]

    def get_column_values(self, column_name):
        self.wait_page_loaded(delay=2)
        table = self.browser.find_elements(by=By.XPATH, value=f"{self.parent_xpath}")[self.table_number-1]
        rows = table.find_elements(by=By.XPATH, value=".//tbody/tr")
        header_index = self.get_headers().index(column_name)
        # self.logger.info(f"column_name: {column_name}, header_index: {header_index}")
        return [row.find_element(by=By.XPATH, value=f"./td[{header_index+1}]").text.strip() for row in rows]

    def get_table_content(self, skip_las_n_rows=None, skip_last_column_if_empty=True, delay=2, only_current_page=False):
        self.wait_page_loaded(delay=delay)
        self.wh.wait_element_visible(by=By.XPATH, value=f"{self.parent_xpath}", delay=30)
        table = self.browser.find_elements(by=By.XPATH, value=f"{self.parent_xpath}")[self.table_number-1]
        rows = table.find_elements(by=By.XPATH, value=".//tbody/tr")
        if skip_las_n_rows:
            # case when rows are not the same format, for example: Wallet policy rules( Wallet settings)
            rows = rows[:-skip_las_n_rows]
        headers = self.get_headers(delay=delay)
        if skip_last_column_if_empty and headers[-1] == '':
            # case when last column without name ( Edit link)
            headers = headers[:-1]
        result = [{} for x in range(len(rows))]
        num_rows_prev = 0
        while True:
            for i, h in enumerate(headers):
                column_values = [row.find_element(by=By.XPATH, value=f"./td[{i + 1}]").text.strip() for row in rows]
                self.logger.info(f"read '{h}' column: {column_values}")
                for j in range(num_rows_prev, len(result)):
                    result[j][h] = column_values[j-num_rows_prev]
            num_rows_prev += len(rows)
            # original = self.browser.find_element(By.TAG_NAME, "body").text
            original = table.find_element(by=By.XPATH, value=".//tbody").text
            table = self.get_all_tables(delay=0)[self.table_number - 1]
            rows_navigations = table.find_elements(by=By.XPATH, value="./../..//*[contains(@class, \"chakra-icon\")]")
            if not rows_navigations or only_current_page:
                break
            rows_navigations[-1].click()
            self.wait_page_loaded(delay=delay)
            # newer = self.browser.find_element(By.TAG_NAME, "body").text
            newer = table.find_element(by=By.XPATH, value=".//tbody").text
            if newer != original:
                self.logger.info(f"newer content found!")
                rows = table.find_elements(by=By.XPATH, value=".//tbody/tr")
                result += [{} for x in range(len(rows))]
            else:
                break
        return result

    def click_in_cell(self, column_name, row_value):
        # TODO: check
        self.wait_page_loaded()
        table = self.browser.find_elements(by=By.XPATH, value=f"{self.parent_xpath}")[self.table_number-1]
        rows = table.find_elements(by=By.XPATH, value=".//tbody/tr")
        header_index = self.get_headers().index(column_name)
        for row in rows:
            if row_value in [r.trim() for r in row.text.split("\n")]:
                row.find_element(by=By.XPATH, value=f"./td[{header_index + 1}]").click()
        raise NoSuchElement(f"Can't find row with '{row_value}' and column {column_name} to click")

    def click_in_cell_by_value(self, row_value, value_in_cell):
        self.wait_page_loaded()
        table = self.browser.find_elements(by=By.XPATH, value=f"{self.parent_xpath}")[self.table_number-1]
        rows = table.find_elements(by=By.XPATH, value=".//tbody/tr")
        # header_index = self.get_headers().index(value_in_cell)
        for row in rows:
            # if row_value in [r.strip() for r in row.text.split("\n")]:
            if row_value in [cell.text for cell in row.find_elements(by=By.XPATH, value=f".//td")]:
                row.find_element(by=By.XPATH, value=f".//*[contains(text(), '{value_in_cell}')]").click()
                self.wait_page_loaded()
                return
        raise NoSuchElement(f"Can't find row with '{row_value}' and cell {value_in_cell} to click")

    def click_in_row(self, row_value):
        self.wait_page_loaded(delay=2)
        table = self.browser.find_elements(by=By.XPATH, value=f"{self.parent_xpath}")[self.table_number-1]
        rows = table.find_elements(by=By.XPATH, value=".//tbody/tr")
        for row in rows:
            # if row_value in [r.strip() for r in row.text.split("\n")]:
            if row_value in [cell.text.strip() for cell in row.find_elements(by=By.XPATH, value=f".//td")]:
                row.find_element(by=By.XPATH, value=f".//td").click()
                self.wait_page_loaded(delay=2)
                return
        raise NoSuchElement(f"Can't find row with '{row_value}' to click")

    def select_row_by_value(self, row_value):
        self.wait_page_loaded()
        table = self.browser.find_elements(by=By.XPATH, value=f"{self.parent_xpath}")[self.table_number-1]
        rows = table.find_elements(by=By.XPATH, value=".//tbody/tr")
        for row in rows:
            if row_value in [cell.text for cell in row.find_elements(by=By.XPATH, value=f".//td")]:
                row.find_element(by=By.XPATH, value=f".//*[contains(@class, 'chakra-checkbox__control')]").click()
                return
        raise NoSuchElement(f"Can't find row with '{row_value}' to click")

    def click_in_row_by_number_with_value(self, row_by_number, value_in_cell):
        self.wait_page_loaded()
        table = self.browser.find_elements(by=By.XPATH, value=f"{self.parent_xpath}")[self.table_number-1]
        rows = table.find_elements(by=By.XPATH, value=".//tbody/tr")
        rows[row_by_number].find_element(by=By.XPATH, value=f".//*[contains(text(), '{value_in_cell}')]").click()
        self.wait_page_loaded()

    def get_inner_body_text(self):
        self.wait_page_loaded()
        return self.browser.find_element(by=By.XPATH, value=f"{self.parent_xpath}//tbody").text

    # get label like: '14 operations'
    def get_table_summary_info(self, filter_above_table=False, delay=1):
        self.wait_page_loaded(delay=delay)
        if filter_above_table:
            return self.browser.find_element(by=By.XPATH, value=f"{self.parent_xpath}//../../div[4]").text
        return self.browser.find_element(by=By.XPATH, value=f"{self.parent_xpath}//../../div[2]").text

