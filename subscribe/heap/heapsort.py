from heapq import *
def heap_sort(iterable):
    h = []
    for value in iterable:
        heappush(h,value)
    return [heappop(h) for _ in range(len(h))]

if __name__ == '__main__':
    print(heap_sort(...))
