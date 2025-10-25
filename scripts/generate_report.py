"""Module for generating a PDF analytics report from blood report data and visualizations.

This module uses ReportLab to create a professional PDF document that includes
an executive summary, key visualizations (infection trends, anemia distribution,
and CRP trends), and a summary of predictive analytics.
"""

from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch
import os

def generate_pdf_report(output_filename: str = "../reports/Blood_Report_Analytics_Report.pdf",
                        executive_summary_path: str = "../docs/executive_summary.md",
                        image_paths: list = None) -> None:
    """Generates a comprehensive PDF analytics report.

    Args:
        output_filename (str): The full path and filename for the output PDF report.
        executive_summary_path (str): The path to the markdown file containing the executive summary.
        image_paths (list): A list of paths to image files to be included in the report.
    """
    if image_paths is None:
        image_paths = [
            "../reports/infection_trends.png",
            "../reports/anemia_distribution.png",
            "../reports/crp_trends.png"
        ]

    doc = SimpleDocTemplate(output_filename, pagesize=letter)
    styles = getSampleStyleSheet()
    story = []

    # Add Title to the report
    story.append(Paragraph("Executive Summary: Blood Report Analytics", styles['h1']))
    story.append(Spacer(1, 0.2 * inch))

    # Read and add executive summary content from markdown file
    try:
        with open(executive_summary_path, "r", encoding='utf-8') as f:
            summary_content = f.read()
    except FileNotFoundError:
        story.append(Paragraph(f"Error: Executive summary file not found at {executive_summary_path}", styles['Normal']))
        summary_content = "Executive summary content could not be loaded."

    # Basic formatting for markdown content
    for line in summary_content.split('\n'):
        if line.startswith('# '):
            story.append(Paragraph(line[2:], styles['h2']))
        elif line.startswith('## '):
            story.append(Paragraph(line[3:], styles['h3']))
        else:
            story.append(Paragraph(line, styles['Normal']))
        story.append(Spacer(1, 0.1 * inch))

    # Add a section for Key Visualizations
    story.append(Paragraph("Key Visualizations", styles['h2']))
    story.append(Spacer(1, 0.2 * inch))

    # Add images to the report
    for img_path in image_paths:
        if os.path.exists(img_path):
            img = Image(img_path, width=6*inch, height=3.5*inch)
            story.append(img)
            story.append(Spacer(1, 0.1 * inch))
        else:
            story.append(Paragraph(f"Image not found: {img_path}", styles['Normal']))
        story.append(Spacer(1, 0.2 * inch))

    # Build the PDF document
    doc.build(story)
    print(f"✅ PDF report generated: {output_filename}")

if __name__ == '__main__':
    # Default image paths for standalone execution
    default_image_paths = [
        "../reports/infection_trends.png",
        "../reports/anemia_distribution.png",
        "../reports/crp_trends.png"
    ]
    generate_pdf_report(image_paths=default_image_paths)