"""SecurityEventContextMappingBswModule AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_SecurityExtractTemplate.pdf (page 38)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SecurityExtractTemplate.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SecurityExtractTemplate.security_event_context_mapping import (
    SecurityEventContextMapping,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    String,
)


class SecurityEventContextMappingBswModule(SecurityEventContextMapping):
    """AUTOSAR SecurityEventContextMappingBswModule."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    affected_bsw: Optional[String]
    def __init__(self) -> None:
        """Initialize SecurityEventContextMappingBswModule."""
        super().__init__()
        self.affected_bsw: Optional[String] = None
    def serialize(self) -> ET.Element:
        """Serialize SecurityEventContextMappingBswModule to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = ARObject._get_xml_tag(self)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(SecurityEventContextMappingBswModule, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize affected_bsw
        if self.affected_bsw is not None:
            serialized = ARObject._serialize_item(self.affected_bsw, "String")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("AFFECTED-BSW")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "SecurityEventContextMappingBswModule":
        """Deserialize XML element to SecurityEventContextMappingBswModule object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized SecurityEventContextMappingBswModule object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(SecurityEventContextMappingBswModule, cls).deserialize(element)

        # Parse affected_bsw
        child = ARObject._find_child_element(element, "AFFECTED-BSW")
        if child is not None:
            affected_bsw_value = child.text
            obj.affected_bsw = affected_bsw_value

        return obj



class SecurityEventContextMappingBswModuleBuilder:
    """Builder for SecurityEventContextMappingBswModule."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SecurityEventContextMappingBswModule = SecurityEventContextMappingBswModule()

    def build(self) -> SecurityEventContextMappingBswModule:
        """Build and return SecurityEventContextMappingBswModule object.

        Returns:
            SecurityEventContextMappingBswModule instance
        """
        # TODO: Add validation
        return self._obj
