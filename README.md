<div align="center">
  <h1>Icon ls</h1>
</div>

<div>
  <p>
    <ul>
      <li><a href="#installation">Instalation</a></li>
      <li><a href="#usage">Usage</a></li>
      <li><a href="">Configuration</a></li>
      <li><a href="">Troubbleshooting</a></li>
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
  <b>Options</b>
  <pre>
      -sh -a --show-hidden            Shows the hidden files
      -oh -hi --only-hidden           Shows ONLY the hidden files
      -ex --exclude                   Excludes a file extension, for example:
                                              ls -ex 'py'
                                              This will exclude all the python files
  </pre>
  </p>
</div>
