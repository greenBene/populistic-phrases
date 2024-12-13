# Analyzing texts for populistic phrases

This small python script uses the german populism dictionary with 238 phrases from J. Gründl [1] to find populistic phrases in texts.

It prints out all found matches per paragraph.

As input it requires files with a name in the first line, and one line per paragraph for the following lines.
Empty lines are ignored. 
All files in the subfolder `./texts` are automatically analyzed.

To avoid copyright issues, only an self created example text is given in the `./texts/` subfolder. 

## Run
Assuming python3 is installed:

* `python main.py`

## References

[1] Gründl, J. (2022). Populist ideas on social media: A dictionary-based measurement of populist communication. New Media & Society, 24(6), 1481-1499. https://doi.org/10.1177/1461444820976970