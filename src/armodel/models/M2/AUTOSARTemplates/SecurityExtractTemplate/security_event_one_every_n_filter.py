"""SecurityEventOneEveryNFilter AUTOSAR element."""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject


class SecurityEventOneEveryNFilter(AbstractSecurityEventFilter):
    """AUTOSAR SecurityEventOneEveryNFilter."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
    }

    def __init__(self) -> None:
        """Initialize SecurityEventOneEveryNFilter."""
        super().__init__()


class SecurityEventOneEveryNFilterBuilder:
    """Builder for SecurityEventOneEveryNFilter."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SecurityEventOneEveryNFilter = SecurityEventOneEveryNFilter()

    def build(self) -> SecurityEventOneEveryNFilter:
        """Build and return SecurityEventOneEveryNFilter object.

        Returns:
            SecurityEventOneEveryNFilter instance
        """
        # TODO: Add validation
        return self._obj
