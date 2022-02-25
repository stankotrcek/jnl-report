"""
report.py

Example of a report generator for ledger-cli with template support.
"""
import os
import subprocess
from mako.template import Template

period = "2022-02"
end_date = "2022-03-01"

tmp_file = "report.mako"
tex_file = f"report/report_{period}.tex"
pdf_file = f"report/report_{period}.pdf"

qry = {}
data = {}
data["parameters"] = {"period": period, "end_date": end_date}

reg_format = "%8d & %-.10P & %-.25A & %12t & %12T  \\\\\\\\ "

# region Query
qry[
    "bal-exp"
] = f'ledger -f data.ledger bal "^expense"  --end {end_date}'  # balance on date

qry[
    "reg-exp"
] = f'ledger -f data.ledger reg "^expense"    -p {period}'  # register for period

qry[
    "exp-table"
] = f'ledger -f data.ledger reg "^expense"  --format "{reg_format}"   -p {period}'  # register for period

# endregion

# region get Data
output = subprocess.run(qry["bal-exp"], shell=True, capture_output=True, text=True)
data["bal-exp"] = output.stdout if output.stderr == "" else output.stderr

output = subprocess.run(qry["reg-exp"], shell=True, capture_output=True, text=True)
data["reg-exp"] = output.stdout if output.stderr == "" else output.stderr

output = subprocess.run(qry["exp-table"], shell=True, capture_output=True, text=True)
data["exp-table"] = output.stdout if output.stderr == "" else output.stderr

# endregion

# region create TEX file from mako template
mytemplate = Template(filename=tmp_file)
render_out = mytemplate.render(data=data)

new_file = open(tex_file, mode="w", encoding="utf-8")
new_file.write(render_out)
new_file.close()
# endregion

# region create PDF
subprocess.run(
    f"pdflatex -aux-directory=latex-aux  -interaction=batchmode -output-directory=report -quiet  {tex_file} , shell=True"
)
# endregion

# open generated PDF
# os.startfile(f"report\{pdf_file}")

