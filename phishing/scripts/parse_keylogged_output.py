import pandas as pd
import datetime
import os
import numpy as np
import itertools

os.chdir('../')

from configs.keylog_cfg import *

#####################
##### functions #####
#####################

def raw_keylog_data_to_df(raw_keylogged_data):

    list_of_dfs = []

    counter = 0

    for data in raw_keylogged_data:

        tmp = {k:v for k,v in [i.split(': ') for i in data]}
        raw_keylog_dict = {}
        raw_keylog_dict['timestamp'] = list(tmp.keys())
        raw_keylog_dict['keypress'] = list(tmp.values())

        df_tmp = pd.DataFrame(raw_keylog_dict)
        df_tmp['file_suffix'] = files_to_read[counter][-11:].replace('.', '').replace('txt', '')
        counter += 1

        list_of_dfs.append(df_tmp)

    df = pd.concat(list_of_dfs, axis=0)

    return df


def group_keylogged_df(df, groupby_keypress = 'Key.enter'):

    df['group'] = np.nan
    df.loc[df['keypress'] == groupby_keypress, 'group'] = 1
    df['group'] = df.groupby('keypress')['group'].transform(lambda x: x.cumsum())
    df['group'].bfill(inplace=True)

    df_grouped = df.groupby('group').agg({'timestamp': [min, max],
                             'keypress': [lambda x: ''.join(x)],
                             'file_suffix': [min]})

    df_grouped.columns = list(pd.Index([str(e[0]).lower() + '_' + str(e[1]).lower()\
                                        for e in df_grouped.columns.tolist()])\
                              .str.replace(' ', '_')\
                              .str.replace('_<lambda>', '')\
                              .str.replace('file_suffix_min', 'file_suffix'))
    df_grouped.reset_index(inplace=True, drop=True)

    return df_grouped



########################################
##### parse the raw keylogged data #####
########################################

files_to_read = [READ_KEYLOGGED_DIR + i for i in list(itertools.chain(*list(itertools.chain.from_iterable([f for f in os.walk(READ_KEYLOGGED_DIR)])))) if i.endswith('.txt')]

raw_keylogged_data = []

for f in files_to_read:
    raw_keylogged_data.append(open(f, 'r').readlines())

df = raw_keylog_data_to_df(raw_keylogged_data)
df['keypress'] = df['keypress'].str.replace('\n', '').str.replace("'", "")

df_grouped = group_keylogged_df(df)

df_grouped.to_csv(WRITE_KEYLOGGED_DIR + str(datetime.datetime.today()).replace(' ', ''))
