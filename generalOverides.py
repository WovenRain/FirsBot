def fixOutput(response):
  first_line = str(response).partition("\n")[0]
  
  if first_line == "Please try again with a more appropriate inputs.":
    return "... GPT-J didn't like the inputs"
  
  #split up into individual ifs cause im stupid i guess
  if first_line == "" or first_line == None or first_line[0:1] == "??" or first_line[0:1] == "--" or first_line[0:1] == "__" or first_line[0:1] == "!!" or first_line[0:1] == "**": return response 
  #return whole response if weird response - as above
  #full response is a debug thing, 
  #now caught by loop in main
  
  if first_line == "Sorry, the public API is limited to around 20 queries per every 30 minutes.": 
    return "We've run out of queries :confounded:"

  if first_line[0] == "_" or first_line[0] == "~":
    return response
  
  #otherwise send the first line of response
  return first_line