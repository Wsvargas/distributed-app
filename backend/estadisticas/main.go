package main

import (
	"database/sql"
	"encoding/json"
	"fmt"
	"log"
	"net/http"
	"time"

	"github.com/go-sql-driver/mysql"
	"github.com/graphql-go/graphql"
	"github.com/graphql-go/handler"
)

// Configuración de la base de datos
var db *sql.DB

func connectDatabase() {
	dsn := "admin:password@tcp(estadisticas.ctomew44ejiz.us-east-1.rds.amazonaws.com:3306)/estadisticas"
	var err error
	db, err = sql.Open("mysql", dsn)
	if err != nil {
		log.Fatalf("❌ Error al conectar a MariaDB: %v", err)
	}
	if err = db.Ping(); err != nil {
		log.Fatalf("❌ No se pudo hacer ping a la base de datos: %v", err)
	}
	log.Println("✅ Conectado a MariaDB en AWS RDS")
}

// Definir modelo de reserva
type Reserva struct {
	IDReserva    int     `json:"id_reserva"`
	IDUsuario    int     `json:"id_usuario"`
	IDVuelo      int     `json:"id_vuelo"`
	FechaReserva string  `json:"fecha_reserva"`
	Estado       string  `json:"estado"`
	TotalPagado  float64 `json:"total_pagado"`
}

// Definir esquema GraphQL
var reservaType = graphql.NewObject(
	graphql.ObjectConfig{
		Name: "Reserva",
		Fields: graphql.Fields{
			"id_reserva":    &graphql.Field{Type: graphql.Int},
			"id_usuario":    &graphql.Field{Type: graphql.Int},
			"id_vuelo":      &graphql.Field{Type: graphql.Int},
			"fecha_reserva": &graphql.Field{Type: graphql.String},
			"estado":        &graphql.Field{Type: graphql.String},
			"total_pagado":  &graphql.Field{Type: graphql.Float},
		},
	},
)

// Definir esquema con Queries y Mutations
var rootQuery = graphql.NewObject(graphql.ObjectConfig{
	Name: "Query",
	Fields: graphql.Fields{
		"obtenerReservasPorUsuario": &graphql.Field{
			Type: graphql.NewList(reservaType),
			Args: graphql.FieldConfigArgument{"id_usuario": &graphql.ArgumentConfig{Type: graphql.Int}},
			Resolve: func(params graphql.ResolveParams) (interface{}, error) {
				idUsuario := params.Args["id_usuario"].(int)
				return obtenerReservasPorUsuario(idUsuario)
			},
		},
	},
})

var rootMutation = graphql.NewObject(graphql.ObjectConfig{
	Name: "Mutation",
	Fields: graphql.Fields{
		"crearReserva": &graphql.Field{
			Type: reservaType,
			Args: graphql.FieldConfigArgument{
				"id_usuario":   &graphql.ArgumentConfig{Type: graphql.Int},
				"id_vuelo":     &graphql.ArgumentConfig{Type: graphql.Int},
				"total_pagado": &graphql.ArgumentConfig{Type: graphql.Float},
			},
			Resolve: func(params graphql.ResolveParams) (interface{}, error) {
				idUsuario := params.Args["id_usuario"].(int)
				idVuelo := params.Args["id_vuelo"].(int)
				totalPagado := params.Args["total_pagado"].(float64)
				return crearReserva(idUsuario, idVuelo, totalPagado)
			},
		},
	},
})

var schema, _ = graphql.NewSchema(graphql.SchemaConfig{
	Query:    rootQuery,
	Mutation: rootMutation,
})

// Función para obtener reservas de un usuario
func obtenerReservasPorUsuario(idUsuario int) ([]Reserva, error) {
	query := "SELECT id_reserva, id_usuario, id_vuelo, fecha_reserva, estado, total_pagado FROM reservas WHERE id_usuario = ?"
	rows, err := db.Query(query, idUsuario)
	if err != nil {
		return nil, err
	}
	defer rows.Close()

	var reservas []Reserva
	for rows.Next() {
		var r Reserva
		err := rows.Scan(&r.IDReserva, &r.IDUsuario, &r.IDVuelo, &r.FechaReserva, &r.Estado, &r.TotalPagado)
		if err != nil {
			return nil, err
		}
		reservas = append(reservas, r)
	}
	return reservas, nil
}

// Función para crear una nueva reserva
func crearReserva(idUsuario, idVuelo int, totalPagado float64) (*Reserva, error) {
	query := "INSERT INTO reservas (id_usuario, id_vuelo, fecha_reserva, estado, total_pagado) VALUES (?, ?, ?, 'confirmada', ?)"
	fecha := time.Now().Format("2006-01-02 15:04:05")
	result, err := db.Exec(query, idUsuario, idVuelo, fecha, totalPagado)
	if err != nil {
		return nil, err
	}

	id, err := result.LastInsertId()
	if err != nil {
		return nil, err
	}

	return &Reserva{IDReserva: int(id), IDUsuario: idUsuario, IDVuelo: idVuelo, FechaReserva: fecha, Estado: "confirmada", TotalPagado: totalPagado}, nil
}

func main() {
	connectDatabase()

	h := handler.New(&handler.Config{
		Schema:   &schema,
		Pretty:   true,
		GraphiQL: true,
	})

	http.Handle("/graphql", h)
	fmt.Println("🚀 Servidor GraphQL corriendo en http://localhost:8080/graphql")
	log.Fatal(http.ListenAndServe(":8080", nil))
}
