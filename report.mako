\documentclass[a4paper, 10pt]{article}

\usepackage{hyperref}
\usepackage[utf8]{inputenc}
\usepackage{fontawesome}
\usepackage{xcolor}
\usepackage[datesep=., style=ddmmyyyy]{datetime2}
\usepackage{booktabs}

\title{Poročilo obdobja} 
\author{}
\date{}
\setlength{\parindent}{0pt}
\usepackage{geometry}
\geometry{a4paper, portrait, left=2.5cm, right=1cm, top=2cm, bottom=1.5cm }


\usepackage{multicol}
\setlength{\columnsep}{1.5cm}
\setlength{\columnseprule}{0.2pt}

\begin{document}

\section*{Report period: ${data['parameters']['period']} }
print date: \today

\section{Expenses balance}

\begin{verbatim}
${data['bal-exp']} 
\end{verbatim}

\section{Expenses register}

\begin{verbatim}
${data['reg-exp']} 
\end{verbatim}

\section{Expenses table}

\begin{tabular}{lllrr}
\toprule
\textbf{Date} & \textbf{Payee} & \textbf{Account}& \textbf{Amount} & \textbf{Total}  \\\\

\midrule
${data['exp-table']} 
\bottomrule
\end{tabular}

\end{document}  
