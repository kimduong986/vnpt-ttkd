#========================================
# Scheduler Jobs
#========================================
from apscheduler.schedulers.background import BackgroundScheduler
from pytz import utc
scheduler = BackgroundScheduler()
scheduler.configure(timezone=utc)

# jobs
import scheduler_jobs

scheduler.add_job(scheduler_jobs.update_ioffice, 'interval', days=1)
# scheduler.add_job(scheduler_jobs.free_system_storage, 'interval', hours=3)

scheduler.start()

#========================================