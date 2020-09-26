import GlassDoorScraper as gs
import pandas as pd

path = "chromedriver"
df= gs.get_jobs("Data Scientist", 15, False, path, 15)
df