def fixOutput(response):
  first_line = str(response).partition("\n")[0]
  if first_line == "Please try again with a more appropriate inputs.":
    return "..."
  elif first_line == "" or first_line == None or first_line[0:2] == "???" or first_line[0:2] == "---" or first_line[0:2] == "___" or first_line[0:2] == "!!!" or first_line[0:2] == "***": return response #return whole response if weird response
  #full response is a debug thing
  
  return first_line