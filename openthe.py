#!/usr/bin/env python3

import os
import sys

class make_openable(object):
  openable_funcs = {}

  def __init__(self, id, description):
    if id in self.__class__.openable_funcs:
      raise RuntimeError('An openable id %s already exists' % id)
    self.id = id
    self.description = description

  def __call__(self, f):
    self.f = f
    self.__class__.openable_funcs[self.id] = self
    return f;


@make_openable('iphone-sim', 'Opens the iPhone simulator.')
def open_the_iphone_sim():
  os.system('open /Applications/Xcode.app/Contents/Applications/iPhone\ Simulator.app')
  return True

def print_invalid():
  print('Invalid. Please supply what to open, or use --list for a list of things you can open.')

if len(sys.argv) < 2:
  print_invalid()
  exit()

input_str = '-'.join(sys.argv[1:])

if input_str == '--list':

  print('\nopenthe [the most convenient command ever]')
  print('==========================================')
  print('Available openables are listed below:')
  print('[hint: dashes in command names may be replaced with white space]\n')

  for id in make_openable.openable_funcs:
    print(" - %s\t%s" % (id, make_openable.openable_funcs[id].description))
  print('')

elif input_str in make_openable.openable_funcs:
  make_openable.openable_funcs[input_str].f()
else:
  print_invalid()
