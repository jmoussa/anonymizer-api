# Anonymizer Application

This application will take user specific data (in JSON format) and anonymize it based on the (`hashed:`) prefix the user will add to their fields in the config.
Then will have the ability to de-anonymize but only small amounts of the data, and with an exclusive set of credentials.

This app uses:

- Anaconda (for Python environemnt management)
- Python FastAPI+WebSockets [docs](https://fastapi.tiangolo.com/)
- Pymongo [docs](https://pymongo.readthedocs.io/en/stable/)
- MongoDB [docs](https://docs.mongodb.com/manual/)


## Setting up and running

I've set it up so that you only need to use the `run` script to start.
Be sure to set the S3 environement variables for access

```bash
conda env create -f environment.yml
conda activate anonymizer
python setup.py develop
cd anonymizer
cp config.template.py config.py # edit config.py with your configuration parameters
./run
```

Currently the `auth` module isn't in use (doesn't really need to be, it's just another layer of security)

__For quick API documentation, navigate to `localhost:8000/docs` after starting the server__
