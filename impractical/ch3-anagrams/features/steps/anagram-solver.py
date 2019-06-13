from behave import given, when, then
import requests
from flask import jsonify

BASE_URL = "http://localhost:5000/"
SERVICE_URL = "http://localhost:5000/anagram-solver"
PARAMS = ""

@given(u'the server is available')
def step_impl(context):
    response = requests.get(url = BASE_URL, params = PARAMS)
    assert response.status_code == 200

@when(u'I input "{keyword}"')
def step_impl(context, keyword):
    context.responses = []
    context.responses.append(requests.get(url = SERVICE_URL + '/' + keyword, params = PARAMS))

@then(u'the result should contain "{result}"')
def step_impl(context, result):
    for r in context.responses:
        assert result in r.text

"""
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
        original = r.text.replace(" ", "")
        reversed = r.text[::-1].replace(" ", "")
        assert original == reversed
"""
@when(u'the user submits a post')
def step_impl(context):
    context.response = requests.post(url = SERVICE_URL, params = PARAMS)
    
@then(u'the system returns an error code')
def step_impl(context):
    assert context.response.status_code in [400, 404, 405, 500, 501, 502, 503]
