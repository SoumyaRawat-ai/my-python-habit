import PyPDF2

def move_page(input_pdf_path, output_pdf_path, source_page_num, dest_page_num):
    # Open the input PDF file
    with open(input_pdf_path, 'rb') as input_file:
        reader = PyPDF2.PdfReader(input_file)
        writer = PyPDF2.PdfWriter()

        # Adjust for zero-based indexing
        source_page_num -= 1
        dest_page_num -= 1

        # Get the page to move
        page_to_move = reader.pages[source_page_num]
        
        # Add pages to the writer in the new order
        for i in range(len(reader.pages)):
            if i == dest_page_num:
                writer.add_page(page_to_move)
            if i != source_page_num:
                writer.add_page(reader.pages[i])
        
        # If destination is the last page
        if dest_page_num >= len(reader.pages):
            writer.add_page(page_to_move)

        # Write the output PDF file
        with open(output_pdf_path, 'wb') as output_file:
            writer.write(output_file)

input_pdf = r"C:\Users\soumy\Downloads\Sports For Life Project.pdf"
output_pdf = r"C:\Users\soumy\Downloads\Sports For Life Project_Rearranged.pdf"
move_page(input_pdf, output_pdf, 23, 1)  # Example: move 23rd page to 1st position
