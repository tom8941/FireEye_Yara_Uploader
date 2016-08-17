# FireEye_Yara_Uploader

This is a little script that give the possibility to upload yara file automatically on fireeye cms.
By combining this project with this other one to export yara from MISP: MISP-IOC-Validator (https://github.com/tom8941/MISP-IOC-Validator),
you can get an export of validated yara rules from MISP and upload it automatically into FireEye CMS.

## Prerequisite

- install of the following module:
 - selenium for python (http://selenium-python.readthedocs.io/installation.html)
- The server should have a X server running
- Be sure that the X session of the user that is running the script is open (you can even "lock the screen" of the Desktop session)
- xterm should be installed on the system
- This script has been desgined to run with Firefox only (some Firefox version may be incompatible with some selenium version)

## Usage and Examples

```
parameters : 
  -f FILE, --file FILE  yara file to upload
  -c CMS, --cms CMS     cms ip or hostname
  -u USER, --user USER  cms user account
  -p PASSWORD, --password PASSWORD

DISPLAY=:0 xterm -e './fe_yara_uploader.py -u user -p password -c cmsfireeye.local  -f /tmp/yara_rules.yml

If there is some errors you can add -hold option in front of xterm to let the Xwindow open
```

You can modify time.sleep() in the script if you want. There are not always necessary.

## External Source
 
selenium : http://www.seleniumhq.org/
MISP-IOC-Validator : https://github.com/tom8941/MISP-IOC-Validator
