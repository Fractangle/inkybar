# inkybar - Barcodes for Inky pHAT

Draw barcodes with functions as similar in feel as possible to the inkyphat drawing functions.

##Example

```python
import inkybar
import inkyphat

# Draw a code-39 barcode
inkybar.c39rect("HELLO WORLD.")
inkyphat.show()

# Clear the screen
inkyphat.rectangle((0, 0, inkyphat.WIDTH, inkyphat.HEIGHT), inkyphat.WHITE)

# Draw a code-128 barcode
inkybar.c128rect("Hello, world!")
inkyphat.show()

# Clear the screen
inkyphat.rectangle((0, 0, inkyphat.WIDTH, inkyphat.HEIGHT), inkyphat.WHITE)

# Draw narrower barcodes at specific positions
inkybar.c39rect("HERE", (5, 5), 15)
inkybar.c128rect("There", (90, None), 25)
inkybar.c39rect("ANYWHERE", (None, 75), 20)
inkyphat.show()
```

## Usage:

### Code 39:

```python
inkybar.c39rect(text, xy=(None, None), height=inkyphat.HEIGHT, smashCase=False)
```

Draws a Code 39 barcode.

`text` is the text to encode. If it contains characters that can't be represented in Code 39, raises `ValueError`.

`xy` is a 2-tuple of x and y coordinates corresponding to the top-left corner of the barcode (including the quiet zone). If either of them are set to `None`, the barcode will be centered along that axis. Defaults to `(None, None)`, which centers it in the screen.

`height` is the height in pixels to draw the barcode. If omitted, defaults to `inkyphat.HEIGHT`.

`smashCase`, if `True`, converts the string to uppercase before attempting to encode it. (Code 39 only supports monocase characters.)

---

```python
inkybar.c39bits(text, smashCase=False)
```

Returns an array of 1s and 0s corresponding to black and white pixels (including the quiet zone).

`text` is the text to encode. If it contains characters that can't be represented in Code 39, raises `ValueError`.

`smashCase`, if `True`, converts the string to uppercase before attempting to encode it. (Code 39 only supports monocase characters.)

### Code 128:

```python
inkybar.c128rect(text, xy=(None, None), height=inkyphat.HEIGHT)
```

`text` is the text to encode. If it contains characters that can't be represented in Code 128, raises `ValueError`.

`xy` is a 2-tuple of x and y coordinates corresponding to the top-left corner of the barcode (including the quiet zone). If either of them are set to `None`, the barcode will be centered along that axis. Defaults to `(None, None)`, which centers it in the screen.

`height` is the height in pixels to draw the barcode. If omitted, defaults to `inkyphat.HEIGHT`.

---

```python
inkybar.c128bits(text)
```

Returns an array of 1s and 0s corresponding to black and white pixels (including the quiet zone).

## To-do list
* TODO: Text below barcode bars
