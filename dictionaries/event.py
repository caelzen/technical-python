class Event:
	def __init__(self, event_date, event_type, machine_name, user):
		self.event_date = event_date
		self.event_type = event_type
		self.machine_name = machine_name
		self.user = user

events = [
	Event('2020-01-21 12:45:56', 'login', 'myworkstation.local', 'jordan'),
	Event('2020-01-22 15:53:42', 'logout', 'webserver.local', 'jordan'),
	Event('2020-01-21 18:53:21', 'login', 'webserver.local', 'lane'),
	Event('2020-01-22 10:25:34', 'logout', 'myworkstation.local', 'jordan'),
	Event('2020-01-21 08:20:01', 'login', 'webserver.local', 'jordan'),
	Event('2020-01-23 11:24:35', 'logout', 'mailserver.local', 'chris'),
]


def get_event_date(event):
		return event.event_date

def current_users(events):
	events.sort(key=get_event_date)
	machines = {}

	for event in events:
		if event.machine_name not in machines:
			machines[event.machine_name] = set()
		if event.event_type == 'login':
			machines[event.machine_name].add(event.user)
		elif event.event_type == 'logout':
			if event.user in machines[event.machine_name]:
				machines[event.machine_name].remove(event.user)
		
	return machines


def generate_report(machines):
	for machine, users in machines.items():
		if len(users) > 0:
			user_list = ', '.join(users)
			print('{}: {}'.format(machine, user_list))


users = current_users(events)
generate_report(users)


# generate_report(users)