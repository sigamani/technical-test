# Qudo analysis pipeline 

Create the environment with conda

`conda env create --file environment.yml`

Activate the environment

`conda activate qudo-env`

# 1) Download data, then clean and add weighting columns
`python main.py process`

# 2) Run a segmentation of your choice
`python main.py segment -s rules -c 'Go City:AIDA_WW_ABA_IMS_07062021'` (rules-based)

`python main.py segment` (kmodes clustering)

# 3) Produce report
`python main.py report`

# 4) Run tests
`pytest`
