# RuneScrape
### A market forcaster for Oldschool Runescape using deep learning with help of Tensorflow and Keras.

This model and dataset were able to achieve a ~18% accuracy when trying to predict future prices of items. Due to the low chance, we highly advise you don't attempt to make your fortunes using this program.

### Team

* Steven Proctor
* Margaret Fletcher
* Matthew Manoly
* Harrison Ratcliffe
* Zachary Taylor

### Data

Data was gathered by a python webscraper using BeautifulSoup, and saved locally to a file labeled as the current day. By gathering the 60 day price data, the 30 day price data and the daily price data we were able to make a full range of 90 days worth of prices to check. Due to Jagex locking out IPs after so many queries in rapid succession to their api, we end up having to wait a long time to pull every single item.

### The Net

Using jupyter notebook (so we can run specific snippets, not have to retrain every time we run, etc) we constructed a network, trained it using some of our data and tested on a seperate set. We would look at 4 days worth of prices, get the trends, exactly how much the item's price changed, and try to predict the 5th day. Then we would see if we were right, the move on and do the next 4 days.

Luckily, we had access to a machine at Intel that handled a lot of the heavier lifting for us with the neural network and made operating it much faster than if we had tried on our own machines.
