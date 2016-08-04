import sys
s = sys.stdin.read()
s = s.replace("https://cdnjs.cloudflare.com/ajax/libs/reveal.js/3.1.0/css/theme/simple.css", "sky2.css")
s = s.replace("""html {
  font-size: 10px;
  -webkit-tap-highlight-color: rgba(0, 0, 0, 0);
}
body {
  font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
  font-size: 13px;
  line-height: 1.42857143;
  color: #000;
  background-color: #fff;
}""", "")
s = s.replace("""@-moz-document url-prefix() {
  div.inner_cell {
    overflow-x: hidden;
  }""", """@-moz-document url-prefix() {
  div.inner_cell {
    overflow: visible;
  }""")
s = s.replace("""div.text_cell.rendered .rendered_html {
  /* The H1 height seems miscalculated, we are just hidding the scrollbar */
  overflow-y: hidden;
}""","""div.text_cell.rendered .rendered_html {
  /* The H1 height seems miscalculated, we are just hidding the scrollbar */
  overflow: visible;
}""")
s = s.replace("history: true,", "history: true,\n  width: 1600,\n  height: 900,\n")
sys.stdout.write(s)