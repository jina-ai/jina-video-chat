import time
import sys
import cv2

if len(sys.argv) == 3:
    server_address = sys.argv[1]
    user = sys.argv[2]
else:
    print('Usage: ./client.py <server_address> <user>')
    sys.exit(1)

prev_frame_time = time.perf_counter()


def render_recv(resp):
    global prev_frame_time

    fps = 1 / (time.perf_counter() - prev_frame_time)

    prev_frame_time = time.perf_counter()

    for d in resp.docs:
        frame = d.tensor
        # putting the FPS count on the frame
        cv2.putText(
            frame,
            f'FPS {fps:0.0f}',
            (7, 70),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (100, 255, 0),
            3,
            cv2.LINE_AA,
        )

        # displaying the frame with fps
        cv2.imshow('output', frame)


from jina import Client
from docarray import Document

c = Client(host=server_address)
c.post(
    '/',
    Document.generator_from_webcam(tags={'user': user}, show_window=False, height_width=(200, 300)),
    on_done=render_recv,
    request_size=1,
)
