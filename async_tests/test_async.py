import asyncio
import pytest

from asyncio import sleep

from .elements import elements_list


async def check(locator):
   await locator.hover()

async def job(page_object):
   chunk = 100
   tasks = []

   res = 0
   for el in elements_list:
      locator = page_object.locator(el)
      tasks.append(asyncio.create_task(check(locator)))
      res += 1
      if len(tasks) == chunk:
         await asyncio.gather(*tasks)
         tasks = []
   return res


@pytest.mark.asyncio
async def test_run(page_object):
   res = await job(page_object)
   print(f"\n\nElements hovered: {res}")
