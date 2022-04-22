from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
import yfinance as yf
from django.shortcuts import render
from tkinter import *


def index(request):
    return HttpResponse('Main Page')


def my_list(request):
    pass


def ticker_list(request):
   # return HttpResponse('Tickers list')
    template = 'ticker_list.html'
    return render(request, template)


def ticker_detail_render(request, ticker_request):
    template = 'ticker_detail.html'
    return render(request, template)


# @app.route('/')
# def student():
#     return render_template('index.html')
#
#
# @app.route('/result', methods=['POST', 'GET'])
# def result():
#     if request.method == 'POST':
#         result = request.form
#         return render_template("result.html", result=result)
#
#
# if __name__ == '__main__':
#     app.run(debug=True)


# def clicked():
#     lbl.configure(text='Enter the ticker')
#
#     window = Tk()
#     window.title('Ticker slug')
#     window.geometry('400x250')
#     lbl = Label(window, text='Ticker:')
#     lbl.grid(column=0, row=0)
#     txt = Entry(window, width=10)
#     txt.grid(column=1, row=0)
#     btn = Button(window, text="Не нажимать!", command=clicked)
#     btn.grid(column=2, row=0)
#     window.mainloop()