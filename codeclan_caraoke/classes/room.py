class Room:


    def __init__(self, guest, check_in, check_out):
        self.guest = guest
        self.check_in = check_in
        self.check_out = check_out
        self.guests = []
        self.till = 0
        self.songs = []


    def guest_check_in(self):
        if self.check_in == True:
            return True
        else:
            return

    def guest_check_out(self):
        if self.check_out == True:
            return True
        else:
            return

    def add_song_to_room(self, song):
        self.songs.append(song)
        return self.songs

    def add_guest_to_room(self, guest):
        self.guests.append(guest)
        return self.guests
        
        
    def number_of_guests_in_room(self):
        return len(self.guests)

    def room_is_full(self):
        if len(self.guests) == 3:
            return "room full"

    def charge_customer(self, amount):
        self.till += amount
        # return self.till

    def customer_favourite_song(self, song):
        for songs in self.songs:
            if songs == song:
                return "woop! this is my favourite song"
    
    def remove_guests_from_room(self):
        return self.guests.clear()

