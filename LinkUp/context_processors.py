import time

def version(request):
    return {
        'version': time.time()
    }
