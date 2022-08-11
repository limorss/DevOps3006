from flask import Flask, request

# Create http server and run it
app = Flask("something")
my_example = '''
<html>
<head> 
</head>
<body>
<p>&nbsp;</p>
<table style="border-collapse: collapse; width: 100%;" border="1">
<tbody>
<tr>
<td style="width: 11.1111%;">&nbsp;</td>
<td style="width: 11.1111%;">&nbsp;</td>
<td style="width: 11.1111%;">&nbsp;</td>
<td style="width: 11.1111%;">&nbsp;</td>
<td style="width: 11.1111%;">&nbsp;</td>
<td style="width: 11.1111%;">&nbsp;</td>
<td style="width: 11.1111%;">&nbsp;</td>
<td style="width: 11.1111%;">&nbsp;</td>
<td style="width: 11.1111%;">&nbsp;</td>
</tr>
<tr>
<td style="width: 11.1111%;">&nbsp;</td>
<td style="width: 11.1111%;">&nbsp;</td>
<td style="width: 11.1111%;">&nbsp;</td>
<td style="width: 11.1111%;">&nbsp;</td>
<td style="width: 11.1111%;">&nbsp;</td>
<td style="width: 11.1111%;">&nbsp;</td>
<td style="width: 11.1111%;">&nbsp;</td>
<td style="width: 11.1111%;">&nbsp;</td>
<td style="width: 11.1111%;">&nbsp;</td>
</tr>
<tr>
<td style="width: 11.1111%;">&nbsp;</td>
<td style="width: 11.1111%;">&nbsp;</td>
<td style="width: 11.1111%;">&nbsp;</td>
<td style="width: 11.1111%;">&nbsp;</td>
<td style="width: 11.1111%;">&nbsp;</td>
<td style="width: 11.1111%;">&nbsp;</td>
<td style="width: 11.1111%;">&nbsp;</td>
<td style="width: 11.1111%;">&nbsp;</td>
<td style="width: 11.1111%;">&nbsp;</td>
</tr>
<tr>
<td style="width: 11.1111%;">&nbsp;</td>
<td style="width: 11.1111%;">&nbsp;</td>
<td style="width: 11.1111%;">&nbsp;</td>
<td style="width: 11.1111%;">&nbsp;</td>
<td style="width: 11.1111%;">&nbsp;</td>
<td style="width: 11.1111%;">&nbsp;</td>
<td style="width: 11.1111%;">&nbsp;</td>
<td style="width: 11.1111%;">&nbsp;</td>
<td style="width: 11.1111%;">&nbsp;</td>
</tr>
<tr>
<td style="width: 11.1111%;">&nbsp;</td>
<td style="width: 11.1111%;">&nbsp;</td>
<td style="width: 11.1111%;">&nbsp;</td>
<td style="width: 11.1111%;">eeee</td>
<td style="width: 11.1111%;">&nbsp;</td>
<td style="width: 11.1111%;">&nbsp;</td>
<td style="width: 11.1111%;">&nbsp;</td>
<td style="width: 11.1111%;">&nbsp;</td>
<td style="width: 11.1111%;">&nbsp;</td>
</tr>
<tr>
<td style="width: 11.1111%;">&nbsp;</td>
<td style="width: 11.1111%;">&nbsp;</td>
<td style="width: 11.1111%;">&nbsp;</td>
<td style="width: 11.1111%;">&nbsp;</td>
<td style="width: 11.1111%;">&nbsp;</td>
<td style="width: 11.1111%;">&nbsp;</td>
<td style="width: 11.1111%;">&nbsp;</td>
<td style="width: 11.1111%;">&nbsp;</td>
<td style="width: 11.1111%;">&nbsp;</td>
</tr>
<tr>
<td style="width: 11.1111%;">&nbsp;</td>
<td style="width: 11.1111%;">&nbsp;</td>
<td style="width: 11.1111%;">&nbsp;</td>
<td style="width: 11.1111%;">&nbsp;</td>
<td style="width: 11.1111%;">&nbsp;</td>
<td style="width: 11.1111%;">&nbsp;</td>
<td style="width: 11.1111%;">&nbsp;</td>
<td style="width: 11.1111%;">&nbsp;</td>
<td style="width: 11.1111%;">&nbsp;</td>
</tr>
</tbody>
</table>
</body>
</html>
'''

@app.route('/whatismyname', methods=['GET', 'POST', 'DELETE'])
def hello():
    if request.method == 'GET':
        return my_example
    elif request.method == 'POST':
        return "saved new car1"

@app.route('/')
def my_func():
    return "Hello Visuality Systems Automation Developer!"


app.run(host="0.0.0.0", port=5001, debug=False)
