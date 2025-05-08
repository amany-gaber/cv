    return self.real_target(sockets)
  File "/home/docker/venv/lib/python3.9/site-packages/uvicorn/server.py", line 66, in run
    return asyncio.run(self.serve(sockets=sockets))
  File "/usr/lib/python3.9/asyncio/runners.py", line 44, in run
    return loop.run_until_complete(main)
  File "/usr/lib/python3.9/asyncio/base_events.py", line 642, in run_until_complete
    return future.result()
  File "/home/docker/venv/lib/python3.9/site-packages/uvicorn/server.py", line 70, in serve
    await self._serve(sockets)
  File "/home/docker/venv/lib/python3.9/site-packages/uvicorn/server.py", line 77, in _serve
    config.load()
  File "/home/docker/venv/lib/python3.9/site-packages/uvicorn/config.py", line 435, in load
    self.loaded_app = import_from_string(self.app)
  File "/home/docker/venv/lib/python3.9/site-packages/uvicorn/importer.py", line 19, in import_from_string
    module = importlib.import_module(module_str)
  File "/usr/lib/python3.9/importlib/__init__.py", line 127, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
  File "<frozen importlib._bootstrap>", line 1030, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1007, in _find_and_load
  File "<frozen importlib._bootstrap>", line 986, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 680, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 855, in exec_module
  File "<frozen importlib._bootstrap>", line 228, in _call_with_frames_removed
  File "/home/docker/app/main.py", line 3, in <module>
    from routes import router
  File "/home/docker/app/routes/__init__.py", line 3, in <module>
    from .user import router
  File "/home/docker/app/routes/user.py", line 10, in <module>
    job_matcher = JobMatcher()
  File "/home/docker/app/services/main.py", line 29, in __init__
    raise ValueError(self.error)
ValueError: File not found: /home/yaz/specific_job/api/src/static/job_data.csv
Process SpawnProcess-267:
Traceback (most recent call last):
  File "/usr/lib/python3.9/multiprocessing/process.py", line 315, in _bootstrap
    self.run()
  File "/usr/lib/python3.9/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/home/docker/venv/lib/python3.9/site-packages/uvicorn/_subprocess.py", line 80, in subprocess_started
    target(sockets=sockets)
  File "/home/docker/venv/lib/python3.9/site-packages/uvicorn/supervisors/multiprocess.py", line 63, in target
    return self.real_target(sockets)
  File "/home/docker/venv/lib/python3.9/site-packages/uvicorn/server.py", line 66, in run
    return asyncio.run(self.serve(sockets=sockets))
  File "/usr/lib/python3.9/asyncio/runners.py", line 44, in run
    return loop.run_until_complete(main)
  File "/usr/lib/python3.9/asyncio/base_events.py", line 642, in run_until_complete
    return future.result()
  File "/home/docker/venv/lib/python3.9/site-packages/uvicorn/server.py", line 70, in serve
    await self._serve(sockets)
  File "/home/docker/venv/lib/python3.9/site-packages/uvicorn/server.py", line 77, in _serve
    config.load()
  File "/home/docker/venv/lib/python3.9/site-packages/uvicorn/config.py", line 435, in load
    self.loaded_app = import_from_string(self.app)
  File "/home/docker/venv/lib/python3.9/site-packages/uvicorn/importer.py", line 19, in import_from_string
    module = importlib.import_module(module_str)
  File "/usr/lib/python3.9/importlib/__init__.py", line 127, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
  File "<frozen importlib._bootstrap>", line 1030, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1007, in _find_and_load
  File "<frozen importlib._bootstrap>", line 986, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 680, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 855, in exec_module
  File "<frozen importlib._bootstrap>", line 228, in _call_with_frames_removed
  File "/home/docker/app/main.py", line 3, in <module>
    from routes import router
  File "/home/docker/app/routes/__init__.py", line 3, in <module>
    from .user import router
  File "/home/docker/app/routes/user.py", line 10, in <module>
    job_matcher = JobMatcher()
  File "/home/docker/app/services/main.py", line 29, in __init__
    raise ValueError(self.error)
ValueError: File not found: /home/yaz/specific_job/api/src/static/job_data.csv
Process SpawnProcess-265:
Traceback (most recent call last):
  File "/usr/lib/python3.9/multiprocessing/process.py", line 315, in _bootstrap
    self.run()
  File "/usr/lib/python3.9/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/home/docker/venv/lib/python3.9/site-packages/uvicorn/_subprocess.py", line 80, in subprocess_started
    target(sockets=sockets)
  File "/home/docker/venv/lib/python3.9/site-packages/uvicorn/supervisors/multiprocess.py", line 63, in target
    return self.real_target(sockets)
  File "/home/docker/venv/lib/python3.9/site-packages/uvicorn/server.py", line 66, in run
    return asyncio.run(self.serve(sockets=sockets))
  File "/usr/lib/python3.9/asyncio/runners.py", line 44, in run
    return loop.run_until_complete(main)
  File "/usr/lib/python3.9/asyncio/base_events.py", line 642, in run_until_complete
    return future.result()
  File "/home/docker/venv/lib/python3.9/site-packages/uvicorn/server.py", line 70, in serve
    await self._serve(sockets)
  File "/home/docker/venv/lib/python3.9/site-packages/uvicorn/server.py", line 77, in _serve
    config.load()
  File "/home/docker/venv/lib/python3.9/site-packages/uvicorn/config.py", line 435, in load
    self.loaded_app = import_from_string(self.app)
  File "/home/docker/venv/lib/python3.9/site-packages/uvicorn/importer.py", line 19, in import_from_string
    module = importlib.import_module(module_str)
  File "/usr/lib/python3.9/importlib/__init__.py", line 127, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
  File "<frozen importlib._bootstrap>", line 1030, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1007, in _find_and_load
  File "<frozen importlib._bootstrap>", line 986, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 680, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 855, in exec_module
  File "<frozen importlib._bootstrap>", line 228, in _call_with_frames_removed
  File "/home/docker/app/main.py", line 3, in <module>
    from routes import router
  File "/home/docker/app/routes/__init__.py", line 3, in <module>
    from .user import router
  File "/home/docker/app/routes/user.py", line 10, in <module>
    job_matcher = JobMatcher()
  File "/home/docker/app/services/main.py", line 29, in __init__
    raise ValueError(self.error)
ValueError: File not found: /home/yaz/specific_job/api/src/static/job_data.csv
INFO:     Waiting for child process [6609]
INFO:     Child process [6609] died
INFO:     Waiting for child process [6610]
INFO:     Child process [6610] died
INFO:     Waiting for child process [6608]
INFO:     Child process [6608] died
Process SpawnProcess-268:
Traceback (most recent call last):
  File "/usr/lib/python3.9/multiprocessing/process.py", line 315, in _bootstrap
    self.run()
  File "/usr/lib/python3.9/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/home/docker/venv/lib/python3.9/site-packages/uvicorn/_subprocess.py", line 80, in subprocess_started
    target(sockets=sockets)
  File "/home/docker/venv/lib/python3.9/site-packages/uvicorn/supervisors/multiprocess.py", line 63, in target
    return self.real_target(sockets)
  File "/home/docker/venv/lib/python3.9/site-packages/uvicorn/server.py", line 66, in run
    return asyncio.run(self.serve(sockets=sockets))
  File "/usr/lib/python3.9/asyncio/runners.py", line 44, in run
    return loop.run_until_complete(main)
  File "/usr/lib/python3.9/asyncio/base_events.py", line 642, in run_until_complete
    return future.result()
  File "/home/docker/venv/lib/python3.9/site-packages/uvicorn/server.py", line 70, in serve
    await self._serve(sockets)
  File "/home/docker/venv/lib/python3.9/site-packages/uvicorn/server.py", line 77, in _serve
    config.load()
  File "/home/docker/venv/lib/python3.9/site-packages/uvicorn/config.py", line 435, in load
    self.loaded_app = import_from_string(self.app)
  File "/home/docker/venv/lib/python3.9/site-packages/uvicorn/importer.py", line 19, in import_from_string
    module = importlib.import_module(module_str)
  File "/usr/lib/python3.9/importlib/__init__.py", line 127, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
  File "<frozen importlib._bootstrap>", line 1030, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1007, in _find_and_load
  File "<frozen importlib._bootstrap>", line 986, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 680, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 855, in exec_module
  File "<frozen importlib._bootstrap>", line 228, in _call_with_frames_removed
  File "/home/docker/app/main.py", line 3, in <module>
    from routes import router
  File "/home/docker/app/routes/__init__.py", line 3, in <module>
    from .user import router
  File "/home/docker/app/routes/user.py", line 10, in <module>
    job_matcher = JobMatcher()
  File "/home/docker/app/services/main.py", line 29, in __init__
    raise ValueError(self.error)
