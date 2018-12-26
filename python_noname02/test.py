#coding:utf-8
from LogHandle import Logger
import urllib3
import os

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
		r = http.urlopen(method='GET', url=url, timeout=10, retries=False, redirect=False)
		status = r.status
		result.append([url,status])
		Logger.info("%s : %s" % (url, status))
		host = urllib3.get_host(url)
		if(status in [301,302]):
			redirect = r.get_redirect_location()
			if(urllib3.get_host(redirect)[1] == None):
				redirect = host[0] + '://' + host[1] + '/' + redirect
			Logger.debug(u'重定向url:%s' % redirect)
			if(redirect==url):
				# 自己重定向自己，跳出
				pass
			else:
				return getHttpStatusCode2(redirect,result)
	except urllib3.exceptions.MaxRetryError as e:
		Logger.debug(u'---- return ----')
		result.append([url,'链接无效'])
		return '链接无效'
	except urllib3.exceptions.ConnectTimeoutError as e:
		# 链接超时
		Logger.debug(u'---- return ----')
		result.append([url,'链接超时'])
		return '链接超时'
	except urllib3.exceptions.SSLError as e:
		# 链接超时
		Logger.debug(u'---- return ----')
		result.append([url,'SSLError'])
		return 'SSLError'
	except ConnectionResetError as e:
		raise
	except urllib3.exceptions.ProtocolError as e:
		raise
	except:
		raise
	else:
		return status
		Logger.debug(u'---- return1:%s ----' % status)
		Logger.debug(u'---- getHttpStatusCode2 ---- END ----')

result = []
print(getHttpStatusCode2('12ccce.cn',result))
