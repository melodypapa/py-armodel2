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

    def serialize(self) -> ET.Element:
        """Serialize SecurityEventOneEveryNFilter to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(SecurityEventOneEveryNFilter, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize n
        if self.n is not None:
            serialized = ARObject._serialize_item(self.n, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("N")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

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