ValueError: File not found: /home/yaz/specific_job/api/src/static/job_data.csv
Process SpawnProcess-269:
Traceback (most recent call last):
  File "/usr/lib/python3.9/multiprocessing/process.py", line 315, in _bootstrap
    self.run()
  File "/usr/lib/python3.9/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/home/docker/venv/lib/python3.9/site-packages/uvicorn/_subprocess.py", line 80, in subprocess_started
    target(sockets=sockets)
  File "/home/docker/venv/lib/python3.9/site-packages/uvicorn/supervisors/multiprocess.py", line 63, in target
    return self.real_target(sockets)
  File "/home/docker/venv/lib/python3.9/site-packages/uvicorn/server.py", line 66, in run
    return asyncio.run(self.serve(sockets=sockets))
  File "/usr/lib/python3.9/asyncio/runners.py", line 44, in run
    return loop.run_until_complete(main)
  File "/usr/lib/python3.9/asyncio/base_events.py", line 642, in run_until_complete
    return future.result()
  File "/home/docker/venv/lib/python3.9/site-packages/uvicorn/server.py", line 70, in serve
    await self._serve(sockets)
  File "/home/docker/venv/lib/python3.9/site-packages/uvicorn/server.py", line 77, in _serve
    config.load()
  File "/home/docker/venv/lib/python3.9/site-packages/uvicorn/config.py", line 435, in load
    self.loaded_app = import_from_string(self.app)
  File "/home/docker/venv/lib/python3.9/site-packages/uvicorn/importer.py", line 19, in import_from_string
    module = importlib.import_module(module_str)
  File "/usr/lib/python3.9/importlib/__init__.py", line 127, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
  File "<frozen importlib._bootstrap>", line 1030, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1007, in _find_and_load
  File "<frozen importlib._bootstrap>", line 986, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 680, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 855, in exec_module
  File "<frozen importlib._bootstrap>", line 228, in _call_with_frames_removed
  File "/home/docker/app/main.py", line 3, in <module>
    from routes import router
  File "/home/docker/app/routes/__init__.py", line 3, in <module>
    from .user import router
  File "/home/docker/app/routes/user.py", line 10, in <module>
    job_matcher = JobMatcher()
  File "/home/docker/app/services/main.py", line 29, in __init__
    raise ValueError(self.error)
ValueError: File not found: /home/yaz/specific_job/api/src/static/job_data.csv
INFO:     Waiting for child process [6683]
INFO:     Child process [6683] died
INFO:     Waiting for child process [6684]
INFO:     Child process [6684] died
Process SpawnProcess-270:
Traceback (most recent call last):
  File "/usr/lib/python3.9/multiprocessing/process.py", line 315, in _bootstrap
    self.run()
  File "/usr/lib/python3.9/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/home/docker/venv/lib/python3.9/site-packages/uvicorn/_subprocess.py", line 80, in subprocess_started
    target(sockets=sockets)
  File "/home/docker/venv/lib/python3.9/site-packages/uvicorn/supervisors/multiprocess.py", line 63, in target
    return self.real_target(sockets)
  File "/home/docker/venv/lib/python3.9/site-packages/uvicorn/server.py", line 66, in run
    return asyncio.run(self.serve(sockets=sockets))
  File "/usr/lib/python3.9/asyncio/runners.py", line 44, in run
    return loop.run_until_complete(main)
  File "/usr/lib/python3.9/asyncio/base_events.py", line 642, in run_until_complete
    return future.result()
  File "/home/docker/venv/lib/python3.9/site-packages/uvicorn/server.py", line 70, in serve
    await self._serve(sockets)
  File "/home/docker/venv/lib/python3.9/site-packages/uvicorn/server.py", line 77, in _serve
    config.load()
  File "/home/docker/venv/lib/python3.9/site-packages/uvicorn/config.py", line 435, in load
    self.loaded_app = import_from_string(self.app)
  File "/home/docker/venv/lib/python3.9/site-packages/uvicorn/importer.py", line 19, in import_from_string
    module = importlib.import_module(module_str)
  File "/usr/lib/python3.9/importlib/__init__.py", line 127, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
  File "<frozen importlib._bootstrap>", line 1030, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1007, in _find_and_load
  File "<frozen importlib._bootstrap>", line 986, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 680, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 855, in exec_module
  File "<frozen importlib._bootstrap>", line 228, in _call_with_frames_removed
  File "/home/docker/app/main.py", line 3, in <module>
    from routes import router
  File "/home/docker/app/routes/__init__.py", line 3, in <module>
    from .user import router
  File "/home/docker/app/routes/user.py", line 10, in <module>
    job_matcher = JobMatcher()
  File "/home/docker/app/services/main.py", line 29, in __init__
    raise ValueError(self.error)
ValueError: File not found: /home/yaz/specific_job/api/src/static/job_data.csv
INFO:     Waiting for child process [6733]
INFO:     Child process [6733] died
Process SpawnProcess-272:
Traceback (most recent call last):
  File "/usr/lib/python3.9/multiprocessing/process.py", line 315, in _bootstrap
    self.run()
  File "/usr/lib/python3.9/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/home/docker/venv/lib/python3.9/site-packages/uvicorn/_subprocess.py", line 80, in subprocess_started
    target(sockets=sockets)
  File "/home/docker/venv/lib/python3.9/site-packages/uvicorn/supervisors/multiprocess.py", line 63, in target
    return self.real_target(sockets)
  File "/home/docker/venv/lib/python3.9/site-packages/uvicorn/server.py", line 66, in run
    return asyncio.run(self.serve(sockets=sockets))
  File "/usr/lib/python3.9/asyncio/runners.py", line 44, in run
    return loop.run_until_complete(main)
  File "/usr/lib/python3.9/asyncio/base_events.py", line 642, in run_until_complete
    return future.result()
  File "/home/docker/venv/lib/python3.9/site-packages/uvicorn/server.py", line 70, in serve
    await self._serve(sockets)
  File "/home/docker/venv/lib/python3.9/site-packages/uvicorn/server.py", line 77, in _serve
    config.load()
  File "/home/docker/venv/lib/python3.9/site-packages/uvicorn/config.py", line 435, in load
    self.loaded_app = import_from_string(self.app)
  File "/home/docker/venv/lib/python3.9/site-packages/uvicorn/importer.py", line 19, in import_from_string
    module = importlib.import_module(module_str)
  File "/usr/lib/python3.9/importlib/__init__.py", line 127, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
  File "<frozen importlib._bootstrap>", line 1030, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1007, in _find_and_load
  File "<frozen importlib._bootstrap>", line 986, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 680, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 855, in exec_module
  File "<frozen importlib._bootstrap>", line 228, in _call_with_frames_removed
  File "/home/docker/app/main.py", line 3, in <module>
    from routes import router
  File "/home/docker/app/routes/__init__.py", line 3, in <module>
    from .user import router
  File "/home/docker/app/routes/user.py", line 10, in <module>
    job_matcher = JobMatcher()
  File "/home/docker/app/services/main.py", line 29, in __init__
    raise ValueError(self.error)
ValueError: File not found: /home/yaz/specific_job/api/src/static/job_data.csv
Process SpawnProcess-271:
Traceback (most recent call last):
  File "/usr/lib/python3.9/multiprocessing/process.py", line 315, in _bootstrap
    self.run()
  File "/usr/lib/python3.9/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/home/docker/venv/lib/python3.9/site-packages/uvicorn/_subprocess.py", line 80, in subprocess_started
    target(sockets=sockets)
  File "/home/docker/venv/lib/python3.9/site-packages/uvicorn/supervisors/multiprocess.py", line 63, in target
    return self.real_target(sockets)
  File "/home/docker/venv/lib/python3.9/site-packages/uvicorn/server.py", line 66, in run
    return asyncio.run(self.serve(sockets=sockets))
  File "/usr/lib/python3.9/asyncio/runners.py", line 44, in run
    return loop.run_until_complete(main)
  File "/usr/lib/python3.9/asyncio/base_events.py", line 642, in run_until_complete
    return future.result()
  File "/home/docker/venv/lib/python3.9/site-packages/uvicorn/server.py", line 70, in serve
    await self._serve(sockets)
  File "/home/docker/venv/lib/python3.9/site-packages/uvicorn/server.py", line 77, in _serve
    config.load()
  File "/home/docker/venv/lib/python3.9/site-packages/uvicorn/config.py", line 435, in load
    self.loaded_app = import_from_string(self.app)
  File "/home/docker/venv/lib/python3.9/site-packages/uvicorn/importer.py", line 19, in import_from_string
    module = importlib.import_module(module_str)
  File "/usr/lib/python3.9/importlib/__init__.py", line 127, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
  File "<frozen importlib._bootstrap>", line 1030, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1007, in _find_and_load
  File "<frozen importlib._bootstrap>", line 986, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 680, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 855, in exec_module
  File "<frozen importlib._bootstrap>", line 228, in _call_with_frames_removed
  File "/home/docker/app/main.py", line 3, in <module>
    from routes import router
  File "/home/docker/app/routes/__init__.py", line 3, in <module>
    from .user import router
  File "/home/docker/app/routes/user.py", line 10, in <module>
    job_matcher = JobMatcher()
  File "/home/docker/app/services/main.py", line 29, in __init__
    raise ValueError(self.error)
ValueError: File not found: /home/yaz/specific_job/api/src/static/job_data.csv
Process SpawnProcess-273:
Traceback (most recent call last):
  File "/usr/lib/python3.9/multiprocessing/process.py", line 315, in _bootstrap
    self.run()
  File "/usr/lib/python3.9/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/home/docker/venv/lib/python3.9/site-packages/uvicorn/_subprocess.py", line 80, in subprocess_started
    target(sockets=sockets)
  File "/home/docker/venv/lib/python3.9/site-packages/uvicorn/supervisors/multiprocess.py", line 63, in target
    return self.real_target(sockets)
  File "/home/docker/venv/lib/python3.9/site-packages/uvicorn/server.py", line 66, in run
    return asyncio.run(self.serve(sockets=sockets))
  File "/usr/lib/python3.9/asyncio/runners.py", line 44, in run
    return loop.run_until_complete(main)
  File "/usr/lib/python3.9/asyncio/base_events.py", line 642, in run_until_complete
    return future.result()
  File "/home/docker/venv/lib/python3.9/site-packages/uvicorn/server.py", line 70, in serve
    await self._serve(sockets)
  File "/home/docker/venv/lib/python3.9/site-packages/uvicorn/server.py", line 77, in _serve
    config.load()
  File "/home/docker/venv/lib/python3.9/site-packages/uvicorn/config.py", line 435, in load
    self.loaded_app = import_from_string(self.app)
  File "/home/docker/venv/lib/python3.9/site-packages/uvicorn/importer.py", line 19, in import_from_string
    module = importlib.import_module(module_str)
  File "/usr/lib/python3.9/importlib/__init__.py", line 127, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
  File "<frozen importlib._bootstrap>", line 1030, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1007, in _find_and_load
  File "<frozen importlib._bootstrap>", line 986, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 680, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 855, in exec_module
  File "<frozen importlib._bootstrap>", line 228, in _call_with_frames_removed
  File "/home/docker/app/main.py", line 3, in <module>
    from routes import router
  File "/home/docker/app/routes/__init__.py", line 3, in <module>
    from .user import router
  File "/home/docker/app/routes/user.py", line 10, in <module>
    job_matcher = JobMatcher()
  File "/home/docker/app/services/main.py", line 29, in __init__
    raise ValueError(self.error)
