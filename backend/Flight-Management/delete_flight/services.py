from models import db_postgres, Flight

def delete_flight_service(flight_id):
    """
    Service to delete a flight by ID
    """
    flight = Flight.query.get(flight_id)
    if not flight:
        return {"error": "Flight not found"}, 404

    try:
        db_postgres.session.delete(flight)
        db_postgres.session.commit()
        return {"message": "Flight deleted successfully"}, 200
    except Exception as e:
        db_postgres.session.rollback()
        return {"error": str(e)}, 500
