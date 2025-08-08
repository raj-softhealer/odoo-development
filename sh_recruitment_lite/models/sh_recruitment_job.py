from odoo import fields,models


class RecruitmentJob(models.Model):
    _name="recruitment.job"
    _description="SH Recruitement Job"

    name=fields.Char(string="Job Position", required=True)
    sh_hiring_manager_id=fields.Many2one("res.users", string="Responsible", domain="[('groups_id', '=', 29)]")
    sh_state=fields.Selection([
        ("draft","Draft"),
        ("open","Open"),
        ("closed","Closed"),
    ], string="Position Status")

    sh_applicant_ids=fields.One2many("recruitment.applicant","sh_job_id",string="Applicant Name ")
    