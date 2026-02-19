"""SecurityEventOneEveryNFilter AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_SecurityExtractTemplate.pdf (page 24)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SecurityExtractTemplate.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SecurityExtractTemplate.abstract_security_event_filter import (
    AbstractSecurityEventFilter,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)


class SecurityEventOneEveryNFilter(AbstractSecurityEventFilter):
    """AUTOSAR SecurityEventOneEveryNFilter."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    n: Optional[PositiveInteger]
    def __init__(self) -> None:
        """Initialize SecurityEventOneEveryNFilter."""
        super().__init__()
        self.n: Optional[PositiveInteger] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "SecurityEventOneEveryNFilter":
        """Deserialize XML element to SecurityEventOneEveryNFilter object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized SecurityEventOneEveryNFilter object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(SecurityEventOneEveryNFilter, cls).deserialize(element)

        # Parse n
        child = ARObject._find_child_element(element, "N")
        if child is not None:
            n_value = child.text
            obj.n = n_value

        return obj



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
