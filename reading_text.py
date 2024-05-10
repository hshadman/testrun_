import spacy
import pandas as pd

text_data = pd.read_csv('clinical_trials_dataset.csv',sep='\t')
print(text_data)