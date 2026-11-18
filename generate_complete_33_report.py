"""
Master 33-Page IEEE Access Research Report Generator
Author: AGARSHNA R (RA2411026050061)
Department: B.Tech CSE (AIML), SRM IST
"""

import os
import sys
import subprocess
import pypdf

def build_report():
    print("Building 33-page IEEE Access report HTML...")
    
    # Read the CSS styling and each page's content
    import report_pages_data
    html_content = report_pages_data.get_full_html()
    
    output_html = r"C:\project\ann_project\report_33_pages.html"
    output_pdf = r"C:\project\ann_project\Diabetes_Prediction_EDL_Report_33_Pages.pdf"
    
    with open(output_html, "w", encoding="utf-8") as f:
        f.write(html_content)
    
    print(f"HTML written to {output_html}. Size: {os.path.getsize(output_html)} bytes.")
    print("Compiling HTML to PDF using Chrome Headless...")
    
    cmd = [
        r"C:\Program Files\Google\Chrome\Application\chrome.exe",
        "--headless=new",
        "--disable-gpu",
        "--no-sandbox",
        "--no-pdf-header-footer",
        f"--print-to-pdf={output_pdf}",
        f"file:///{output_html.replace(os.sep, '/')}"
    ]
    
    res = subprocess.run(cmd, capture_output=True, text=True)
    if res.returncode != 0:
        print("Chrome error:", res.stderr)
        return False
        
    if not os.path.exists(output_pdf):
        print("PDF was not created!")
        return False
        
    reader = pypdf.PdfReader(output_pdf)
    num_pages = len(reader.pages)
    print(f"SUCCESS: Generated PDF has {num_pages} pages! File size: {os.path.getsize(output_pdf):,} bytes.")
    assert num_pages == 33, f"Expected exactly 33 pages, but got {num_pages}!"
    print("ALL VERIFICATIONS PASSED: Exactly 33 pages generated matching IEEE Access layout!")
    return True

if __name__ == '__main__':
    build_report()
