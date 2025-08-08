{
    'name': 'Recruitement Lite',
    'version': '1.0.0',
    'summary': 'This module will manage job positions and the applications received for them',
    'description': """
    This module if given as Week 1 Exam
    """,
    'author': 'Softhealer Trainee - Raj Muliya',
    'category': 'Hiring System',
    'depends': ['base'],
    'sequence':"1",
    'data': [
        'security/ir.model.access.csv',
        'security/sh_security_groups.xml',
        'security/sh_record_rules.xml',
        'views/sh_recruitment_applicant_view.xml',
        'views/sh_recruitment_job_view.xml',
        'views/sh_recruitment_skill_view.xml',
        'views/sh_recruitment_stage_view.xml',
        'views/menu_view.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
    'license': 'LGPL-3',
}