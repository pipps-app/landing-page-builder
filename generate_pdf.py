from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'Business Information Form', 0, 1, 'C')

    def chapter_title(self, title):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, title, 0, 1, 'L')
        self.ln(5)

    def chapter_body(self, body):
        self.set_font('Arial', '', 12)
        self.multi_cell(0, 10, body)
        self.ln()

pdf = PDF()
pdf.add_page()

# Content
content = [
    ("Business Details & Branding", "1. Upload Your Logo (Optional):\n2. Business Name*:\n3. Your Tagline or Slogan (Optional):\n4. Preferred Heading Font Style (Optional):\n5. Preferred Heading Color (Optional):"),
    ("About Your Business (Optional)", "6. Your Business Story:\n7. Your Mission:\n8. What Makes You Unique?"),
    ("Marketing & SEO", "9. What is the main goal of your landing page?*:\n10. Who is your ideal customer? (Optional):\n11. List 5-10 keywords (Optional):"),
    ("Services / Products (Optional)", "12. List up to 10 key services or products:"),
    ("Contact Information", "13. Email Address for Customer Contact*:\n14. Phone Number (Optional):\n15. Is this a WhatsApp number?:\n16. Business Address (Optional):"),
    ("Social Media & Website Links (Optional)", "17. Primary Website Link (e.g., Etsy, Booking Page):\n18. Facebook:\n19. Instagram:\n20. X (Twitter):\n21. LinkedIn:"),
    ("Other Custom Links (Optional)", "22. Add up to 5 other important links:"),
    ("Business Images (Optional)", "23. Upload up to 5 images:"),
    ("Submission", "24. Submit Button:")
]

for title, body in content:
    pdf.chapter_title(title)
    pdf.chapter_body(body)

pdf.output("Business_Information_Form.pdf")
