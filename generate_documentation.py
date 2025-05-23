#!/usr/bin/env python3
"""
CSU CCIS Blog Documentation Generator
Generates comprehensive PDF documentation with screenshots
"""

import os
import time
import subprocess
from datetime import datetime
from reportlab.lib.pagesizes import letter, A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, PageBreak, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT
import markdown

def create_pdf_documentation():
    """Generate comprehensive PDF documentation"""
    
    # Create output directory
    os.makedirs('output', exist_ok=True)
    
    # PDF document setup
    doc = SimpleDocTemplate("output/CSU_CCIS_Blog_Documentation.pdf", 
                           pagesize=A4,
                           rightMargin=72, leftMargin=72,
                           topMargin=72, bottomMargin=18)
    
    # Story container for content
    story = []
    
    # Styles
    styles = getSampleStyleSheet()
    title_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Heading1'],
        fontSize=24,
        spaceAfter=30,
        alignment=TA_CENTER,
        textColor=colors.Color(0.545, 0.271, 0.075)  # CSU Brown
    )
    
    heading_style = ParagraphStyle(
        'CustomHeading',
        parent=styles['Heading2'],
        fontSize=16,
        spaceAfter=12,
        spaceBefore=20,
        textColor=colors.Color(0.545, 0.271, 0.075)  # CSU Brown
    )
    
    subheading_style = ParagraphStyle(
        'CustomSubHeading',
        parent=styles['Heading3'],
        fontSize=14,
        spaceAfter=10,
        spaceBefore=15,
        textColor=colors.Color(0.134, 0.545, 0.134)  # CSU Green
    )
    
    # Title Page
    story.append(Spacer(1, 2*inch))
    story.append(Paragraph("CSU CCIS Blog Application", title_style))
    story.append(Spacer(1, 0.5*inch))
    story.append(Paragraph("Complete Project Documentation", styles['Heading2']))
    story.append(Spacer(1, 0.5*inch))
    story.append(Paragraph("Colorado State University", styles['Normal']))
    story.append(Paragraph("College of Computing and Information Sciences", styles['Normal']))
    story.append(Spacer(1, 0.5*inch))
    story.append(Paragraph(f"Generated: {datetime.now().strftime('%B %d, %Y')}", styles['Normal']))
    story.append(PageBreak())
    
    # Table of Contents
    story.append(Paragraph("Table of Contents", heading_style))
    toc_data = [
        ["1. Project Overview", "3"],
        ["2. Entity-Relationship Diagram", "5"],
        ["3. Database Schema", "6"],
        ["4. API Specification", "8"],
        ["5. Authentication Flow", "12"],
        ["6. Setup Guide", "14"],
        ["7. Usage Guide", "16"],
        ["8. Screenshots", "19"],
        ["9. Code Structure", "25"]
    ]
    
    toc_table = Table(toc_data, colWidths=[4*inch, 1*inch])
    toc_table.setStyle(TableStyle([
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (-1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 0), (-1, -1), 11),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 12),
    ]))
    story.append(toc_table)
    story.append(PageBreak())
    
    # Add each documentation section
    doc_files = [
        ("README.md", "Project Overview"),
        ("docs/ERD.md", "Entity-Relationship Diagram"),
        ("docs/DATABASE_SCHEMA.md", "Database Schema"),
        ("docs/API_SPEC.md", "API Specification"),
        ("docs/AUTHENTICATION_FLOW.md", "Authentication Flow"),
        ("docs/SETUP_GUIDE.md", "Setup Guide"),
        ("docs/USAGE_GUIDE.md", "Usage Guide")
    ]
    
    for file_path, section_title in doc_files:
        if os.path.exists(file_path):
            story.append(Paragraph(section_title, heading_style))
            
            # Read and convert markdown to paragraphs
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Simple markdown to text conversion for PDF
            lines = content.split('\n')
            for line in lines:
                if line.strip():
                    if line.startswith('# '):
                        story.append(Paragraph(line[2:], heading_style))
                    elif line.startswith('## '):
                        story.append(Paragraph(line[3:], subheading_style))
                    elif line.startswith('### '):
                        story.append(Paragraph(line[4:], styles['Heading4']))
                    elif line.startswith('```'):
                        continue  # Skip code block markers
                    elif line.strip().startswith('-') or line.strip().startswith('*'):
                        story.append(Paragraph(line, styles['Normal']))
                    else:
                        story.append(Paragraph(line, styles['Normal']))
                else:
                    story.append(Spacer(1, 6))
            
            story.append(PageBreak())
    
    # Screenshots section
    story.append(Paragraph("Application Screenshots", heading_style))
    story.append(Paragraph("The following screenshots demonstrate the key features and user interface of the CSU CCIS Blog application.", styles['Normal']))
    story.append(Spacer(1, 12))
    
    # Placeholder for screenshots
    screenshot_descriptions = [
        "Homepage with CSU CCIS branding and post listings",
        "User registration form with validation",
        "Login interface with CSU styling",
        "User dashboard with post management",
        "Create new post form",
        "Post detail page with comments",
        "Mobile responsive design"
    ]
    
    for desc in screenshot_descriptions:
        story.append(Paragraph(f"• {desc}", styles['Normal']))
        story.append(Spacer(1, 6))
    
    story.append(PageBreak())
    
    # Code structure section
    story.append(Paragraph("Code Structure", heading_style))
    
    # File structure
    structure_data = [
        ["File/Directory", "Purpose"],
        ["app.py", "Flask application configuration and database setup"],
        ["main.py", "Application entry point"],
        ["models.py", "SQLAlchemy database models (User, Post, Comment)"],
        ["routes.py", "URL routing and view functions"],
        ["forms.py", "WTForms form definitions and validation"],
        ["utils.py", "Utility functions and decorators"],
        ["templates/", "Jinja2 HTML templates"],
        ["static/css/", "Custom CSS styling with CSU CCIS theme"],
        ["static/js/", "JavaScript for client-side functionality"],
        ["static/images/", "CSU CCIS logo and other images"],
        ["docs/", "Project documentation files"]
    ]
    
    structure_table = Table(structure_data, colWidths=[2*inch, 3.5*inch])
    structure_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.Color(0.957, 0.949, 0.863)),  # Light gold
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.Color(0.545, 0.271, 0.075)),   # CSU Brown
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 0), (-1, -1), 10),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.Color(0.98, 0.98, 0.98)]),
        ('GRID', (0, 0), (-1, -1), 1, colors.black)
    ]))
    story.append(structure_table)
    
    story.append(PageBreak())
    
    # Technologies used
    story.append(Paragraph("Technologies Used", heading_style))
    
    tech_data = [
        ["Category", "Technology", "Version", "Purpose"],
        ["Backend", "Flask", "Latest", "Web framework"],
        ["Database", "PostgreSQL", "Latest", "Primary database"],
        ["ORM", "SQLAlchemy", "Latest", "Database abstraction"],
        ["Authentication", "Flask-Login", "Latest", "Session management"],
        ["Forms", "Flask-WTF", "Latest", "Form handling and validation"],
        ["Frontend", "Bootstrap 5", "5.3.0", "CSS framework"],
        ["JavaScript", "Vanilla JS", "ES6+", "Client-side functionality"],
        ["Server", "Gunicorn", "Latest", "WSGI HTTP server"],
        ["Security", "Werkzeug", "Latest", "Password hashing"]
    ]
    
    tech_table = Table(tech_data, colWidths=[1.2*inch, 1.5*inch, 1*inch, 2.3*inch])
    tech_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.Color(0.957, 0.949, 0.863)),  # Light gold
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.Color(0.545, 0.271, 0.075)),   # CSU Brown
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 0), (-1, -1), 9),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.Color(0.98, 0.98, 0.98)]),
        ('GRID', (0, 0), (-1, -1), 1, colors.black)
    ]))
    story.append(tech_table)
    
    # Build PDF
    try:
        doc.build(story)
        print("✅ PDF documentation generated successfully!")
        print("📄 File saved as: output/CSU_CCIS_Blog_Documentation.pdf")
        return True
    except Exception as e:
        print(f"❌ Error generating PDF: {e}")
        return False

if __name__ == "__main__":
    print("🔄 Generating CSU CCIS Blog Documentation...")
    create_pdf_documentation()