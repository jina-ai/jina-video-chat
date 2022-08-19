import numpy as np
from jina import Executor, requests


class VideoChatExecutor(Executor):
    last_user_frames = {}

    @requests
    def foo(self, docs, **kwargs):
        for d in docs:

            self.last_user_frames[d.tags['user']] = d.tensor

            if len(self.last_user_frames) > 1:
                d.tensor = np.concatenate(list(self.last_user_frames.values()), axis=0)
