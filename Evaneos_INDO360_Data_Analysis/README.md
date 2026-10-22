# 🌏 Evaneos "Indonesia 360": Booking Data Analysis (Python, pandas)

**Client:** Evaneos, Paris (international travel marketplace), through Wise Steps Consulting
**Role:** Project Assistant / Data Analyst (internship, under senior supervision) · **Year:** 2025
**Tools:** Python, pandas, regex text classification, Excel, Google Colab

## The project

Evaneos works with local travel agencies to sell tailor-made trips, and Indonesia (Bali above all) is one of its fast-growing markets. The INDO360 study helped Evaneos and its partner agencies build sustainability commitments and guidelines around three themes: **overtourism, carbon emissions and a sustainable supply chain**, aligned with the Travelife certification.

My part was the data. Evaneos shared an export of its internal booking database, and I turned it into the quantitative base the consulting team used for the overtourism and carbon analysis.

## What I did

- **Cleaned and structured about 29,000 raw booking records into 16,000+ analysis-ready itinerary-day rows covering about 1,200 trips**, with Python and pandas: messy, multilingual itinerary text, missing values, duplicates and inconsistent spellings.
- **Built a keyword-based destination classifier**: a dictionary of Indonesian destinations and their real-world spellings (for example `Tegalalang`, `Tegallalang`, `Tegalallang`), matched with regex word boundaries across the day title, accommodation, transport and activity fields.
- **Lifted day-level tags to trip level** (`groupby(...).transform('max')`), so every trip knows every destination it visits, even on days that do not mention it.
- **Separated popularity from time spent**: share of trips that visit a destination vs share of real days spent there, which shows where visitor pressure actually concentrates.
- **Measured seasonality**: Bali vs non-Bali trips per season.
- Prepared tables and visuals for the final report. The strategic analysis and recommendations were written by the consulting team.

## Files

| File | What it is |
|---|---|
| [`indo360_destination_analysis.ipynb`](indo360_destination_analysis.ipynb) | The analysis notebook, runnable end to end on a small fictional sample |

To run it on your own itinerary export, set `DATA_PATH` in the first code cell. Expected columns: `trip_id`, `day_index`, `day_title`, `accommodation`, `transport`, `activity`, `destination`, `season`.

## Data and confidentiality

This folder contains **code only**. No Evaneos data, results or findings are published here:

- every cell output from the original notebook is removed;
- the column names are generic, not the client's database schema;
- the sample data in the notebook is fictional (made-up trips such as `T001`);
- the analysis logic is the same as the notebook used in the project; comments are translated to English and one garbled keyword (an encoding error) is fixed.

The scale figures above (records, rows, trips) describe the size of the work, not the client's business results.
