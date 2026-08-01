import ipaddress
import re


DOMAIN_REGEX = re.compile(
    r"^(?:[a-zA-Z0-9]"
    r"(?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?\.)+"
    r"[a-zA-Z]{2,}$"
)


def is_valid_ip(target: str) -> bool:
    """
    Validate IPv4 or IPv6 address.
    """
    try:
        ipaddress.ip_address(target)
        return True
    except ValueError:
        return False


def is_valid_domain(target: str) -> bool:
    """
    Validate domain name.
    """
    return bool(DOMAIN_REGEX.fullmatch(target))


def is_valid_target(target: str) -> bool:
    """
    Validate target as IP or domain.
    """
    return is_valid_ip(target) or is_valid_domain(target)
