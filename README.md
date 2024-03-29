# Genshin Impact Macros
Automate interactions with characters in the game Genshin Impact with this Python script. The script simulates mouse clicks to progress through character conversations and randomly selects answers to the dialogue prompts.

## Setup
To get started with the Genshin Impact Macros, follow these steps:

1. Set up a virtual environment:
    ```bash
    python -m venv venv
    venv\Scripts\activate
    ```

2. Install dependencies using pip:
    ```bash
    pip install -r requirements.txt
    ```

3. Deactivate the virtual environment
    ```bash
    deactivate
    ```

4. **Create a .bat file with the following content, make sure to replace `C:\location\to\genshin-macros` with the actual path to your `genshin-macros` directory**: This will activate the virtual environment and execute the macros file from the right directory 
    ```bat
    @echo off
    cd C:\location\to\genshin-macros
    call venv\Scripts\activate
    python genshin_macros.py
    ```

5. **Create a shortcut of the .bat file and move it to `C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Genshin Impact`:** Placing the shortcut in this location will make 
it accessible from the Start Menu.

6. **Right-click the shortcut and enable "Run as administrator":** This step ensures the script has the necessary permissions to interact with the game.

## How to use
To use the Genshin Impact Macros:
* Press **SHIFT + W + S** to **activate** the autoclicking: This will start the automated clicking of conversations.
* Press **SHIFT** to **deactivate** the autoclicking: This will stop the automated clicking.

Now, when you click on the shortcut, the Genshin Impact Macros will automatically initiate and handle conversations with characters within the game, saving you time and effort during gameplay.

Please exercise caution while using this script and ensure compliance with the game's terms of service. Enjoy your automated conversations in Genshin Impact!
