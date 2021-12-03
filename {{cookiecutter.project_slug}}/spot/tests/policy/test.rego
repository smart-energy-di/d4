# policy/auth.rego

package httpapi.authz

# bob is alice's manager, and betty is charlie's.
subordinates = {"alice": [], "charlie": [], "bob": ["alice"], "betty": ["charlie"]}


# HTTP API request
#import input

test_dbg = input

default allow = false

# Allow users to get their own salaries.
allow {
  some username
  input.request_method == "GET"
  input.request_path = ["finance", "salary", username]
  input.user == username
#  username == "alice"
}

# Allow managers to get their subordinates' salaries.
allow {
  some username
  input.request_method == "GET"
  input.request_path = ["finance", "salary", username]
  subordinates[input.user][_] == username
}
