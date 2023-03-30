# How to run

## Requirements
- `conda`
- `make`

1. Setup the conda environment
```bash
conda env create -n cs-471-generals -f requirements.yaml
conda activate cs-471-generals
```

2. Create game:
Go to the [generals bot server](https://bot.generals.io/) and create a custom game.
    - click play
    - it might force you to play a short tutorial
    - create a custom game

3. Create secrets:
Create a file called `secrets.sh` and fill it with the following (replacing any `<fielsd>` with valid content)
```bash
export GAME_ID="<game_id_from_the_url>"
export USER_ID="<whatever you want>"
export USERNAME="<whatever you want>"
```

Now run
```bash
source secrets.sh
```

4. Run the project code
```bash
make run
```

5. You should now be able to talk to your computer and the player that is run through the API will react. 
There is currently no UI to go with it, but you can give it some commands and it will run them on the battlefield.
You can kill the process with `^C` and then watch the replay to see how the actions interacted with the units on the field.