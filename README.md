# Adobe Hackathon – Round 1B: Persona-Driven Document Intelligence

##  Challenge Theme
**"Connecting the Dots Through Docs"**

Build a system that analyzes a set of PDF documents and extracts the most relevant sections based on:
- A defined **persona**
- A specific **job to be done**

The system mimics how a human would search through multiple documents to find focused content for a task (e.g., a data scientist writing a survey).

---

### 🛠️ Libraries Used

- **PyPDF2**  
  For reading and extracting text from PDF documents.

- **re**  
  Used for detecting heading patterns with regular expressions.

- **json**  
  Used to output structured data in a readable format.

- **datetime**  
  To timestamp the analysis for traceability.

- **pathlib**  
  For clean and portable file system operations.


##  Approach

1. **Metadata Initialization**  
   - Reads the `persona` and `job_to_be_done` from text input files.  
   - Collects the names of all input PDFs.  
   - Generates a processing timestamp.

2. **Text Extraction**  
   - Reads each page of every input PDF using `PyPDF2`.  
   - Extracts text line-by-line and identifies headings or key content using formatting heuristics and regex.

3. **Relevant Section Ranking**  
   - Ranks top 5 most relevant sections per PDF based on keyword/persona matching and structural weight.

4. **Sub-Section Analysis**  
   - For each top-ranked section, extracts a summary/preview (typically the first few lines of the section’s page).

5. **Output**:  
   The system returns a structured `.json` file per document with the format:

```json
{
  "metadata": {
    "input_documents": ["doc1.pdf", "doc2.pdf"],
    "persona": "PhD Researcher",
    "job_to_be_done": "Survey recent research trends",
    "processing_timestamp": "2025-07-22T14:25:00Z"
  },
  "extracted_sections": [
    {
      "document": "doc1.pdf",
      "page_number": 5,
      "section_title": "Advancements in Large Language Models",
      "importance_rank": 1
    }
  ],
  "subsection_analysis": [
    {
      "document": "doc1.pdf",
      "page": 5,
      "section_title": "Advancements in Large Language Models",
      "refined_text": "Recent transformer-based models have significantly improved NLP..."
    }
  ]
}