ValueError: File not found: /home/yaz/specific_job/api/src/static/job_data.csv
INFO:     Waiting for child process [6759]
INFO:     Child process [6759] died
INFO:     Waiting for child process [6808]
INFO:     Child process [6808] died
INFO:     Waiting for child process [6758]
INFO:     Child process [6758] died
Process SpawnProcess-274:
Traceback (most recent call last):
  File "/usr/lib/python3.9/multiprocessing/process.py", line 315, in _bootstrap
    self.run()
  File "/usr/lib/python3.9/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/home/docker/venv/lib/python3.9/site-packages/uvicorn/_subprocess.py", line 80, in subprocess_started
    target(sockets=sockets)
  File "/home/docker/venv/lib/python3.9/site-packages/uvicorn/supervisors/multiprocess.py", line 63, in target
    return self.real_target(sockets)
  File "/home/docker/venv/lib/python3.9/site-packages/uvicorn/server.py", line 66, in run
    return asyncio.run(self.serve(sockets=sockets))
  File "/usr/lib/python3.9/asyncio/runners.py", line 44, in run
    return loop.run_until_complete(main)
  File "/usr/lib/python3.9/asyncio/base_events.py", line 642, in run_until_complete
    return future.result()
  File "/home/docker/venv/lib/python3.9/site-packages/uvicorn/server.py", line 70, in serve
    await self._serve(sockets)
  File "/home/docker/venv/lib/python3.9/site-packages/uvicorn/server.py", line 77, in _serve
    config.load()
  File "/home/docker/venv/lib/python3.9/site-packages/uvicorn/config.py", line 435, in load
    self.loaded_app = import_from_string(self.app)
  File "/home/docker/venv/lib/python3.9/site-packages/uvicorn/importer.py", line 19, in import_from_string
    module = importlib.import_module(module_str)
  File "/usr/lib/python3.9/importlib/__init__.py", line 127, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
  File "<frozen importlib._bootstrap>", line 1030, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1007, in _find_and_load
  File "<frozen importlib._bootstrap>", line 986, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 680, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 855, in exec_module
  File "<frozen importlib._bootstrap>", line 228, in _call_with_frames_removed
  File "/home/docker/app/main.py", line 3, in <module>
    from routes import router
  File "/home/docker/app/routes/__init__.py", line 3, in <module>
    from .user import router
  File "/home/docker/app/routes/user.py", line 10, in <module>
    job_matcher = JobMatcher()
  File "/home/docker/app/services/main.py", line 29, in __init__
    raise ValueError(self.error)
ValueError: File not found: /home/yaz/specific_job/api/src/static/job_data.csv
Process SpawnProcess-276:
Traceback (most recent call last):
  File "/usr/lib/python3.9/multiprocessing/process.py", line 315, in _bootstrap
    self.run()
  File "/usr/lib/python3.9/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/home/docker/venv/lib/python3.9/site-packages/uvicorn/_subprocess.py", line 80, in subprocess_started
    target(sockets=sockets)
  File "/home/docker/venv/lib/python3.9/site-packages/uvicorn/supervisors/multiprocess.py", line 63, in target
    return self.real_target(sockets)
  File "/home/docker/venv/lib/python3.9/site-packages/uvicorn/server.py", line 66, in run
    return asyncio.run(self.serve(sockets=sockets))
  File "/usr/lib/python3.9/asyncio/runners.py", line 44, in run
    return loop.run_until_complete(main)
  File "/usr/lib/python3.9/asyncio/base_events.py", line 642, in run_until_complete
    return future.result()
  File "/home/docker/venv/lib/python3.9/site-packages/uvicorn/server.py", line 70, in serve
    await self._serve(sockets)
  File "/home/docker/venv/lib/python3.9/site-packages/uvicorn/server.py", line 77, in _serve
    config.load()
  File "/home/docker/venv/lib/python3.9/site-packages/uvicorn/config.py", line 435, in load
    self.loaded_app = import_from_string(self.app)
  File "/home/docker/venv/lib/python3.9/site-packages/uvicorn/importer.py", line 19, in import_from_string
    module = importlib.import_module(module_str)
  File "/usr/lib/python3.9/importlib/__init__.py", line 127, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
  File "<frozen importlib._bootstrap>", line 1030, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1007, in _find_and_load
  File "<frozen importlib._bootstrap>", line 986, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 680, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 855, in exec_module
  File "<frozen importlib._bootstrap>", line 228, in _call_with_frames_removed
  File "/home/docker/app/main.py", line 3, in <module>
    from routes import router
  File "/home/docker/app/routes/__init__.py", line 3, in <module>
    from .user import router
  File "/home/docker/app/routes/user.py", line 10, in <module>
    job_matcher = JobMatcher()
  File "/home/docker/app/services/main.py", line 29, in __init__
    raise ValueError(self.error)
ValueError: File not found: /home/yaz/specific_job/api/src/static/job_data.csv
Process SpawnProcess-275:
Traceback (most recent call last):
  File "/usr/lib/python3.9/multiprocessing/process.py", line 315, in _bootstrap
    self.run()
  File "/usr/lib/python3.9/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/home/docker/venv/lib/python3.9/site-packages/uvicorn/_subprocess.py", line 80, in subprocess_started
    target(sockets=sockets)
  File "/home/docker/venv/lib/python3.9/site-packages/uvicorn/supervisors/multiprocess.py", line 63, in target
    return self.real_target(sockets)
  File "/home/docker/venv/lib/python3.9/site-packages/uvicorn/server.py", line 66, in run
    return asyncio.run(self.serve(sockets=sockets))
  File "/usr/lib/python3.9/asyncio/runners.py", line 44, in run
    return loop.run_until_complete(main)
  File "/usr/lib/python3.9/asyncio/base_events.py", line 642, in run_until_complete
    return future.result()
  File "/home/docker/venv/lib/python3.9/site-packages/uvicorn/server.py", line 70, in serve
    await self._serve(sockets)
  File "/home/docker/venv/lib/python3.9/site-packages/uvicorn/server.py", line 77, in _serve
    config.load()
  File "/home/docker/venv/lib/python3.9/site-packages/uvicorn/config.py", line 435, in load
    self.loaded_app = import_from_string(self.app)
  File "/home/docker/venv/lib/python3.9/site-packages/uvicorn/importer.py", line 19, in import_from_string
    module = importlib.import_module(module_str)
  File "/usr/lib/python3.9/importlib/__init__.py", line 127, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
  File "<frozen importlib._bootstrap>", line 1030, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1007, in _find_and_load
  File "<frozen importlib._bootstrap>", line 986, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 680, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 855, in exec_module
  File "<frozen importlib._bootstrap>", line 228, in _call_with_frames_removed
  File "/home/docker/app/main.py", line 3, in <module>
    from routes import router
  File "/home/docker/app/routes/__init__.py", line 3, in <module>
    from .user import router
  File "/home/docker/app/routes/user.py", line 10, in <module>
    job_matcher = JobMatcher()
  File "/home/docker/app/services/main.py", line 29, in __init__
    raise ValueError(self.error)
ValueError: File not found: /home/yaz/specific_job/api/src/static/job_data.csv
INFO:     Waiting for child process [6833]
INFO:     Child process [6833] died
INFO:     Waiting for child process [6858]
INFO:     Child process [6858] died
INFO:     Waiting for child process [6859]
INFO:     Child process [6859] died
Process SpawnProcess-277:
Traceback (most recent call last):
  File "/usr/lib/python3.9/multiprocessing/process.py", line 315, in _bootstrap
    self.run()
  File "/usr/lib/python3.9/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/home/docker/venv/lib/python3.9/site-packages/uvicorn/_subprocess.py", line 80, in subprocess_started
    target(sockets=sockets)
  File "/home/docker/venv/lib/python3.9/site-packages/uvicorn/supervisors/multiprocess.py", line 63, in target
    return self.real_target(sockets)
  File "/home/docker/venv/lib/python3.9/site-packages/uvicorn/server.py", line 66, in run
    return asyncio.run(self.serve(sockets=sockets))
  File "/usr/lib/python3.9/asyncio/runners.py", line 44, in run
    return loop.run_until_complete(main)
  File "/usr/lib/python3.9/asyncio/base_events.py", line 642, in run_until_complete
    return future.result()
  File "/home/docker/venv/lib/python3.9/site-packages/uvicorn/server.py", line 70, in serve
    await self._serve(sockets)
  File "/home/docker/venv/lib/python3.9/site-packages/uvicorn/server.py", line 77, in _serve
    config.load()
  File "/home/docker/venv/lib/python3.9/site-packages/uvicorn/config.py", line 435, in load
    self.loaded_app = import_from_string(self.app)
  File "/home/docker/venv/lib/python3.9/site-packages/uvicorn/importer.py", line 19, in import_from_string
    module = importlib.import_module(module_str)
  File "/usr/lib/python3.9/importlib/__init__.py", line 127, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
  File "<frozen importlib._bootstrap>", line 1030, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1007, in _find_and_load
  File "<frozen importlib._bootstrap>", line 986, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 680, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 855, in exec_module
  File "<frozen importlib._bootstrap>", line 228, in _call_with_frames_removed
  File "/home/docker/app/main.py", line 3, in <module>
    from routes import router
  File "/home/docker/app/routes/__init__.py", line 3, in <module>
    from .user import router
  File "/home/docker/app/routes/user.py", line 10, in <module>
    job_matcher = JobMatcher()
  File "/home/docker/app/services/main.py", line 29, in __init__
    raise ValueError(self.error)
