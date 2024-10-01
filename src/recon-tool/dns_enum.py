import dns.resolver # type: ignore

class DNSEnumerator:
    def __init__(self, target):
        self.target = target

    def enumerate(self):
        record_types = ['A', 'AAAA', 'CNAME', 'MX', 'NS', 'SOA', 'TXT']
        results = {}
        for record_type in record_types:
            try:
                answers = dns.resolver.resolve(self.target, record_type)
                results[record_type] = [str(rdata) for rdata in answers]
            except dns.resolver.NXDOMAIN:
                results[record_type] = ["Domain does not exist"]
            except dns.resolver.NoAnswer:
                results[record_type] = []
            except Exception as e:
                results[record_type] = [f"Error: {str(e)}"]
        return results
                