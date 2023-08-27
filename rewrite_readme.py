from long_description import LONG_DESCRIPTION

"""
This is to rewrite anew the readme file, 
so that one only has to change the long_description file.

The readme.md will be uploaded on github as the description of the project.

You have to be in main anederli folder when you run this script via terminal.
"""

def rewrite_readme():
    with open('README.md', 'w') as f:
        f.write("# canederli\n\n")  # package name here
        f.write(LONG_DESCRIPTION)


if __name__ == "__main__":
    rewrite_readme()