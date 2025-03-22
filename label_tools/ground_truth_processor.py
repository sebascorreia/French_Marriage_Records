import json
import re

def label_processing(filename):
    with open(filename, "r", encoding='utf-8') as f:
        data = json.load(f)
    labels_ner = data["ground_truth"]["train"]
    images = {}
    for img_filename, image_data in labels_ner.items():
        images[img_filename] = {}
        text = image_data["text"]
        records = record_separator(text)
        for i, record in enumerate(records):
            images[img_filename][f"record_{i+1}"]= text_cleaner(record)

    print("NER text: \n" + labels_ner["AD075EC_V4E_04831_0022-left.png"]["text"])
    print("\n ---- // ---- \n")
    print("Clean text: \n")
    print(images["AD075EC_V4E_04831_0022-left.png"])
    return images

def record_separator(record):
    if "ⒷⓂⓜⓝ" in record:
        return record.split("ⒷⓂⓜⓝ")
    return [record]
def text_cleaner(text):
    allowed_chars = r"[^A-Za-zÀ-ÖØ-öø-ÿ0-9.,:;!?()\"'&*\-\s\n]"
    clean_text = re.sub(allowed_chars, " ", text)
    clean_text = re.sub(r"[ ]{2,}", " ", clean_text).strip()
    return clean_text
def save_json(data, filename):
    with open(filename, "w", encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
        f.close()
        print("Data saved successfully")

if __name__ == "__main__":
    filename= "/m-popp_datasets/handwritten/labels/labels-handwritten-encoding-1.json"
    labels = label_processing(filename)
    save_json(labels, "/m-popp_datasets/handwritten/labels/processed_labels.json")
