```bash

virtualenv venv
source venv/bin/activate
pip install -r requirements.txt

python demo/manage.py migrate
python demo/manage.py runscript create_default_data
python demo/manage.py shell_plus --notebook

```

than clieck the ipython notebook file to enjoy the workshop
