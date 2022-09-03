from time import sleep

from .elements import elements_list


def check(locator):
   locator.hover()


def test_run(page_object):
   res = 0
   for el in elements_list:
      locator = page_object.locator(el)
      check(locator)
      res += 1
   print(f"\n\nElements hovered: {res}")
