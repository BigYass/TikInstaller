import asyncio
import threading
import time
import os
from api import paper

async def test_paper_api() -> None:
  print('Getting Paper projects...')
  t = await paper.get_latest_version_url()
  
  print('Link : ' + t)
   
  pass

def test_loop(_time: int = 10) -> None:
  print('  Start Loop', os.getpid())
  while _time > 0:
    print('  Looped', _time)
    _time -= 1
    time.sleep(2) 
    
  print('  Loop finished')
  
def test_async() -> None:
  task = asyncio.create_task(test_loop())
  
  print('Some stuff...')
  
  time.sleep(3)
  
  print('Some other stuff...')
  
  print('Last stuff...')

def test_thread() -> None:
  t = threading.Thread(target=test_loop, args=[5])
  t.daemon = True

  t.start()
  
  print('sheesh')
  
  time.sleep(3)
  
  print('wooow', os.getpid())
  
  t.join()
  
  print('end')
  
async def test() -> None:
  print('Starting tests...')
  
  # print('Testing Paper Download API...')
  # await test_paper_api()
  
  # print('Testing asyncio...')
  # await test_async()
  
  print('Testing threads...')
  test_thread()

if __name__ == '__main__':
  print('test')
  asyncio.run(test())