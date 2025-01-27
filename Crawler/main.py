import threading
from queue import Queue
from spider import Spider
from domain import *
from general import *

PROJECT_NAME = 'epocacosmeticos'
HOMEPAGE = 'http://www.epocacosmeticos.com.br/'
DOMAIN_NAME = get_domain_name(HOMEPAGE)
QUEUE_FILE = PROJECT_NAME + '/queue.csv'
CRAWLED_FILE = PROJECT_NAME + '/crawled.csv'
NUMBER_OR_THREADS = 8
queue = Queue()
Spider(PROJECT_NAME, HOMEPAGE, DOMAIN_NAME)

def create_workers():
    for _ in range(NUMBER_OR_THREADS):
        t = threading.Thread(target=work)
        t.deamon = True
        t.start()

def work():
    while True:
        url = queue.get()
        Spider.crawl_page(threading.current_thread().name, url)
        queue.task_done()

def create_jobs():
    for link in file_to_set(QUEUE_FILE):
        queue.put(link)
    queue.join()
    crawl()

def crawl():
    queued_links = file_to_set(QUEUE_FILE)
    if len(queued_links) > 0:
        print(str(len(queued_links)) + ' links in the queue')
        create_jobs()

create_workers()
crawl()