# ---
# jupyter:
#   jupytext:
#     cell_metadata_filter: all
#     notebook_metadata_filter: all,-language_info
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.3.3
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# The following notebook generates [NHS Dictionary of Medicines and Devices codes](https://ebmdatalab.net/what-is-the-dmd-the-nhs-dictionary-of-medicines-and-devices/) for antihistamines. You can see current [antihistamine prescribing patterns on OpenPrescribing](https://openprescribing.net/bnf/030401/)

#import libraries
from ebmdatalab import bq
import pandas as pd
import os

# +
sql = '''WITH bnf_codes AS (
  SELECT bnf_code FROM hscic.presentation WHERE 
    bnf_code LIKE  "030401%" # antihistamine
    )

SELECT "vmp" AS type, id, bnf_code, nm
FROM dmd.vmp
WHERE bnf_code IN (SELECT * FROM bnf_codes)

UNION ALL

SELECT "amp" AS type, id, bnf_code, descr
FROM dmd.amp
WHERE bnf_code IN (SELECT * FROM bnf_codes)

ORDER BY type, bnf_code, id'''

antihistamine_codelist = bq.cached_read(sql, csv_path=os.path.join('..','data','antihistamine_codelist.csv'))
pd.set_option('display.max_rows', None)
pd.set_option('display.max_colwidth', None)
antihistamine_codelist
# -