ValueError: File not found: /home/yaz/specific_job/api/src/static/job_data.csv
Process SpawnProcess-278:
Traceback (most recent call last):
  File "/usr/lib/python3.9/multiprocessing/process.py", line 315, in _bootstrap
    self.run()
  File "/usr/lib/python3.9/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/home/docker/venv/lib/python3.9/site-packages/uvicorn/_subprocess.py", line 80, in subprocess_started
    target(sockets=sockets)
  File "/home/docker/venv/lib/python3.9/site-packages/uvicorn/supervisors/multiprocess.py", line 63, in target
    return self.real_target(sockets)
  File "/home/docker/venv/lib/python3.9/site-packages/uvicorn/server.py", line 66, in run
    return asyncio.run(self.serve(sockets=sockets))
  File "/usr/lib/python3.9/asyncio/runners.py", line 44, in run
    return loop.run_until_complete(main)
  File "/usr/lib/python3.9/asyncio/base_events.py", line 642, in run_until_complete
    return future.result()
  File "/home/docker/venv/lib/python3.9/site-packages/uvicorn/server.py", line 70, in serve
    await self._serve(sockets)
  File "/home/docker/venv/lib/python3.9/site-packages/uvicorn/server.py", line 77, in _serve
    config.load()
  File "/home/docker/venv/lib/python3.9/site-packages/uvicorn/config.py", line 435, in load
    self.loaded_app = import_from_string(self.app)
  File "/home/docker/venv/lib/python3.9/site-packages/uvicorn/importer.py", line 19, in import_from_string
    module = importlib.import_module(module_str)
  File "/usr/lib/python3.9/importlib/__init__.py", line 127, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
  File "<frozen importlib._bootstrap>", line 1030, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1007, in _find_and_load
  File "<frozen importlib._bootstrap>", line 986, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 680, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 855, in exec_module
  File "<frozen importlib._bootstrap>", line 228, in _call_with_frames_removed
  File "/home/docker/app/main.py", line 3, in <module>
    from routes import router
  File "/home/docker/app/routes/__init__.py", line 3, in <module>
    from .user import router
  File "/home/docker/app/routes/user.py", line 10, in <module>
    job_matcher = JobMatcher()
  File "/home/docker/app/services/main.py", line 29, in __init__
    raise ValueError(self.error)
ValueError: File not found: /home/yaz/specific_job/api/src/static/job_data.csv
Process SpawnProcess-279:
Traceback (most recent call last):
  File "/usr/lib/python3.9/multiprocessing/process.py", line 315, in _bootstrap
    self.run()
  File "/usr/lib/python3.9/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/home/docker/venv/lib/python3.9/site-packages/uvicorn/_subprocess.py", line 80, in subprocess_started
    target(sockets=sockets)
  File "/home/docker/venv/lib/python3.9/site-packages/uvicorn/supervisors/multiprocess.py", line 63, in target
    return self.real_target(sockets)
  File "/home/docker/venv/lib/python3.9/site-packages/uvicorn/server.py", line 66, in run
    return asyncio.run(self.serve(sockets=sockets))
  File "/usr/lib/python3.9/asyncio/runners.py", line 44, in run
    return loop.run_until_complete(main)
  File "/usr/lib/python3.9/asyncio/base_events.py", line 642, in run_until_complete
    return future.result()
  File "/home/docker/venv/lib/python3.9/site-packages/uvicorn/server.py", line 70, in serve
    await self._serve(sockets)
  File "/home/docker/venv/lib/python3.9/site-packages/uvicorn/server.py", line 77, in _serve
    config.load()
  File "/home/docker/venv/lib/python3.9/site-packages/uvicorn/config.py", line 435, in load
    self.loaded_app = import_from_string(self.app)
  File "/home/docker/venv/lib/python3.9/site-packages/uvicorn/importer.py", line 19, in import_from_string
    module = importlib.import_module(module_str)
  File "/usr/lib/python3.9/importlib/__init__.py", line 127, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
  File "<frozen importlib._bootstrap>", line 1030, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1007, in _find_and_load
  File "<frozen importlib._bootstrap>", line 986, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 680, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 855, in exec_module
  File "<frozen importlib._bootstrap>", line 228, in _call_with_frames_removed
  File "/home/docker/app/main.py", line 3, in <module>
    from routes import router
  File "/home/docker/app/routes/__init__.py", line 3, in <module>
    from .user import router
  File "/home/docker/app/routes/user.py", line 10, in <module>
    job_matcher = JobMatcher()
  File "/home/docker/app/services/main.py", line 29, in __init__
    raise ValueError(self.error)
ValueError: File not found: /home/yaz/specific_job/api/src/static/job_data.csv
INFO:     Waiting for child process [6908]
INFO:     Child process [6908] died
INFO:     Waiting for child process [6933]
INFO:     Child process [6933] died
INFO:     Waiting for child process [6934]
INFO:     Child process [6934] died
Process SpawnProcess-280:
Traceback (most recent call last):
  File "/usr/lib/python3.9/multiprocessing/process.py", line 315, in _bootstrap
    self.run()
  File "/usr/lib/python3.9/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/home/docker/venv/lib/python3.9/site-packages/uvicorn/_subprocess.py", line 80, in subprocess_started
    target(sockets=sockets)
  File "/home/docker/venv/lib/python3.9/site-packages/uvicorn/supervisors/multiprocess.py", line 63, in target
    return self.real_target(sockets)
  File "/home/docker/venv/lib/python3.9/site-packages/uvicorn/server.py", line 66, in run
    return asyncio.run(self.serve(sockets=sockets))
  File "/usr/lib/python3.9/asyncio/runners.py", line 44, in run
    return loop.run_until_complete(main)
  File "/usr/lib/python3.9/asyncio/base_events.py", line 642, in run_until_complete
    return future.result()
  File "/home/docker/venv/lib/python3.9/site-packages/uvicorn/server.py", line 70, in serve
    await self._serve(sockets)
  File "/home/docker/venv/lib/python3.9/site-packages/uvicorn/server.py", line 77, in _serve
    config.load()
  File "/home/docker/venv/lib/python3.9/site-packages/uvicorn/config.py", line 435, in load
    self.loaded_app = import_from_string(self.app)
  File "/home/docker/venv/lib/python3.9/site-packages/uvicorn/importer.py", line 19, in import_from_string
    module = importlib.import_module(module_str)
  File "/usr/lib/python3.9/importlib/__init__.py", line 127, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
  File "<frozen importlib._bootstrap>", line 1030, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1007, in _find_and_load
  File "<frozen importlib._bootstrap>", line 986, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 680, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 855, in exec_module
  File "<frozen importlib._bootstrap>", line 228, in _call_with_frames_removed
  File "/home/docker/app/main.py", line 3, in <module>
    from routes import router
  File "/home/docker/app/routes/__init__.py", line 3, in <module>
    from .user import router
  File "/home/docker/app/routes/user.py", line 10, in <module>
    job_matcher = JobMatcher()
  File "/home/docker/app/services/main.py", line 29, in __init__
    raise ValueError(self.error)
ValueError: File not found: /home/yaz/specific_job/api/src/static/job_data.csv
INFO:     Waiting for child process [6983]
INFO:     Child process [6983] died
Process SpawnProcess-282:
Traceback (most recent call last):
  File "/usr/lib/python3.9/multiprocessing/process.py", line 315, in _bootstrap
    self.run()
  File "/usr/lib/python3.9/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/home/docker/venv/lib/python3.9/site-packages/uvicorn/_subprocess.py", line 80, in subprocess_started
    target(sockets=sockets)
  File "/home/docker/venv/lib/python3.9/site-packages/uvicorn/supervisors/multiprocess.py", line 63, in target
    return self.real_target(sockets)
  File "/home/docker/venv/lib/python3.9/site-packages/uvicorn/server.py", line 66, in run
    return asyncio.run(self.serve(sockets=sockets))
  File "/usr/lib/python3.9/asyncio/runners.py", line 44, in run
    return loop.run_until_complete(main)
  File "/usr/lib/python3.9/asyncio/base_events.py", line 642, in run_until_complete
    return future.result()
  File "/home/docker/venv/lib/python3.9/site-packages/uvicorn/server.py", line 70, in serve
    await self._serve(sockets)
  File "/home/docker/venv/lib/python3.9/site-packages/uvicorn/server.py", line 77, in _serve
    config.load()
  File "/home/docker/venv/lib/python3.9/site-packages/uvicorn/config.py", line 435, in load
    self.loaded_app = import_from_string(self.app)
  File "/home/docker/venv/lib/python3.9/site-packages/uvicorn/importer.py", line 19, in import_from_string
    module = importlib.import_module(module_str)
  File "/usr/lib/python3.9/importlib/__init__.py", line 127, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
  File "<frozen importlib._bootstrap>", line 1030, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1007, in _find_and_load
  File "<frozen importlib._bootstrap>", line 986, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 680, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 855, in exec_module
  File "<frozen importlib._bootstrap>", line 228, in _call_with_frames_removed
  File "/home/docker/app/main.py", line 3, in <module>
    from routes import router
  File "/home/docker/app/routes/__init__.py", line 3, in <module>
    from .user import router
  File "/home/docker/app/routes/user.py", line 10, in <module>
    job_matcher = JobMatcher()
  File "/home/docker/app/services/main.py", line 29, in __init__
    raise ValueError(self.error)
