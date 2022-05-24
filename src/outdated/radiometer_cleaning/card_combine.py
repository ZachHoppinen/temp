"""
Combines .dat files for hourly and minute 4-component radiometer records from a SD card.

Usage:
    card_combine.py [-o output] [-i input]

Options:
    -o output       destination dir [default: ../../banner/radiometer/data/combined/]
    -i input        directory the card files are stored on [default: ../../banner/radiometer/data/raw/*/*/]
"""

import pandas as pd
from glob import glob
from tqdm.auto import tqdm
from docopt import docopt
import logging
from os.path import join

def main(args):
    out_dir = args.get('-o')
    in_dir = args.get('-i')

    logger.info(f'Searching {in_dir}...')

    for ftype in ['Hourly', 'Minute']:
        fps = glob(join(in_dir , f'*{ftype}*.dat'))
        logger.info(f'Found {len(fps)} {ftype} files...')
        if len(fps) > 0:
            comb = pd.DataFrame()
            for i in tqdm(fps):
                df = pd.read_csv(i, skiprows = 1)
                comb = comb.append(df[2:], ignore_index=True)
            comb.loc[:,'datetime'] = pd.to_datetime(comb.TIMESTAMP)
            comb = comb.drop('TIMESTAMP',axis = 1)
            comb = comb.set_index('datetime')
            comb = comb.sort_index()
            for col in comb.columns:
                try:
                    comb[col] = comb[col].astype('f8')
                except:
                    pass
            fname = f'{ftype}_{comb.index[0].date()}_{comb.index[-1].date()}.csv'
            out_fp = join(out_dir, fname)
            logger.info(f'Saving to {out_fp}...')
            comb.to_csv(out_fp)

if __name__ == '__main__':
    logger = logging.getLogger(__name__)
    logging.basicConfig()
    logger.setLevel(logging.DEBUG)
    args = docopt(__doc__)
    main(args)