from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch

def generate_pdf_report(output_filename="Blood_Report_Analytics_Report.pdf"):
    doc = SimpleDocTemplate(output_filename, pagesize=letter)
    styles = getSampleStyleSheet()
    story = []

    # Title
    story.append(Paragraph("Executive Summary: Blood Report Analytics", styles['h1']))
    story.append(Spacer(1, 0.2 * inch))

    # Read executive summary content
    with open("executive_summary.md", "r") as f:
        summary_content = f.read()
    
    # Add summary content (basic formatting for markdown)
    for line in summary_content.split('\n'):
        if line.startswith('# '):
            story.append(Paragraph(line[2:], styles['h2']))
        elif line.startswith('## '):
            story.append(Paragraph(line[3:], styles['h3']))
        else:
            story.append(Paragraph(line, styles['Normal']))
        story.append(Spacer(1, 0.1 * inch))

    # Add visuals
    story.append(Paragraph("Key Visualizations", styles['h2']))
    story.append(Spacer(1, 0.2 * inch))

    images = ["infection_trends.png", "anemia_distribution.png", "crp_trends.png"]
    for img_path in images:
        try:
            img = Image(img_path, width=6*inch, height=3.5*inch)
            story.append(img)
            story.append(Spacer(1, 0.1 * inch))
        except FileNotFoundError:
            story.append(Paragraph(f"Image not found: {img_path}", styles['Normal']))
        story.append(Spacer(1, 0.2 * inch))

    doc.build(story)
    print(f"PDF report generated: {output_filename}")

if __name__ == '__main__':
    generate_pdf_report()