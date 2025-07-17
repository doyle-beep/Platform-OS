
import pymysql # type: ignore
from flask import Flask, render_template # type: ignore
from flask_bootstrap import Bootstrap5 # type: ignore
from functions import platcomprehensive, oscomprehensive, systhings
from flask_wtf import CSRFProtect # type: ignore

app = Flask(__name__)
app.config.from_object(__name__)
app.secret_key = 'tO$&!|0wkamvVia0?n$NqI'

bootstrap = Bootstrap5(app)
csrf = CSRFProtect(app)

@app.route('/')
def diagnostics():
    platcomp = platcomprehensive()
    oscomp = oscomprehensive()
    s = systhings()
    return render_template('index.html', plat=platcomp, osc = oscomp, s = s)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
