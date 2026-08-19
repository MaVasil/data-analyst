import PyPDF2
import os
from pathlib import Path


def merge_pdfs(pdf_files, output_filename):
    """
    Merge multiple PDF files into one.
    
    Args:
        pdf_files (list): List of PDF file paths to merge
        output_filename (str): Name of the output merged PDF file
    """
    try:
        # Create PDF merger object
        pdf_merger = PyPDF2.PdfMerger()
        
        # Add each PDF file to the merger
        for pdf_file in pdf_files:
            if not os.path.exists(pdf_file):
                print(f"✗ File not found: {pdf_file}")
                return False
            
            if not pdf_file.lower().endswith('.pdf'):
                print(f"✗ Not a PDF file: {pdf_file}")
                return False
            
            try:
                pdf_merger.append(pdf_file)
                print(f"✓ Added: {pdf_file}")
            except Exception as e:
                print(f"✗ Error adding {pdf_file}: {str(e)}")
                pdf_merger.close()
                return False
        
        # Write merged PDF to output file
        with open(output_filename, 'wb') as output_file:
            pdf_merger.write(output_file)
        
        pdf_merger.close()
        print(f"\n✓ PDFs merged successfully!")
        print(f"✓ Output file: {output_filename}")
        return True
    
    except Exception as e:
        print(f"✗ Error during merge: {str(e)}")
        return False


def get_pdf_files_from_folder(folder_path):
    """
    Get all PDF files from a folder.
    
    Args:
        folder_path (str): Path to the folder
    
    Returns:
        list: List of PDF file paths
    """
    pdf_files = []
    
    if not os.path.exists(folder_path):
        print(f"✗ Folder not found: {folder_path}")
        return pdf_files
    
    for file in sorted(os.listdir(folder_path)):
        if file.lower().endswith('.pdf'):
            full_path = os.path.join(folder_path, file)
            pdf_files.append(full_path)
    
    return pdf_files


def display_menu():
    """Display main menu options."""
    print("\n" + "="*60)
    print(" "*15 + "PDF MERGER APPLICATION")
    print("="*60)
    print("\n1. Merge PDFs from a folder")
    print("2. Merge specific PDF files")
    print("3. Exit")
    print("-"*60)


def option_merge_folder():
    """Merge all PDF files from a folder."""
    print("\n--- Merge PDFs from Folder ---")
    folder_path = input("Enter folder path: ").strip()
    
    pdf_files = get_pdf_files_from_folder(folder_path)
    
    if not pdf_files:
        print("✗ No PDF files found in this folder.")
        return
    
    print(f"\nFound {len(pdf_files)} PDF file(s):")
    for i, pdf in enumerate(pdf_files, 1):
        print(f"  {i}. {os.path.basename(pdf)}")
    
    output_name = input("\nEnter output filename (e.g., merged.pdf): ").strip()
    
    if not output_name.lower().endswith('.pdf'):
        output_name += '.pdf'
    
    print(f"\nMerging {len(pdf_files)} PDFs...")
    merge_pdfs(pdf_files, output_name)


def option_merge_specific():
    """Merge specific PDF files selected by user."""
    print("\n--- Merge Specific PDF Files ---")
    pdf_files = []
    
    print("Enter PDF file paths one by one (press Enter with empty path when done):\n")
    
    count = 1
    while True:
        file_path = input(f"PDF file {count}: ").strip()
        
        if file_path == "":
            break
        
        if os.path.exists(file_path) and file_path.lower().endswith('.pdf'):
            pdf_files.append(file_path)
            print(f"✓ Added: {os.path.basename(file_path)}")
            count += 1
        else:
            print(f"✗ Invalid file or not a PDF: {file_path}")
    
    if not pdf_files:
        print("✗ No valid PDF files added.")
        return
    
    print(f"\nTotal PDFs to merge: {len(pdf_files)}")
    output_name = input("Enter output filename (e.g., merged.pdf): ").strip()
    
    if not output_name.lower().endswith('.pdf'):
        output_name += '.pdf'
    
    print(f"\nMerging {len(pdf_files)} PDFs...")
    merge_pdfs(pdf_files, output_name)


def main():
    """Main application loop."""
    while True:
        display_menu()
        choice = input("Select an option (1/2/3): ").strip()
        
        if choice == "1":
            option_merge_folder()
        elif choice == "2":
            option_merge_specific()
        elif choice == "3":
            print("\nThank you for using PDF Merger! Goodbye!\n")
            break
        else:
            print("✗ Invalid option. Please select 1, 2, or 3.")


if __name__ == "__main__":
    print("\nInitializing PDF Merger...")
    
    # Check if PyPDF2 is installed
    try:
        import PyPDF2
    except ImportError:
        print("\n✗ PyPDF2 is not installed.")
        print("Install it using: pip install PyPDF2")
        exit()
    
    main()
