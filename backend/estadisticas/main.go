package main

import (
	"database/sql"
	"fmt"
	"log"
	"net/http"

	"github.com/99designs/gqlgen/graphql/handler"
	"github.com/99designs/gqlgen/graphql/handler/lru"
	"github.com/99designs/gqlgen/graphql/handler/playground"
	"github.com/99designs/gqlgen/graphql/schema"
	_ "github.com/go-sql-driver/mysql"
)

// Configuración de conexión a MariaDB en RDS AWS
const dbUser = "admin"
const dbPass = "password"
const dbHost = "estadisticas.ctomew44ejiz.us-east-1.rds.amazonaws.com"
const dbPort = "3306"
const dbName = "estadisticas"

var db *sql.DB

// Estructura para Reservas
type Reserva struct {
	ID        int    `json:"id"`
	UsuarioID int    `json:"usuario_id"`
	VueloID   int    `json:"vuelo_id"`
	Estado    string `json:"estado"`
}

// Resolver GraphQL
var resolvers = struct {
	Query struct {
		Reservas func() ([]Reserva, error)
	}
}{
	Query: struct {
		Reservas func() ([]Reserva, error)
	}{
		Reservas: func() ([]Reserva, error) {
			rows, err := db.Query("SELECT id_reserva, id_usuario, id_vuelo, estado FROM reservas")
			if err != nil {
				return nil, err
			}
			defer rows.Close()

			var reservas []Reserva
			for rows.Next() {
				var r Reserva
				if err := rows.Scan(&r.ID, &r.UsuarioID, &r.VueloID, &r.Estado); err != nil {
					return nil, err
				}
				reservas = append(reservas, r)
			}
			return reservas, nil
		},
	},
}

// Definir esquema GraphQL en string
const schemaString = `
schema {
    query: Query
}

type Query {
    reservas: [Reserva!]!
}

type Reserva {
    id: ID!
    usuario_id: Int!
    vuelo_id: Int!
    estado: String!
}`

// Función principal
func main() {
	// Conectar a MariaDB
	dsn := fmt.Sprintf("%s:%s@tcp(%s:%s)/%s", dbUser, dbPass, dbHost, dbPort, dbName)
	var err error
	db, err = sql.Open("mysql", dsn)
	if err != nil {
		log.Fatal("❌ Error conectando a MariaDB:", err)
	}
	defer db.Close()

	// Configurar GraphQL
	execSchema := schema.MustParse(schemaString)
	srv := handler.New(execSchema.Exec(resolvers))
	srv.SetQueryCache(lru.New(1000))

	http.Handle("/graphql", srv)
	http.Handle("/", playground.Handler("GraphQL Playground", "/graphql"))

	fmt.Println("🚀 Servidor corriendo en http://localhost:8080/")
	log.Fatal(http.ListenAndServe(":8080", nil))
}
