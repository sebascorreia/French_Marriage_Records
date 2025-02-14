import pytesseract
import spacy
import os
import pandas as pd

nlp = spacy.load('fr_core_news_sm')

train_folder = r"D:\Sebas\Personal_Projects\French_Marriage_Records\m-popp_datasets\handwritten\images\trial"
test_folder= r"D:\Sebas\Personal_Projects\French_Marriage_Records\m-popp_datasets\handwritten\images\test"
validation_folder = r"D:\Sebas\Personal_Projects\French_Marriage_Records\m-popp_datasets\handwritten\images\valid"
data = []

for file in os.listdir(train_folder):
    if file.endswith(".png"):
        img_path = os.path.join(train_folder, file)
        text = pytesseract.image_to_string(img_path, lang='fra')

        doc = nlp(text)
        entities = {ent.label_: [] for ent in doc.ents}

        for ent in doc.ents:
            entities[ent.label_].append(ent.text)
        data.append({
            "Image Name": file,
            "Extracted Text": text,
            "Persons": ", ".join(entities.get("PER", [])),
            "Locations": ", ".join(entities.get("LOC", [])),
            "Dates": ", ".join(entities.get("DATE", [])),
            "Organizations": ", ".join(entities.get("ORG", [])),
        })
        df = pd.DataFrame(data)
        df.to_csv(f"{file}.csv", index=False)
        print("processing complete")