# SST-EYE
Spider a web server for forms where it inputs a simple math Server Side Template Injection(SSTI) payload to test for exploitation


### use
python3 ssteye.py xxx.com


python3 ssteye.py -f list-of-ips.txt



### how it works


tests for ssti with math thats +49(can change in code) it finds the a form on a site then fills it out from the ssti_testpram.txt list and checks for str 48

change it if you dont want false + but i use it for ctfs
