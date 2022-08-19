# video-chat

Jina-powered multi-user video chat, to showcase how to use to build a real-time streaming solution.

![da55389b1126b937e0c1d451ac54bac9 (1)](https://user-images.githubusercontent.com/2041322/185625220-40c1f887-3be4-49df-9318-c49e0fb7365e.gif)


Or you can call it **_Joom_**!


## Prerequisites

First, you need a webcam.


## Run server

Server **doesn't need** a webcam of course.

```bash
pip install -U jina
git clone https://github.com/hanxiao/video-chat.git
cd video-chat
jina flow --uses flow.yml
```

Note down the server address:

![](.github/server.png)

### Run client

```bash
pip install opencv-python
pip install -U jina docarray
git clone https://github.com/hanxiao/video-chat.git
cd video-chat
python client.py grpcs://your-server-address-from-last-image johannes
```

where `johannes` is the name of the user, must be different from other users.
