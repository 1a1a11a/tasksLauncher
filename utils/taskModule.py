

import os
import re 

class taskClass:
	def __init__(self, taskname, taskcommand):
		self.taskname = taskname 
		self.taskcommand = taskcommand 

		if isinstance(taskcommand, list):
			self.taskcommand_list = taskcommand
			self.taskcommand_str  = " ".join(taskcommand)
		elif isinstance(taskcommand, str):
			self.taskcommand_list = taskcommand.split()
			self.taskcommand_str  = taskcommand  

		self.executing_nodes = []
		self.submit_time = -1 
		self.last_check_time = -1 
		self.pid = -1
		self.status = "not submit"		# submitted, finished, failed  


		self.RAM_requirement = None 
		self.load_requirement = None 

	def __str__(self):
		return "{}: {}, command: {}, submit time: {}, last check time: {}, "\
					"remote pid: {}, executing nodes: {}".format(
					self.taskname, self.status, self.taskcommand_str, self.submit_time, 
					self.last_check_time, self.pid, self.executing_nodes)

	def __repr__(self):
		return self.__str__() 


def load_task_status(task_status_loc="task.status"):
	""" load task status from task_status_loc, 
		this file is generated by jobSubmitter, 
		this function is used by monitoring service 
		
	Keyword Arguments:
		task_status_loc {str} -- [description] (default: {"task.status"})
	""" 

	task_status_list = []
	if not os.path.exists(task_status_loc): 
		return tast_status_list

	# task1: finished, command: pwd, submit time: -1, last check time: 1502910768.866982, remote pid: -1, executing nodes: []
	regex = re.compile(r"(?P<taskname>.+?): (?P<status>\w+?), command: (?P<command>.+?), "\
							"submit time: (?P<submitTime>-?[0-9.:]+), last check time: (?P<lct>-?[0-9.:]+), "\
							"remote pid: (?P<remotePID>-?\d+), executing nodes: (?P<nodes>.+)")
	with open(task_status_loc) as ifile:
		for line in ifile:
			m = regex.search(line)
			if m:
				task_status = (m.group("taskname"), m.group("status"), 
					m.group("command"), m.group("submitTime"), 
					m.group("lct"), m.group("remotePID"), m.group("nodes"))
				task_status_list.append(task_status)

	return task_status_list 



if __name__ == "__main__":
	get_task_status() 

