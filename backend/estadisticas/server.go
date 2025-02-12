package main

import (
	"database/sql"
	"fmt"
	"log"
	"net/http"
	"strconv"

	"github.com/99designs/gqlgen/graphql/handler"
	"github.com/99designs/gqlgen/graphql/playground"
	_ "github.com/go-sql-driver/mysql"
	"github.com/graphql-go/graphql"
	"your_project/config"
)

var db *sql.DB

// Definir tipo Reserva en GraphQL
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

// Definir consultas GraphQL
var rootQuery = graphql.NewObject(graphql.ObjectConfig{
	Name: "Query",
	Fields: graphql.Fields{
		"reservasPorUsuario": &graphql.Field{
			Type:        graphql.NewList(reservaType),
			Description: "Obtener reservas de un usuario",
			Args: graphql.FieldConfigArgument{
				"id_usuario": &graphql.ArgumentConfig{Type: graphql.Int},
			},
			Resolve: func(params graphql.ResolveParams) (interface{}, error) {
				idUsuario, _ := params.Args["id_usuario"].(int)
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

					reservas = append(reservas, map[string]interface{}{
						"id_reserva":    id_reserva,
						"id_usuario":    id_usuario,
						"id_vuelo":      id_vuelo,
						"fecha_reserva": fecha_reserva,
						"estado":        estado,
						"total_pagado":  total_pagado,
					})
				}
				return reservas, nil
			},
		},
		"totalIngresos": &graphql.Field{
			Type:        graphql.Float,
			Description: "Obtener total de ingresos",
			Resolve: func(params graphql.ResolveParams) (interface{}, error) {
				var total float64
				err := db.QueryRow("SELECT SUM(total_pagado) FROM reservas").Scan(&total)
				if err != nil {
					return nil, err
				}
				return total, nil
			},
		},
	},
})

// Definir el esquema GraphQL
var schema, _ = graphql.NewSchema(graphql.SchemaConfig{Query: rootQuery})

func main() {
	// Conectar a la BD
	db = config.ConnectDB()
	defer db.Close()

	// Iniciar el servidor GraphQL
	http.Handle("/graphql", handler.NewDefaultServer(schema))
	http.Handle("/", playground.Handler("GraphQL Playground", "/graphql"))

	fmt.Println("🚀 Servidor GraphQL corriendo en http://localhost:5006")
	log.Fatal(http.ListenAndServe(":5006", nil))
}
