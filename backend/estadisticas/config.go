package config

import (
	"database/sql"
	"fmt"
	"log"

	_ "github.com/go-sql-driver/mysql"
)

// Conexión a MariaDB
func ConnectDB() *sql.DB {
	// 📌 Datos de conexión a AWS RDS MariaDB
	dsn := "admin:password@tcp(estadisticas.ctomew44ejiz.us-east-1.rds.amazonaws.com:3306)/estadisticas"
	
	db, err := sql.Open("mysql", dsn)
	if err != nil {
		log.Fatal("❌ Error conectando a MariaDB:", err)
	}

	// Verifica la conexión
	err = db.Ping()
	if err != nil {
		log.Fatal("❌ Error haciendo ping a MariaDB:", err)
	}

	fmt.Println("✅ Conectado a MariaDB en AWS RDS")
	return db
}
