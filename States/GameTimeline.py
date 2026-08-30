from States.TimelineState import CountryTimeline, SeasonSnapshot


class GameTimeline:
    def __init__(self, year=None, season=None):
        self.year = year
        self.season = season
        self.country_timelines = {}

    def add_country_state(self, country, state):
        timeline = self.country_timelines.setdefault(country, CountryTimeline(country))
        timeline.add_snapshot(SeasonSnapshot(state.year, state.season, state))
        return timeline

    def add_season_states(self, year, season, states):
        self.year = year
        self.season = season
        for state in states:
            self.add_country_state(state.country, state)
        return self

    def get_country_timeline(self, country):
        return self.country_timelines.get(country)

    def get_snapshot(self, country, year, season):
        timeline = self.get_country_timeline(country)
        if not timeline:
            return None
        return timeline.get_snapshot(year, season)

    def get_season_summary(self, year, season):
        summary = {}
        for country, timeline in self.country_timelines.items():
            snapshot = timeline.get_snapshot(year, season)
            if snapshot:
                summary[country] = snapshot.country_state
        return summary

    def as_dict(self):
        return {
            "year": self.year,
            "season": self.season,
            "countries": {
                country: timeline.as_dict() for country, timeline in self.country_timelines.items()
            },
        }
