import os
import sys
import argparse
import fire
from getpass import getpass

def hi(name='world'):
    print(f'THIS IS VALUE: {name}')
    return f'hi {name}'

if __name__=='__main__':
    fire.Fire(hi)
