import GlassDoorScraper as gs
import pandas as pd

path = "chromedriver"
df= gs.get_jobs("Data Scientist", 1500, False, path, 15)
df.to_csv('DS_Jobs.csv', index=False)