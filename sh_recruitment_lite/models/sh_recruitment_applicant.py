from odoo import fields,models


class RecruitmentApplicant(models.Model):
    _name="recruitment.applicant"
    _description="SH Recruitement Applicant"

    name=fields.Char(string="Name of Applicant", required=True)
    sh_email=fields.Char(string="Applicant Email")
    sh_job_id=fields.Many2one("recruitment.job", string="Job Position", required=True)
    sh_stage_id=fields.Many2one("recruitment.stage", string="Stage",default=1, required=True)
    sh_applicant_user_id=fields.Many2one("res.users",string="Applicant User id")
    sh_skill_ids=fields.Many2many("recruitment.skill","recruitment_skill_table_rel","user_id","skill_id",string="Skills")
    sh_rejection_reason=fields.Char(string="Rejection Reason")