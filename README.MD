# Minecraft Mod Helper aka mc-mod-helper

### By GalaxyGamingBoy

### License: MIT

## Commands - How To Use The Utility

To run the program type the following on the terminal:

- Windows `.\mcmodhelper.exe`
- Universal `./mcmodhelper.py`

Next you type the option.
Here is a list:
`itemconfig`, `blockconfig`, `tooltiplang`, `loottable`, `needstool`

## Here is the syntax with all of the options

To add an item to lang and create model file type this:     
`itemconfig 'modid' 'item_name_same_as_registered' 'item_name_in_inventory' 'langfile' 'texture_name'`     
For Example:     
`itemconfig 'test_modid' 'test_item' 'Test Item' 'en-us' 'test_item'`     

---

To add a block to lang, create model and basic blockstate     
`blockconfig 'modid' 'block_name_same_as_registered' 'block_name_in_inventory' 'langfile' 'texture_name'`     
For Example:     
`blockconfig 'test_modid' 'test_block' 'Test Block' 'en-us' 'test_block'`     

---

To add a tooltip to lang type this:     
`tooltiplang 'modid' 'tooltip' 'target_item_or_block' 'entry_num' 'langfile'`     
For Example:     
`toltiplang 'test_modid' 'This is a test tooltip' 'test_item' '0' 'en-us'`     

---

To add a basic loottable type this:     
`loottable 'modid' 'block'`          
For Example:     
`loottable 'test_modid' 'test_block'`     

---

To add a block to a specific `harvest level` and `tool type` type this:     
`needstool 'modid' 'harvest_level' 'tool_type' 'block'`     
For Example:     
`needstool 'test_modid' 'iron' 'axe' 'test_block'`     

---

## Instruction - Download & Install

1. Download latest release `mcmodhelper-universal.zip for linux/mac/windows (.py) or mcmodehelper-windows.zip for Windows` file
2. Extract the zip file
3. Place the contents of the zip file (`template (Folder) + .py or .exe file depending on version`)
   to `src/main/resources`
4. Completed!

---

## Building

### Universal ZIP

The .py file provided is developed with `Python 3.9.5`  
The following .py file needs these extensions:

- Typer [- PyPi Link](https://pypi.org/project/typer/)

### Windows Build

The Windows EXE file is generated with `Pyinstaller` and the command is:     
`pyinstaller --onefile --icon icon.ico .\mcmodhelper.py`
