<div align="center">
  <h1>Icon ls</h1>
</div>

<div>
  <p>
    <ul>
      <li><a href="#installation">Instalation</a></li>
      <li><a href="#usage">Usage</a></li>
      <li><a href="#config">Configuration</a></li>
    </ul>
  </p>
</div>

-----

<div>
  <h1 id="installation">Installation</h1>
  
  <p>
    The first thing that we need, are <a href="https://nerdfonts.com" target="blank_">the nerd fonts</a>, so we can see and personalize the icons in the script <br>
  
  So to do this, we will download any font from <a href="https://nerdfonts.com/font-downloads" target='blank_'>here</a> and copy them to your fonts directory

  <h4>If you dont have the .fonts directory...</h4>
  <pre>
    mkdir ~/.fonts
    mv any-font.zip ~/.fonts
    unzip ~/.fonts/any-font.zip
  </pre>

  and you'll have your font installed

  then, you need to <b>change your terminal font to the installed one</b>, so check your terminal emulator wiki to do that

  <hr>
  
  After installing the font, you can install the script now
  <pre>
    curl https://raw.githubusercontent.com/MrJakeSir/Icon-ls/master/ls.py -o path/to/script
  </pre>

  after you install the script, you have two options:

  <ul>
    <li>You can create a binary file by using <a href="https://www.pyinstaller.org/">pyinstaller</a> or py2bin</li>
    <li>Or you can create a simple alias in your .zshrc to call the script</li>
  </ul>

  I will explain <b>the second option</b> because it is way easier and its the same thing
  
  we need to go our home directory
  <pre>
    cd
  </pre>
  
  and then edit your shell config file
  for this, you can use vim, neovim, emacs, nano or any other
  
  <pre>
    # USE YOUR TEXT EDITOR HERE
    
    # For zsh
    nvim .zshrc

    # bash shell
    nvim .bashrc
  </pre>
  
  then, add this line to the end of your file, changing the <i>path/to/script.py</i> to your actual path 
  
  <pre>
    alias ls="python3 path/to/script.py"
  </pre>
  
  <b>restart your terminal</b> and you're done!
  

  </p>

</div>

-----

<div>
  <h1 id="usage">Usage</h1>
  <p>
  Type in your terminal 
  <code>ls</code>
  
  <b>Options</b>
  <pre>
      -h  --help                      Shows this dialog
      -sh -a --show-hidden            Shows the hidden files
      -oh -hi --only-hidden           Shows ONLY the hidden files
      -ex --exclude                   Excludes a file extension, for example:
                                              ls -ex 'py'
                                              This will exclude all the python files
  </pre>


  </p>
</div>


<div>
  <h1 id="config">Configuration</h1>
  <p>
  All you need is in the class <b>Extensions</b>
  It contains all the configuration options, you don't have to 
  create any directory in .config, you just mofify the script itself.

  <h2>Changing icons</h2>
  All the icons are in the variable called <b>self.extensions</b>, 
  it is just a python dictionary, you can add filetypes there with its icon,
  you just need to add the dictionary item

  <pre>
    self.extensions = {
      #... some items here
      'filetype': '<icon>'
    }
  </pre>

  <h2>Changing colors</h2>
  For this, will be a little more complex than just changing the icons.
  First of all, we need to search for this line of code:
  <pre>
    # Change this to custom if you want                                                                                                                                                       
    # to specify a color for each filetype
    # if it is custom, it will use self.filetype_color dictionary
    # to the colorscheme                                                                                                                                                                      
    self.colortype = 'rainbow'
    # self.colortype = 'custom'  
  </pre>
  
  Once found, you have to comment the line self.colortype = 'rainbow'
  by adding a hash symbol at the start of the line, then, you need to
  remove the comment from the line below of it.

  after doing that, it will look something like this
  <pre>
    # Change this to custom if you want                                                                                                                                                       
    # to specify a color for each filetype
    # if it is custom, it will use self.filetype_color dictionary                                                                                                                             
    # to the colorscheme                                                                                                                                                                      
    # self.colortype = 'rainbow'
    self.colortype = 'custom'
  </pre>

  After doing this, we need to find also this line of code
  
  <pre>
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

  </pre>
  
  'file' is the default colour the files

  As you can see in the commented lines, there are examples of 
  how you can add a specific color to the filetype you want, the
  colors are in rgb format, so the first element in the tupple represents
  RED value, second element in the tupple represents GREEN value and the 
  last element in the tupple represents blue value
  
  for example, this line: 
  <code>python = (252, 244, 3) </code>
  <br>
  
  This will show a yellow colour, based on python scheme

  we can add this to our dictionary to make it look something like 
  <pre>
    self.filetype_color = dict(
      # some lines of code..
      python = (252, 244, 3)
    )
  </pre>

  In order to this to work, we'll need to specify the file extension that this item is related to

  To do this, we just need to go to the python function right below it and add a condition for this
  extension. Don't worry! it's very easy! also, there are commented examples that you can use to guide.
  
  the condition has this syntax
  <pre>
    elif extension == 'filetype-extension':
      return 'filetype'
  </pre>
  
  yo need to add that line of code here

  <img src="https://media.discordapp.net/attachments/862479155022659604/875953641855545424/unknown.png?width=696&height=454" alt="codeline">

  Is that easy! using python example...
  <pre>
    elif extension == 'py':
      return 'python'
  </pre>
  
  If the filetype you are refering to, has <b>more than one</b> extensions, you can
  simply use a python list and the <b>in</b> statement

  <pre>
    elif extension in ['py',
                       'pyc']:
      return 'python'
  </pre>
  
  and that's it!

  <h2>Default options</h2>
  <h3>End</h3>
  You can change the separator between each line, the default separator is
  a newline <code>\n</code>, but you can use any other 
  
  just modify this line of code and change the end for whatever you want
  <img src="https://media.discordapp.net/attachments/862479155022659604/875956033716092938/unknown.png?width=488&height=259" alt="end">
  
  <h3>Hidden files or dotfiles</h3>
  You can set the script to show hidden files by default,
  by just changing <code>SHOW\_HIDDEN</code> variable to <b>True</b>
  <img src="https://media.discordapp.net/attachments/862479155022659604/875956540383854592/unknown.png?width=337&height=120" alt="showhidden">
  
  </p>
</div>

-----

<div>
  <h1>Thanks for using my script!</h1>
</div>
