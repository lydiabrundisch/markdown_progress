# markdown_progress

This is a short workflow to count the number of unticked and ticked checkmarks in a markdown file to update a progress bar. 

## Progress

This README.md file serves as example file formatted in Obsidian flavor markdown, so the display on Github is not fully supported.
Move this file into your vault. Make sure to adapt the paths to the python script and the markdown file if necessary.
In reading mode, hover the code section to reveal the button saying 'Copy' and click it.
Click on 'Open command prompt'. Paste from your clipboard and press enter.
The progress bar will be updated to display the relative share of checked check marks compared to all checkmarks in the file.

```Terminal
py C:\Vault\progress.py
1
C:/Vault/README.md
```

[Open command prompt](<file:///cmd.exe>)

<label for="progress-bar">Adventure progress: </label> <progress id="progress-bar" value="2" max="5"></progress>

## Current projects

- [x] Go on a paddle board trip
- [ ] Go scuba diving
- [ ] Go surfing
- [x] Get a henna tattoo
- [ ] Make a costume for Halloween
