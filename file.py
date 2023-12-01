import pywifi
import time
from pywifi import const
 
# WiFi scanner
def wifi_scan():
    # initialise wifi
    wifi = pywifi.PyWiFi()
    # use the first interface
    interface = wifi.interfaces()[0]
    # start scan
    interface.scan()
    for i in range(4):
        time.sleep(1)
        print('\rScanning WiFi, please wait...（' + str(3 - i), end='）')
    print('\rScan Completed！\n' + '-' * 38)
    print('\r{:4}{:6}{}'.format('No.', 'Strength', 'wifi name'))
    # Scan result，scan_results() returns a set, each being a wifi object
    bss = interface.scan_results()
    # a set storing wifi name
    wifi_name_set = set()
    for w in bss:
        # dealing with decoding
        wifi_name_and_signal = (100 + w.signal, w.ssid.encode('raw_unicode_escape').decode('utf-8'))
        wifi_name_set.add(wifi_name_and_signal)
    # store into a list sorted by signal strength
    wifi_name_list = list(wifi_name_set)
    wifi_name_list = sorted(wifi_name_list, key=lambda a: a[0], reverse=True)
    num = 0
    # format output
    while num < len(wifi_name_list):
        print('\r{:<6d}{:<8d}{}'.format(num, wifi_name_list[num][0], wifi_name_list[num][1]))
        num += 1
    print('-'…
