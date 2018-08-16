準備好 virtualenv ，執行好下面的指令以後，就可以開始本次的 workshop


```bash

virtualenv venv
source venv/bin/activate
pip install -r requirements.txt

cd demo
python manage.py migrate
python manage.py runscript create_default_data
python manage.py shell_plus --notebook

```

啟動以後，看到附檔名為  ipynb 的檔案以後，按下開始執行 jupyter notebook
