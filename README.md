# Mapreduce-search-engine

## Introduction:
The objective of this project is to develop a basic search engine using the MapReduce paradigm, specifically Apache Hadoop's MapReduce framework. The project involves two primary tasks: document indexing and query processing. Document indexing involves processing a large corpus of text documents to create an index that allows for efficient retrieval of relevant documents. Query processing involves analyzing user queries and identifying the most relevant documents from the index.

## Dataset Description:
The dataset used for this project is a portion of the English Wikipedia dump provided by Wikimedia, comprising around 5 million Wikipedia articles. Each article is represented by an ARTICLE_ID, TITLE, SECTION_TITLE, and SECTION_TEXT. The focus of this project is primarily on the ARTICLE_ID and SECTION_TEXT columns, where basic text cleaning is performed to ensure accurate results.

# Development Approach:
The development of the search engine involves several steps, including understanding the MapReduce framework, implementing document indexing, query processing, and organizing the project. Each task is broken down into smaller components, with separate Mapper and Reducer files written for clarity and modularity.

# Tasks and Components:

**Document Indexing:**
**Mapper:** Processes each document to generate term frequency (TF) vectors.
**Reducer:** Aggregates TF vectors and calculates inverse document frequency (IDF) to generate TF-IDF vectors.

# Query Processing:

**Query Vectorizer:**

**Mapper:** Processes the user query to generate a vector representation.
**Reducer:** Aggregates query vector components to create the query vector.

# Relevance Analyzer:

**Mapper:** Computes the relevance score between documents and the query.
**Reducer:** Aggregates relevance scores and selects the top relevant documents.

# Index Store:

**Mapper:** Prepares the index data for storage.
**Reducer:** Aggregates index data and stores it in a suitable format.

# Technological Considerations:

The project utilizes Apache Hadoop's MapReduce framework due to its ability to handle large-scale data processing efficiently.
Text processing techniques such as TF-IDF vectorization are employed for document indexing and query processing.
The choice of Python programming language for implementing Mapper and Reducer functions facilitates ease of development and integration with Hadoop.

# Conclusion:
Developing a naïve search engine utilizing MapReduce offers valuable insights into large-scale data processing and information retrieval techniques. By following the MapReduce paradigm and leveraging technologies like Hadoop, teams can efficiently handle vast amounts of textual data and deliver relevant search results in real-time. This project serves as a foundational step towards building more advanced search engines and information retrieval systems.
