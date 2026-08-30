class SeasonSnapshot:
    def __init__(self, year, season, country_state):
        self.year = year
        self.season = season
        self.country_state = country_state


class CountryTimeline:
    def __init__(self, country):
        self.country = country
        self.snapshots = []
        self._snapshot_index = {}

    def add_snapshot(self, snapshot):
        self.snapshots.append(snapshot)
        key = (snapshot.year, snapshot.season)
        self._snapshot_index[key] = snapshot

    def get_snapshot(self, year, season):
        return self._snapshot_index.get((year, season))

    def metric_history(self, metric_name):
        values = []
        for snapshot in self.snapshots:
            state = snapshot.country_state
            if hasattr(state, metric_name):
                values.append(getattr(state, metric_name))
        return values

    def front_count(self):
        if not self.snapshots:
            return 0
        latest = self.snapshots[-1].country_state
        return getattr(latest, "active_fronts", 0)

    def last_state(self):
        return self.snapshots[-1].country_state if self.snapshots else None

    def as_dict(self):
        return {
            "country": self.country,
            "snapshots": [
                {
                    "year": snapshot.year,
                    "season": snapshot.season,
                    "state": snapshot.country_state.__dict__.copy(),
                }
                for snapshot in self.snapshots
            ],
        }
