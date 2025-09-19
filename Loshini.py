from http.server import HTTPServer, BaseHTTPRequestHandler
content = """
<!DOCTYPE html>
<html>
    <head>
        <title>DEVICE SPECIFICATIONS</title>
    </head>

    <body bgcolor="pink">
        <h1 align="center">DEVICE SPECIFICATIONS - 25002119</h1>
        <table border="2">
            <tr bgcolor="purple">
                <th>S.No</th>
                <th>Device Specification</th>
                <th>Description</th>
            </tr>
            <tr>
                <td>1</td>
                <td>Storage</td>
                <td>954GB</td>
            </tr>
            <tr>
                <td>2</td>
                <td>Graphics Card</td>
                <td>128MB</td>
            </tr>
            <tr>
                <td>3</td>
                <td>Installed RAM</td>
                <td>16.0GB</td>
            </tr>
            <tr>
                <td>4</td>
                <td>Processor</td>
                <td>Intel(R) Core(TM) Ultra 5 125H</td>
            </tr>
            <tr>
                <td>5</td>
                <td>Device Name</td>
                <td>Loshini</td>
            </tr>
        </table>
    </body>
</html>
"""
class myhandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("request received")
        self.send_response(200)
        self.send_header('content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())
server_address = ('',8000)
httpd = HTTPServer(server_address,myhandler)
print("my webserver is running...")
httpd.serve_forever()