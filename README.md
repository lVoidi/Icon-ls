<div align="center">
  <h1>Icon ls</h1>

</div>

![image](https://user-images.githubusercontent.com/81118866/129489117-f2151b54-3418-4094-89b8-cd0add78805f.png)


<div>
  <p>
    <ul>
      <li><a href="#installation">Installation</a></li>
      <li><a href="#docker">Docker</a></li>
      <li><a href="#usage">Usage</a></li>
      <li><a href="#config">Configuration</a></li>
    </ul>
  </p>
</div>

-----

<div>
  <h1 id="installation">Installation</h1>
  
  <p>
It is required to have a terminal with nerd fonts installed: <a href="https://nerdfonts.com" target="blank_">the nerd fonts</a>. <br>

  <hr>

  After you install the script, you have 3 options:

  <ul>
    <li>You can create a binary file by using <a href="https://www.pyinstaller.org/">pyinstaller</a> or py2bin</li>
    <li>You can create a simple alias in your .zshrc to call the script</li>
    <li>Or you can make the script executable</li>
  </ul>

  I will explain <b>the second option</b> because it is way easier and its the same thing
  
  we need to go our home directory
  <pre>
    cd
  </pre>
  
  and then edit your shell config file.
  For this, you can use vim, neovim, emacs, nano or any other
  
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
  
  <b>NOTE:</b>
  To make your script executable use the command <b>chmod +x /path/to/script.py</b>

  </p>

</div>

-----

<div>
  <h1 id="docker">Docker</h1>
  
  <p>
    You can also run this tool using Docker. The Docker setup includes the required Nerd Fonts pre-installed.
  
  <h3>Using docker-compose (Recommended)</h3>
  
  <pre>
    # Build and run the container
    docker-compose run ls-icons

    # To run in a specific directory
    docker-compose run ls-icons directory/

    # To run with options
    docker-compose run ls-icons -sh
  </pre>

  <h3>Using Docker directly</h3>
  
  <pre>
    # Build the image
    docker build -t icon-ls .

    # Run the container
    docker run --rm -v $(pwd):/app icon-ls

    # To run in a specific directory
    docker run --rm -v $(pwd):/app -w /app icon-ls directory/

    # To run with options
    docker run --rm -v $(pwd):/app icon-ls -sh
  </pre>

  <b>Note:</b> The Docker setup includes:
  <ul>
    <li>Pre-installed DejaVuSansMono Nerd Font</li>
    <li>Python 3.9 environment</li>
    <li>Proper terminal color support</li>
  </ul>
  </p>
</div>

-----

<div>
  <h1 id="usage">Usage</h1>
  <p>
  Type in your terminal 
  <code>ls</code>

  You can also see what's inside a directory
  <code>ls directory/</code>
  
  <b>Options</b>
  <pre>
      -h  --help                      Shows this dialog
      -sh -a --show-hidden            Shows the hidden files
      -oh -hi --only-hidden           Shows ONLY the hidden files
      -ex --exclude                   Excludes a file extension, for example:
                                              ls -ex 'py'
                                              This will exclude all the python files
      -od -d --only-dirs              This will display only the directories
  </pre>
  </p>
</div>

-----




<div>
  <h1>Thanks for using my script!</h1>
</div>
