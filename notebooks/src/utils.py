import pandas as pd


def get_csv(path, remove_dubious=False):
    """
    A function to import a csv with the file contents typical of those generated by [ecad.eu].
    Expects a string which represents the path of the file to open.
    """
    frame = pd.read_csv(path, sep=",", skiprows=range(0, 19), skipinitialspace=True)
    frame.drop(frame[frame.iloc[:, 3] == 9].index, inplace=True)
    if remove_dubious:
        frame.drop(frame[frame.iloc[:, 3] == 1].index, inplace=True)
    return frame


def smash_tables(tables):
    """
    A function to merge the tables that are typical of those generated by [ecad.eu].
    Expects a list of pandas tables that each have their 'main feature' on the third column,
    and which contain a column called 'DATE'.
    """

    assert tables

    all = tables[0]

    left_name = all.columns[2]
    right_name = ""

    for table in tables[1:]:
        right_name = table.columns[2]
        all = pd.merge(
            all,
            table,
            on="DATE",
            how="outer",
            suffixes=("_" + left_name, "_" + right_name),
        )

        left_name = right_name
        right_name = ""

    return all


def get_cointrin(remove_dubious=False):
    cc = get_csv("../data/cointrin-geneve/CC_STAID000240.txt", remove_dubious)
    hu = get_csv("../data/cointrin-geneve/HU_STAID000240.txt", remove_dubious)
    pp = get_csv("../data/cointrin-geneve/PP_STAID000240.txt", remove_dubious)
    qq = get_csv("../data/cointrin-geneve/QQ_STAID000240.txt", remove_dubious)
    rr = get_csv("../data/cointrin-geneve/RR_STAID000240.txt", remove_dubious)
    sd = get_csv("../data/cointrin-geneve/SD_STAID000240.txt", remove_dubious)
    ss = get_csv("../data/cointrin-geneve/SS_STAID000240.txt", remove_dubious)
    tg = get_csv("../data/cointrin-geneve/TG_STAID000240.txt", remove_dubious)
    tn = get_csv("../data/cointrin-geneve/TN_STAID000240.txt", remove_dubious)
    tx = get_csv("../data/cointrin-geneve/TX_STAID000240.txt", remove_dubious)

    tables = [cc, hu, pp, qq, rr, sd, ss, tg, tn, tx]
    return smash_tables(tables)


def get_observatoire(remove_dubious=False):
    cc = get_csv("../data/observatoire-geneve/CC_STAID000241.txt", remove_dubious)
    hu = get_csv("../data/observatoire-geneve/HU_STAID000241.txt", remove_dubious)
    qq = get_csv("../data/observatoire-geneve/QQ_STAID000241.txt", remove_dubious)
    rr = get_csv("../data/observatoire-geneve/RR_STAID000241.txt", remove_dubious)
    sd = get_csv("../data/observatoire-geneve/SD_STAID000241.txt", remove_dubious)
    ss = get_csv("../data/observatoire-geneve/SS_STAID000241.txt", remove_dubious)
    tg = get_csv("../data/observatoire-geneve/TG_STAID000241.txt", remove_dubious)
    tn = get_csv("../data/observatoire-geneve/TN_STAID000241.txt", remove_dubious)
    tx = get_csv("../data/observatoire-geneve/TX_STAID000241.txt", remove_dubious)

    tables = [cc, hu, qq, rr, sd, ss, tg, tn, tx]
    return smash_tables(tables)
