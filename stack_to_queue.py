"""Module for transformation stack to queue"""
from arraystack import ArrayStack
from arrayqueue import ArrayQueue
from copy import deepcopy


def stack_to_queue(stack: ArrayStack) -> ArrayQueue:
    """
    Converts stack to queue and returns Queue object
    """
    queue = ArrayQueue()
    copy_of_stack = deepcopy(stack)

    while not copy_of_stack.isEmpty():
        queue.add(copy_of_stack.pop())

    return queue
