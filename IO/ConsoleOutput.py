class ConsoleOutput:
    """
    Prints forecast results in a clean, readable format.
    """

    def display(self, forecast_results, season_label):
        print(f"Forecast for {season_label}:")
        for country, data in forecast_results.items():
            print(f"  {country}:")
            print(f"    SC: {data['sc']}")
            print(f"    Momentum: {data['momentum']}")
            print(f"    EMA Momentum: {data['ema']}")
            print(f"    CGI: {data['cgi']}")
            print(f"    Projected SCs: {data['projected_scs']}")
            print(f"    Forecast Score: {data['forecast_score']}")
            print(f"    Win Outlook: {data['win_outlook']:.2%}")
            print()  # Blank line for better readability