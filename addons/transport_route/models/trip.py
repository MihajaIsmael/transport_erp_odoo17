# transport_route/models/trip.py
from odoo import api, fields, models
from odoo.exceptions import ValidationError


class TransportTrip(models.Model):
    _name = "transport.trip"
    _description = "Transport Trip"
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _order = "departure_datetime desc"

    name = fields.Char(copy=False, readonly=True, default="New", index=True)
    active = fields.Boolean(default=True)

    route_id = fields.Many2one("transport.route", required=True, tracking=True)
    departure_datetime = fields.Datetime(required=True, tracking=True)
    arrival_datetime = fields.Datetime(tracking=True)

    capacity = fields.Integer(default=0, tracking=True)
    reserved_seats = fields.Integer(default=0, tracking=True)
    available_seats = fields.Integer(compute="_compute_available_seats", store=True)

    state = fields.Selection(
        [
            ("draft", "Draft"),
            ("confirmed", "Confirmed"),
            ("in_progress", "In progress"),
            ("done", "Done"),
            ("cancelled", "Cancelled"),
        ],
        default="draft",
        tracking=True,
    )

    # Préparation intégration (à activer quand vos modules existent)
    vehicle_id = fields.Many2one(
        "transport.vehicle",
        string="Vehicle",
        tracking=True,
        # commente si le modèle n'existe pas encore
    )
    driver_id = fields.Many2one(
        "transport.driver",
        string="Driver",
        tracking=True,
        # commente si le modèle n'existe pas encore
    )

    @api.depends("capacity", "reserved_seats")
    def _compute_available_seats(self):
        for rec in self:
            rec.available_seats = max(rec.capacity - rec.reserved_seats, 0)

    @api.constrains("capacity", "reserved_seats")
    def _check_capacity(self):
        for rec in self:
            if rec.capacity < 0:
                raise ValidationError("Capacity cannot be negative.")
            if rec.reserved_seats < 0:
                raise ValidationError("Reserved seats cannot be negative.")
            if rec.reserved_seats > rec.capacity:
                raise ValidationError("Reserved seats cannot exceed capacity.")

    @api.constrains("departure_datetime", "arrival_datetime")
    def _check_dates(self):
        for rec in self:
            if rec.arrival_datetime and rec.departure_datetime and rec.arrival_datetime <= rec.departure_datetime:
                raise ValidationError("Arrival must be after departure.")

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if vals.get("name", "New") == "New":
                vals["name"] = self.env["ir.sequence"].next_by_code("transport.trip") or "TRIP"
        return super().create(vals_list)

    # Actions workflow simples
    def action_confirm(self):
        self.write({"state": "confirmed"})

    def action_start(self):
        self.write({"state": "in_progress"})

    def action_done(self):
        self.write({"state": "done"})

    def action_cancel(self):
        self.write({"state": "cancelled"})

    def action_set_draft(self):
        self.write({"state": "draft"})