ValueError: File not found: /home/yaz/specific_job/api/src/static/job_data.csv
Process SpawnProcess-281:
Traceback (most recent call last):
  File "/usr/lib/python3.9/multiprocessing/process.py", line 315, in _bootstrap
    self.run()
  File "/usr/lib/python3.9/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/home/docker/venv/lib/python3.9/site-packages/uvicorn/_subprocess.py", line 80, in subprocess_started
    target(sockets=sockets)
  File "/home/docker/venv/lib/python3.9/site-packages/uvicorn/supervisors/multiprocess.py", line 63, in target
    return self.real_target(sockets)
  File "/home/docker/venv/lib/python3.9/site-packages/uvicorn/server.py", line 66, in run
    return asyncio.run(self.serve(sockets=sockets))
  File "/usr/lib/python3.9/asyncio/runners.py", line 44, in run
    return loop.run_until_complete(main)
  File "/usr/lib/python3.9/asyncio/base_events.py", line 642, in run_until_complete
    return future.result()
  File "/home/docker/venv/lib/python3.9/site-packages/uvicorn/server.py", line 70, in serve
    await self._serve(sockets)
  File "/home/docker/venv/lib/python3.9/site-packages/uvicorn/server.py", line 77, in _serve
    config.load()
  File "/home/docker/venv/lib/python3.9/site-packages/uvicorn/config.py", line 435, in load
    self.loaded_app = import_from_string(self.app)
  File "/home/docker/venv/lib/python3.9/site-packages/uvicorn/importer.py", line 19, in import_from_string
    module = importlib.import_module(module_str)
  File "/usr/lib/python3.9/importlib/__init__.py", line 127, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
  File "<frozen importlib._bootstrap>", line 1030, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1007, in _find_and_load
  File "<frozen importlib._bootstrap>", line 986, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 680, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 855, in exec_module
  File "<frozen importlib._bootstrap>", line 228, in _call_with_frames_removed
  File "/home/docker/app/main.py", line 3, in <module>
    from routes import router
  File "/home/docker/app/routes/__init__.py", line 3, in <module>
    from .user import router
  File "/home/docker/app/routes/user.py", line 10, in <module>
    job_matcher = JobMatcher()
  File "/home/docker/app/services/main.py", line 29, in __init__
    raise ValueError(self.error)
ValueError: File not found: /home/yaz/specific_job/api/src/static/job_data.csv
INFO:     Waiting for child process [7008]
INFO:     Child process [7008] died
INFO:     Waiting for child process [7009]
INFO:     Child process [7009] died
Process SpawnProcess-283:
Traceback (most recent call last):
  File "/usr/lib/python3.9/multiprocessing/process.py", line 315, in _bootstrap
    self.run()
  File "/usr/lib/python3.9/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/home/docker/venv/lib/python3.9/site-packages/uvicorn/_subprocess.py", line 80, in subprocess_started
    target(sockets=sockets)
  File "/home/docker/venv/lib/python3.9/site-packages/uvicorn/supervisors/multiprocess.py", line 63, in target
    return self.real_target(sockets)
  File "/home/docker/venv/lib/python3.9/site-packages/uvicorn/server.py", line 66, in run
    return asyncio.run(self.serve(sockets=sockets))
  File "/usr/lib/python3.9/asyncio/runners.py", line 44, in run
    return loop.run_until_complete(main)
  File "/usr/lib/python3.9/asyncio/base_events.py", line 642, in run_until_complete
    return future.result()
  File "/home/docker/venv/lib/python3.9/site-packages/uvicorn/server.py", line 70, in serve
    await self._serve(sockets)
  File "/home/docker/venv/lib/python3.9/site-packages/uvicorn/server.py", line 77, in _serve
    config.load()
  File "/home/docker/venv/lib/python3.9/site-packages/uvicorn/config.py", line 435, in load
    self.loaded_app = import_from_string(self.app)
  File "/home/docker/venv/lib/python3.9/site-packages/uvicorn/importer.py", line 19, in import_from_string
    module = importlib.import_module(module_str)
  File "/usr/lib/python3.9/importlib/__init__.py", line 127, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
  File "<frozen importlib._bootstrap>", line 1030, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1007, in _find_and_load
  File "<frozen importlib._bootstrap>", line 986, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 680, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 855, in exec_module
  File "<frozen importlib._bootstrap>", line 228, in _call_with_frames_removed
  File "/home/docker/app/main.py", line 3, in <module>
    from routes import router
  File "/home/docker/app/routes/__init__.py", line 3, in <module>
    from .user import router
  File "/home/docker/app/routes/user.py", line 10, in <module>
    job_matcher = JobMatcher()
  File "/home/docker/app/services/main.py", line 29, in __init__
    raise ValueError(self.error)
ValueError: File not found: /home/yaz/specific_job/api/src/static/job_data.csv
INFO:     Waiting for child process [7058]
INFO:     Child process [7058] died
Process SpawnProcess-284:
Traceback (most recent call last):
  File "/usr/lib/python3.9/multiprocessing/process.py", line 315, in _bootstrap
    self.run()
  File "/usr/lib/python3.9/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/home/docker/venv/lib/python3.9/site-packages/uvicorn/_subprocess.py", line 80, in subprocess_started
    target(sockets=sockets)
  File "/home/docker/venv/lib/python3.9/site-packages/uvicorn/supervisors/multiprocess.py", line 63, in target
    return self.real_target(sockets)
  File "/home/docker/venv/lib/python3.9/site-packages/uvicorn/server.py", line 66, in run
    return asyncio.run(self.serve(sockets=sockets))
  File "/usr/lib/python3.9/asyncio/runners.py", line 44, in run
    return loop.run_until_complete(main)
  File "/usr/lib/python3.9/asyncio/base_events.py", line 642, in run_until_complete
    return future.result()
  File "/home/docker/venv/lib/python3.9/site-packages/uvicorn/server.py", line 70, in serve
    await self._serve(sockets)
  File "/home/docker/venv/lib/python3.9/site-packages/uvicorn/server.py", line 77, in _serve
    config.load()
  File "/home/docker/venv/lib/python3.9/site-packages/uvicorn/config.py", line 435, in load
    self.loaded_app = import_from_string(self.app)
  File "/home/docker/venv/lib/python3.9/site-packages/uvicorn/importer.py", line 19, in import_from_string
    module = importlib.import_module(module_str)
  File "/usr/lib/python3.9/importlib/__init__.py", line 127, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
  File "<frozen importlib._bootstrap>", line 1030, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1007, in _find_and_load
  File "<frozen importlib._bootstrap>", line 986, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 680, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 855, in exec_module
  File "<frozen importlib._bootstrap>", line 228, in _call_with_frames_removed
  File "/home/docker/app/main.py", line 3, in <module>
    from routes import router
  File "/home/docker/app/routes/__init__.py", line 3, in <module>
    from .user import router
  File "/home/docker/app/routes/user.py", line 10, in <module>
    job_matcher = JobMatcher()
  File "/home/docker/app/services/main.py", line 29, in __init__
    raise ValueError(self.error)
ValueError: File not found: /home/yaz/specific_job/api/src/static/job_data.csv
Process SpawnProcess-285:
Traceback (most recent call last):
  File "/usr/lib/python3.9/multiprocessing/process.py", line 315, in _bootstrap
    self.run()
  File "/usr/lib/python3.9/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/home/docker/venv/lib/python3.9/site-packages/uvicorn/_subprocess.py", line 80, in subprocess_started
    target(sockets=sockets)
  File "/home/docker/venv/lib/python3.9/site-packages/uvicorn/supervisors/multiprocess.py", line 63, in target
    return self.real_target(sockets)
  File "/home/docker/venv/lib/python3.9/site-packages/uvicorn/server.py", line 66, in run
    return asyncio.run(self.serve(sockets=sockets))
  File "/usr/lib/python3.9/asyncio/runners.py", line 44, in run
    return loop.run_until_complete(main)
  File "/usr/lib/python3.9/asyncio/base_events.py", line 642, in run_until_complete
    return future.result()
  File "/home/docker/venv/lib/python3.9/site-packages/uvicorn/server.py", line 70, in serve
    await self._serve(sockets)
  File "/home/docker/venv/lib/python3.9/site-packages/uvicorn/server.py", line 77, in _serve
    config.load()
  File "/home/docker/venv/lib/python3.9/site-packages/uvicorn/config.py", line 435, in load
    self.loaded_app = import_from_string(self.app)
  File "/home/docker/venv/lib/python3.9/site-packages/uvicorn/importer.py", line 19, in import_from_string
    module = importlib.import_module(module_str)
  File "/usr/lib/python3.9/importlib/__init__.py", line 127, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
  File "<frozen importlib._bootstrap>", line 1030, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1007, in _find_and_load
  File "<frozen importlib._bootstrap>", line 986, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 680, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 855, in exec_module
  File "<frozen importlib._bootstrap>", line 228, in _call_with_frames_removed
  File "/home/docker/app/main.py", line 3, in <module>
    from routes import router
  File "/home/docker/app/routes/__init__.py", line 3, in <module>
    from .user import router
  File "/home/docker/app/routes/user.py", line 10, in <module>
    job_matcher = JobMatcher()
  File "/home/docker/app/services/main.py", line 29, in __init__
    raise ValueError(self.error)
