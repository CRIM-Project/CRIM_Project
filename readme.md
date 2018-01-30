# CRIM Data Conversion Project :musical_score:

Convert and organize CRIM data set for furture analysis.

## Project Home Page

* [CRIM Homepage](https://sites.google.com/a/haverford.edu/crim-project/) - Check this out!

	to pull the data from the api and write it to CSVs run:
		`$ python3 counts.py`  

In the future a command line interface will be added and the functionally of the script will be expanded.

As of right now this script writes 7 csvs and one json file. Below is a brief description of each:

##### ema.csv / ema.json
As a csv this file has two features *SongTitle* and *Counts*. *SongTitle* is the title of the piece (e.g. Lassus Roland de : Lassus. Susanne un jour ) and *Counts* is a list of dictionary items. Each dictionary has the keys *measures* and *Song_From*. The *measures* information was pulled from the ema field of the json (which was pulled from the api). The *measures* value signifies which measures of the *SongTitle* were related to the *Song_From* in the users session. Below is an example of one row of the csv  

```
Lassus Roland de : Lassus. Susanne un jour, [ {'measures': '1-2', 'Song_From': 'Lassus, Roland de : Lassus. Susanne un jour'}, ... , {'measures': '31-35', 'Song_From': 'Lassus, Roland de : Lassus. Susanne un jour'} ]
```

The ema.json contains the exact same information but in a .json format

##### relationship_types.csv  

##### user_counts.csv

##### title_counts.csv

##### assertion_types.csv

##### assertion_titles.csv

##### assertion_scores.csv


## Visualizations
Currently we are working on two visualizations.
	One is a a modified chord diagram to visualize the relationship between musical types and relationship types. This was largerly inspired by visualcinnamon's blog [post](https://www.visualcinnamon.com/2015/08/stretched-chord.html). This visualization is in the `matrix/` directory.


## Contributors

Maddy Hodges, Tosin Alliyu
