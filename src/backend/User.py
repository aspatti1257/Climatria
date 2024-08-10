# A Customer using this service
class User:

    def __init__(self, email, name, phone_number, ba, lat, long, last_alert):
        self._id = email  # Unique identifier for all customers. Not a protected field, but a unique key for Mongo.
        self.name = name
        self.phone_number = phone_number
        self.ba = ba
        self.lat = lat
        self.long = long
        self.last_alert = last_alert

    def __eq__(self, other):
        if not isinstance(other, User):
            return NotImplemented

        return (self._id == other._id and
                self.name == other.name and
                self.phone_number == other.phone_number and
                self.ba == other.ba and
                self.lat == other.lat and
                self.long == other.long and
                self.last_alert == other.last_alert)

    def get_id(self):
        return self._id
