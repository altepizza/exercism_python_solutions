import json


class RestAPI:
    def __init__(self, database=None):
        self.database = database

        self.POST_ENDPOINTS = {
            '/add': self.api_add_post,
            '/iou': self.api_iou_post
        }
        self.GET_ENDPOINTS = {'/users': self.api_users_get}
        self.USER_TEMPLATE = {
            'name': None,
            'owes': {},
            'owed_by': {},
            'balance': 0.0
        }

# Entrypoints

    def get(self, url, payload=None):
        try:
            parsed_payload = json.loads(payload)
        except Exception:
            parsed_payload = {}
        handler = self.GET_ENDPOINTS[url]
        return json.dumps(handler(parsed_payload))

    def post(self, url, payload=None):
        parsed_payload = json.loads(payload)
        handler = self.POST_ENDPOINTS[url]
        return json.dumps(handler(parsed_payload))

# API handlers

    def api_add_post(self, payload):
        new_username = payload.get('user')
        if new_username:
            new_user = self.USER_TEMPLATE.copy()
            new_user['name'] = new_username
            self.database['users'].append(new_user)
            return new_user

    def api_iou_post(self, payload):
        lender = self._get_user_from_db(payload['lender'])
        borrower = self._get_user_from_db(payload['borrower'])
        amount = payload['amount']

        lender = self._update_balance(lender, amount)
        borrower = self._update_balance(borrower, -amount)

        lender, borrower, amount = self._even_out_lender_borrower(
            lender, borrower, amount)

        if amount:
            borrower = self._update_owes(borrower, lender, amount)
            lender = self._update_owed_by(lender, borrower, amount)

        sorted_output = sorted([lender, borrower], key=lambda k: k['name'])
        return {'users': sorted_output}

    def api_users_get(self, payload):
        users = payload.get('users')
        if users:
            return {
                'users': [
                    entry for entry in self.database['users']
                    if entry['name'] in users
                ]
            }
        return {'users': self.database['users']}


# Helpers

    def _even_out_lender_borrower(self, lender, borrower, amount):
        if borrower['name'] in lender['owes']:
            if (lender['owes'][borrower['name']] - amount) > 0:
                lender['owes'][borrower['name']] -= amount
                borrower['owed_by'][lender['name']] -= amount
                amount = 0
            else:
                amount -= lender['owes'][borrower['name']]
                del lender['owes'][borrower['name']]
                del borrower['owed_by'][lender['name']]
        return lender, borrower, amount

    def _get_user_from_db(self, name):
        for user in self.database['users']:
            if user['name'] == name:
                return user

    def _update_balance(self, user, amount):
        user['balance'] = user['balance'] + amount
        return user

    def _update_owed_by(self, lender, borrower, amount):
        if borrower['name'] in lender['owed_by']:
            lender['owed_by'][borrower['name']] += amount
        else:
            lender['owed_by'][borrower['name']] = amount
        return lender

    def _update_owes(self, user, lender, amount):
        if lender['name'] in user['owes']:
            user['owes'][lender['name']] += amount
        else:
            user['owes'][lender['name']] = amount
        return user
