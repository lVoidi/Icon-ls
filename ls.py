#!/usr/bin/python3

import os
from sys import argv
from pathlib import Path
import random

class Extensions:
    def __init__(self):
        
        # Change this to custom if you want
        # to specify a color for each filetype 

        # if it is custom, it will use self.filetype_color dictionary
        # to the colorscheme
        self.colortype = 'rainbow'
        self.end = "\n"
        self.show_hidden = False
        self.only_hidden = False
        self.only_dirs = False
        self.excluded = []
        self.files = os.listdir()
        
        # self.colortype = 'custom'
        self.extensions = {
            'folder': '',
            '.config': '',
            'iso': '',
            'mp3': '',
            'flac': '',
            'm4a': '',
            'wav': '',
            'conf': '',
            'lua': '',
            'html': '',
            'htm': '',
            'css': '',
            'js': '',
            'json': '',
            'rs': '',
            'c': '',
            'h': '',
            'ppt': '󱎐',
            'docx': '󱎒',
            'doc': '󱎒',
            'xls': '󱎏',
            'pdf': '',
            'gz': '',
            'xz': '',
            'bz2': '',
            'bz': '',
            'zip': '',
            'rar': '',
            'zst': '',
            'tar': '',
            'tgz': '',
            'cpp': '',
            'hpp': '',
            'cs': '',
            'png': '',
            'jpg': '',
            'jpeg': '',
            'bmp': '',
            'tif': '',
            'tiff': '',
            'git': '',
            'svg': '',
            'mp4': '',
            'avi': '',
            'mkv': '',
            'vim': '',
            '.vim': '',
            'ts': 'ﯤ',
            'deb': '',
            'md': '',
            'java': '',
            'py': '',
            'pyc': '',
            'php': '',
            'ui': '类',
            'exe': '',
            'appimage': '',
            'sh': '',
            'sql': '',
            'db': '',
            'sqlite': '',
            'sqlite3': '',
            'default': ''
        }
        
        # You can change the filetype color here
        # or you can also add more customized filetypes
        # the colors are in Red, Green and Blue format
        #   filetype    =    (r, g, b)
        self.filetype_color = dict(
            directory = (230, 255, 230),
            file = (255, 230, 230),
            # Examples for different filetypes
            # python = (252, 244, 3),
            # lua = (0, 0, 255)
        )
    
    def generate_rgb_color(self) -> int:
        return random.randint(180, 255)
    
    def return_filetype(self, file):
        
        # File extension, you can play with this to 
        # add custom colors to different filetypes.
        
        # Remember that the value that this function
        # will return, will be used to get the key from
        # the dictionary self.filetype_color
        
        extension = Path(file).suffix.lower().replace('.', '')

        if os.path.isdir(file):
            return 'directory'

        # Different filetype examples
        '''
        elif extension == 'py':
            return 'python'
        
        elif extension == 'lua':
            return 'lua'
        '''       
        # If it is none of them, it will return 
        # the default value
        return 'file'

    
"""
This class will return every single file in a directory in colors 
"""
class Ls(Extensions):
    def __init__(self, args):
        self.args = args
        self.path = os.getcwd()
        super().__init__()
        # Available arguments
        for arg in args:
            if arg in ['-sh', '-a', '--show-hidden']:
                self.show_hidden = True

            elif arg in ['-oh', '-hi', '--only-hidden']:
                self.only_hidden = True
            
            elif arg in ['-od', '-d', '--only-dirs']:
                self.only_dirs = True
            
            elif arg in ['-ex', '--exclude']:
                self.excluded.append(args[args.index(arg)+1])

            elif os.path.isdir(arg):
                self.files = os.listdir(arg)
                self.path = arg
            
            elif arg in ['-h', '--help']:
                self.help()
                exit()

    def help(self):
        print('''
Thanks for using my script!
Available options
-sh -a --show-hidden\t\tShows the hidden files
-oh -hi --only-hidden\t\tShows ONLY the hidden files
-ex --exclude       \t\tExcludes a file extension, for example:
                    \t\t\tls -ex 'py'
                    \t\t\tThis will exclude all the python files
-od -d --only-dirs  \t\tThis will display only the directories
                ''')
    
    
    def show_files(self):
        """
        This function will iterate through every single file with the specified flags
        """
        new_files = []
        for file in self.files:

            if Path(file).suffix.lower().replace('.', '') in self.excluded:
                pass
            
            elif self.show_hidden:
                new_files.append(file)
                
                
            elif self.only_dirs:
                if os.path.isdir(file):
                    new_files.append(file)
                
            elif self.only_hidden:
                if self.is_hidden(file):
                    new_files.append(file)
                
            else:
                if not self.is_hidden(file):
                    new_files.append(file)
    
        self.files = sorted(new_files)

    def is_hidden(self, file):
        """
        Checks if a file is hidden, by checking if it has a dot in the start of its name
        """
        return file.startswith('.')
    
    def is_config_file(self, file):
        """
        Checks if its a configuration file
        """
        for config_ext in ['conf', 'rc']:
            if self.is_hidden(file) or file.startswith(config_ext) or file.endswith(config_ext):
                return True

        return False 

    def file_icon(self, file: str):
        """
        Returns the relationed icon with the filename
        """
        try:
            file_extension = Path(file).suffix.lower().replace('.', '')

            if file == '.config':
                return self.extensions['.config']
            
            elif os.path.isdir(f"{self.path}/{file}"):
                return self.extensions['folder']
            
            elif self.is_config_file(file):
                return self.extensions['conf']
            
            elif file_extension in self.extensions:
                return self.extensions[file_extension]
            
            else:
                return self.extensions['default']
        
        except Exception as e:
            print(type(e).__name__, e)
            exit()

    def get_color_escape(self, r, g, b):
        return f'\033[38;2;{r};{g};{b}m'
    
    def print_(self, file):
        """
        this will print the file with its icon
        """
        colorscheme = (self.generate_rgb_color() for _ in range(3))

        if self.colortype == 'custom':
            filetype = self.return_filetype(file)
            colorscheme = self.filetype_color[filetype]
            print(self.get_color_escape(*colorscheme),
                  self.file_icon(file), '\033[0m',
                  file, end=self.end)  
        else:
            print(
                self.get_color_escape(*colorscheme),
                self.file_icon(file), '\033[0m',
                file, end=self.end)        
        
    def run_(self):
        """
        Prints every single file in a list
        """
        for file_index in range(len(self.files)):
            self.print_(self.files[file_index])


ls = Ls(argv)
ls.show_files()
ls.run_()