ValueError: File not found: /home/yaz/specific_job/api/src/static/job_data.csv
INFO:     Waiting for child process [7083]
INFO:     Child process [7083] died
INFO:     Waiting for child process [7084]
INFO:     Child process [7084] died
Process SpawnProcess-286:
Traceback (most recent call last):
  File "/usr/lib/python3.9/multiprocessing/process.py", line 315, in _bootstrap
    self.run()
  File "/usr/lib/python3.9/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/home/docker/venv/lib/python3.9/site-packages/uvicorn/_subprocess.py", line 80, in subprocess_started
    target(sockets=sockets)
  File "/home/docker/venv/lib/python3.9/site-packages/uvicorn/supervisors/multiprocess.py", line 63, in target
    return self.real_target(sockets)
  File "/home/docker/venv/lib/python3.9/site-packages/uvicorn/server.py", line 66, in run
    return asyncio.run(self.serve(sockets=sockets))
  File "/usr/lib/python3.9/asyncio/runners.py", line 44, in run
    return loop.run_until_complete(main)
  File "/usr/lib/python3.9/asyncio/base_events.py", line 642, in run_until_complete
    return future.result()
  File "/home/docker/venv/lib/python3.9/site-packages/uvicorn/server.py", line 70, in serve
    await self._serve(sockets)
  File "/home/docker/venv/lib/python3.9/site-packages/uvicorn/server.py", line 77, in _serve
    config.load()
  File "/home/docker/venv/lib/python3.9/site-packages/uvicorn/config.py", line 435, in load
    self.loaded_app = import_from_string(self.app)
  File "/home/docker/venv/lib/python3.9/site-packages/uvicorn/importer.py", line 19, in import_from_string
    module = importlib.import_module(module_str)
  File "/usr/lib/python3.9/importlib/__init__.py", line 127, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
  File "<frozen importlib._bootstrap>", line 1030, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1007, in _find_and_load
  File "<frozen importlib._bootstrap>", line 986, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 680, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 855, in exec_module
  File "<frozen importlib._bootstrap>", line 228, in _call_with_frames_removed
  File "/home/docker/app/main.py", line 3, in <module>
    from routes import router
  File "/home/docker/app/routes/__init__.py", line 3, in <module>
    from .user import router
  File "/home/docker/app/routes/user.py", line 10, in <module>
    job_matcher = JobMatcher()
  File "/home/docker/app/services/main.py", line 29, in __init__
    raise ValueError(self.error)
ValueError: File not found: /home/yaz/specific_job/api/src/static/job_data.csv
INFO:     Waiting for child process [7133]
INFO:     Child process [7133] died
Process SpawnProcess-287:
Traceback (most recent call last):
  File "/usr/lib/python3.9/multiprocessing/process.py", line 315, in _bootstrap
    self.run()
  File "/usr/lib/python3.9/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/home/docker/venv/lib/python3.9/site-packages/uvicorn/_subprocess.py", line 80, in subprocess_started
    target(sockets=sockets)
  File "/home/docker/venv/lib/python3.9/site-packages/uvicorn/supervisors/multiprocess.py", line 63, in target
    return self.real_target(sockets)
  File "/home/docker/venv/lib/python3.9/site-packages/uvicorn/server.py", line 66, in run
    return asyncio.run(self.serve(sockets=sockets))
  File "/usr/lib/python3.9/asyncio/runners.py", line 44, in run
    return loop.run_until_complete(main)
  File "/usr/lib/python3.9/asyncio/base_events.py", line 642, in run_until_complete
    return future.result()
  File "/home/docker/venv/lib/python3.9/site-packages/uvicorn/server.py", line 70, in serve
    await self._serve(sockets)
  File "/home/docker/venv/lib/python3.9/site-packages/uvicorn/server.py", line 77, in _serve
    config.load()
  File "/home/docker/venv/lib/python3.9/site-packages/uvicorn/config.py", line 435, in load
    self.loaded_app = import_from_string(self.app)
  File "/home/docker/venv/lib/python3.9/site-packages/uvicorn/importer.py", line 19, in import_from_string
    module = importlib.import_module(module_str)
  File "/usr/lib/python3.9/importlib/__init__.py", line 127, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
  File "<frozen importlib._bootstrap>", line 1030, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1007, in _find_and_load
  File "<frozen importlib._bootstrap>", line 986, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 680, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 855, in exec_module
  File "<frozen importlib._bootstrap>", line 228, in _call_with_frames_removed
  File "/home/docker/app/main.py", line 3, in <module>
    from routes import router
  File "/home/docker/app/routes/__init__.py", line 3, in <module>
    from .user import router
  File "/home/docker/app/routes/user.py", line 10, in <module>
    job_matcher = JobMatcher()
  File "/home/docker/app/services/main.py", line 29, in __init__
    raise ValueError(self.error)
ValueError: File not found: /home/yaz/specific_job/api/src/static/job_data.csv
Process SpawnProcess-288:
Traceback (most recent call last):
  File "/usr/lib/python3.9/multiprocessing/process.py", line 315, in _bootstrap
    self.run()
  File "/usr/lib/python3.9/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/home/docker/venv/lib/python3.9/site-packages/uvicorn/_subprocess.py", line 80, in subprocess_started
    target(sockets=sockets)
  File "/home/docker/venv/lib/python3.9/site-packages/uvicorn/supervisors/multiprocess.py", line 63, in target
    return self.real_target(sockets)
  File "/home/docker/venv/lib/python3.9/site-packages/uvicorn/server.py", line 66, in run
    return asyncio.run(self.serve(sockets=sockets))
  File "/usr/lib/python3.9/asyncio/runners.py", line 44, in run
    return loop.run_until_complete(main)
  File "/usr/lib/python3.9/asyncio/base_events.py", line 642, in run_until_complete
    return future.result()
  File "/home/docker/venv/lib/python3.9/site-packages/uvicorn/server.py", line 70, in serve
    await self._serve(sockets)
  File "/home/docker/venv/lib/python3.9/site-packages/uvicorn/server.py", line 77, in _serve
    config.load()
  File "/home/docker/venv/lib/python3.9/site-packages/uvicorn/config.py", line 435, in load
    self.loaded_app = import_from_string(self.app)
  File "/home/docker/venv/lib/python3.9/site-packages/uvicorn/importer.py", line 19, in import_from_string
    module = importlib.import_module(module_str)
  File "/usr/lib/python3.9/importlib/__init__.py", line 127, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
  File "<frozen importlib._bootstrap>", line 1030, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1007, in _find_and_load
  File "<frozen importlib._bootstrap>", line 986, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 680, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 855, in exec_module
  File "<frozen importlib._bootstrap>", line 228, in _call_with_frames_removed
  File "/home/docker/app/main.py", line 3, in <module>
    from routes import router
  File "/home/docker/app/routes/__init__.py", line 3, in <module>
    from .user import router
  File "/home/docker/app/routes/user.py", line 10, in <module>
    job_matcher = JobMatcher()
  File "/home/docker/app/services/main.py", line 29, in __init__
    raise ValueError(self.error)
ValueError: File not found: /home/yaz/specific_job/api/src/static/job_data.csv




















yaz@gpu:~/specific_job$ docker ps
CONTAINER ID   IMAGE                                                      COMMAND                  CREATED          STATUS                          PORTS                                                                                                                                       NAMES
11d4b53c939a   specificjob-api                                            "uvicorn main:app --…"   23 minutes ago   Up 23 minutes                   0.0.0.0:6437->8080/tcp, [::]:6437->8080/tcp                                                                                                 spisficjob-api-1
ab9daddbb340   confluentinc/cp-kafka:7.5.0                                "/etc/confluent/dock…"   2 hours ago      Up 2 hours                      0.0.0.0:4567->4567/tcp, [::]:4567->4567/tcp, 9092/tcp                                                                                       ivs5-kafka-1
1a8732f0a46d   confluentinc/cp-zookeeper:7.5.0                            "/etc/confluent/dock…"   2 hours ago      Up 2 hours                      2888/tcp, 3888/tcp, 0.0.0.0:3456->2181/tcp, [::]:3456->2181/tcp                                                                             ivs5-zookeeper-1
0150c0768bdf   timescale/timescaledb:latest-pg14                          "docker-entrypoint.s…"   2 hours ago      Up 2 hours                      0.0.0.0:5678->5432/tcp, [::]:5678->5432/tcp                                                                                                 timescaledb
9eb1faa0e9d3   postgres:14                                                "docker-entrypoint.s…"   2 hours ago      Up 2 hours                      0.0.0.0:6789->5432/tcp, [::]:6789->5432/tcp                                                                                                 postgres
ad2cd5d18841   docker.infogerance.d-fi.fr/nginx-domain:2.9.0              "/docker-entrypoint.…"   7 hours ago      Up 3 hours                      0.0.0.0:80->80/tcp, [::]:80->80/tcp, 0.0.0.0:443->443/tcp, [::]:443->443/tcp                                                                domain-client-1
fd0e88ed5362   cvm-api:1.0.0                                              "uvicorn main:app --…"   27 hours ago     Up 3 hours                      0.0.0.0:6438->8080/tcp, [::]:6438->8080/tcp                                                                                                 jobmatch_api
4320544f2a4e   docker.infogerance.d-fi.fr/opportunity-detector-fe:0.0.1   "dotnet OpportunityD…"   3 days ago       Up 3 hours                      443/tcp, 0.0.0.0:5205->80/tcp, [::]:5205->80/tcp                                                                                            opportunity-detector-fe-1
e4eed8699610   docker.infogerance.d-fi.fr/opportunity-detector-be:0.0.1   "dotnet OpportunityD…"   3 days ago       Up 3 hours                      443/tcp, 0.0.0.0:5204->80/tcp, [::]:5204->80/tcp                                                                                            opportunity-detector-be-1
48bf931f9f64   postgres                                                   "docker-entrypoint.s…"   3 days ago       Up 3 hours                      0.0.0.0:5206->5432/tcp, [::]:5206->5432/tcp                                                                                                 opportunity-detector-db-1
23f7611f0ad0   docker.infogerance.d-fi.fr/meapal-front:1.0.6              "/docker-entrypoint.…"   3 days ago       Up 12 minutes                   0.0.0.0:5144->80/tcp, [::]:5144->80/tcp                                                                                                     meapal-client-1
7810e5b346b1   project_graduation_api                                     "uvicorn main:app --…"   8 days ago       Up 3 hours                      0.0.0.0:5111->8080/tcp, [::]:5111->8080/tcp                                                                                                 project_toursium
7bce721ddb6c   voice-api:1.0.0                                            "uvicorn main:app --…"   8 days ago       Up 3 hours                      0.0.0.0:4444->8080/tcp, [::]:4444->8080/tcp                                                                                                 voice_toon_api
1ef8daa96af3   debezium/debezium-ui:latest                                "/deployments/run-ja…"   2 weeks ago      Up 3 hours                      0.0.0.0:8568->8080/tcp, [::]:8568->8080/tcp                                                                                                 debezium-ui
5e9aa6cd4123   debezium/connect:3.0.0.Final                               "/docker-entrypoint.…"   2 weeks ago      Up 3 hours (unhealthy)          8778/tcp, 9092/tcp, 0.0.0.0:8093->8083/tcp, [::]:8093->8083/tcp                                                                             debezium
fa8d230cf079   confluentinc/cp-enterprise-control-center:latest           "/etc/confluent/dock…"   2 weeks ago      Up 3 hours (unhealthy)          0.0.0.0:9321->9021/tcp, [::]:9321->9021/tcp                                                                                                 control-center
194c62554175   confluentinc/cp-kafka:7.4.0                                "/etc/confluent/dock…"   2 weeks ago      Up 3 hours (healthy)            0.0.0.0:9092->9092/tcp, [::]:9092->9092/tcp, 0.0.0.0:9101->9101/tcp, [::]:9101->9101/tcp, 0.0.0.0:29092->29092/tcp, [::]:29092->29092/tcp   broker
d2fe1598b7e4   bitnami/spark:latest                                       "/bin/sh -c 'pip ins…"   2 weeks ago      Up 3 hours                                                                                                                                                                  spark-worker
ee048f667bc8   bitnami/spark:latest                                       "/bin/sh -c 'pip ins…"   2 weeks ago      Up 3 hours                      0.0.0.0:7077->7077/tcp, [::]:7077->7077/tcp, 0.0.0.0:8081->8081/tcp, [::]:8081->8081/tcp                                                    spark-master
2df05a750140   confluentinc/cp-zookeeper:7.4.0                            "/etc/confluent/dock…"   2 weeks ago      Up 3 hours (healthy)            2888/tcp, 0.0.0.0:2181->2181/tcp, [::]:2181->2181/tcp, 3888/tcp                                                                             zookeeper
b9d4f0acba57   dpage/pgadmin4:latest                                      "/entrypoint.sh"         2 weeks ago      Up 3 hours                      443/tcp, 0.0.0.0:5050->80/tcp, [::]:5050->80/tcp                                                                                            pgadmin
bafa3d4a6635   grafana/grafana:latest                                     "/run.sh"                2 weeks ago      Restarting (1) 48 seconds ago                                                                                                                                               grafana
yaz@gpu:~/specific_job$ 



