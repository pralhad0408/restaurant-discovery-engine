# Restaurant Discovery Engine

A Python command-line application for exploring a curated restaurant dataset using interactive filters. Built as a personal project for the [Boot.dev](https://www.boot.dev/) backend development curriculum.

## Features

The **Discover restaurants** mode lets you:

- Search by cuisine (case-insensitive).
- Set a maximum cost per person.
- Require vegetarian options.
- Combine filters, change selections, and clear filters without restarting.
- View matching restaurants with their location, cuisines, and estimated cost per person.

The menu also includes **Help me decide** and **Surprise me** as placeholders for future development. These modes do not yet provide recommendations.

## Requirements

- Python 3.10 or newer
- `pytest` for running the test suite (not required to use the application)

## Getting started

Clone the repository:

```bash
git clone https://github.com/pralhad0408/restaurant-discovery-engine.git
cd restaurant-discovery-engine
```

Run the application:

```bash
python3 src/main.py
```

On Windows, use `python src/main.py` if `python3` is not available.

The application reads `data/besteats_restaurants_summary.csv` automatically. Keep the `data/` directory in place.

## Example workflow

1. Choose **Discover restaurants** from the main menu.
2. Select a cuisine, such as `Italian`.
3. Optionally set a maximum cost per person and enable vegetarian options.
4. Choose **Show matching restaurants**.
5. Change or clear filters to explore different results.

At least one filter must be active before displaying the restaurant list.

## Running tests

Install the development dependency:

```bash
python3 -m pip install -r requirements.txt
```

Run the tests from the repository root:

```bash
python3 -m pytest -v
```

Tests cover CSV parsing and normalization, filtering logic, and interactive CLI behavior.

## Project structure

```text
restaurant-discovery-engine/
├── data/
│   └── besteats_restaurants_summary.csv
├── src/
│   ├── csv_loader.py
│   ├── discovery.py
│   ├── main.py
│   └── restaurant.py
├── tests/
│   ├── conftest.py
│   ├── test_csv_loader.py
│   ├── test_discovery.py
│   └── test_main.py
├── pytest.ini
├── requirements.txt
└── README.MD
```

## Current scope and future work

The current release implements **Discover restaurants**. Planned features include a guided **Help me decide** recommendation mode and a randomized **Surprise me** mode. Restaurant recommendations and ranking are not implemented yet.

Restaurant details come from the included curated CSV; the application does not fetch live opening hours, menus, or availability.

## License

See [LICENSE](LICENSE).
