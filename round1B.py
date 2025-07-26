from pathlib import Path
import json
from datetime import datetime
from PyPDF2 import PdfReader
import re

# Load persona and job
persona = Path("/app/input/persona.txt").read_text().strip()
job_to_be_done = Path("/app/input/job.txt").read_text().strip()

input_dir = Path("/app/input")
output_dir = Path("/app/output")
output_dir.mkdir(parents=True, exist_ok=True)

for pdf_file in input_dir.glob("*.pdf"):
    if pdf_file.suffix != ".pdf":
        continue

    reader = PdfReader(str(pdf_file))

    # One result per PDF
    results = {
        "metadata": {
            "input_documents": [pdf_file.name],
            "persona": persona,
            "job_to_be_done": job_to_be_done,
            "processing_timestamp": datetime.utcnow().isoformat() + "Z"
        },
        "extracted_sections": [],
        "subsection_analysis": []
    }

    section_counter = 0

    for i, page in enumerate(reader.pages):
        text = page.extract_text()
        if not text:
            continue

        lines = text.split('\n')

        for line in lines:
            line = line.strip()
            # Heuristic: line is likely a section if it's moderately long and title-like
            if len(line.split()) > 3 and line.istitle():
                section_counter += 1
                results["extracted_sections"].append({
                    "document": pdf_file.name,
                    "page_number": i + 1,
                    "section_title": line,
                    "importance_rank": section_counter  # Simple ranking by order found
                })
                results["subsection_analysis"].append({
                    "document": pdf_file.name,
                    "page": i + 1,
                    "section_title": line,
                    "refined_text": text[:250].strip()  # Preview snippet
                })
                if section_counter >= 5:
                    break  # Only take top 5 sections per PDF
        if section_counter >= 5:
            break

    # Write output JSON
    output_file = output_dir / f"{pdf_file.stem}.json"
    with open(output_file, "w") as f:
        json.dump(results, f, indent=2)
