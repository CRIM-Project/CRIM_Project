# CRIM Data Conversion Project :musical_score:

Convert and organize CRIM data set for furture analysis.

## Project Home Page

* [CRIM Homepage](https://sites.google.com/a/haverford.edu/crim-project/) - Check this out!

	to pull the data from the api and write it to CSVs run:
		`$python3 counts.py`

## Visualizations
Currently we are working on two visualizations.
	One is a a modified chord diagram to visualize the relationship between musical types and relationship types. This was largerly inspired by visualcinnamon's blog [post](https://www.visualcinnamon.com/2015/08/stretched-chord.html). This visualization is in the `matrix/` directory.

	### Heat Map Visualization
	The heat map visualization can be accessed in the file temp_html.html. While there is currently no visualization on this page, we have built a script in JavaScript that aggregates all the information needed to build a heat map for a particular piece. The way the script works is that given a score title from the CRIM API [post] (http://92.154.49.37/CRIM/api/citation),

	![Example score title search]( readme_images/temp_html_input.png "In this example we are searching...")

	it generates information for that specific score from the ema.json file, which is a json that contains all the scores in the CRIM API, where each score has information about what other musical piece each of its measure stems from. The information that is returned as an output from the search is a list of all the other musical pieces that is in this score as well as what measure(s) each of these musical pieces can be found in the score.

	![Example output of search]( readme_images/temp_html_output.png "In this example output...")



## Contributors

Maddy Hodges, Tosin Alliyu
