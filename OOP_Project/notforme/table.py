from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter, A4
from reportlab.platypus import Table, TableStyle
import os

from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import Table, TableStyle, SimpleDocTemplate

def create_dynamic_table(pdf_path, table_data):
    # Create a PDF file
    doc = SimpleDocTemplate(pdf_path, pagesize=letter)
    
    # Function to add content to the canvas
    def add_content_to_canvas(canvas, doc):
        # Define a style for the table
        style = TableStyle([
            ('ALIGN', (0, 0), (-1, 0), 'CENTER'),
            ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (0, -1), 'LEFT'),
            ('ALIGN', (2, 0), (2, -1), 'CENTER'),
            ('ALIGN', (1, 0), (1, -1), 'RIGHT'),
            ('ALIGN', (3, 0), (3, -1), 'RIGHT'),
            ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
            ('GRID', (0, 0), (-1, -1), 1, colors.black)
        ])

        # Create a table
        table = Table(table_data)
        table.setStyle(style)

        # Draw the table on the canvas
        table.wrapOn(canvas, 0, 0)
        table.drawOn(canvas, 10, 500)  # Adjust the coordinates as needed

    # Add content to the PDF document using the canvas
    doc.build([add_content_to_canvas])

table_data_4rows = [
    ['Header1', 'Header2', 'Header3', 'Header4'],
    ['Left1', 'Center2', 'Center3', 'Right4'],
    ['Left1', 'Center2', 'Center3', 'Right4'],
    ['Left1', 'Center2', 'Center3', 'Right4']
]

table_data_10rows = [
    ['Header1', 'Header2', 'Header3', 'Header4'],
    ['Left1', 'Center2', 'Center3', 'Right4'],
    ['Left1', 'Center2', 'Center3', 'Right4'],
    ['Left1', 'Center2', 'Center3', 'Right4'],
    ['Left1', 'Center2', 'Center3', 'Right4'],
    ['Left1', 'Center2', 'Center3', 'Right4'],
    ['Left1', 'Center2', 'Center3', 'Right4'],
    ['Left1', 'Center2', 'Center3', 'Right4'],
    ['Left1', 'Center2', 'Center3', 'Right4'],
    ['Left1', 'Center2', 'Center3', 'Right4']
]

# Create PDF with 4 rows
target_path = os.getcwd() + "\\booking"
if not os.path.exists(target_path):
    print("heyyy")
    os.makedirs(target_path)
pdf_path_4rows = os.path.join(target_path, 'table_4rows.pdf')
create_dynamic_table(pdf_path_4rows, table_data_4rows)

# Create PDF with 10 rows
pdf_path_10rows = os.path.join(target_path, 'table_10rows.pdf')
create_dynamic_table(pdf_path_10rows, table_data_10rows)
