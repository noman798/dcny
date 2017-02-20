import traceback


def retry(times):
    def _(func):
        def __(*args, **kwds):
            count = 0
            while 1:
                try:
                    return func(*args, **kwds)
                except:
                    if count == times:
                        return
                    count += 1
                    traceback.print_exc()
        return __
    return _
