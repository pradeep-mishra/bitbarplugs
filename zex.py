#!/bin/bash

#
# Include BitBar metadata like this at the top of the file
# (commented out, of course):
#
# <bitbar.title>My Position</bitbar.title>
# <bitbar.version>v1.0</bitbar.version>
# <bitbar.author>Pradeep Mishra</bitbar.author>
# <bitbar.author.github>ipradeep-mishra</bitbar.author.github>
# <bitbar.desc>Test</bitbar.desc>
# <bitbar.image>https://camo.githubusercontent.com/5cec3248a9fc4eede235ead682a65f977577f670/68747470733a2f2f7261772e6769746875622e636f6d2f6d6174727965722f6269746261722f6d61737465722f446f63732f4269744261722d4578616d706c652d4d656e752e706e67</bitbar.image>
# <bitbar.abouturl>https://github.com/pradeep-mishra/bitbarplugs/new/master/zex.py</bitbar.abouturl>
#

import urllib2

url = "http://localhost:9090/get"
response = urllib2.urlopen(url).read()
echo response
