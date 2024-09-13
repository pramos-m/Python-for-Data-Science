#before execution do those cmnds;
    # python3 -m build
    # pip install ./dist/ft_package-0.0.1.tar.gz
    # pip install ./dist/ft_package-0.0.1-py3-none-any.whl
from ft_package import count_in_list
print(count_in_list(["toto", "tata", "toto"], "toto"))
print(count_in_list(["toto", "tata", "toto"], "tutu"))

#   pip list | grep ft_package
#   pip show -v ft_package

