#!/usr/bin/env python3
"""Offline integrity checks on curated, source-derived Vanker HW8 evidence."""
from __future__ import annotations
import csv
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EVIDENCE = ROOT / 'evidence'

def read_json(name):
    return json.loads((EVIDENCE / name).read_text(encoding='utf-8'))

def read_csv(name):
    with (EVIDENCE / name).open(encoding='utf-8', newline='') as f:
        return list(csv.DictReader(f))

def verify():
    sample = read_json('muestra-hw5.json')
    assert (sample['total'],sample['fail'],sample['pass'])==(114,65,49)
    assert sample['fail']+sample['pass']==sample['total']
    assert sample['additional_holdout_l5']['total']==15

    split = read_json('reparto-hw8.json')
    assert len(split['development'])==7 and len(split['test'])==5
    assert len(set(split['development']+split['test']))==12

    manual = read_csv('intervenciones-manuales.csv')
    assert len(manual)==4
    assert manual[0]['candidate']=='starting_version'
    assert [r['decision'] for r in manual[1:]]==['revert']*3
    assert [(int(r['passed']),int(r['M6_passed']),int(r['M1_passed'])) for r in manual]==[(2,0,2),(4,3,1),(5,3,2),(4,3,1)]

    search = read_json('busqueda-hw8.json')
    assert search['budget_max']==150
    assert search['budget_used']==sum(int(c['budget_case_calls']) for c in search['candidates'])==14
    assert search['candidates'][-1]['development_passed']==7

    results = read_csv('resultados-test-hw8.csv')
    matrix = read_csv('matriz-test-hw8.csv')
    assert len(results)==4 and len(matrix)==5
    assert set(r['case_id'] for r in matrix)==set(split['test'])
    assert [int(r['passed']) for r in results]==[1,2,1,5]
    assert sum(int(r['total']) for r in results)==20
    assert all(int(r['total'])==5 for r in results)
    for row in results:
        id=row['config_id']
        passes=sum(case['config_'+id]=='Pass' for case in matrix)
        assert passes==int(row['passed'])
        for mode in ['M1','M6']:
            cases=[case for case in matrix if case['mode']==mode]
            assert sum(case['config_'+id]=='Pass' for case in cases)==int(row[mode+'_passed'])
            assert len(cases)==int(row[mode+'_total'])
        actual_cost=float(row['agent_cost_usd'])/5*100
        assert abs(actual_cost-float(row['cost_per_100_conversations_usd']))<0.00001  # original agent_cost_usd rounded to 6 dp

    start=results[2]; final=results[3]
    assert start['model']==final['model']=='gpt-5.6-luna'
    assert (int(start['passed']),int(final['passed']))==(1,5)
    cost_delta=float(final['cost_per_100_conversations_usd'])-float(start['cost_per_100_conversations_usd'])
    assert abs(cost_delta+0.00254)<1e-9

    findings=read_json('hallazgos-editoriales.json')
    assert len(findings['findings'])==2
    assert all(v['status']=='open' for v in findings['findings'])
    assert findings['individually_human_adjudicated_all_traces'] is False
    version=read_json('version-final.json')
    assert version['name']=='s2' and not version['production_approved']

    print('OK: selected data are internally consistent; 4 configurations, 20 test verdicts.')
    print('Same-model comparison: 1/5 -> 5/5; agent cost/100: 0.07284 -> 0.07030 USD.')
    print('CAUTION: this verifies curated evidence, not independent original model runs.')
    return True

if __name__=='__main__':
    verify()
