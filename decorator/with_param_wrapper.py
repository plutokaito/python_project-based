def makeHtmlTag(tag, *args, **kwds):
    def real_decorator(fn):
        css_class = " class='{0}'".format(kwds['css_class']) if "css_class" in kwds else ""
        def wrapped(*args, **kwds):
            return "<"+tag+css_class+">" + fn(*args, **kwds) + "</"+tag+">"
        return wrapped
    return real_decorator

@makeHtmlTag(tag = 'div', css_class="bold_css")
@makeHtmlTag(tag = 'i',css_class="op_edit")
def hello(msg):
    return msg

print(hello("hello world"))
print(hello.__name__)
