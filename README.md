# inkybar - Barcodes for Inky pHAT

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

## To-do list
* TODO: Text below barcode bars
* TODO: Fully support code 128 format
