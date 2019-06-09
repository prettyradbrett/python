from behave import given, when, then
import requests
from flask import jsonify

BASE_URL = "http://localhost:5000/"
SERVICE_URL = "http://localhost:5000/palingram-spells"
PARAMS = ""

@given(u'the server is available')
def step_impl(context):
    response = requests.get(url = BASE_URL, params = PARAMS)
    assert response.status_code == 200

@when(u'the user requests a palingram')
def step_impl(context):
    context.responses = []
    context.responses.append(requests.get(url = SERVICE_URL, params = PARAMS))

@then(u'the system returns a multi-word phrase')
def step_impl(context):
    for r in context.responses:
        assert ' ' in r.text

@then(u'it is identical when all characters are reversed')
def step_impl(context):
    for r in context.responses:
        original = r.text
        reversed = r.text[::-1]
        assert original == reversed

@when(u'the user submits a post')
def step_impl(context):
    context.response = requests.post(url = SERVICE_URL, params = PARAMS)
    
@then(u'the system returns an error code')
def step_impl(context):
    assert context.response.status_code == 405

@then(u'it is unique for each request')
def step_impl(context):
    context.execute_steps('''
        when the user requests a palingram
    ''')
    response_texts = []
    for r in context.responses:
        response_texts.append(r.text)

    context.execute_steps('''
        when the user requests a palingram
    ''')
    for r in context.responses:
        response_texts.append(r.text)

    assert len(response_texts) == len(set(response_texts))

@then(u'it starts with the text "Jeff"')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then it starts with the text "Jeff"'