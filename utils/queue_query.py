from collections import deque


class QueueQuery(object):

    def __init__(self, size):
        self.query_queue = deque([], maxlen=size)

    def add(self, speaker: str, turn_data: dict):
        self.query_queue.append({"speaker": speaker, "info": turn_data})

    def get_last_turn(self):
        return self.query_queue[-1]
