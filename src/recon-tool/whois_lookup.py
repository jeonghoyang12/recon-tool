import whois # type: ignore

class WHOISLookup:
    def __init__(self, target):
        self.target = target

    def lookup(self):
        try:
            domain_info = whois.whois(self.target)
            return domain_info
        except Exception as e:
            return f"WHOIS lookup failed: {str(e)}"
    