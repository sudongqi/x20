import os
import shutil

if os.path.exists("./dist"):
    shutil.rmtree("./dist")

os.system("python -m build")
os.system("python -m twine upload --repository pypi dist/* --verbose")

os.system("git rm --cached -r *")
os.system("git add .")
os.system('git commit -a -m "update"')
os.system("git push origin main")
