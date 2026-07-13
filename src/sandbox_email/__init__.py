"""sandbox_email package - email normalization and validation utilities."""

from .normalize import normalize_email
from .validate import is_valid_email

__all__ = ["normalize_email", "is_valid_email"]