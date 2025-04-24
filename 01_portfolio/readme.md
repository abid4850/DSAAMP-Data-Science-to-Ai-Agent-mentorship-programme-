# Building a portfolio

we will use mkdocs for building a portfolio. Mkdocs is a static site generator that is geared towards project documentation. It is written in python and uses the jinja2 templating engine. Mkdocs is easy to use and has a lot of features that make it a good choice for building a portfolio.

link to the documentation is[here](http://www.mkdocs.org/getting-started/)

## 1. Install mkdocs
'''bash 
conda create -n mkdocs python=3.12 -y
conda activate mkdocs
pip install mkdocs
'''

## 2. Create a new mkdocs projects
'''bash
mkdocs new my_portfolio
cd my_portfolio
'''

## 3 Run the development server 
'''bash
mkdocs serve
'''

> This is how you can specify the port and host
> (i am using a websit using mkdocs. how can i specify the port number for server command? for using gpt)
'''bash
mkdocs serve -a 127.0.0.1:8000




