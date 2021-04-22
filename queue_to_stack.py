"""Module for transformation queue to stack"""
from arraystack import ArrayStack
from arrayqueue import ArrayQueue
from copy import deepcopy


def queue_to_stack(queue: ArrayQueue) -> ArrayStack:
    """
    Converts queue to stack and returns Stack object
    """
    stack = ArrayStack()
    copy_of_queue = deepcopy(queue)

    for ind in range(len(queue), 0, -1):
        ind -= 1
        stack.add(copy_of_queue.remove(ind))

    return stack
