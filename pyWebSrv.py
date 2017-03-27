import sys
import os
import time
import BaseHTTPServer

HOST_NAME = 'example.net' # !!!REMEMBER TO CHANGE THIS!!!
PORT_NUMBER = 80 # Maybe set this to 9000.

def doSpeedTest():
    # run a speed test
    result = os.popen("speedtest-cli --simple").read()
    if 'Cannot' in result:
        return "Try again later"
    return result

class MyHandler(BaseHTTPServer.BaseHTTPRequestHandler):
    def do_HEAD(s):
        s.send_response(200)
        s.send_header("Content-type", "text/html")
        s.end_headers()
    def do_GET(s):
        """Respond to a GET request."""
        s.send_response(200)
        s.send_header("Content-type", "text/html")
        if s.path == '/':
            s.send_header("Refresh", "1; url=/speedtest")
            s.end_headers()
            s.wfile.write("<html><head><title>Pi Speed Test</title></head>")
            msg = "Performing Speed Test...\nplease wait 30 seconds..."
            s.wfile.write('<pre><span class="inner-pre" style="font-size: 30px">%s</pre>' % msg)
        elif s.path == '/speedtest':
            msg = doSpeedTest()
            s.end_headers()
            s.wfile.write("<html><head><title>Pi Speed Test Results</title></head>")
            s.wfile.write('<pre><span class="inner-pre" style="font-size: 30px">%s</pre>' % msg)
        s.wfile.write("</body></html>")

if __name__ == '__main__':
    name = port = None
    if sys.argv[1:]:
        name = sys.argv[1]
    if sys.argv[2:]:
        port = int(sys.argv[2])
    if not name: name = HOST_NAME
    if not port: port = PORT_NUMBER
    server_class = BaseHTTPServer.HTTPServer
    httpd = server_class((name, port), MyHandler)
    print time.asctime(), "Server Starts - %s:%s" % (name, port)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    print time.asctime(), "Server Stops - %s:%s" % (name, port)
