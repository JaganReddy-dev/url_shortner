class IDGenerator:
    def __init__(self, start=0):
        self.count = start

        def generate(self):
            self.count += 1
            return self.count


# url_map
# - incremental ID (e.g. 1, 2, 3)
# - short_code (e.g. 05c4VCkJ)
# - long url (eg: https://www.google.com)
# - user_id (e.g. GLGDTYXEEAUUNRH8H6LN8TWOUJ9F)
# - api_key (e.g. SA1S23RKNF3JRI2R982IR94H2)
# - created_at (e.g. 2023-01-01)
# - expires_at (e.g. 2023-10-01)

# users
# - user_id (e.g. GLGDTYXEEAUUNRH8H6LN8TWOUJ9F)
# - user_name (e.g. test)
# - is_active (e.g. True)
# - created_at (e.g. 2023-01-01)

# apis
#  - id (eg: F1WF313RQ8U31I4JE24HUF)
# - name (e.g. DEV_API_KEY)
# - api_key (e.g. SA1S23RKNF3JRI2R982IR94H2)
#  - created_at (e.g. 2023-01-01)
# - expires_at (e.g. 2023-10-01)
# - user_id (e.g. GLGDTYXEEAUUNRH8H6LN8TWOUJ9F)
# - is_active (e.g. True)
