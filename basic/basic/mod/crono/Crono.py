


import time

class Crono:
    
    start_time = None

    def start():
        Crono.start_time = time.time()

    def stop():
        end_time = time.time()
        elapsed_time = end_time - Crono.start_time
        return elapsed_time