# Engines/FinalPositionEngine.py
class FinalPositionEngine:
    def compute_final_positions(self, movement_orders, retreat_orders):
        final_positions = {}

        # Movement phase
        for country, orders in movement_orders.items():
            for o in orders:
                action = (o.get("action") or "").upper()

                if action in {"BUILD", "DISBAND"}:
                    if o.get("success"):
                        if action == "BUILD":
                            final_positions[o["from"]] = country
                        else:
                            final_positions.pop(o["from"], None)
                    continue

                if o["dislodged"]:
                    continue  # unit must retreat or be destroyed

                if o["success"] and o["to"]:
                    final_positions[o["to"]] = country
                else:
                    final_positions[o["from"]] = country

        # Retreat phase
        for country, orders in retreat_orders.items():
            for o in orders:
                if o["success"] and o["to"]:
                    final_positions[o["to"]] = country
                # failed retreat → destroyed

        return final_positions
