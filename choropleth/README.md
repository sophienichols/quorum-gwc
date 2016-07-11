# Choropleth Project
In this project you are going to generate a map with each state colored by the number of times a given word or phrase has been mentioned in Congress.

##Overall Process
1. Use our state API and person API to figure out which Members represent which states.
2. Use our document API to find the number of documents from Members representing a given state that mention a particular word or phrase.
3. Combine your results into a CSV.
4. Visualize that CSV through a choropleth visualization you'll run on your local server on your computer.
5. Choose your own words and phrases and see if you can find something that commonly mentioned by Members from your state but not from other states.

## How to Run Your Localserver
1. `cd` into the approprate directory (choropleth/, for example)
2. Run `python -m SimpleHTTPServer`
3. Go to `localhost:8000` in your local browser
4. Rejoice!