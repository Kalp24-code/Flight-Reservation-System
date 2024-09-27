import tkinter as tk
from tkinter import messagebox, font
from tkcalendar import DateEntry
from PIL import Image, ImageTk
from fpdf import FPDF


class FlightReservationSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Flight Reservation System")
        self.root.geometry("800x500")
        self.root.config(bg="#2C3E50")

        self.flights = self.load_flights()
        self.bookings = []

        # Load background image
        self.bg_image = Image.open("aeroplane.jpg")  # Ensure the path is correct
        self.bg_image = self.bg_image.resize((800, 500), Image.LANCZOS)
        self.bg_photo = ImageTk.PhotoImage(self.bg_image)

        self.background_label = tk.Label(self.root, image=self.bg_photo)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)

        self.create_widgets()

    def create_widgets(self):
        title_font = font.Font(size=20, weight='bold')
        title_label = tk.Label(self.root, text="Flight Reservation System", font=title_font, bg="#2C3E50", fg="#ffffff")
        title_label.pack(pady=10)

        # Search Flight Frame
        search_frame = tk.Frame(self.root, bg="#ffffff")
        search_frame.pack(pady=10)

        tk.Label(search_frame, text="From:", bg="#ffffff").grid(row=0, column=0, padx=5, pady=5)
        self.from_entry = tk.Entry(search_frame)
        self.from_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(search_frame, text="To:", bg="#ffffff").grid(row=1, column=0, padx=5, pady=5)
        self.to_entry = tk.Entry(search_frame)
        self.to_entry.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(search_frame, text="Date:", bg="#ffffff").grid(row=2, column=0, padx=5, pady=5)
        self.date_entry = DateEntry(search_frame, width=12, background='darkblue', foreground='white', borderwidth=2)
        self.date_entry.grid(row=2, column=1, padx=5, pady=5)

        self.search_button = tk.Button(search_frame, text="Search Flights", command=self.search_flights, bg="#2980B9",
                                       fg="white")
        self.search_button.grid(row=3, columnspan=2, pady=10)

        # Available Flights Frame
        self.flights_frame = tk.Frame(self.root, bg="#2C3E50")
        self.flights_frame.pack(pady=10)

        self.flights_listbox = tk.Listbox(self.flights_frame, width=70, height=10)
        self.flights_listbox.pack(padx=10, pady=10)

        self.book_button = tk.Button(self.flights_frame, text="Book Flight", command=self.book_flight, bg="#27AE60",
                                     fg="white")
        self.book_button.pack(pady=5)

        # View All Scheduled Flights Button
        self.view_all_button = tk.Button(self.root, text="View All Scheduled Flights", command=self.view_all_flights,
                                         bg="#2980B9", fg="white")
        self.view_all_button.pack(pady=5)

        # My Bookings Frame
        self.bookings_frame = tk.Frame(self.root, bg="#2C3E50")
        self.bookings_frame.pack(pady=10)

        self.view_bookings_button = tk.Button(self.bookings_frame, text="View My Bookings", command=self.view_bookings,
                                              bg="#2980B9", fg="white")
        self.view_bookings_button.pack(pady=5)

        # Export Flights as PDF
        self.export_pdf_button = tk.Button(self.root, text="Export Flights to PDF", command=self.export_flights_pdf,
                                           bg="#2980B9", fg="white")
        self.export_pdf_button.pack(pady=5)

    def load_flights(self):
        return [
            {"flight_no": "FL001", "from": "Delhi (DEL)", "to": "Heathrow (LHR, London)", "date": "01/10/2024", "departure": "22:00", "arrival": "05:30 (next day)", "airline": "Air India"},
            {"flight_no": "FL002", "from": "Mumbai (BOM)", "to": "John F. Kennedy (JFK, NYC)", "date": "01/10/2024", "departure": "21:00", "arrival": "06:00 (next day)", "airline": "American Airlines"},
            {"flight_no": "FL003", "from": "Bengaluru (BLR)", "to": "Singapore Changi (SIN)", "date": "01/10/2024", "departure": "23:00", "arrival": "06:00 (next day)", "airline": "Singapore Airlines"},
            {"flight_no": "FL004", "from": "Chennai (MAA)", "to": "Dubai International (DXB)", "date": "01/10/2024", "departure": "22:30", "arrival": "00:30 (next day)", "airline": "Emirates"},
            {"flight_no": "FL005", "from": "Kolkata (CCU)", "to": "Frankfurt (FRA, Germany)", "date": "01/10/2024", "departure": "19:30", "arrival": "23:00", "airline": "Lufthansa"},
            {"flight_no": "FL006", "from": "Hyderabad (HYD)", "to": "Doha Hamad (DOH, Qatar)", "date": "01/10/2024", "departure": "23:10", "arrival": "02:00 (next day)", "airline": "Qatar Airways"},
            {"flight_no": "FL007", "from": "Delhi (DEL)", "to": "Narita (NRT, Tokyo)", "date": "02/10/2024", "departure": "01:00", "arrival": "09:00", "airline": "All Nippon Airways"},
            {"flight_no": "FL008", "from": "Mumbai (BOM)", "to": "Charles de Gaulle (CDG, Paris)", "date": "02/10/2024", "departure": "22:00", "arrival": "06:30 (next day)", "airline": "Air France"},
            {"flight_no": "FL009", "from": "Bengaluru (BLR)", "to": "London Gatwick (LGW)", "date": "02/10/2024", "departure": "22:30", "arrival": "06:00 (next day)", "airline": "British Airways"},
            {"flight_no": "FL010", "from": "Chennai (MAA)", "to": "Kuala Lumpur (KUL)", "date": "02/10/2024", "departure": "21:00", "arrival": "06:00 (next day)", "airline": "Malaysia Airlines"},
            {"flight_no": "FL011", "from": "Kolkata (CCU)", "to": "Hong Kong International (HKG)", "date": "02/10/2024", "departure": "20:30", "arrival": "00:30 (next day)", "airline": "Cathay Pacific"},
            {"flight_no": "FL012", "from": "Hyderabad (HYD)", "to": "Amsterdam Schiphol (AMS)", "date": "02/10/2024", "departure": "22:00", "arrival": "06:00 (next day)", "airline": "KLM"},
            {"flight_no": "FL013", "from": "Delhi (DEL)", "to": "Toronto Pearson (YYZ)", "date": "03/10/2024", "departure": "00:30", "arrival": "07:00", "airline": "Air Canada"},
            {"flight_no": "FL014", "from": "Mumbai (BOM)", "to": "Los Angeles (LAX)", "date": "03/10/2024", "departure": "21:00", "arrival": "14:00 (next day)", "airline": "United Airlines"},
            {"flight_no": "FL015", "from": "Bengaluru (BLR)", "to": "Zurich (ZRH, Switzerland)", "date": "03/10/2024", "departure": "22:00", "arrival": "05:30 (next day)", "airline": "Swiss International Air Lines"},
            {"flight_no": "FL016", "from": "Chennai (MAA)", "to": "San Francisco (SFO)", "date": "03/10/2024", "departure": "20:00", "arrival": "14:00 (next day)", "airline": "United Airlines"},
            {"flight_no": "FL017", "from": "Kolkata (CCU)", "to": "Singapore Changi (SIN)", "date": "03/10/2024", "departure": "21:00", "arrival": "06:00 (next day)", "airline": "Singapore Airlines"},
            {"flight_no": "FL018", "from": "Hyderabad (HYD)", "to": "Jeddah (JED, Saudi Arabia)", "date": "03/10/2024", "departure": "22:30", "arrival": "00:30 (next day)", "airline": "Saudi Airlines"},
            {"flight_no": "FL019", "from": "Delhi (DEL)", "to": "Bangkok (BKK, Thailand)", "date": "04/10/2024", "departure": "01:00", "arrival": "07:00", "airline": "Thai Airways"},
            {"flight_no": "FL020", "from": "Mumbai (BOM)", "to": "Istanbul Airport (IST)", "date": "04/10/2024", "departure": "22:00", "arrival": "06:30 (next day)", "airline": "Turkish Airlines"},
            {"flight_no": "FL021", "from": "Bengaluru (BLR)", "to": "Melbourne (MEL)", "date": "04/10/2024", "departure": "23:00", "arrival": "06:30 (next day)", "airline": "Qantas"},
            {"flight_no": "FL022", "from": "Chennai (MAA)", "to": "Abu Dhabi (AUH)", "date": "04/10/2024", "departure": "21:30", "arrival": "00:00 (next day)", "airline": "Etihad Airways"},
            {"flight_no": "FL023", "from": "Kolkata (CCU)", "to": "Male (MLE, Maldives)", "date": "04/10/2024", "departure": "19:00", "arrival": "21:00", "airline": "Maldivian Airlines"},
            {"flight_no": "FL024", "from": "Hyderabad (HYD)", "to": "Cairo International (CAI)", "date": "04/10/2024", "departure": "22:00", "arrival": "23:30", "airline": "EgyptAir"},
            {"flight_no": "FL025", "from": "Delhi (DEL)", "to": "Sydney Kingsford Smith (SYD)", "date": "05/10/2024", "departure": "01:30", "arrival": "09:30", "airline": "Qantas"},
            {"flight_no": "FL026", "from": "Mumbai (BOM)", "to": "Johannesburg (JNB, South Africa)", "date": "05/10/2024", "departure": "22:30", "arrival": "08:00 (next day)", "airline": "South African Airways"},
            {"flight_no": "FL027", "from": "Bengaluru (BLR)", "to": "Washington Dulles (IAD)", "date": "05/10/2024", "departure": "23:00", "arrival": "06:00 (next day)", "airline": "United Airlines"},
            {"flight_no": "FL028", "from": "Chennai (MAA)", "to": "Frankfurt (FRA)", "date": "05/10/2024", "departure": "21:00", "arrival": "05:30 (next day)", "airline": "Lufthansa"},
            {"flight_no": "FL029", "from": "Kolkata (CCU)", "to": "Brussels Airport (BRU)", "date": "05/10/2024", "departure": "19:30", "arrival": "23:00", "airline": "Brussels Airlines"},
            {"flight_no": "FL030", "from": "Hyderabad (HYD)", "to": "Toronto Pearson (YYZ)", "date": "05/10/2024", "departure": "22:00", "arrival": "06:00 (next day)", "airline": "Air Canada"},
            {"flight_no": "FL031", "from": "Delhi (DEL)", "to": "Los Angeles (LAX)", "date": "06/10/2024", "departure": "01:30", "arrival": "14:00", "airline": "American Airlines"},
            {"flight_no": "FL032", "from": "Mumbai (BOM)", "to": "Vancouver (YVR)", "date": "06/10/2024", "departure": "21:00", "arrival": "06:00 (next day)", "airline": "Air Canada"},
            {"flight_no": "FL033", "from": "Bengaluru (BLR)", "to": "Doha Hamad (DOH)", "date": "06/10/2024", "departure": "22:30", "arrival": "02:00 (next day)", "airline": "Qatar Airways"},
            {"flight_no": "FL034", "from": "Chennai (MAA)", "to": "Singapore Changi (SIN)", "date": "06/10/2024", "departure": "20:00", "arrival": "06:00 (next day)", "airline": "Singapore Airlines"},
            {"flight_no": "FL035", "from": "Kolkata (CCU)", "to": "Dubai International (DXB)", "date": "06/10/2024", "departure": "19:00", "arrival": "00:00 (next day)", "airline": "Emirates"},
            {"flight_no": "FL036", "from": "Hyderabad (HYD)", "to": "Kuala Lumpur (KUL)", "date": "06/10/2024", "departure": "21:30", "arrival": "06:00 (next day)", "airline": "Malaysia Airlines"},
            {"flight_no": "FL037", "from": "Delhi (DEL)", "to": "New York (JFK)", "date": "07/10/2024", "departure": "22:00", "arrival": "05:00 (next day)", "airline": "Delta Airlines"},
            {"flight_no": "FL038", "from": "Mumbai (BOM)", "to": "London Heathrow (LHR)", "date": "07/10/2024", "departure": "21:00", "arrival": "06:30 (next day)", "airline": "British Airways"},
            {"flight_no": "FL039", "from": "Bengaluru (BLR)", "to": "San Francisco (SFO)", "date": "07/10/2024", "departure": "23:00", "arrival": "06:30 (next day)", "airline": "United Airlines"},
            {"flight_no": "FL040", "from": "Chennai (MAA)", "to": "Amsterdam Schiphol (AMS)", "date": "07/10/2024", "departure": "22:00", "arrival": "06:30 (next day)", "airline": "KLM"},
            {"flight_no": "FL041", "from": "Kolkata (CCU)", "to": "Istanbul Airport (IST)", "date": "07/10/2024", "departure": "20:30", "arrival": "00:30 (next day)", "airline": "Turkish Airlines"},
            {"flight_no": "FL042", "from": "Hyderabad (HYD)", "to": "Tokyo Narita (NRT)", "date": "07/10/2024", "departure": "21:30", "arrival": "09:30 (next day)", "airline": "All Nippon Airways"},
            {"flight_no": "FL043", "from": "Delhi (DEL)", "to": "Male (MLE, Maldives)", "date": "08/10/2024", "departure": "00:30", "arrival": "02:00", "airline": "Maldivian Airlines"},
            {"flight_no": "FL044", "from": "Mumbai (BOM)", "to": "Cairo International (CAI)", "date": "08/10/2024", "departure": "22:00", "arrival": "23:30", "airline": "EgyptAir"},
            {"flight_no": "FL045", "from": "Bengaluru (BLR)", "to": "Zurich (ZRH)", "date": "08/10/2024", "departure": "22:00", "arrival": "05:30 (next day)", "airline": "Swiss International"},
            {"flight_no": "FL046", "from": "Chennai (MAA)", "to": "Toronto Pearson (YYZ)", "date": "08/10/2024", "departure": "21:00", "arrival": "07:00 (next day)", "airline": "Air Canada"},
            {"flight_no": "FL047", "from": "Kolkata (CCU)", "to": "Brussels Airport (BRU)", "date": "08/10/2024", "departure": "19:30", "arrival": "23:00", "airline": "Brussels Airlines"},
            {"flight_no": "FL048", "from": "Hyderabad (HYD)", "to": "Washington Dulles (IAD)", "date": "08/10/2024", "departure": "22:00", "arrival": "06:00 (next day)", "airline": "United Airlines"},
            {"flight_no": "FL049", "from": "Delhi (DEL)", "to": "Sydney Kingsford Smith (SYD)", "date": "09/10/2024", "departure": "01:30", "arrival": "09:30", "airline": "Qantas"},
            {"flight_no": "FL050", "from": "Mumbai (BOM)", "to": "Hong Kong International (HKG)", "date": "09/10/2024", "departure": "22:30", "arrival": "05:00 (next day)", "airline": "Cathay Pacific"},
            {"flight_no": "FL051", "from": "Bengaluru (BLR)", "to": "Frankfurt (FRA)", "date": "09/10/2024", "departure": "22:00", "arrival": "05:30 (next day)", "airline": "Lufthansa"},
            {"flight_no": "FL052", "from": "Chennai (MAA)", "to": "Dubai International (DXB)", "date": "09/10/2024", "departure": "21:00", "arrival": "00:00 (next day)", "airline": "Emirates"},
            {"flight_no": "FL053", "from": "Kolkata (CCU)", "to": "Doha Hamad (DOH)", "date": "09/10/2024", "departure": "20:30", "arrival": "00:00 (next day)", "airline": "Qatar Airways"},
            {"flight_no": "FL054", "from": "Hyderabad (HYD)", "to": "Singapore Changi (SIN)", "date": "09/10/2024", "departure": "22:30", "arrival": "06:00 (next day)", "airline": "Singapore Airlines"},
            {"flight_no": "FL055", "from": "Delhi (DEL)", "to": "Bangkok (BKK)", "date": "10/10/2024", "departure": "01:00", "arrival": "07:00", "airline": "Thai Airways"},
            {"flight_no": "FL056", "from": "Mumbai (BOM)", "to": "New York (JFK)", "date": "10/10/2024", "departure": "22:00", "arrival": "05:00 (next day)", "airline": "American Airlines"},
            {"flight_no": "FL057", "from": "Bengaluru (BLR)", "to": "London Heathrow (LHR)", "date": "10/10/2024", "departure": "21:30", "arrival": "06:30 (next day)", "airline": "British Airways"},
            {"flight_no": "FL058", "from": "Chennai (MAA)", "to": "Amsterdam Schiphol (AMS)", "date": "10/10/2024", "departure": "20:30", "arrival": "06:30 (next day)", "airline": "KLM"},
            {"flight_no": "FL059", "from": "Kolkata (CCU)", "to": "Singapore Changi (SIN)", "date": "10/10/2024", "departure": "19:00", "arrival": "00:30 (next day)", "airline": "Singapore Airlines"},
            {"flight_no": "FL060", "from": "Hyderabad (HYD)", "to": "Toronto Pearson (YYZ)", "date": "10/10/2024", "departure": "22:00", "arrival": "06:00 (next day)", "airline": "Air Canada"},
            {"flight_no": "FL061", "from": "Delhi (DEL)", "to": "Zurich (ZRH)", "date": "11/10/2024", "departure": "00:30", "arrival": "07:00", "airline": "Swiss International"},
            {"flight_no": "FL062", "from": "Mumbai (BOM)", "to": "Los Angeles (LAX)", "date": "11/10/2024", "departure": "22:00", "arrival": "14:00 (next day)", "airline": "United Airlines"},
            {"flight_no": "FL063", "from": "Bengaluru (BLR)", "to": "Doha Hamad (DOH)", "date": "11/10/2024", "departure": "22:30", "arrival": "02:00 (next day)", "airline": "Qatar Airways"},
            {"flight_no": "FL064", "from": "Chennai (MAA)", "to": "San Francisco (SFO)", "date": "11/10/2024", "departure": "21:00", "arrival": "14:00 (next day)", "airline": "United Airlines"},
            {"flight_no": "FL065", "from": "Kolkata (CCU)", "to": "Dubai International (DXB)", "date": "11/10/2024", "departure": "19:30", "arrival": "00:00 (next day)", "airline": "Emirates"},
            {"flight_no": "FL066", "from": "Hyderabad (HYD)", "to": "Frankfurt (FRA)", "date": "11/10/2024", "departure": "22:00", "arrival": "05:30 (next day)", "airline": "Lufthansa"},
            {"flight_no": "FL067", "from": "Delhi (DEL)", "to": "Melbourne (MEL)", "date": "12/10/2024", "departure": "01:30", "arrival": "09:30", "airline": "Qantas"},
            {"flight_no": "FL068", "from": "Mumbai (BOM)", "to": "Brussels Airport (BRU)", "date": "12/10/2024", "departure": "22:00", "arrival": "05:30 (next day)", "airline": "Brussels Airlines"},
            {"flight_no": "FL069", "from": "Bengaluru (BLR)", "to": "Jeddah (JED, Saudi Arabia)", "date": "12/10/2024", "departure": "22:30", "arrival": "00:30 (next day)", "airline": "Saudi Airlines"},
            {"flight_no": "FL070", "from": "Chennai (MAA)", "to": "Toronto Pearson (YYZ)", "date": "12/10/2024", "departure": "21:00", "arrival": "07:00 (next day)", "airline": "Air Canada"},
            {"flight_no": "FL071", "from": "Kolkata (CCU)", "to": "Cairo International (CAI)", "date": "12/10/2024", "departure": "19:00", "arrival": "23:00", "airline": "EgyptAir"},
            {"flight_no": "FL072", "from": "Hyderabad (HYD)", "to": "Amsterdam Schiphol (AMS)", "date": "12/10/2024", "departure": "22:00", "arrival": "06:00 (next day)", "airline": "KLM"},
            {"flight_no": "FL073", "from": "Delhi (DEL)", "to": "Hong Kong International (HKG)", "date": "13/10/2024", "departure": "01:00", "arrival": "06:00", "airline": "Cathay Pacific"},
            {"flight_no": "FL074", "from": "Mumbai (BOM)", "to": "New York (JFK)", "date": "13/10/2024", "departure": "22:00", "arrival": "05:00 (next day)", "airline": "Delta Airlines"},
            {"flight_no": "FL075", "from": "Bengaluru (BLR)", "to": "London Heathrow (LHR)", "date": "13/10/2024", "departure": "21:30", "arrival": "06:30 (next day)", "airline": "British Airways"},
            {"flight_no": "FL076", "from": "Chennai (MAA)", "to": "Frankfurt (FRA)", "date": "13/10/2024", "departure": "20:30", "arrival": "05:30 (next day)", "airline": "Lufthansa"},
            {"flight_no": "FL077", "from": "Kolkata (CCU)", "to": "Dubai International (DXB)", "date": "13/10/2024", "departure": "19:30", "arrival": "00:00 (next day)", "airline": "Emirates"},
            {"flight_no": "FL078", "from": "Hyderabad (HYD)", "to": "Toronto Pearson (YYZ)", "date": "13/10/2024", "departure": "22:00", "arrival": "06:00 (next day)", "airline": "Air Canada"},
            {"flight_no": "FL079", "from": "Delhi (DEL)", "to": "Abu Dhabi (AUH)", "date": "14/10/2024", "departure": "00:30", "arrival": "02:00", "airline": "Etihad Airways"},
            {"flight_no": "FL080", "from": "Mumbai (BOM)", "to": "Cairo International (CAI)", "date": "14/10/2024", "departure": "22:00", "arrival": "23:30", "airline": "EgyptAir"},
            {"flight_no": "FL081", "from": "Bengaluru (BLR)", "to": "Singapore Changi (SIN)", "date": "14/10/2024", "departure": "22:30", "arrival": "06:00 (next day)", "airline": "Singapore Airlines"},
            {"flight_no": "FL082", "from": "Chennai (MAA)", "to": "Jeddah (JED)", "date": "14/10/2024", "departure": "21:00", "arrival": "00:00 (next day)", "airline": "Saudi Airlines"},
            {"flight_no": "FL083", "from": "Kolkata (CCU)", "to": "Zurich (ZRH)", "date": "14/10/2024", "departure": "19:00", "arrival": "05:30 (next day)", "airline": "Swiss International"},
            {"flight_no": "FL084", "from": "Hyderabad (HYD)", "to": "Amsterdam Schiphol (AMS)", "date": "14/10/2024", "departure": "22:00", "arrival": "06:00 (next day)", "airline": "KLM"},
            {"flight_no": "FL085", "from": "Delhi (DEL)", "to": "Bangkok (BKK)", "date": "15/10/2024", "departure": "01:00", "arrival": "07:00", "airline": "Thai Airways"},
            {"flight_no": "FL086", "from": "Mumbai (BOM)", "to": "Toronto Pearson (YYZ)", "date": "15/10/2024", "departure": "22:00", "arrival": "07:00 (next day)", "airline": "Air Canada"},
            {"flight_no": "FL087", "from": "Bengaluru (BLR)", "to": "San Francisco (SFO)", "date": "15/10/2024", "departure": "22:30", "arrival": "14:00 (next day)", "airline": "United Airlines"},
            {"flight_no": "FL088", "from": "Chennai (MAA)", "to": "Los Angeles (LAX)", "date": "15/10/2024", "departure": "20:00", "arrival": "14:00 (next day)", "airline": "American Airlines"},
            {"flight_no": "FL089", "from": "Kolkata (CCU)", "to": "Hong Kong International (HKG)", "date": "15/10/2024", "departure": "19:30", "arrival": "00:00 (next day)", "airline": "Cathay Pacific"},
            {"flight_no": "FL090", "from": "Hyderabad (HYD)", "to": "Frankfurt (FRA)", "date": "15/10/2024", "departure": "22:00", "arrival": "05:30 (next day)", "airline": "Lufthansa"},
            {"flight_no": "FL091", "from": "Delhi (DEL)", "to": "Sydney (SYD)", "date": "16/10/2024", "departure": "01:30", "arrival": "09:30", "airline": "Qantas"},
            {"flight_no": "FL092", "from": "Mumbai (BOM)", "to": "Melbourne (MEL)", "date": "16/10/2024", "departure": "22:00", "arrival": "06:30 (next day)", "airline": "Qantas"},
            {"flight_no": "FL093", "from": "Bengaluru (BLR)", "to": "Doha (DOH)", "date": "16/10/2024", "departure": "22:30", "arrival": "02:00 (next day)", "airline": "Qatar Airways"},
            {"flight_no": "FL094", "from": "Chennai (MAA)", "to": "Toronto (YYZ)", "date": "16/10/2024", "departure": "21:00", "arrival": "07:00 (next day)", "airline": "Air Canada"},
            {"flight_no": "FL095", "from": "Kolkata (CCU)", "to": "Brussels (BRU)", "date": "16/10/2024", "departure": "20:30", "arrival": "06:30 (next day)", "airline": "Brussels Airlines"},
            {"flight_no": "FL096", "from": "Hyderabad (HYD)", "to": "London (LHR)", "date": "16/10/2024", "departure": "22:00", "arrival": "06:30 (next day)", "airline": "British Airways"},
            {"flight_no": "FL097", "from": "Delhi (DEL)", "to": "Abu Dhabi (AUH)", "date": "17/10/2024", "departure": "00:30", "arrival": "02:00", "airline": "Etihad Airways"},
            {"flight_no": "FL098", "from": "Mumbai (BOM)", "to": "Frankfurt (FRA)", "date": "17/10/2024", "departure": "22:00", "arrival": "05:30 (next day)", "airline": "Lufthansa"},
            {"flight_no": "FL099", "from": "Bengaluru (BLR)", "to": "Cairo (CAI)", "date": "17/10/2024", "departure": "22:30", "arrival": "00:00 (next day)", "airline": "EgyptAir"},
            {"flight_no": "FL100", "from": "Chennai (MAA)", "to": "New York (JFK)", "date": "17/10/2024", "departure": "20:00", "arrival": "05:00 (next day)", "airline": "Delta Airlines"}
        ]

    def search_flights(self):
        from_city = self.from_entry.get().strip()
        to_city = self.to_entry.get().strip()
        date = self.date_entry.get()

        self.flights_listbox.delete(0, tk.END)

        matches = [
            flight for flight in self.flights
            if (flight["from"].lower() == from_city.lower() and
                flight["to"].lower() == to_city.lower() and
                flight["date"] == date)
        ]

        if matches:
            for flight in matches:
                self.flights_listbox.insert(tk.END,
                                            f"{flight['flight_no']} | {flight['from']} -> {flight['to']} | {flight['date']} | {flight['departure']} | {flight['arrival']} | {flight['airline']}")
        else:
            messagebox.showinfo("No Flights Found", "No flights found for the selected date.")
            self.show_alternative_flights(from_city, to_city)

    def view_all_flights(self):
        self.flights_listbox.delete(0, tk.END)
        for flight in self.flights:
            self.flights_listbox.insert(tk.END,
                                        f"{flight['flight_no']} | {flight['from']} -> {flight['to']} | {flight['date']} | {flight['departure']} | {flight['arrival']} | {flight['airline']}")

    def show_alternative_flights(self, from_city, to_city):
        alternatives = [
            flight for flight in self.flights
            if (flight["from"].lower() == from_city.lower() and
                flight["to"].lower() == to_city.lower())
        ]

        if alternatives:
            alternative_msg = "Available flights on other dates:\n"
            for flight in alternatives:
                alternative_msg += f"{flight['flight_no']} | {flight['from']} -> {flight['to']} | {flight['date']} | {flight['departure']} | {flight['arrival']} | {flight['airline']}\n"
            messagebox.showinfo("Alternative Flights", alternative_msg)
        else:
            messagebox.showinfo("No Flights", "No flights found for the selected route.")

    def book_flight(self):
        selected_flight = self.flights_listbox.curselection()
        if selected_flight:
            flight_info = self.flights_listbox.get(selected_flight)
            self.bookings.append(flight_info)
            messagebox.showinfo("Success", "Flight booked successfully!")
        else:
            messagebox.showwarning("Selection Error", "Please select a flight to book.")

    def view_bookings(self):
        if self.bookings:
            bookings_info = "\n".join(self.bookings)
            messagebox.showinfo("My Bookings", bookings_info)
        else:
            messagebox.showinfo("My Bookings", "No bookings found.")

    def export_flights_pdf(self):
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)

        # Title
        pdf.cell(200, 10, txt="Scheduled Flights", ln=True, align="C")

        # Add flight data
        for flight in self.flights:
            flight_info = f"{flight['flight_no']} | {flight['from']} -> {flight['to']} | {flight['date']} | {flight['departure']} | {flight['arrival']} | {flight['airline']}"
            pdf.cell(200, 10, txt=flight_info, ln=True)

        pdf.output("Scheduled_Flights.pdf")
        messagebox.showinfo("Success", "Flights exported to PDF successfully!")


if __name__ == "__main__":
    root = tk.Tk()
    app = FlightReservationSystem(root)
    root.mainloop()
