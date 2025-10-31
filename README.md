# Mozart Musical Dice Game

This project plays a randomly generated waltz using the rules of Mozart's Musical Dice Game. It stitches together pre-recorded measures that live in the `mozart/` folder.

## Requirements

- Python 3.8+
- `simpleaudio` for audio playback (`pip install simpleaudio`)

## Usage

```
python3 musical_dice_game.py --help
```

To play a waltz with the bundled samples:

```
python3 musical_dice_game.py
```

If you store the Mozart samples elsewhere, point the script at that directory:

```
python3 musical_dice_game.py --samples /path/to/mozart
```

The script rolls virtual dice to pick measures for both the minuet and trio sections, then plays them sequentially. Use `Ctrl+C` to stop playback early if needed.
