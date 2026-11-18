"""
Assembler module for the 33-page IEEE Access report.
Combines Part 1, Part 2, and Part 3.
"""

import report_pages_part1 as p1
import report_pages_part2 as p2
import report_pages_part3 as p3

css_styles = """
<style>
@page {
    size: letter; /* 8.5in x 11in */
    margin: 0;
}
* {
    box-sizing: border-box;
    -webkit-print-color-adjust: exact !important;
    print-color-adjust: exact !important;
}
html, body {
    margin: 0;
    padding: 0;
    background-color: #ffffff;
    font-family: 'Times New Roman', Times, 'Nimbus Roman No9 L', serif;
    font-size: 8.35pt;
    line-height: 1.21;
    color: #111111;
}

.page {
    width: 8.5in;
    height: 11in;
    padding: 0.38in 0.46in 0.36in 0.46in;
    position: relative;
    page-break-after: always;
    break-after: page;
    overflow: hidden;
    background: #ffffff;
}

/* Page Header & Footer */
.page-header {
    height: 0.25in;
    border-bottom: 0.6pt solid #002855;
    display: flex;
    justify-content: space-between;
    align-items: flex-end;
    padding-bottom: 2px;
    font-family: Arial, Helvetica, sans-serif;
    font-size: 7.2pt;
    color: #333333;
    margin-bottom: 8px;
}
.header-left { font-weight: bold; }
.header-right { font-style: italic; }

.ieee-logo-text {
    font-family: Arial, Helvetica, sans-serif;
    font-weight: 900;
    letter-spacing: -0.5px;
}
.ieee-blue { color: #002855; font-size: 8.5pt; }
.ieee-access { color: #00b5e2; font-size: 8.5pt; font-style: italic; font-weight: 300; }

.page-footer {
    position: absolute;
    bottom: 0.32in;
    left: 0.46in;
    right: 0.46in;
    height: 0.22in;
    border-top: 0.5pt solid #cccccc;
    display: flex;
    justify-content: space-between;
    align-items: center;
    font-family: Arial, Helvetica, sans-serif;
    font-size: 7pt;
    color: #555555;
}
.footer-center { font-size: 6.2pt; color: #777777; text-align: center; max-width: 70%; }

/* Two-column layout */
.content-body {
    height: 9.85in;
    column-count: 2;
    column-gap: 1.5pc;
    column-fill: balance;
    text-align: justify;
    text-justify: inter-word;
}

.full-width {
    column-span: all;
    margin-bottom: 8px;
}

/* Typography */
h1.doc-title {
    font-family: Arial, Helvetica, sans-serif;
    color: #002855;
    font-size: 18.5pt;
    font-weight: 900;
    line-height: 1.15;
    margin: 4px 0 8px 0;
    text-align: left;
}

.authors-block {
    font-family: Arial, Helvetica, sans-serif;
    font-size: 9pt;
    font-weight: bold;
    color: #111111;
    margin-bottom: 5px;
    line-height: 1.3;
}
.affil-block {
    font-family: Arial, Helvetica, sans-serif;
    font-size: 7.2pt;
    color: #444444;
    line-height: 1.25;
    margin-bottom: 6px;
}
.corresp-block {
    font-family: Arial, Helvetica, sans-serif;
    font-size: 7.2pt;
    color: #222222;
    margin-bottom: 8px;
    font-weight: 500;
}

/* Page 1 Masthead */
.masthead-top {
    display: flex;
    justify-content: space-between;
    align-items: flex-start;
    border-bottom: 1.5pt solid #002855;
    padding-bottom: 4px;
    margin-bottom: 8px;
}
.masthead-meta {
    font-family: Arial, Helvetica, sans-serif;
    font-size: 6.8pt;
    color: #444444;
    line-height: 1.2;
}
.masthead-doi {
    font-family: Arial, Helvetica, sans-serif;
    font-size: 6.8pt;
    color: #222222;
    font-weight: bold;
    margin-top: 2px;
}
.masthead-logo {
    text-align: right;
}
.masthead-logo-title {
    font-family: Arial, Helvetica, sans-serif;
    font-size: 13pt;
    font-weight: 900;
}
.masthead-logo-sub {
    font-family: Arial, Helvetica, sans-serif;
    font-size: 5.5pt;
    color: #555555;
    letter-spacing: 0.5px;
    text-transform: uppercase;
}

.article-badge-container {
    display: flex;
    align-items: center;
    gap: 8px;
    margin: 6px 0;
}
.striped-bar {
    width: 32px;
    height: 15px;
    background: repeating-linear-gradient(45deg, #00b5e2, #00b5e2 2px, #ffffff 2px, #ffffff 4px);
    border-radius: 2px;
}
.article-badge {
    background: #0072bc;
    color: #ffffff;
    font-family: Arial, Helvetica, sans-serif;
    font-size: 7.5pt;
    font-weight: 900;
    padding: 2px 8px;
    border-radius: 3px;
    letter-spacing: 0.8px;
    text-transform: uppercase;
}

/* Abstract and Index Terms */
.abstract-box {
    margin-bottom: 6px;
    font-size: 8.1pt;
    line-height: 1.23;
    text-align: justify;
}
.abstract-title {
    color: #0072bc;
    font-family: Arial, Helvetica, sans-serif;
    font-size: 7.8pt;
    font-weight: 900;
    letter-spacing: 0.5px;
}
.index-terms-title {
    color: #0072bc;
    font-family: Arial, Helvetica, sans-serif;
    font-size: 7.8pt;
    font-weight: 900;
    letter-spacing: 0.5px;
}
.cyan-sq {
    color: #00b5e2;
    font-size: 9pt;
    margin-right: 3px;
}

/* Headings */
h2.sec-heading {
    font-family: Arial, Helvetica, sans-serif;
    color: #0072bc;
    font-size: 8.8pt;
    font-weight: 900;
    text-transform: uppercase;
    margin: 8px 0 3px 0;
    letter-spacing: 0.3px;
    border-bottom: 0.3pt solid #e2e8f0;
    padding-bottom: 1px;
}
h3.subsec-heading {
    font-family: 'Times New Roman', Times, serif;
    font-size: 8.4pt;
    font-weight: bold;
    font-style: italic;
    color: #002855;
    margin: 6px 0 2px 0;
}

p {
    margin: 0 0 4px 0;
    text-indent: 1em;
}
p.no-indent {
    text-indent: 0;
}

/* Tables */
table.ieee-table {
    width: 100%;
    border-collapse: collapse;
    margin: 5px 0;
    font-size: 7.1pt;
    line-height: 1.15;
}
table.ieee-table th {
    border-top: 1.2pt solid #000000;
    border-bottom: 0.6pt solid #000000;
    padding: 2.5px 2px;
    font-family: Arial, Helvetica, sans-serif;
    font-weight: bold;
    text-align: center;
    background-color: #f8fafc;
}
table.ieee-table td {
    padding: 2px 2px;
    text-align: center;
    border-bottom: 0.3pt solid #e5e7eb;
}
table.ieee-table tr.last-row td {
    border-bottom: 1.2pt solid #000000;
}
.table-caption {
    font-family: Arial, Helvetica, sans-serif;
    font-size: 7.1pt;
    font-weight: bold;
    color: #002855;
    text-align: center;
    margin-bottom: 2px;
    text-transform: uppercase;
}

/* Figures */
.fig-container {
    margin: 5px 0;
    text-align: center;
}
.fig-container img {
    max-width: 100%;
    height: auto;
    border: 0.4pt solid #cbd5e1;
    border-radius: 2px;
}
.fig-caption {
    font-family: Arial, Helvetica, sans-serif;
    font-size: 7pt;
    line-height: 1.18;
    text-align: justify;
    color: #222222;
    margin-top: 2px;
}
.fig-caption strong {
    color: #002855;
    font-weight: bold;
}

/* Equations */
.eq-box {
    margin: 4px 0;
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 0 8px;
    font-style: italic;
    font-size: 8pt;
}
.eq-math {
    flex-grow: 1;
    text-align: center;
}
.eq-num {
    font-style: normal;
    font-family: Arial, Helvetica, sans-serif;
    font-size: 7.2pt;
    color: #333333;
}

/* Bio Box */
.bio-item {
    display: flex;
    gap: 8px;
    margin-top: 8px;
    align-items: flex-start;
}
.bio-img {
    width: 0.82in;
    height: 1.02in;
    border: 0.6pt solid #002855;
    object-fit: cover;
}
.bio-text {
    flex: 1;
    font-size: 7.5pt;
    line-height: 1.18;
    text-align: justify;
}
.bio-name {
    font-family: Arial, Helvetica, sans-serif;
    font-weight: bold;
    color: #002855;
    font-size: 8pt;
}

/* Callout boxes */
.callout-box {
    background-color: #f0f9ff;
    border-left: 2pt solid #0284c7;
    padding: 3px 5px;
    margin: 4px 0;
    font-size: 7.6pt;
    line-height: 1.18;
}

ul.ieee-list {
    margin: 2px 0 4px 10px;
    padding: 0;
    font-size: 8pt;
}
ul.ieee-list li {
    margin-bottom: 2px;
    text-align: justify;
}
</style>
"""

def get_full_html():
    pages = [
        p1.get_page_1(), p1.get_page_2(), p1.get_page_3(), p1.get_page_4(), p1.get_page_5(),
        p1.get_page_6(), p1.get_page_7(), p1.get_page_8(), p1.get_page_9(), p1.get_page_10(), p1.get_page_11(),
        p2.get_page_12(), p2.get_page_13(), p2.get_page_14(), p2.get_page_15(), p2.get_page_16(),
        p2.get_page_17(), p2.get_page_18(), p2.get_page_19(), p2.get_page_20(), p2.get_page_21(), p2.get_page_22(),
        p3.get_page_23(), p3.get_page_24(), p3.get_page_25(), p3.get_page_26(), p3.get_page_27(),
        p3.get_page_28(), p3.get_page_29(), p3.get_page_30(), p3.get_page_31(), p3.get_page_32(), p3.get_page_33()
    ]
    
    assert len(pages) == 33, f"Expected 33 pages, but have {len(pages)}"
    
    doc = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>An Innovative Ensemble Deep Learning Clinical Decision Support System for Diabetes Prediction - AGARSHNA R (RA2411026050061)</title>
    {css_styles}
</head>
<body>
""" + "\n".join(pages) + """
</body>
</html>"""
    return doc