version: '3.8'


services:
  api:
    build:
      context: ./api
      dockerfile: Dockerfile
    image: specificjob-api
    ports:
      - "6437:8080"
    volumes:
      - ./api/src:/home/docker/app
    environment:
      - PYTHONUNBUFFERED=1
    restart: unless-stopped




    


























yaz@gpu:~/specific_job$ docker logs spisficjob-api-1
INFO:     Uvicorn running on http://0.0.0.0:8080 (Press CTRL+C to quit)
INFO:     Started parent process [1]
yaz@gpu:~/specific_job$ 











/home/yaz/specific_job/api/src/routes:
__init__.py  __pycache__  service.py  user.py

/home/yaz/specific_job/api/src/routes/__pycache__:
__init__.cpython-312.pyc  user.cpython-312.pyc

/home/yaz/specific_job/api/src/schemas:
error.py  __init__.py  __pycache__  user.py

/home/yaz/specific_job/api/src/schemas/__pycache__:
error.cpython-312.pyc  __init__.cpython-312.pyc  user.cpython-312.pyc

/home/yaz/specific_job/api/src/services:
__init__.py  main.py  __pycache__

/home/yaz/specific_job/api/src/services/__pycache__:
__init__.cpython-312.pyc  main.cpython-312.pyc

/home/yaz/specific_job/api/src/static:
job_data.csv
yaz@gpu:~/specific_job$ cd ~/specific_job
docker compose down  # Stop and remove any existing containers
docker compose up -d --build
WARN[0000] /home/yaz/specific_job/docker-compose.yml: the attribute `version` is obsolete, it will be ignored, please remove it to avoid potential confusion 
WARN[0000] /home/yaz/specific_job/docker-compose.yml: the attribute `version` is obsolete, it will be ignored, please remove it to avoid potential confusion 
Compose can now delegate builds to bake for better performance.
 To do so, set COMPOSE_BAKE=true.
[+] Building 382.5s (21/21) FINISHED                                                                                                                          docker:default
 => [api internal] load build definition from dockerfile                                                                                                                0.0s
 => => transferring dockerfile: 986B                                                                                                                                    0.0s
 => [api internal] load metadata for docker.io/library/python:3.9-slim                                                                                                  1.0s
 => [api internal] load .dockerignore                                                                                                                                   0.0s
 => => transferring context: 2B                                                                                                                                         0.0s
 => [api internal] load build context                                                                                                                                   0.0s
 => => transferring context: 265.23kB                                                                                                                                   0.0s
 => [api builder-image 1/9] FROM docker.io/library/python:3.9-slim@sha256:bef8d69306a7905f55cd523f5604de1dde45bbf745ba896dbb89f6d15c727170                             14.3s
 => => resolve docker.io/library/python:3.9-slim@sha256:bef8d69306a7905f55cd523f5604de1dde45bbf745ba896dbb89f6d15c727170                                                0.0s
 => => sha256:d691b80d5159dfbcf2c1daad72a24c0fb9a55b6d90d6a11dcd46384ff1afa64d 3.51MB / 3.51MB                                                                          4.5s
 => => sha256:84b1a677eccc72224f1c1f6beece7da2221414861259d64d106a62d9b1f704e0 14.93MB / 14.93MB                                                                       13.6s
 => => sha256:fb95b45635cb4f373b9afdfb37bc513f1cc179ce6bd32904fb5570188eee2f29 249B / 249B                                                                              0.4s
 => => sha256:bef8d69306a7905f55cd523f5604de1dde45bbf745ba896dbb89f6d15c727170 10.41kB / 10.41kB                                                                        0.0s
 => => sha256:c8ecde0b63a4881272d794f7fcf2ba2ed4c0f7594c8d783905423e7e964ade28 1.75kB / 1.75kB                                                                          0.0s
 => => sha256:9a041530811d5397b63cb7255cdcdd27195706cf5faf81d77242cd01d7a68da8 5.29kB / 5.29kB                                                                          0.0s
 => => extracting sha256:d691b80d5159dfbcf2c1daad72a24c0fb9a55b6d90d6a11dcd46384ff1afa64d                                                                               0.2s
 => => extracting sha256:84b1a677eccc72224f1c1f6beece7da2221414861259d64d106a62d9b1f704e0                                                                               0.7s
 => => extracting sha256:fb95b45635cb4f373b9afdfb37bc513f1cc179ce6bd32904fb5570188eee2f29                                                                               0.0s
 => [api builder-image 2/9] RUN apt-get update && apt-get install -y --no-install-recommends     build-essential     ffmpeg libavcodec-extra libopus0                 257.1s
 => [api runner-image 2/7] RUN apt-get update && apt-get install -y --no-install-recommends     ffmpeg libavcodec-extra libopus0                                      202.2s
 => [api runner-image 3/7] RUN useradd --create-home docker                                                                                                             0.2s
 => [api builder-image 3/9] RUN pip install --upgrade pip                                                                                                               5.5s
 => [api builder-image 4/9] RUN pip install nltk                                                                                                                        5.5s
 => [api builder-image 5/9] RUN python3 -m nltk.downloader punkt                                                                                                       10.1s
 => [api builder-image 6/9] COPY requirements.txt .                                                                                                                     0.0s
 => [api builder-image 7/9] RUN pip install --no-cache-dir -r requirements.txt                                                                                         48.0s
 => [api builder-image 8/9] RUN pip install --no-cache-dir --force-reinstall numpy==1.26.4 pandas==2.2.2                                                               33.8s
 => [api builder-image 9/9] RUN pip cache purge                                                                                                                         0.5s
 => [api runner-image 4/7] COPY --from=builder-image /usr/local /usr/local                                                                                              1.8s
 => [api runner-image 5/7] RUN mkdir /home/docker/app                                                                                                                   0.2s
 => [api runner-image 6/7] WORKDIR /home/docker/app                                                                                                                     0.0s
 => [api runner-image 7/7] COPY src /home/docker/app                                                                                                                    0.0s
 => [api] exporting to image                                                                                                                                            2.6s
 => => exporting layers                                                                                                                                                 2.6s
 => => writing image sha256:bc2cf340c2e73690a5c74fc1ddb640c09b991cdc88be8e419aeff85b38d782ba                                                                            0.0s
 => => naming to docker.io/library/specificjob-api                                                                                                                      0.0s
 => [api] resolving provenance for metadata file                                                                                                                        0.0s
[+] Running 3/3
 ✔ api                         Built                                                                                                                                    0.0s 
 ✔ Network spisficjob_default  Created                                                                                                                                  0.0s 
 ✔ Container spisficjob-api-1  Started                                                                                                                                  0.3s 
yaz@gpu:~/specific_job$ 

