from flask import render_template, request

from config import app, db
from data import jobs
from models import Application, Job


@app.cli.command("seed")
def seed():
    print("Seeding start...")
    try:
        all_jobs = []
        for job in jobs:
            new_job = Job(**job)
            all_jobs.append(new_job)
        db.session.add_all(all_jobs)
        db.session.commit()
        print("Seeding completed...")
        return True
    except (ValueError, TypeError, Exception) as e:
        print(f"Something went wrong while seeding data...{e}")
        return False


@app.get("/")
def home():
    jobs = Job.query.all()
    return render_template("home.html", jobs=jobs)


@app.get("/jobs/<id>")
def job_details(id):
    job = Job.query.get(id)
    if not job:
        return "<p>Unable to find this job.</p>", 404
    return render_template("job_detail.html", job=job)


@app.post("/jobs/<id>/apply")
def apply_to_job(id):
    try:
        job = Job.query.get(id)
        if not job:
            return "<p>Unable to find this job.</p>", 404
        payload = request.form
        application = Application(**payload, job_id=id)
        db.session.add(application)
        db.session.commit()
        return render_template("application_submitted.html", job=job)
    except (ValueError, TypeError, Exception) as e:
        return (
            f"<p>Somthing went wrong while submitting your application: {e}. Please try again later.</p>",
            500,
        )


if __name__ == "__main__":
    with app.app_context():
        db.create_all()

    app.run(port=8000, debug=True)
