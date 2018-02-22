# CRIM Data Conversion Project :musical_score:

Convert and organize CRIM data set for furture analysis.

## Project Home Page

* [CRIM Homepage](https://sites.google.com/a/haverford.edu/crim-project/) - Check this out!

	to pull the data from the api and write it to CSVs run:

		`$ python3 counts.py`  

In the future a command line interface will be added and the functionally of the script will be expanded.

As of right now this script writes 7 csvs and one json file. Below is a brief description of each:

##### 1. ema.csv / 2. ema.json
As a csv this file has two features *SongTitle* and *Counts*. *SongTitle* is the title of the piece (e.g. Lassus Roland de : Lassus. Susanne un jour ) and *Counts* is a list of dictionary items. Each dictionary has the keys *measures* and *Song_From*. The *measures* information was pulled from the ema field of the json (which was pulled from the api). The *measures* value signifies which measures of the *SongTitle* were related to the *Song_From* in the users session. Below is an example of one row of the csv  

```
Lassus Roland de : Lassus. Susanne un jour, [ {'measures': '1-2', 'Song_From': 'Lassus, Roland de : Lassus. Susanne un jour'}, ... , {'measures': '31-35', 'Song_From': 'Lassus, Roland de : Lassus. Susanne un jour'} ]
```

The ema.json contains the exact same information but in a .json format

##### 3. relationship_types.csv  
This is just a count of the relationships of all of the sessions.   
This file looks like:
```
relationship_types,counts
rt-q,611
rt-tm,697
rt-tnm,1166
None,19
rt-om,108
rt-nm,354
```
##### 4. user_counts.csv
This is just a count of the sessions each user has created. In Omeka each user is assigned a unique id number which is listed as the *users* value.  
 This file looks like:
```
users,counts
1,3
6,19
5,8
15,583
13,2
...
```

##### 5. title_counts.csv
This is a count of for each piece , how many times it was referenced in a session.   
This file looks like:

```
titles,counts
Lassus Roland de : Lassus. Susanne un jour,57
Lassus Roland de : Lassus. Missa Susanne un jour (Kyrie),19
Forestier Mathurin: Forestier. Missa Baisés moy ma doulce amye (Kyrie),9
Lupi Didier: Lupi. Susanne un jour,11
Sermisy Claudin de: Sermisy. Tota pulchra es,147
Josquin Des Prés : Josquin. Baises moy,38
...
```
##### 6. assertion_types.csv
This is a count of the assertion types of all of the sessions.   
This file looks like:
```
assertion_types,counts
mt-sog,472
mt-pe,153
mt-cf,39
mt-fg,869
mt-id,221
...
```
##### 7. assertion_titles.csv
This is a count of the number of assertion made with each piece.   
This file looks like:
```
assertion_titles,counts
None,2
Forestier Mathurin: Forestier. Missa Baisés moy ma doulce amye (Kyrie),8
Lupi Didier: Lupi. Susanne un jour,4
Sermisy Claudin de: Sermisy. Tota pulchra es,16
Josquin Des Prés : Josquin. Baises moy,7
...
```

##### 8. assertion_scores.csv
This is a count of the number of assertion made for each unique score id.   
This file looks like:

```
assertion_scores,counts
c11,1782
c25,31
c13,4
c392,1
c406,1
c77,1
c140,1
...
```

## Visualizations
Currently we are working on two visualizations.
	One is a a modified chord diagram to visualize the relationship between musical types and relationship types. This was largely inspired by visualcinnamon's blog [post](https://www.visualcinnamon.com/2015/08/stretched-chord.html). This visualization is in the `matrix/` directory.

##### Heat Map Visualization
The heat map visualization can be accessed in the file temp_html.html. While there is currently no visualization on this page, we have built a script in JavaScript that aggregates all the information needed to build a heat map for a particular piece. The way the script works is that given a score title from the CRIM API (http://92.154.49.37/CRIM/api/citation),

###### Example score title search:
![Example score title search]( readme_images/temp_html_input.png)

```
In this example we are searching for the score titled, "Lassus, Roland de : Lassus. Susanne un jour."
```

it generates information for that specific score from the ema.json file, which is a json that contains all the scores in the CRIM API, where each score has information about what other musical piece each of its measure stems from. The information that is returned as an output from the search is a list of the names of the different musical piece influences that is in this score as well as what measure(s) each of these musical influences can be found in the score. Note that the list is made up of the names of scores that are also from the CRIM API.

###### Example output of search:
![Example output of search]( readme_images/temp_html_output.png "In this example output...")

```
This example output shows a list of the names of the different musical piece influences in the Lassus, Roland de : Lassus. Susanne un jour piece and the measure(s) where they can each be found.
```

##### Next steps
We are in the process of creating a parallel timelines layout (swimlanes) for representing state of time-series over time. This time-line would be the measures in a score. The code for this is cloned from [vasturiano's repo](https://github.com/vasturiano/timelines-chart).

Richard has suggested that " we could have the 'groups' assigned to each Work_ID, then the 'labels' could be the individual Analyst_IDs (that is, the folks who made observations about each piece).  Colors could map to musical types or relationship types (two different views, I suppose).  Tooltip could reveal basic information about the item, plus a URL link to the music.  The timeline at the bottom could be from the start to the end of each piece".

###### Droplet
We are in the process of starting a website to better collect all of our work on this Droplet: http://159.65.177.99/

###### To do list
- [ ] Have view with users, scores and music|relationships types as the color
- [ ] Have relationship types ( y-axis ), scores, music types as color
- [ ] fix measures axis line up
- [ ] view heatmap for one score at a time
- [ ] look into actual heatmap opacity functionality
- [ ] look into being able to toggle between different types of axis
- [ ] make scripts to generate the jsons that the above visualizations will require



## Contributors :tada:

:octocat: [Maddy Hodges](https://github.com/Mfhodges) & [Tosin Alliyu](https://github.com/TA2018)  
With support by [Haverford College Digital Scholarship](https://github.com/hcdigitalscholarship)
