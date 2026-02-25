# transport_route/__manifest__.py
{
    "name": "Transport - Routes & Trips",
    "version": "17.0.1.0.0",
    "category": "Transport",
    "summary": "Gestion des lignes, arrêts et voyages planifiés",
    "depends": [
        "base",
        "mail",
        # Décommente si existants dans votre projet:
        # "transport_vehicle",
        # "transport_driver",
    ],
    "data": [
        "security/security.xml",
        "security/ir.model.access.csv",
        "data/sequence.xml",
        "views/route_views.xml",
        "views/trip_views.xml",
        "views/menu.xml",
    ],
    "application": True,
    "license": "LGPL-3",
}