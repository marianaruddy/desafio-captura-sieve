from urllib.parse import urlparse

def get_domain_name(url):
    try:
        results = get_sub_domain_name(url).split('.')
        print(results[-2] + '.' + results[-1])
        if results[-2] == 'com':
            return results[-3] + '.' + results[-2]
        return results[-2] + '.' + results[-1]
        
    except:
        return ''
def get_sub_domain_name(url):
    try:
        return urlparse(url).netloc
    except:
        return ''
