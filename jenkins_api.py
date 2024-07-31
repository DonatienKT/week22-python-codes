import jenkins
import csv



def listJenkinsJobs(Jenkins_url,Jenkins_username,Jenkins_pass):

    server = jenkins.Jenkins(Jenkins_url, Jenkins_username, Jenkins_pass)
    number_job = server.jobs_count()
    job_name=server.get_all_jobs()

    num_job=server.jobs_count()
    num_nod=server.get_nodes()
    _job=server.get_all_jobs()

#    print(f"The number of jobs is: {num_job}")
    job_list=[]

    for jb in _job:
        job_name=jb.get('name')
        job_url=jb.get('url')
        job_color=jb.get('color')
        job_list.append([job_name, job_url, job_color])
    return job_list


#print("*************")
#print(num_nod)

def storeJenkinsInfo(file_name,job_list):
    with open(file_name, 'w',newline='') as f:
        writer = csv.writer(f)
        HEADER=['Job_name', 'Job_url', 'Job_color']
        writer.writerow(HEADER)
        for j in job_list:
            writer.writerow(j)

def main():
    jobs=listJenkinsJobs('http://54.160.108.55:8080','devops','devops')
    #print(jobs)
    storeJenkinsInfo("week22.csv",jobs)
    print("Successfull generate and upload of file!")

if __name__=="___main___":    
    main()  