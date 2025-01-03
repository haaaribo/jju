# -*- coding: utf-8 -*-
"""00_Document_Loader.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Fxm7s_ElCeEm91CmmBSOm79U4mTQtuai

# documnet od defination
"""

from langchain_core.documents import Document

document = Document(page_content = '안녕하세요? 이건 랭체인의 도큐먼드입니다.')

document

document.__dict__

document.metadata["source"] = "Jun_repo"
document.metadata["page"] = 1
document.metadata["author"] = "Jun"

document.metadata

document.page_content

print(document.id)

"""# 2. Documnet Load Test"""

FILE_PATH = '/content/유상민_육계중량추정을 위한 모델 비교.pdf'

FILE_PATH

pip install pypdf

pip install langchain-community

from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader(FILE_PATH)

docs = loader.load()

len(docs)

pip install langchain

from langchain.text_splitter import RecursiveCharacterTextSplitter

text_splitter = RecursiveCharacterTextSplitter(chunk_size=200, chunk_overlap=0)

FILE_PATH = '/content/유상민_육계중량추정을 위한 모델 비교.pdf'

loader = PyPDFLoader(FILE_PATH)

split_docs = loader.load_and_split(text_splitter = text_splitter)

print(f"문서의 길이: {len(split_docs)}")

split_docs[10]

"""# 실습에 활용한 문서

https://spri.kr/posts/view/23669


- page_content: 문서의 내용을 나타내는 문자열
- metadata: 문서의 메타데이터를 나타내는 딕셔너리
"""

from langchain_core.documents import Document

document = Document(page_content = '안녕하세요? 이건 랭체인의 도큐먼트입니다.')

document.__dict__

# 메타데이터 추가

document.metadata["source"] = "MinNote"
document.metadata["page"] = 1
document.metadata["author"] = "유상민"

"""## document loader

- pyPdfLoader: PDF파일을 로드하는 로더.
- CSVLoader: CSV파일 로드하는 로더.
- UnstructuredHTMLLoader: HTML "
- JSONLoader: JSON파일 "
- TextLoader: 텍스트파일 "
- DirectoryLoader: 디텍토리파일 "
- UpstagerLoader
- LLaMAIndexLoader

# 1. PyPDFLoader
"""

FILE_PATH = '/content/data/SPRI_AI_Brief_2023년12월호_F.pdf'

!pip install langchain-community

pip install PyPDF

from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader(FILE_PATH)

# PDF로더
docs = loader.load()

# 로드된 문서의 수 확인
len(docs)

print(docs[5])

"""# 2. TextSplit"""

from langchain_text_splitters import RecursiveCharacterTextSplitter

text_splitter = RecursiveCharacterTextSplitter(chunk_size = 200, chunk_overlap = 0)

loader = PyPDFLoader(FILE_PATH)

split_docs = loader.load_and_split(text_splitter=text_splitter)

print(f"문서의 길이: {len(split_docs)}")

split_docs[5]

"""# 3. lazy_load"""

loader.lazy_load()

for doc in loader.lazy_load():
  print(doc)
  print("===" * 20)

"""# 5. aload()"""

adocs = loader.aload()

# a가 앞에 붙는다? => 비동기..?

# 문서 로드
await adocs