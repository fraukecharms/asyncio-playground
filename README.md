# `asyncio` Playground

Some introductory `asyncio` examples including the new `TaskGroup` API in Python 3.11.

## Installation

Create and activate a virtual environment.
```shell
python3 -m venv ~/.asyncio-playground
source ~/.asyncio-playground/bin/activate
```

Upgrade pip and install requirements.
```shell
pip install --upgrade pip
pip install -r requirements.txt
```


## Usage

Start an iPython shell in the `src` directory. 
```shell
cd src
ipython
```

Load the `autoreload` extension.
```python
%load_ext autoreload
%autoreload 2
```

And have fun :).
```python
import coroutines_and_tasks.ex4_gather_vs_taskgroup as ex4
ex4.main(entrypoint=ex4.entrypoint_taskgroup)
```


## References
### Blog Posts

* [Waiting in asyncio by Hynek Schlawack (updated in 2023)](https://hynek.me/articles/waiting-in-asyncio/)

* [Making 1 million requests with python-aiohttp by  Paweł Miech (updated in 2023)](https://pawelmhm.github.io/asyncio/python/aiohttp/2016/04/22/asyncio-aiohttp.html)

* [Weekly Report, November 22 - 28 2021 by Łukasz Langa](https://lukasz.langa.pl/6d439b86-3834-481a-b95c-ac9c6956545b/)

* [The Heisenbug lurking in your async code by Will McGugan](https://textual.textualize.io/blog/2023/02/11/the-heisenbug-lurking-in-your-async-code/#the-heisenbug-lurking-in-your-async-code)



### EuroPython2023 Talk by Junya Fukuda

[Asyncio Evolved: Enhanced Exception Handling with TaskGroup in Python 3.11](https://ep2023.europython.eu/session/asyncio-evolved-enhanced-exception-handling-with-taskgroup-in-python-311)

[Slides](https://speakerdeck.com/jrfk/asyncio-evolved-enhanced-exception-handling-with-taskgroup-in-python-3-dot-11-europython-2023?slide=33) &emsp; [Code](https://github.com/jrfk/talk/tree/main/EuroPython2023) &emsp; [Youtube](https://youtu.be/y_upeUWmOeU?t=8364)
