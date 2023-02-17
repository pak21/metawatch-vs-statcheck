#!/usr/bin/env python3

import pandas as pd
import scipy.stats

def poisson_test(row):
    k1 = row['metawatch_k']
    n1 = row['metawatch_n']

    k2 = row['statcheck_k']
    n2 = row['statcheck_n']

    return scipy.stats.poisson_means_test(k1, n1, k2, n2, alternative='two-sided')[1]

def main():
    data = pd.read_csv('metawatch-vs-statcheck.csv').set_index('Faction')
    data.columns = ['metawatch_f', 'statcheck_f', 'statcheck_n']

    # Assume Metawatch has twice as much data as Statcheck
    data['metawatch_n'] = 2 * data['statcheck_n']

    data['metawatch_k'] = (data['metawatch_f'] * data['metawatch_n']).round()
    data['statcheck_k'] = (data['statcheck_f'] * data['statcheck_n']).round()

    data['p_value'] = data.apply(poisson_test, axis='columns')

    print(data.sort_values('p_value'))

if __name__ == '__main__':
    main()
