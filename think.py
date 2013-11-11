import urllib2,re,urlparse,urllib,os,sys,shutil
from bs4 import BeautifulSoup
def download_progress(count, block_size, total_size):
    percent = int( (count*block_size*100)/total_size )
    sys.stdout.write("\r[" + '#' * (percent/2) + '-' * (50 - percent/2) + "] %3d%% of %d MB" % (percent, total_size/(1024 * 1024)) )
response = urllib2.urlopen('http://think.vsworld.com/vod.php')
html=response.read()
x=[]
for i,line in enumerate(html.splitlines(True)):
	x.append(line)
print 'Input Title'
title=raw_input()
title=title.upper()
j=0
link=''
for i in x:
	if title in i:
		link=x[j-2]
	j+=1 
loc=link[-27:-4]
if os.path.exists(loc):
                print '[!] \"%s\" already exists on disk, skipping!' % (title, )
else:        
                urllib.urlretrieve(link[12:-4], loc, reporthook=download_progress)


x=open(loc,'r')
y=re.findall(loc[:-5]+'.*\.ts',x.read())
x=open(title+'.ts','wb')
for i in y:
	print i
	urllib.urlretrieve('https://s3-ap-southeast-1.amazonaws.com/thinkgoa/'+loc[0].upper()+loc[1:5]+'/'+i,i,reporthook=download_progress)
	shutil.copyfileobj(open(i,'rb'), x)
	os.remove(i)	
	print ''

os.remove(loc)

