INIT_RESULT_TABLE_HTML = """
<!DOCTYPE html>
<html>
<head>
<style>
table {
  font-family: arial, sans-serif;
  border-collapse: collapse;
  width: 100%;
}

td, th {
  border: 1px solid #dddddd;
  text-align: left;
  padding: 8px;
}

</style>
</head>
<body>

<h2>RESULTADOS</h2>

<table>
  <tr>
    <th>Prueba</th>
    <th>Resultado</th>
  </tr>
"""

END_RESULT_TABLE_HTML = """
</table>
</body>
</html>
"""

def titleHTML(msg,level=1):
    return(f"<h{level}> {msg} </h{level}>")


def rowResultTableHTML(test, result):
    if result == 'Failed':
        color = '#ff6666'
    elif result == 'Success':
        color = '#03AC13'
    elif result == 'Skipped':
        color = '#ED820E'

    line = f"""
    <tr>
    <td>{test}</td>
    <td style="background-color:{color};">{result} </td>
    </tr>"""

    return line

def tableHTML(middle_table_HTML):
    return (INIT_RESULT_TABLE_HTML + middle_table_HTML + END_RESULT_TABLE_HTML)