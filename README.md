# FedRateCalc open data

U.S. federal rate, calendar, holiday, wage, sales tax and electricity price data in CSV, JSON and ICS, mirrored from the [FedRateCalc open data hub](https://fedratecalc.com/data/). Each dataset is generated from official sources (Federal Reserve Board, BLS, BEA, OPM, EIA, state labor and tax departments) and checked on the date shown on its page.

Synced from https://fedratecalc.com/data/ on 2026-11-15. The website is the canonical, most current copy; this repository is a convenience mirror.

## Datasets

| Dataset | Files | Updated | Page |
| --- | --- | --- | --- |
| Electricity rates by state (EIA Table 5.6.A) | [`electricity-rates-by-state.csv`](data/electricity-rates-by-state.csv), [`electricity-rates-by-state.json`](data/electricity-rates-by-state.json) | 2026-11-05 | [fedratecalc.com/data/electricity-rates-by-state/](https://fedratecalc.com/data/electricity-rates-by-state/) |
| FOMC meeting dates 2026-2027 | [`fomc-meetings-2026-2027.csv`](data/fomc-meetings-2026-2027.csv), [`fomc-meetings-2026-2027.json`](data/fomc-meetings-2026-2027.json), [`fomc-meetings-2026-2027.ics`](data/fomc-meetings-2026-2027.ics) | 2026-11-05 | [fedratecalc.com/data/fomc-meetings-2026-2027/](https://fedratecalc.com/data/fomc-meetings-2026-2027/) |
| FOMC rate decisions 2025-2026 | [`fomc-decisions.csv`](data/fomc-decisions.csv), [`fomc-decisions.json`](data/fomc-decisions.json) | 2026-11-05 | [fedratecalc.com/data/fomc-decisions/](https://fedratecalc.com/data/fomc-decisions/) |
| Federal funds target rate and range changes since 1990 | [`fed-funds-target-range-history.csv`](data/fed-funds-target-range-history.csv), [`fed-funds-target-range-history.json`](data/fed-funds-target-range-history.json) | 2026-11-05 | [fedratecalc.com/data/fed-funds-target-range-history/](https://fedratecalc.com/data/fed-funds-target-range-history/) |
| State minimum wage rates 2026-2027 | [`state-minimum-wage-2026-2027.csv`](data/state-minimum-wage-2026-2027.csv), [`state-minimum-wage-2026-2027.json`](data/state-minimum-wage-2026-2027.json) | 2026-11-05 | [fedratecalc.com/data/state-minimum-wage-2026-2027/](https://fedratecalc.com/data/state-minimum-wage-2026-2027/) |
| State sales tax rates by state | [`state-sales-tax-rates.csv`](data/state-sales-tax-rates.csv), [`state-sales-tax-rates.json`](data/state-sales-tax-rates.json) | 2026-11-05 | [fedratecalc.com/data/state-sales-tax-rates/](https://fedratecalc.com/data/state-sales-tax-rates/) |
| U.S. economic data release calendar 2026 | [`us-economic-release-calendar-2026.csv`](data/us-economic-release-calendar-2026.csv), [`us-economic-release-calendar-2026.ics`](data/us-economic-release-calendar-2026.ics) | 2026-11-05 | [fedratecalc.com/data/us-economic-release-calendar-2026/](https://fedratecalc.com/data/us-economic-release-calendar-2026/) |
| U.S. federal holidays 2026-2028 with observed dates | [`us-federal-holidays-2026-2028.csv`](data/us-federal-holidays-2026-2028.csv), [`us-federal-holidays-2026-2028.json`](data/us-federal-holidays-2026-2028.json), [`us-federal-holidays-2026-2028.ics`](data/us-federal-holidays-2026-2028.ics) | 2026-11-05 | [fedratecalc.com/data/us-federal-holidays-2026-2028/](https://fedratecalc.com/data/us-federal-holidays-2026-2028/) |

## License and citation

The compiled datasets are licensed under [CC BY 4.0](LICENSE): credit **FedRateCalc** with a link to https://fedratecalc.com/data/. The underlying U.S. government figures are in the public domain.

Suggested citation: FedRateCalc. *<dataset name>*. https://fedratecalc.com/data/ (accessed <date>).

GitHub shows a "Cite this repository" button from [CITATION.cff](CITATION.cff).

## Updates

Files are refreshed from the website when the underlying data changes (for example after an FOMC meeting or a new release calendar, a state sales tax rate, or a new EIA electricity price month). Corrections: open an issue, or see the source links on each dataset page.
