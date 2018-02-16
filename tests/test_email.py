from app.email import verify_email

def test_basic_email_text_only():
	assert verify_email("name@email.com") == True

def test_basic_email_with_numbers():
	assert verify_email("n1a2m3e4@email.com") == True

def test_email_with_periods():
	assert verify_email("n.a.m.e@email.com") == True

def test_email_with_begining_period():
	assert verify_email(".n.a.m.e@email.com") == False

def test_email_with_ending_period():
	assert verify_email("n.a.m.e.@email.com") == False

def test_email_with_two_periods():
	assert verify_email("na..me@email.com") == False

def test_email_starting_with_number():
	assert verify_email("1name@email.com") == False

def test_email_with_symbols():
	assert verify_email("!$%*+-=?^_{|}~@email.com") == True

def test_email_with_sub_domain():
	assert verify_email("!$%*+-=?^_{|}~@email.org.us") == True

def test_email_with_no_at_or_domain():
	assert verify_email("not_email") == False

def test_email_with_no_domain():
	assert verify_email("not_email@") == False

def test_email_with_no_at():
	assert verify_email("not_emaildomain.com") == False
