import webview

webview.create_window('Hello world', 'https://pywebview.flowrl.com/')
webview.start()

if __name__ == '__main__':
    webview.create_window('Debug window', 'https://pywebview.flowrl.com/hello')
    webview.start(debug=True)
