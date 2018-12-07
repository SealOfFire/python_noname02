#coding:utf-8
from LogHandle import Logger
import urllib3

http = urllib3.PoolManager()
#s=http.urlopen(method='GET', url='http://hao.163.com',redirect=False)
#print(s.status)
#print(s.get_redirect_location())
#r = http.request('GET', u'http://hao.163.com',)
#print(r.geturl())
#print(r.status)
#print(r.data.decode())
pass

def getHttpStatusCode2(url, result):
	'''
	获取http状态吗
	'''
	Logger.debug(u'---- getHttpStatusCode2 ---- BEGIN ----')
	Logger.debug(u'---- params1:url:%s ----' % url)
	status = ''
	try:
		r = http.urlopen(method='GET', url=url, redirect=False)
		status = r.status
		result.append([url,status])
		Logger.info("%s : %s" % (url, status))

		if(status in [301,302]):
			redirect = r.get_redirect_location()
			Logger.debug(u'重定向url:%s' % redirect)
			return getHttpStatusCode2(redirect,result)
	except urllib3.exceptions.MaxRetryError as e:
		Logger.debug(u'---- return ----')
		result.append([url,'链接无效'])
		return '链接无效'
	except:
		raise
	else:
		return status
		Logger.debug(u'---- return1:%s ----' % status)
		Logger.debug(u'---- getHttpStatusCode2 ---- END ----')

result = []
print(getHttpStatusCode2('http://hao.163.com',result))

pass