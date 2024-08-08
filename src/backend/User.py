# A Customer using this service
class User:

    def __init__(self, email, name, ba, lat, long, last_alert):
        self._id = email  # Unique identifier for all customers.
        self.name = name
        self.ba = ba
        self.lat = lat
        self.long = long
        self.last_alert = last_alert

    def __eq__(self, other):
        if not isinstance(other, User):
            return NotImplemented

        return (self._id == other._id and
                self.name == other.name and
                self.ba == other.ba and
                self.lat == other.lat and
                self.long == other.long and
                self.last_alert == other.last_alert)