yaz@gpu:~/specific_job$ ls
api  docker-compose.yml  README.md
yaz@gpu:~/specific_job$ cd api
yaz@gpu:~/specific_job/api$ ls
dockerfile  Makefile  README.md  requirements.txt  src
yaz@gpu:~/specific_job/api$ cd src
yaz@gpu:~/specific_job/api/src$ ls
config  main.py  __pycache__  routes  schemas  services  static
yaz@gpu:~/specific_job/api/src$ cd config
yaz@gpu:~/specific_job/api/src/config$ ls
__init__.py  __pycache__  setting.py
yaz@gpu:~/specific_job/api/src/config$ cd schema
bash: cd: schema: No such file or directory
yaz@gpu:~/specific_job/api/src/config$ cd ..
yaz@gpu:~/specific_job/api/src$ cd schema
bash: cd: schema: No such file or directory
yaz@gpu:~/specific_job/api/src$ cd schemas
yaz@gpu:~/specific_job/api/src/schemas$ ls
error.py  __init__.py  __pycache__  user.py
yaz@gpu:~/specific_job/api/src/schemas$ cd ..
yaz@gpu:~/specific_job/api/src$ cd services
yaz@gpu:~/specific_job/api/src/services$ ls
__init__.py  main.py  __pycache__
yaz@gpu:~/specific_job/api/src/services$ cd ..
yaz@gpu:~/specific_job/api/src$ cd static
yaz@gpu:~/specific_job/api/src/static$ ls
job_data.csv
yaz@gpu:~/specific_job/api/src/static$ ^C
yaz@gpu:~/specific_job/api/src/static$ 








from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    APP_ROOT: str = "/api/v0"
    APP_NAME: str = "jobs"
    APP_DESCRIPTION: str = "specific-job"
    DOMAIN: str = "0.0.0.0"
    BACKEND_PORT: int = 8080
    DEBUG_MODE: bool = True


import uvicorn
from fastapi import APIRouter
from services import *

service = APIRouter(
    prefix="/specific-job",
    tags=["Perdict"]
)


if __name__ == "__main__":
    uvicorn.run(service)

# uvicorn main:app --reload



from fastapi import APIRouter, UploadFile, File, Form, HTTPException
from services.main import JobMatcher

router = APIRouter(
    prefix="/specific job",
    tags=["specific job"]
)

job_matcher = JobMatcher()

@router.post("/inference")
async def match_cv(
    file: UploadFile = File(...),
    job_title: str = Form(...),
    governorate: str = Form(...),
    level: str = Form(...)
):
    if not file.filename.endswith((".pdf", ".docx", ".txt")):
        raise HTTPException(status_code=400, detail="Only PDF, DOCX, and TXT files are supported.")

    try:
        result = job_matcher.match_job(file, job_title, governorate, level)
        if "error" in result:
            raise HTTPException(status_code=400, detail=result["error"])
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))




import os
import re
import pandas as pd
import PyPDF2
import docx
import nltk
from fastapi import UploadFile
from io import BytesIO

# Download NLTK data (punkt for tokenization)
try:
    nltk.download('punkt', quiet=True)
except Exception as e:
    print(f"Warning: Failed to download NLTK punkt: {e}")

# Constants
STOPWORDS = set([
    "a", "the", "of", "and", "to", "up", "i", "com", "student", "education", "experience"
])

class JobMatcher:
    def __init__(self):
        # Resolve the path to job_data.csv relative to this file
        base_dir = os.path.dirname(os.path.abspath(__file__))
        self.data_path = '/home/yaz/specific_job/api/src/static/job_data.csv'
        self.df, self.error = self.load_data()
        if self.error:
            raise ValueError(self.error)
        self.all_skills = self.get_all_skills()

    def load_data(self):
        try:
            if not os.path.exists(self.data_path):
                return None, f"File not found: {self.data_path}"
            df = pd.read_csv(self.data_path)
            required_columns = ['Job Title', 'skills', 'Governorate']
            for col in required_columns:
                if col not in df.columns:
                    return None, f"Missing column: {col}"
            level_col = 'professional level' if 'professional level' in df.columns else 'professional Level'
            if level_col not in df.columns:
                return None, "Missing professional level column"
            return df, None
        except Exception as e:
            return None, f"Error loading data: {e}"

    def extract_text_from_cv(self, file: UploadFile):
        text = ""
        ext = file.filename.split('.')[-1].lower()
        try:
            file_content = file.file.read()  # Read file content into memory
            if ext == 'pdf':
                reader = PyPDF2.PdfReader(BytesIO(file_content))
                for page in reader.pages:
                    text += page.extract_text() or ""
            elif ext == 'docx':
                doc = docx.Document(BytesIO(file_content))
                text = "\n".join([para.text for para in doc.paragraphs])
            elif ext == 'txt':
                text = file_content.decode('utf-8')
            else:
                return None, f"Unsupported file format: {ext}"
            return text, None
        except Exception as e:
            return None, str(e)

    def extract_skills(self, text, skills_list):
        if not text:
            return []
        text = text.lower()
        found = [s for s in skills_list if re.search(r'\b' + re.escape(s.lower()) + r'\b', text)]
        filtered = [s for s in found if s.lower() not in STOPWORDS and len(s) > 2]
        return list(set(filtered))

    def analyze_skills(self, user_skills, job_skills):
        user_lower = set(s.lower() for s in user_skills)
        matched = [s for s in job_skills if s.lower() in user_lower]
        missing = [s for s in job_skills if s.lower() not in user_lower]
        return matched, missing

    def get_all_skills(self):
        if self.df is None:
            raise ValueError("DataFrame not loaded. Check the job_data.csv file.")
        all_skills = []
        for skill_text in self.df['skills']:
            skills = [s.strip() for s in str(skill_text).split(',')]
            all_skills.extend(skills)
        return list(set(all_skills))

    def match_job(self, file: UploadFile, job_title: str, governorate: str, level: str):
        # Validate inputs
        job_title = job_title.strip().lower()
        governorate = governorate.strip().lower()
        level = level.strip().lower()
        if not all([job_title, governorate, level]):
            return {"error": "Job title, governorate, and level must not be empty."}

        # Extract text from CV
        text, error = self.extract_text_from_cv(file)
        if error:
            return {"error": error}

        # Extract user skills
        user_skills = self.extract_skills(text, self.all_skills)
        if not user_skills:
            return {"error": "No valid skills found in CV."}

        # Normalize DataFrame for matching
        if self.df is None:
            return {"error": "DataFrame not available for matching."}
        df = self.df.copy()  # Use a copy to avoid modifying the original
        level_col = 'professional level' if 'professional level' in df.columns else 'professional Level'
        df['job_title_lower'] = df['Job Title'].str.strip().str.lower()
        df['governorate_lower'] = df['Governorate'].str.strip().str.lower()
        df['level_lower'] = df[level_col].str.strip().str.lower()

        # Find matching job
        job_row = df[
            (df['job_title_lower'] == job_title) &
            (df['governorate_lower'] == governorate) &
            (df['level_lower'] == level)
        ]

        if job_row.empty:
            job_row = df[df['job_title_lower'] == job_title]
            if job_row.empty:
                return {"error": f"No matching job found for title '{job_title}'."}

        # Extract job skills
        job_skills = [s.strip() for s in job_row.iloc[0]['skills'].split(',')]
        matched, missing = self.analyze_skills(user_skills, job_skills)
        percent = round((len(matched) / len(job_skills)) * 100, 2) if job_skills else 0
        top_missing = missing[:5] if len(missing) > 5 else missing

        return {
            "summary": f"You match {len(matched)} out of {len(job_skills)} required skills ({percent:.1f}%) for the job '{job_title.title()}' in {governorate.title()} ({level} level).",
            "cv_skills_found": user_skills,
            "matched_skills": {
                "count": len(matched),
                "skills": matched
            },
            "missing_skills": {
                "count": len(missing),
                "skills": missing
            },
            "top_missing_suggestions": top_missing,
            "recommendation": f"To improve your chances, consider learning or highlighting these skills in your CV: {', '.join(top_missing)}."
        }




from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from routes.user import router
import uvicorn
from config import settings

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include the routes from src/routes/user.py
app.include_router(router)

@app.get("/")
def root():
    return {"message": "Click /docs to see the API documentation"}

@app.exception_handler(404)
def not_found_error(request, exc):
    return {"detail": "Page Not Found. Click /docs to see the API documentation"}

@app.exception_handler(Exception)
def handle_exception(request, exc):
    return {"message": f"Oops! {str(exc)}. Please try again!"}

if __name__ == "__main__":
    uvicorn.run(
        "main:app",  # Runs relative to the current directory (api/src/)
        host=settings.DOMAIN,
        port=settings.BACKEND_PORT,
        reload=settings.DEBUG_MODE if hasattr(settings, "DEBUG_MODE") else False,
    )



FROM ubuntu:20.04 AS builder-image
ARG DEBIAN_FRONTEND=noninteractive
RUN apt-get update && apt-get install -y --no-install-recommends \
    python3.9 python3.9-dev python3.9-venv python3-pip python3-wheel \
    build-essential git \
    ffmpeg libavcodec-extra libopus0
RUN python3.9 -m venv /home/docker/venv
ENV PATH="/home/docker/venv/bin:$PATH"
RUN python3.9 -m pip install --upgrade pip
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

FROM ubuntu:20.04 AS runner-image
RUN apt-get update && apt-get install -y --no-install-recommends \
    python3.9 python3-venv \
    ffmpeg libavcodec-extra libopus0
RUN useradd --create-home docker
COPY --from=builder-image /home/docker/venv /home/docker/venv
USER docker
RUN mkdir /home/docker/app
WORKDIR /home/docker/app
COPY ./src /home/docker/app
EXPOSE 8080
ENV PYTHONUNBUFFERED=1
ENV VIRTUAL_ENV=/home/docker/venv
ENV PATH="/home/docker/venv/bin:$PATH"
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080", "--workers", "3", "--log-level", "debug", "--timeout-keep-alive", "1000"]
