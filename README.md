# inkybar - Barcodes for Inky pHAT

```python
import inkybar
import inkyphat

# Draw a code-39 barcode
inkybar.c39rect("HELLO WORLD.")
inkyphat.show()

inkybar.c128rect("Hello, world!")
inkyphat.show()
```

## To-do list
* TODO: Text below barcode bars
* TODO: Fully support code 128 format
