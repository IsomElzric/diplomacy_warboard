from dashboard_server import build_uploaded_payload

text = '''1906 Fall
Austria
A Alb H  SUCCEEDS
A Bud H  SUCCEEDS
F ION H  SUCCEEDS
A Tyr H  FAILS (Insufficient hold strength)
   Disband  SUCCEEDS
F TYS H  SUCCEEDS

France
A Bur - Mun  SUCCEEDS
A Edi H  SUCCEEDS
F ENG - NTH  FAILS (Attack strength is not greater than the prevent strength)
A Kie H  SUCCEEDS
A Lvp H  SUCCEEDS
F MAO - WES  SUCCEEDS
A Mun - Sil  SUCCEEDS
F NAO - NWG  FAILS (Attack strength is not greater than the defend strength)
F Pic - Bel  SUCCEEDS
A Ruh S Kie  SUCCEEDS
A Ser - Rum  FAILS (Attack strength is not greater than the defend strength)
A War S Mun - Sil  SUCCEEDS
F WES - LYO  SUCCEEDS

Russia
A Ber S Den - Kie  SUCCEEDS
F BLA S Rum  SUCCEEDS
A Boh S Vie - Tyr  SUCCEEDS
A Den - Kie  FAILS (Attack strength is not greater than the defend strength)
F NWG S SKA - NTH  FAILS (Disrupted by attack)
A Nwy H  SUCCEEDS
A Pru - Sil  FAILS (Attack strength is not greater than the prevent strength)
A Rum H  SUCCEEDS
F SKA - NTH  FAILS (Attack strength is not greater than the prevent strength)
A Vie - Tyr  SUCCEEDS

Turkey
F Ank H  SUCCEEDS
A Arm H  SUCCEEDS
A Bul H  SUCCEEDS
A Con H  SUCCEEDS
A Gre H  SUCCEEDS'''

payload = build_uploaded_payload(text, year=1906, season='Fall', mode='season')
print(payload['selectedSeason'])
print(sorted(payload['countries'].keys()))
for country, data in payload['countries'].items():
    cur = data['current']
    print(country, 'sc=', cur.get('sc'), 'units=', cur.get('units'), 'momentum=', cur.get('momentum'), 'ema=', cur.get('ema_momentum'), 'cgi=', cur.get('cgi'))
print('board units', len(payload['board']['units']))
print('scOwners sample', list(payload['board']['scOwners'].items())[:12])
