from odoo import fields,models


class RecruitmentStage(models.Model):
    _name="recruitment.stage"
    _description="SH Recruitement Stage"

    name=fields.Char(string="Recruitement Stage", required=True)