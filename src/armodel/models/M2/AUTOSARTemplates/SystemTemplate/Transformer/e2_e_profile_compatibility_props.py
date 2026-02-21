"""E2EProfileCompatibilityProps AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 202)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 807)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Transformer.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
)


class E2EProfileCompatibilityProps(ARElement):
    """AUTOSAR E2EProfileCompatibilityProps."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    transit_to_invalid: Optional[Boolean]
    def __init__(self) -> None:
        """Initialize E2EProfileCompatibilityProps."""
        super().__init__()
        self.transit_to_invalid: Optional[Boolean] = None

    def serialize(self) -> ET.Element:
        """Serialize E2EProfileCompatibilityProps to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(E2EProfileCompatibilityProps, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize transit_to_invalid
        if self.transit_to_invalid is not None:
            serialized = ARObject._serialize_item(self.transit_to_invalid, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TRANSIT-TO-INVALID")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "E2EProfileCompatibilityProps":
        """Deserialize XML element to E2EProfileCompatibilityProps object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized E2EProfileCompatibilityProps object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(E2EProfileCompatibilityProps, cls).deserialize(element)

        # Parse transit_to_invalid
        child = ARObject._find_child_element(element, "TRANSIT-TO-INVALID")
        if child is not None:
            transit_to_invalid_value = child.text
            obj.transit_to_invalid = transit_to_invalid_value

        return obj



class E2EProfileCompatibilityPropsBuilder:
    """Builder for E2EProfileCompatibilityProps."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: E2EProfileCompatibilityProps = E2EProfileCompatibilityProps()

    def build(self) -> E2EProfileCompatibilityProps:
        """Build and return E2EProfileCompatibilityProps object.

        Returns:
            E2EProfileCompatibilityProps instance
        """
        # TODO: Add validation
        return self._obj
