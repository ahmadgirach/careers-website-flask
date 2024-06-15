from config import db
from cuid2 import Cuid

class Job(db.Model):
    id = db.Column(db.String(30), primary_key=True, default=Cuid().generate)
    title = db.Column(db.String(20))
    location = db.Column(db.String(100))
    salary = db.Column(db.String(20), nullable=True)
    currency = db.Column(db.String(10))
    responsibilities = db.Column(db.String(1000))
    requirements = db.Column(db.String(1000))
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    updated_at = db.Column(db.DateTime, default=db.func.current_timestamp())

    def __str__(self) -> str:
        return f"{self.title} at {self.location}"


class Application(db.Model):
    id = db.Column(db.String(30), primary_key=True, default=Cuid().generate)
    job_id = db.Column(db.String(30))
    first_name = db.Column(db.String(30))
    last_name = db.Column(db.String(30))
    email = db.Column(db.String(30))
    phone_number = db.Column(db.String(20), nullable=True)
    resume_url = db.Column(db.String(500))
    linkedin_url = db.Column(db.String(500), nullable=True)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    updated_at = db.Column(db.DateTime, default=db.func.current_timestamp())

    def full_name(self) -> str:
        return f"{self.first_name} {self.last_name}"

    def __str__(self) -> str:
        return f"{self.full_name()} applied to '{self.job_id}'"
 