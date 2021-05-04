__author__ = "Alex BOURG"
__copyright__ = "Copyright 2021"
__license__ = "GPL"
__version__ = "1.0.1"
__email__ = "alex.bourg@outlook.com"
__status__ = "Production"


import os
import sys

package_dir = os.path.isdir(r"C:\Program64\Python\Packages")


def info(error):
    print(
        "## Please enter the command in the following format:\n- To install one package: offlinepip option packagename\n- To install all avaialable packages:\nofflinepip option all\n"
    )
    print("# Options: install/ uninstall/ upgrade")
    print("# packageName: only one package or all/tout/tous")
    print(error)
    return


def install(package, action, path):
    os.system(f"echo ****************************************************")
    os.system(f"echo {package}")
    os.system(f"echo ****************************************************")

    # Install command
    if action == "install":
        if "pip" in package:
            os.system(
                f"python -m pip install --upgrade pip --no-index --find-links {path}"
            )
        elif "numpy==1.19.2" in package and sys.version_info.minor == 9:
            os.system(f"echo {package} is not compatible with current Python version")
        else:
            os.system(f"pip {action} --no-index --find-links {path} {package}")

    # Uninstall command
    if action == "uninstall":
        if "pip" in package:
            os.system(
                f"python -m pip install --upgrade pip --no-index --find-links {path}"
            )
        elif "numpy==1.19.2" in package and sys.version_info.minor == 9:
            os.system(f"echo {package} is not compatible with current Python version")
        else:
            os.system(f"pip {action} {package} -y")

    # Upgrade command
    if action == "upgrade":
        if "pip" in package:
            os.system(
                f"python -m pip install --upgrade pip --no-index --find-links {path}"
            )
        elif "numpy==1.19.2" in package and sys.version_info.minor == 9:
            os.system(f"echo {package} is not compatible with current Python version")
        else:
            os.system(f"pip install --no-index --find-links {path} {package} -U")


def pip_list():
    os.system(f"pip list")
    return


if __name__ == "__main__":
    try:
        if len(sys.argv) == 3:
            # defining the packages folder path
            if package_dir:
                path = r"C:\Program64\Python\Packages"
            else:
                script = os.path.realpath(__file__)
                path = script[: script.rfind("\\")]

            # defining the command
            if sys.argv[1] == "install".lower():
                action = "install"
            elif sys.argv[1] == "uninstall".lower():
                action = "uninstall"
            elif sys.argv[1] == "upgrade".lower():
                action = "upgrade"
            else:
                info("Error: wrong command")

            # defining the package name
            if (
                sys.argv[2] == "all".lower()
                or sys.argv[2] == "tout".lower()
                or sys.argv[2] == "tous".lower()
            ):
                req = fr"{path}\requirements.txt"
                print(req)
                with open(req) as file:
                    for line in file:
                        install(line, action, path)
            else:
                req = sys.argv[2]
                install(req, action, path)
        elif "list" in sys.argv:
            pip_list()

        else:
            info("Error: wrong input")
    except:
        info()
