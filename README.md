# fantasy_league_of_legends

## API & Docs

Uses the Leaguepedia API for data:
https://lol.fandom.com/wiki/Help:Leaguepedia_API

And also the leaguepedia_parser wrapper to help query the data:
https://github.com/mrtolkien/leaguepedia_parser

## Running Locally
1. Setup local db
'''
make up
make migrate-up
'''
2. Running the service
'''
make service
'''


## Setting up for development

1. Create and activate a virtual environment (venv)
'''
python3 -m venv venv
source venv/bin/activate
'''

2. Install requirements
'''
make install
'''

3. Setup local db
'''
make up
make migrate-up
'''

4. Running Tests