import numpy as np
from jina import Executor, requests, DocumentArray


class VideoChatExecutor(Executor):
    last_user_frames = {}

    @requests
    def foo(self, docs: DocumentArray, **kwargs):
        for d in docs:
            cv2.putText(
                d.tensor,
                d.tags.get('user', 'anonymous'),
                (7, 500),
                cv2.FONT_HERSHEY_SIMPLEX,
                3,
                (100, 255, 0),
                3,
                cv2.LINE_AA,
            )

            self.last_user_frames[d.tags['user']] = d.tensor

            if len(self.last_user_frames) > 1:
                d.tensor = np.concatenate(list(self.last_user_frames.values()), axis=0)
