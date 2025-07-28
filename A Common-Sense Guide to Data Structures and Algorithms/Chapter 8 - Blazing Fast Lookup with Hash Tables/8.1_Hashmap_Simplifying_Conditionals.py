def status_code_meaning(number):
  if number == 200:
    return "OK"
  elif number == 301:
    return "Moved Permanently"
  elif number == 401:
    return "Unauthorized"
  elif number == 404:
    return "Not Found"
  elif number == 500:
    return "Internal Server Error"

# Simplified Below:
STATUS_CODES = {
  200: "OK",
  301: "Moved Permanently",
  401: "Unauthorized",
  404: "Not Found",
  500: "Internal Server Error"
}

def status_code_meaning(number):
	return STATUS_CODES[number]

status_code_meaning(200)