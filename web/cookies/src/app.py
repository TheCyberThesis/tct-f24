from flask import Flask, request, redirect, make_response, render_template

app = Flask(__name__)


FLAG = "TCT{U_kN0w_wH47_4_c00k13_15}"


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

       
        response = make_response(redirect('/dashboard'))

      
        response.set_cookie('is_Admin', '0')  

        
        return response

    return render_template('index.html')



@app.route('/dashboard')
def dashboard():
    is_admin = request.cookies.get('is_Admin')

    if is_admin == '1' or is_admin == 'admin':
        return render_template('dashboard.html', flag=FLAG, is_admin=True)
    else:
        return render_template('dashboard.html', is_admin=False)
    

@app.route('/no_cookies')
def no_cookies():
    return render_template('no_cookies.html')

if __name__ == '__main__':
    app.run(debug=True)#, host='127.0.0.1', port=5000)
