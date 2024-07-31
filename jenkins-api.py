import jenkins

Jenkins_url='http://54.160.108.55:8080'
Jenkins_username='devops'
Jenkins_pass='devops'

server = jenkins.Jenkins(Jenkins_url, Jenkins_username, Jenkins_pass)
number_job = server.jobs_count()
job_name=server.get_all_jobs()
#list_job = server.get
user=server.get_whoami()
_jobs=server.get_jobs()

print(number_job)
print(job_name)
print("************************************")
print(user)

for job in _jobs:
    print("**********************************************")
    print(job["name"])
