import time
import json
import pickle
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
import ReportingModule as Report
import datetime as dt
import keyboard
import win32api, win32con
'''
lReference: https://stackoverflow.com/questions/37088589/selenium-wont-open-a-new-url-in-a-new-tab-python-chrome
https://stackoverflow.com/questions/28431765/open-web-in-new-tab-selenium-python
https://stackoverflow.com/questions/39281806/python-opening-multiple-tabs-using-selenium
'''

class linkedinApply:
    """Allows user to apply on LinkedIn with easy apply

    Attributes:
        username: username for LinkedIn account
        password: password for LinkedIn account
        driverPath: webdriver path for browser driver (Chrome, phantomjs, firefox, etc...)

    """
    def __init__(self, phone, username, password, driverPath, jobTitle, state, resumeLocation, num_loops, follow_company=None, city=None):
        self.username = username
        self.password = password
        self.driverPath = driverPath
        self.city = city
        self.state = state
        self.jobTitle = jobTitle
        self.resumeLocation = resumeLocation
        self.phone = phone
        self.num_loops = num_loops

        if follow_company:
            self.follow_company = "Yes"

        self.currentPageJobsList = []
        self.allEasyApplyJobsList=[]
        self.failedEasyApplyJobsList=[]
        self.appliedEasyApplyJobsList=[]

    def url_generator(self):
        """Generates url for LinkedIn job search with location and job title"""
        base = "https://www.linkedin.com/jobs/search/?keywords="
        jobTitle = self.jobTitle.replace(" ","%20")+"&location="
        state = self.state.replace(" ","%20")

        if self.city:
            city = self.city.replace(" ","%20")+"%2C%20"
            url = base+jobTitle+city+state+"&start=30"
        else:
            url = base + jobTitle + state + "&start=30"

        print(url)
        return url

    def click(self, x,y):
        """Mouse event click for webdriver"""
        win32api.SetCursorPos((x,y))
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)

    def init_driver(self):
        """Initializes instance of webdriver"""
        self.driver = webdriver.Chrome(executable_path=self.driverPath)
        self.driver.wait = WebDriverWait(self.driver, 10)
        return self.driver

    def login(self):
        """Logs into LinkedIn.com"""
        self.driver.get("https://www.linkedin.com/")
        try:
            user_field = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, 'login-email')))

            pw_field = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, 'login-password')))

            login_button = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, 'login-submit')))

            user_field.send_keys(self.username)
            user_field.send_keys(Keys.TAB)
            time.sleep(1)
            pw_field.send_keys(self.password)
            time.sleep(1)
            login_button.click()
        except TimeoutException:
            print("TimeoutException! Username/password field or login button not found on glassdoor.com")

    def searchJobs(self):
        """Searches LinkedIn for jobs matching supplied phrase"""
        url = self.url_generator()
        self.driver.get(url)
        time.sleep(5)

        #Click classic view button
        classic_view_btn = self.driver.find_elements_by_class_name('jobs-search-dropdown__trigger')
        classic_view_btn[1].click()
        time.sleep(1)

        sub_classic_btn = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'jobs-search-dropdown__option-button--single')))

        sub_classic_btn.click()
        time.sleep(1)

        dicts = []

        print(int(self.num_loops))
        for x in range(0, int(self.num_loops)):
            pane = self.driver.find_element_by_class_name("jobs-search-results")

            # start from your target element, here for example, "header"
            all_li = pane.find_elements_by_tag_name("li")

            try:
                for x in all_li:
                    all_children_by_xpath = x.find_elements_by_xpath(".//*")

                    try:
                        #Get link to apply
                        link = x.find_element_by_class_name("job-card-search__link-wrapper")
                        tag = link.get_attribute("href")

                        #Obtain Basic Job Info
                        jobtitle = x.find_element_by_class_name("job-card-search__title").text
                        location = x.find_element_by_class_name("job-card-search__location").text
                        location = location.splitlines()[1]

                        company = x.find_element_by_class_name("job-card-search__company-name").text

                        #Set easy apply to true by default
                        easy_bool = True

                        #If not found then set easy bool to false
                        try:
                            easyapply = x.find_element_by_class_name("job-card-search__easy-apply")
                        except:
                            easy_bool = False

                        #If true apply to job
                        if easy_bool == True:
                            if tag:
                                self.apply_to_job(tag)
                                status = True
                            else:
                                status = False
                        else:
                            status = False

                        l = []
                        # generate dictionary for reporting
                        values = [company, jobtitle, location, easy_bool, status]
                        for v in values:
                            l.append(v)
                        dicts.append(l)

                    except Exception as e:
                        print(str(e))
                        pass

                #Here we try to paginate through if possible
                try:
                    next_button = WebDriverWait(self.driver, 10).until(
                        EC.presence_of_element_located((By.CLASS_NAME, 'next')))

                    self.driver.execute_script("arguments[0].click();", next_button)

                except Exception as e:
                    print(str(e))

            except Exception as e:
                print(str(e))

        self.driver.quit()

        return dicts

    def answerForm1(self):
        try:
            #Here we need to account for different application windows
            time.sleep(1)
            try:
                phone_input = WebDriverWait(self.driver, 3).until(EC.presence_of_element_located((By.ID, 'apply-form-phone-input')))
                phone_input.clear()
                phone_input.send_keys(self.phone)
                time.sleep(1)
            except Exception as e:
                print(str(e))

            try:
                resumeBtn = WebDriverWait(self.driver, 3).until(
                    EC.presence_of_element_located((By.ID, 'file-browse-input')))
                resumeBtn.send_keys(self.resumeLocation)
                time.sleep(1)
            except Exception as e:
                print(str(e))

            try:
                form_submit_btn = WebDriverWait(self.driver, 3).until(
                    EC.presence_of_element_located((By.CLASS_NAME, 'jobs-apply-form__submit-button')))
                form_submit_btn.click()
            except Exception as e:
                print(str(e))

            print("Successfully applied to job!")
            time.sleep(3)

        except:
            print("Primary Form Invalid. Switching to secondary....")
            self.answerForm2()

    def answerForm2(self):
        try:
            try:
                text_fields = self.driver.find_elements_by_class_name("ember-text-field")
                time.sleep(1)
                text_fields[0].send_keys(self.phone)
                time.sleep(2)
            except Exception as e:
                print(str(e))

            try:
                work_auth_check = self.driver.find_element_by_class_name("ember586-answer")
                work_auth_check.click()
                time.sleep(2)
            except Exception as e:
                print(str(e))

            try:
                work_auth_check_two = self.driver.find_element_by_class_name("ember592-answer")
                work_auth_check_two.click()
                time.sleep(2)
            except Exception as e:
                print(str(e))

                # self.driver.execute_script("window.scrollTo(0, Y)")
            try:
                form_submit_btn = WebDriverWait(self.driver, 3).until(
                    EC.presence_of_element_located((By.CLASS_NAME, 'jobs-apply-form__submit-button')))
                form_submit_btn.click()
            except Exception as e:
                print(str(e))

            print("Successfully applied to job!")
            time.sleep(10)
        except:
            print("Primary Form Invalid. Switching to auxillary....")
            self.answerForm3()

    def answerForm3(self):
        try:
            try:
                form_submit_btn = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((By.CLASS_NAME, 'continue-btn')))
                form_submit_btn.click()
            except Exception as e:
                print(str(e))

            print("Successfully applied to job!")
            time.sleep(10)

        except Exception as e:
            print('No forms valid...')
            print(str(e))

    def apply_to_job(self, url):
        #Get main window
        current_window = self.driver.current_window_handle
        self.driver.execute_script('window.open(arguments[0]);', url)

        #Go to app window
        new_window = [window for window in self.driver.window_handles if window != current_window][0]
        self.driver.switch_to.window(new_window)

        #Set init status
        status = False

        #Look for easy apply button
        try:
            easyApplyBtn = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.CLASS_NAME, 'jobs-s-apply__button')))
            easyApplyBtn.click()

            try:
                self.answerForm1()
                status = True
            except:
                status = False

        except:
            print("You have already applied to this job!")
            time.sleep(3)

        # Execute required operations to switch back
        self.driver.close()
        self.driver.switch_to.window(current_window)

        return status
