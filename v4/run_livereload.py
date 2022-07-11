from livereload import Server, shell

if __name__ == '__main__':
    server = Server()
    server.watch('docs/*.rst', shell('make html'), delay=1)
    server.watch('docs/*.md', shell('make html'), delay=1)
    server.watch('docs/*.py', shell('make html'), delay=1)
    server.watch('docs/_static/*', shell('make html'), delay=1)
    server.watch('docs/_templates/*', shell('make html'), delay=1)
    server.serve(root='build/html')