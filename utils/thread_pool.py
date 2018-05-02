#!/usr/bin/env python
# -*- coding: utf-8 -*-

import threading 
import Queue 
import traceback

class ThreadWorker(threading.Thread):
    def __init__(self, job_queue, result_queue):
        super(ThreadWorker, self).__init__()
        self.setDaemon(True)
        self.jobs = job_queue
        self.results = result_queue 

    def run(self):
        while True:
            try:
                func, arg, kwarg = self.jobs.get()
                ret = func(arg, kwarg)
                self.jobs.task_done()
            except Queue.Empty:
                pass
            except Exception as e:
                traceback.print_exc() 


class ThreadPool(object):
    Pool = set()
    def __init__(self, pool_size):
        self.pool_size = pool_size
        self.jobs = Queue.Queue() 
        self.results = Queue.Queue()
        self.init_pool()
        self.start()

    def init_pool(self):
        for i in range(self.pool_size):
            worker = ThreadWorker(self.jobs, self.results)
            self.Pool.add(worker)

    def start(self):
        for t in self.Pool:
            t.start()

    def add_job(self, callback, *args, **kwarg):
        self.jobs.put((callback, args, kwarg))


GThreadPool = ThreadPool(20)
