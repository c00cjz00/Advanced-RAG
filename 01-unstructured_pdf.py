#CMD: ml libs/singularity/3.10.2 ; singularity pull docker://c00cjz00/c00cjz00_cuda11.8_pytorch:2.1.2-cuda11.8-cudnn8-devel-unstructured
#CMD: ml libs/singularity/3.10.2 ; singularity exec --nv /work/u00cjz00/nvidia/cuda118/c00cjz00_cuda11.8_pytorch_2.1.2-cuda11.8-cudnn8-devel-unstructured.sif python3 unstructured_pdf.py 1Q23-EPR-with-Tables-FINAL.pdf 1Q23-EPR-with-Tables-FINAL.json
from typing import Any
from pydantic import BaseModel
from unstructured.partition.pdf import partition_pdf
import sys

#0. check argv
if len(sys.argv) < 2:
    print('no argument')
    sys.exit()

pdf_file=sys.argv[1]
json_file=sys.argv[1]    

#1. pdf reader
raw_pdf_elements = partition_pdf(
    filename=pdf_file,
    extract_images_in_pdf=False,
    infer_table_structure=True,
    chunking_strategy="by_title",
    max_characters=4000,
    new_after_n_chars=3800,
    combine_text_under_n_chars=2000,
    image_output_dir_path=".",
)

#2. category_counts
category_counts = {}

for element in raw_pdf_elements:
    category = str(type(element))
    if category in category_counts:
        category_counts[category] += 1
    else:
        category_counts[category] = 1

unique_categories = set(category_counts.keys())
category_counts

#3. check table or text
class Element(BaseModel):
    type: str
    text: Any

table_elements = []
text_elements = []
for element in raw_pdf_elements:
    if "unstructured.documents.elements.Table" in str(type(element)):
        table_elements.append(Element(type="table", text=str(element)))
    elif "unstructured.documents.elements.CompositeElement" in str(type(element)):
        text_elements.append(Element(type="text", text=str(element)))

#4. print result
print(len(table_elements))
print(len(text_elements))


#5. json
import json
json_list=[]
for i, text in enumerate(text_elements):
    dictionary ={ 
      "item": i,
      "document": "text",
      "text": text.text
    } 
    json_list.append(dictionary)

for i, table in enumerate(table_elements):
    dictionary ={ 
      "item": i,
      "document": "table",
      "text": table.text
    } 
    json_list.append(dictionary)

#json_object = json.dumps(json_list, indent = 4) 
#print(json_object)

with open(json_file, 'w') as fp:
    json.dump(json_list, fp)
