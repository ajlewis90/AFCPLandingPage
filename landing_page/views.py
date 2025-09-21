from django.shortcuts import render
from django.conf import settings
import requests, json
from django.http import JsonResponse
# from signup.forms import ThankyouForm

def display_landing_page(request):
	context = dict()
	return render(request, 'afcp_landing_page.html', context)

def display_b2b_signup_page(request):
	context = dict()
	context['business_sign_up'] = True
	return render(request, 'b2b_signup_page.html', context)	


LOOPS_ENDPOINT = "https://app.loops.so/api/v1/contacts"

def add_contact(request):
	if request.method == "POST" and request.headers.get("X-Requested-With") == "XMLHttpRequest":
		response_data = dict()
		contact_name = request.POST.get('contact_name', '')
		contact_email = request.POST.get('contact_email', '')

		print("Contact name:")
		print(contact_name)
		print(contact_email)
		print("......")

		loops_contact_creation_url = LOOPS_ENDPOINT + "/create"

		headers = {
			"Authorization": f"Bearer {settings.LOOP_API_KEY}",
			"Content-Type": "application/json",
		}

		payload = {
			"email": contact_email,
			"firstName": contact_name,
			"mailingLists": {
				"cmc11am8j08xd0i2o4rk61iv6": True
			}

			#"custom_attributes": {}
		}

		print(payload)

	try:
		response = requests.post(loops_contact_creation_url, json=payload, headers=headers)
		print("RESPONSE STATUS CODE HERE")
		print(response.status_code)    

		if response.status_code == 200:
			print(f"✅ Contact {contact_email} added successfully!")
			response_data = {
				"success": True,
				# Think of using reverse with arguments here
				"message": 'You have been added to our mailing list. You will receive an email from us soon!',
				# "redirect_url": settings.USER_SVC_URL + 'thank-you/'
			}        
		else:
			print(f"❌ Failed to add contact: {response.text}")
			print(response) #Log this using kibana or some monitoring tool
			print(response.text)
			response_data = {
				"success": False,
				"message": 'Oops! Something unexpected happened while sending your details. Please try again after a few minutes or directly email support',		
			}				
	except Exception as e:
		print(e) #Log this using kibana or some other monitoring tool
		response_data = {
			"success": False,
			"message": 'Oops! Something unexpected happened while sending your details. Please try again after a few minutes or directly email support',		
		}			
		return JsonResponse(response_data)	        

	return JsonResponse(response_data)

def add_business_contact(request):
	if request.method == "POST" and request.headers.get("X-Requested-With") == "XMLHttpRequest":
		response_data = dict()
		business_name = request.POST.get('business_name', '')
		business_email = request.POST.get('business_email', '')		
		contact_person_name = request.POST.get('contact_person_name', '')
		contact_number = str(request.POST.get('contact_number', ''))
		business_address = request.POST.get('business_address', '')
		business_city = request.POST.get('business_city', '')
		business_pincode = request.POST.get('business_pincode', '')		

		print("Business name:")
		print(business_name)
		print(business_email)
		print("......")

		loops_contact_creation_url = LOOPS_ENDPOINT + "/create"

		headers = {
			"Authorization": f"Bearer {settings.LOOP_API_KEY}",
			"Content-Type": "application/json",
		}

		payload = {
			"email": business_email,
			"businessEmail": business_email,
			"businessName": business_name,
			"firstName": contact_person_name,
			"contactNumber": contact_number,
			"businessAddress": business_address,
			"businessCity": business_city,
			"businessPincode": business_pincode,

			"mailingLists": {
				"cmbzy0u0m36gm0jy786l702kf": True
			}			
			#"custom_attributes": {}
		}

		print(payload)

	try:
		response = requests.post(loops_contact_creation_url, json=payload, headers=headers)
		print("RESPONSE STATUS CODE HERE")
		print(response.status_code)    

		if response.status_code == 200:
			print(f"✅ Contact {business_email} added successfully!")
			response_data = {
				"success": True,
				# Think of using reverse with arguments here
				"message": 'You have been added to our mailing list. You will receive an email from us soon!',
				# "redirect_url": settings.USER_SVC_URL + 'thank-you/'
			}        
		else:
			print(f"❌ Failed to add contact: {response.text}")
			print(response) #Log this using kibana or some monitoring tool
			print(response.text)
			response_data = {
				"success": False,
				"message": 'Oops! Something unexpected happened while sending your details. Please try again after a few minutes or directly email support',		
			}				
	except Exception as e:
		print(e) #Log this using kibana or some other monitoring tool
		response_data = {
			"success": False,
			"message": 'Oops! Something unexpected happened while sending your details. Please try again after a few minutes or directly email support',		
		}			
		return JsonResponse(response_data)	        

	return JsonResponse(response_data)		