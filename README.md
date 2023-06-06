# Exoplanet Search
## Concept
Concept is to create script that will help astronomers to 
extract data and find exoplanets from frames and pictures
of stars in time.

## Idea
The idea is to write a script that will take data from NASA and ESA
database, [Juliet](https://juliet.readthedocs.io/en/latest/index.html) 
and [Lightcurve](https://docs.lightkurve.org/index.html) api.
The data will be taken from Tess, Kepler and Huble telescope.

Then write some general algorithm that process picture or 
data sets of stars. Then search for exoplanets in data and return 
if there is or there is not an exoplanet.  

## Expected result
The expected result is to have a functional code with few 
examples of exoplanets found. To write a report in Jupyter
or Deepnote. Create presentation in Notion or Deepnote

## Nice to have
To write some simple app with simple UI using wigets from (IpyAladin)[https://github.com/cds-astro/ipyaladin/blob/master/ipyaladin-screenshot.png] . To create UML sheet
that will describe how the code works. And to make it with 
the smallest computing capacity as possible. Run some unit tests. 
If possible contribute or implement in to some open source framework.
Creat Comunication publish with Curvenote.

Sources:
-----------------------------
 - [Juliet](https://juliet.readthedocs.io/en/latest/)
 - [Tess archive](https://archive.stsci.edu/hlsps/tess-data-alerts/)
 - [Test data](https://mast.stsci.edu/portal/Mashup/Clients/Mast/Portal.html)
 - [Lightcurve](https://docs.lightkurve.org/) 
 - [Aladin Lite](https://aladin.u-strasbg.fr/AladinLite/)
 - [Astroquery](https://astroquery.readthedocs.io/en/latest/)
 - [Astropy](https://astroquery.readthedocs.io/en/latest/)

logic to add:
-----------------------------
- create class for trying to find exoplanet automaticly
- create method/function that will try to find it on the spectrum by prolonging the days period
- write automation for getting data from [MAST](https://mast.stsci.edu/portal/Mashup/Clients/Mast/Portal.html)
- write a checker for already found stars from [exoMast](https://exo.mast.stsci.edu/)

## Pseudo
    Create list or dicitonary that will store names and 
    additional parrameters from Tess, Huble and Kepler (...others)
    Create mutliple examples of analyses of exoplanet search 
    from each telescope from bouth Lightcurve and Julia in jupyter
    Create classes and scripts what will automate analyses
    Run the analyses and save, plot and compare results
    Create the simple web app that will be static and 
    sdynamic ideally using jupyter and its extensions
    crate report and documentation of the proces