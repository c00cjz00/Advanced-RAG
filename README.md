# Advanced RAG

**What is RAG?**

Retrieval augmented generation (RAG) is a natural language processing (NLP) technique that employes the capabilities of retrieval and generative based AI models.

**What is Naive RAG?**

Naive RAG often refers to splitting documents into chunks, embedding them, and retrieving chunks based on semantic similarity search to a user question.

It's simple, but of poor overall performance.

**That's why we need Advanced RAG.**

In this tutorials (Advanced RAG), we will learn the techniques and best practices in RAG application development, that can improve the quality of the RAG.

It's crucial to the success of a RAG application.

## Episodes

1. [RAG on Semi-structured data](./01_semi_structured_data.ipynb)
2. [Multi-Modal RAG](./02_multi_modal.ipynb)
3. [Multi-Document RAG with LlamaIndex](./03_llama_index_multi_doc_agent.ipynb)


## c00cjz00
- singularity
```
ml libs/singularity/3.10.2 ; singularity exec --nv /work/u00cjz00/nvidia/cuda118/c00cjz00_cuda11.8_pytorch_2.1.2-cuda11.8-cudnn8-devel-unstructured.sif python3 unstructured_pdf.py 1Q23-EPR-with-Tables-FINAL.pdf 1Q23-EPR-with-Tables-FINAL.json
```
