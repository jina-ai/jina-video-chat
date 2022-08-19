# video-chat

Jina-powered multi-user video chat, to showcase how to use to build a real-time streaming solution.

<img width="350" alt="image" src="https://user-images.githubusercontent.com/2041322/185621065-a54d185f-b4fa-4f73-8a70-e24e2b3a7c17.png">

## Prerequisites

First, you need a webcam.

```bash
pip install -U jina docarray
```

## Run server

Server **doesn't need** a webcam of course.

```bash
git clone https://github.com/hanxiao/video-chat.git
cd video-chat
jina flow --uses flow.yml
```

Note down the server address:

![](.github/server.png)

### Run client

```bash
pip install opencv-python

git clone https://github.com/hanxiao/video-chat.git
cd video-chat
python client.py grpcs://your-server-address-from-last-image johannes
```

where `johannes` is the name of the user, must be different from other users.
