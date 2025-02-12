package main

import (
	"database/sql"
	"fmt"
	"log"
	"net/http"

	"github.com/graphql-go/graphql"
	"github.com/graphql-go/handler"
	_ "github.com/go-sql-driver/mysql"
)

// 📌 Configuración de la base de datos (MariaDB en AWS RDS)
const dbUser = "admin"
const dbPassword = "password"
const dbHost = "estadisticas.ctomew44ejiz.us-east-1.rds.amazonaws.com"
const dbName = "estadisticas"

// 📌 Definir el tipo de datos Reserva
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

// 📌 Definir el esquema GraphQL
var schema, _ = graphql.NewSchema(
	graphql.SchemaConfig{
		Query: graphql.NewObject(
			graphql.ObjectConfig{
				Name: "Query",
				Fields: graphql.Fields{
					"reservas": &graphql.Field{
						Type: graphql.NewList(reservaType),
						Args: graphql.FieldConfigArgument{
							"id_usuario": &graphql.ArgumentConfig{Type: graphql.Int},
						},
						Resolve: func(params graphql.ResolveParams) (interface{}, error) {
							idUsuario, _ := params.Args["id_usuario"].(int)
							return obtenerReservas(idUsuario)
						},
					},
				},
			},
		),
	},
)

// 📌 Función para obtener reservas desde MariaDB
func obtenerReservas(idUsuario int) ([]map[string]interface{}, error) {
	dsn := fmt.Sprintf("%s:%s@tcp(%s)/%s", dbUser, dbPassword, dbHost, dbName)
	db, err := sql.Open("mysql", dsn)
	if err != nil {
		log.Fatal(err)
		return nil, err
	}
	defer db.Close()

	rows, err := db.Query("SELECT * FROM reservas WHERE id_usuario = ?", idUsuario)
	if err != nil {
		return nil, err
	}
	defer rows.Close()

	var reservas []map[string]interface{}
	for rows.Next() {
		var id_reserva, id_usuario, id_vuelo int
		var fecha_reserva, estado string
		var total_pagado float64

		err := rows.Scan(&id_reserva, &id_usuario, &id_vuelo, &fecha_reserva, &estado, &total_pagado)
		if err != nil {
			return nil, err
		}

		reserva := map[string]interface{}{
			"id_reserva":    id_reserva,
			"id_usuario":    id_usuario,
			"id_vuelo":      id_vuelo,
			"fecha_reserva": fecha_reserva,
			"estado":        estado,
			"total_pagado":  total_pagado,
		}
		reservas = append(reservas, reserva)
	}

	return reservas, nil
}

// 📌 Servidor HTTP con GraphQL
func main() {
	h := handler.New(&handler.Config{
		Schema:   &schema,
		GraphiQL: true, // Habilita GraphiQL para pruebas
	})

	http.Handle("/graphql", h)
	fmt.Println("🚀 Servidor corriendo en http://localhost:8080/graphql")
	log.Fatal(http.ListenAndServe(":8080", nil))
}
