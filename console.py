#!/usr/bin/python3
'''File for console'''

import sys
import cmd
import json

import models


class HBNBCommand(cmd.Cmd):
    '''inheritor of cmd'''

    prompt = '(hbnb) '

    def do_quit(self, line):
        '''quit: quit the console'''
        return True

    def do_EOF(self, line):
        '''Ctrl+D: quit the console'''
        return True

    def do_create(self, ClassName):
        '''create [ClassName]: Creates a new instance of BaseModel, 
        saves it (to the JSON file) and prints the id'''
        if not ClassName:
            print("** class name missing **")
        elif ClassName not in models.__all__:
            print("** class doesn't exist **")
        else:
            VerifiedClass = getattr(models, ClassName)
            NewInstance = VerifiedClass()
            NewInstance.save()
            print(NewInstance.id)

    def do_show(self, line):
        '''show [ClassName] [id]: Prints the string representation of an instance
         based on the class name and id'''        
        try:
            ClassName,id = [str(s) for s in line.split()]
        except:
            if line:
                ClassName = line
            else:
                ClassName = None
            id = None
        if not ClassName:
            print("** class name missing **")
        elif not id:
            print("** instance id missing **")
        elif ClassName not in models.__all__:
            print("** class doesn't exist **")
        else:
            Instance = ClassName + '.' + id
            with open('file.json') as SaveFile:
                SavedDict = json.load(SaveFile)
            if Instance in SavedDict:
                print(print_formater(ClassName, id) + str(SavedDict[Instance]))
            else:
                print("** no instance found **")

    def do_destroy(self, line):
        '''destroy [ClassName] [id]: Deletes an instance based on the class name and id'''        
        try:
            ClassName,id = [str(s) for s in line.split()]
        except:
            if line:
                ClassName = line
            else:
                ClassName = None
            id = None
        if not ClassName:
            print("** class name missing **")
        elif ClassName not in models.__all__:
            print("** class doesn't exist **")
        elif not id:
            print("** instance id missing **")
        else:
            Instance = ClassName + '.' + id
            with open('file.json') as SaveFile:
                SavedDict = json.load(SaveFile)
            if Instance in SavedDict:
                del SavedDict[Instance]
                with open('file.json', 'w') as SaveFile:
                    json.dump(SavedDict, SaveFile)
                print (Instance + " deleted")
            else:
                print("** no instance found **")

    def do_all(self, ClassName):
        '''all [ClassName (optional)]: Prints all string representation of 
        all instances based or not on the class name'''
        with open("file.json") as SaveFile:
            SavedDict = json.load(SaveFile)
        printer = []
        if ClassName:
            if ClassName not in models.__all__:
                print("** class doesn't exist **")
            else:
                for key in SavedDict:
                    KeyClass = key.split('.')
                    if KeyClass[0] == ClassName:
                        printer.append(
                            print_formater(KeyClass[0], KeyClass[1]) +
                            str(SavedDict[key])
                            )
                print(printer)
        else:
            for key in SavedDict:
                KeyClass = key.split('.')
                printer.append(
                    print_formater(KeyClass[0], KeyClass[1]) +
                    str(SavedDict[key])
                    )
            print(printer)
        
    def do_update(self, line):
        '''update [ClassName] [id] [AttributeName] [Value]: Updates an instance 
        based on the class name and id by adding or updating attribute'''
        with open("file.json") as SaveFile:
            SavedDict = json.load(SaveFile)
        try:
            ClassName,id,AttrName,Value = [str(s) for s in line.split()]
        except:
            try:
                ClassName,id,AttrName = [str(s) for s in line.split()]
                print("** value missing **")
                return
            except:
                try:
                    ClassName,id = [str(s) for s in line.split()]
                    Instance = ClassName + '.' + id
                    if Instance in SavedDict:
                        print("** attribute name missing **")
                    else:
                        print("** no instance found **")
                    return
                except:
                    if line:
                        if line in models.__all__:
                            print("** instance id missing **")
                        else:
                            print("** class doesn't exist **")
                    else:
                        print("** class name missing **")
        Instance = ClassName + '.' + id
        if Instance in SavedDict:
            SavedDict[Instance][AttrName] = Value
            with open("file.json", "w") as SaveFile:
                json.dump(SavedDict, SaveFile)
        else:
            print("** no instance found **")



def print_formater(ClassName, id):
    strout = "["
    strout += ClassName
    strout += "] ("
    strout += id
    strout += ") "
    return strout


if __name__ == '__main__':
    HBNBCommand().cmdloop()