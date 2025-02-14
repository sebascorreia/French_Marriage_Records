import json
import re


def label_processing(file_name):
    with open(filename, "r", encoding='utf-8') as f:
        data = json.load(f)
    labels_ner = data["ground_truth"]["train"]
    images = {}
    for img_filename, image_data in labels_ner.items():
        if image_data["nb_cols"] != 2:
            print("ORA FODA-SE")
        text = image_data["text"]
        allowed_chars = r"[^A-Za-zÀ-ÖØ-öø-ÿ0-9.,:;!?()\"'&*\-\s\n]"
        clean_text = re.sub(allowed_chars, " ", text)
        clean_text = re.sub(r"[ ]{2,}", " ", clean_text).strip()
        images[img_filename] = clean_text
    print("NER text: \n" + labels_ner["AD075EC_03M240_0052-left.png"]["text"])
    print("\n ---- // ---- \n")
    print("Clean text: \n" + images["AD075EC_03M240_0052-left.png"])
    return images



if __name__ == "__main__":
    filename = "D:\Sebas\Personal_Projects\French_Marriage_Records\m-popp_datasets\handwritten\labels\labels-handwritten-encoding-1.json"
    labels = label_processing(filename)
