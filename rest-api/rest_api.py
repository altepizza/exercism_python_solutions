import json


class RestAPI:
    def __init__(self, database=None):
        self.database = database
        self.POST_ENDPOINTS = {'/add': self._add_user, '/iou': self._iou}
        self.GET_ENDPOINTS = {'/users': self._get_users}
        self.USER_TEMPLATE = {
            'name': None,
            'owes': {},
            'owed_by': {},
            'balance': 0.0
        }

    def get_user_from_db(self, name):
        for user in self.database['users']:
            if user['name'] == name:
                return user

    def update_balance(self, user, amount):
        user['balance'] = user['balance'] + amount
        return user

    def update_owes(self, user, lender, amount):
        if lender['name'] in user['owes']:
            user['owes'][lender['name']] += amount
        else:
            user['owes'][lender['name']] = amount
        return user

    def update_owed_by(self, lender, borrower, amount):
        if borrower['name'] in lender['owed_by']:
            lender['owed_by'][borrower['name']] += amount
        else:
            lender['owed_by'][borrower['name']] = amount
        return lender

    def even_out_lender_borrower(self, lender, borrower, amount):
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

    def _iou(self, payload):
        lender = self.get_user_from_db(payload['lender'])
        borrower = self.get_user_from_db(payload['borrower'])
        amount = payload['amount']

        lender = self.update_balance(lender, amount)
        borrower = self.update_balance(borrower, -amount)

        lender, borrower, amount = self.even_out_lender_borrower(
            lender, borrower, amount)

        if amount:
            borrower = self.update_owes(borrower, lender, amount)
            lender = self.update_owed_by(lender, borrower, amount)

        sorted_output = sorted([lender, borrower], key=lambda k: k['name'])
        return {'users': sorted_output}

    def _get_users(self, payload):
        users = payload.get('users')
        if users:
            return {
                'users': [
                    entry for entry in self.database['users']
                    if entry['name'] in users
                ]
            }
        return {'users': self.database['users']}

    def _add_user(self, payload):
        new_username = payload.get('user')
        if new_username:
            new_user = self.USER_TEMPLATE.copy()
            new_user['name'] = new_username
            self.database['users'].append(new_user)
            return new_user

    def get(self, url, payload=None):
        try:
            p = json.loads(payload)
        except Exception:
            p = {}
        x = self.GET_ENDPOINTS[url]
        return json.dumps(x(p))

    def post(self, url, payload=None):
        p = json.loads(payload)
        x = self.POST_ENDPOINTS[url]
        return json.dumps(x(p))
