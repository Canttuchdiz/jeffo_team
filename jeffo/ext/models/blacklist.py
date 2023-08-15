from jeffo.utils.constants import DisallowedTerms

class Blacklist:

    @staticmethod
    def is_blacklisted(message: str) -> bool:
        combined_message = message.replace(" ", "")
        for term in DisallowedTerms.amTrading:
            if term in combined_message:
                return True
        return False
