package main

import (
    "database/sql"
    "encoding/json"
    "log"
    "net/http"
    "github.com/gorilla/mux"
    _ "github.com/lib/pq"
)

type Reservation struct {
    ID            int    `json:"id"`
    FlightNumber  string `json:"flight_number"`
    CustomerName  string `json:"customer_name"`
    SeatsReserved int    `json:"seats_reserved"`
    Status        string `json:"status"`
    Date          string `json:"date"`
}

var db *sql.DB

func getReservations(w http.ResponseWriter, r *http.Request) {
    rows, err := db.Query("SELECT id, flight_number, customer_name, seats_reserved, status, date FROM reservations")
    if err != nil {
        http.Error(w, "Failed to retrieve reservations", http.StatusInternalServerError)
        return
    }
    defer rows.Close()

    var reservations []Reservation
    for rows.Next() {
        var res Reservation
        if err := rows.Scan(&res.ID, &res.FlightNumber, &res.CustomerName, &res.SeatsReserved, &res.Status, &res.Date); err != nil {
            http.Error(w, "Failed to scan reservation", http.StatusInternalServerError)
            return
        }
        reservations = append(reservations, res)
    }

    w.Header().Set("Content-Type", "application/json")
    json.NewEncoder(w).Encode(reservations)
}

func main() {
    var err error
    db, err = sql.Open("postgres", "host=localhost port=5432 user=postgres password=postgres dbname=reservations sslmode=disable")
    if err != nil {
        log.Fatal("Failed to connect to database:", err)
    }

    router := mux.NewRouter()
    router.HandleFunc("/history", getReservations).Methods("GET")

    log.Println("History service running on port 3002")
    log.Fatal(http.ListenAndServe(":3002", router))
}
