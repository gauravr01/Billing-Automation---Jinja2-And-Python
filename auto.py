from jinja2 import Template
from pyhtml2pdf import converter
import os
# Read in data
data = {
  'Name':'Menzo',
  'Address' :'298 , Shinchi nagar',
  'add2': 'Mumbai - 400002',
  'Amount' : 20000 ,
  'amt_in_text': "Twenty Thousand Rupees Only" ,
  'IN':11,
  'year':19,
  'page':2,
  'space':'Two Full Page',
  'mode':'Color',
  'addi':'Nil',
  'old':'-',
  'bill':'-',
  'total':20000,
  'no':'0311/223',
  'date':'10/12/2022',
  
  }
data2 = {
    'Name': 'John',
    'Address': '123 Main Street',
    'add2': 'New York, NY - 10001',
    'Amount': 15000,
    'amt_in_text': "Fifteen Thousand Rupees Only",
    'IN': 12,
    'year': 20,
    'page': 3,
    'space': 'One Full Page',
    'mode': 'Black and White',
    'addi': 'Additional Charges Apply',
    'old': '50',
    'bill': '2022/123',
    'total': 15000,
    'no': '0412/324',
    'date': '11/01/2022',
}

data3 = {
    'Name': 'Alice',
    'Address': '456 Elm Street',
    'add2': 'Los Angeles, CA - 90001',
    'Amount': 18000,
    'amt_in_text': "Eighteen Thousand Rupees Only",
    'IN': 13,
    'year': 21,
    'page': 4,
    'space': 'Half Page',
    'mode': 'Black and White',
    'addi': 'Additional Charges Apply',
    'old': '25',
    'bill': '2023/045',
    'total': 18000,
    'no': '0523/567',
    'date': '12/15/2022',
}

data4 = {
    'Name': 'Bob',
    'Address': '789 Oak Street',
    'add2': 'Chicago, IL - 60001',
    'Amount': 22000,
    'amt_in_text': "Twenty-Two Thousand Rupees Only",
    'IN': 14,
    'year': 22,
    'page': 5,
    'space': 'Three Full Pages',
    'mode': 'Color',
    'addi': 'Additional Charges Apply',
    'old': '30',
    'bill': '2023/078',
    'total': 22000,
    'no': '0623/678',
    'date': '01/20/2023',
}

data5 = {
    'Name': 'Eve',
    'Address': '101 Pine Street',
    'add2': 'San Francisco, CA - 94101',
    'Amount': 25000,
    'amt_in_text': "Twenty-Five Thousand Rupees Only",
    'IN': 15,
    'year': 23,
    'page': 6,
    'space': 'Four Full Pages',
    'mode': 'Color',
    'addi': 'Additional Charges Apply',
    'old': '35',
    'bill': '2023/101',
    'total': 25000,
    'no': '0723/789',
    'date': '02/25/2023',
}
data_list = [data, data2, data3, data4, data5]

with open('template/billing.html', 'r', encoding='utf-8') as file:
  template_str = file.read()
template = Template(template_str)
for i, data_item in enumerate(data_list):
    # Render template with current data
    html = template.render(data_item)

    # Generate a unique PDF file name for each data set
    pdf_filename = f'Bill_{i + 1}.pdf'  # e.g., Bill_1.pdf, Bill_2.pdf, etc.

    # Write the HTML to a temporary file
    with open('Temp_Billing.html', 'w') as f:
        f.write(html)

    # Convert the HTML to PDF using the temporary file
    path = os.path.abspath('Temp_Billing.html')
    print_option = {
        'landscape': False,
        'paperHeight': 11.7,
        'paperWidth': 8.3,
        'marginTop': 0,
        'marginRight': 0,
        'marginLeft': 0,
        'marginBottom': 0,
        'pageRanges': '1'
    }

    converter.convert(f'file:///{path}', pdf_filename, print_options=print_option)

    # Remove the temporary HTML file
    os.remove('Temp_Billing.html')

print("PDF files generated successfully.")
