import os
from PyPDF2 import PdfMerger

# Folder containing the PDF files
pdf_folder = "allPDF"  # Assuming this folder is in the same directory as the script

# Output PDF file name
output_pdf = "merged_output.pdf"

# Get a list of all PDF files in the folder
pdf_files = [os.path.join(pdf_folder, file) for file in os.listdir(pdf_folder) if file.endswith(".pdf")]

# Sort files alphabetically (optional, if you want to merge in order)
pdf_files.sort()

# Create a PdfMerger object
merger = PdfMerger()

# Loop through each file and append it to the merger
for pdf in pdf_files:
    merger.append(pdf)

# Write the merged PDF to the output file
merger.write(output_pdf)
merger.close()

print(f"Merged PDF saved as {output_pdf}")
