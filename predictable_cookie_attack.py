from attack import Attack
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import subprocess
import time
import json
import os

class PredictableCookieAttack(Attack):
    def __init__(self, link, form_parameter, button, cookie):
        super(PredictableCookieAttack, self).__init__(link, form_parameter, button, cookie, "predictable_cookie")

    def perform(self, output_path):
        print "start predictable_cookie_attack."
        print "=============== TRY: session predictable cookie attack ========================"
        wd = webdriver.Firefox()

        try:
            wd.get(self.link)
            wd.find_element_by_xpath("//input[@name='" + self.form_parameter["account"] + "']").send_keys(self.form_parameter["account_value"])
            wd.find_element_by_xpath("//input[@name='" + self.form_parameter["password"] + "']").send_keys(self.form_parameter["password_value"])
            if self.button == '//form//a[@class="button"]':
                wd.find_element_by_xpath(self.button).click()
            else:
                try:
                    wd.find_element_by_xpath("//input[@value='" + self.button + "']").click()
                except NoSuchElementException:
                    wd.find_element_by_xpath("//button[@value='" + self.button + "']").click()
            first_cookie = ""
            for cookie in wd.get_cookies():
                if cookie["name"] == self.cookie["name"]:
                    first_cookie = cookie["value"]
                    break
            print "first cookie is %s" % first_cookie
            wd.close()
            wd = webdriver.Firefox()
            wd.get(self.link)
            wd.find_element_by_xpath("//input[@name='" + self.form_parameter["account"] + "']").send_keys(self.form_parameter["account_value"])
            wd.find_element_by_xpath("//input[@name='" + self.form_parameter["password"] + "']").send_keys(self.form_parameter["password_value"])
            if self.button == '//form//a[@class="button"]':
                wd.find_element_by_xpath(self.button).click()
            else:
                try:
                    wd.find_element_by_xpath("//input[@value='" + self.button + "']").click()
                except NoSuchElementException:
                    wd.find_element_by_xpath("//button[@value='" + self.button + "']").click()
            second_cookie = ""
            for cookie in wd.get_cookies():
                if cookie["name"] == self.cookie["name"]:
                    second_cookie = cookie["value"]
                    break
            print "second cookie is %s" % second_cookie
            wd.close()
            if "increment" in self.cookie:
                if int(second_cookie) == int(first_cookie) + int(self.cookie["increment"]):
                    exploit = {
                        "page": self.link,
                        "cookie": [{
                            "name": self.cookie["name"],
                            "secure": self.cookie["secure"],
                            "httpOnly": self.cookie["httpOnly"],
                            "attack": ["predictableCookie"]
                        }]
                    }
                    self.phase4_output(exploit, output_path)
                    print "CONFIRMED: increment predictable cookie attack successful."
                else:
                    print "CONFIRMED: not a valid increment predictable cookie issue."
            elif "constant":
                if second_cookie == first_cookie:
                    print "CONFIRMED: constant predictable cookie attack successful."
                    exploit = {
                        "page": self.link,
                        "cookie": [{
                            "name": self.cookie["name"],
                            "secure": self.cookie["secure"],
                            "httpOnly": self.cookie["httpOnly"],
                            "attack": ["predictableCookie"]
                        }]
                    }
                    self.phase4_output(exploit, output_path)
                else:
                    print "CONFIRMED: not a valid constant predictable cookie issue."
            else:
                print "CONFIRMED: not a recognizable predictable cookie issue."
        except NoSuchElementException:
            print "ERROR: not a recognizable predictable cookie issue."

    def phase4_output(self, source, output_path):
        try:
            if os.stat(output_path).st_size > 0:
                with open(output_path) as f:
                    data = json.load(f)
                data.append(source)
                with open(output_path, 'w') as f:
                    json.dump(data, f)
            else:
                with open(output_path, 'w') as f:
                    json.dump([source], f)
        except OSError:
            with open(output_path, 'w+') as f:
                json.dump([source], f)
