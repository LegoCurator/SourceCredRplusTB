import re 
    
filename = './ledger.json'

file = open(filename, 'r')
content = file.read()

# A sample text string where regular expression  
# is searched. 
string = """Hello my Number is 123456789 and 
             my friend's 
             "identityId":"8MoKPdxW4KnbvcolEDtYmYiJXQ"
             "identityId":"8MoKPdxW4KnbvcolEDtYmYiJXQ"
             "identityId":"8MoKPdxW4KnbvcolEDtYmYiJXQ"
             "identityId":"8MoKPdxW4KnbvcolEDtYmYiJXQ"
             "identityId":"8MoKPdxW4KnbvcolEDtYmYiJXQ"
             number is 987654321"""
    
# A sample regular expression to find digits. 
regex = '"identityId":"([A-Za-z0-9]*)"'             
    
matches = re.findall(regex, content) 

with open('./ledger.json', 'a') as file:
    for id in matches:
        file.write("""{"action":{"identityId":\""""+id+"""\","type":"TOGGLE_ACTIVATION"},"ledgerTimestamp":1673277677460,"uuid":"UNRJ5F9vj2TdBq0wYxRFEQ","version":"1"}""" + " \n")