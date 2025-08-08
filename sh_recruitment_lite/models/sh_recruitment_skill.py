from odoo import fields,models


class RecruitmentSkill(models.Model):
    _name="recruitment.skill"
    _description="SH Recruitement Skill"

    name=fields.Char(string="Name of Skill", required=True)