from selenium import webdriver

proxyIP = "127.0.0.1"
proxyPort = 9150

'''proxy_settings = {"network.proxy.type": 1,
                  "network.proxy.ssl": proxyIP,
                  "network.proxy.ssl_port": proxyPort,
                  "network.proxy.socks": proxyIP,
                  "network.proxy.socks_port": proxyPort,
                  "network.proxy.socks_remote_dns": True,
                  "network.proxy.ftp": proxyIP,
                  "network.proxy.ftp_port": proxyPort
                  }'''

profile = webdriver.FirefoxProfile()
profile.set_preference("network.proxy.type", 1)
profile.set_preference("network.proxy.ssl", proxyIP)
profile.set_preference("network.proxy.ssl_port", proxyPort)
profile.set_preference("network.proxy.socks", proxyIP)
profile.set_preference("network.proxy.socks_port", proxyPort)
profile.set_preference("network.proxy.socks_remote_dns", True)
profile.set_preference("network.proxy.ftp", proxyIP)
profile.set_preference("network.proxy.ftp_port", proxyPort)


driver = webdriver.Firefox(profile)
driver.get("http://zqktlwi4fecvo6ri.onion/wiki/index.php/Main_Page")