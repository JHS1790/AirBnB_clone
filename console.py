#!/usr/bin/python3
'''File for console'''

import cmd

class HBNBCommand(cmd.Cmd):
    '''inheritor of cmd'''

    prompt = '(hbnb)'

    def do_quit(self, line):
        '''quit: quit the console'''
        return True

    def do_EOF(self, line):
        '''Ctrl+D: quit the console'''
        return True

if __name__ == '__main__':
    HBNBCommand().cmdloop()