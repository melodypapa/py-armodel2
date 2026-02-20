"""DiagnosticAuthRole AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 77)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_Dcm.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics.diagnostic_common_element import (
    DiagnosticCommonElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    PositiveInteger,
)


class DiagnosticAuthRole(DiagnosticCommonElement):
    """AUTOSAR DiagnosticAuthRole."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    bit_position: Optional[PositiveInteger]
    is_default: Optional[Boolean]
    def __init__(self) -> None:
        """Initialize DiagnosticAuthRole."""
        super().__init__()
        self.bit_position: Optional[PositiveInteger] = None
        self.is_default: Optional[Boolean] = None

    def serialize(self) -> ET.Element:
        """Serialize DiagnosticAuthRole to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DiagnosticAuthRole, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize bit_position
        if self.bit_position is not None:
            serialized = ARObject._serialize_item(self.bit_position, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("BIT-POSITION")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize is_default
        if self.is_default is not None:
            serialized = ARObject._serialize_item(self.is_default, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("IS-DEFAULT")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticAuthRole":
        """Deserialize XML element to DiagnosticAuthRole object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DiagnosticAuthRole object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DiagnosticAuthRole, cls).deserialize(element)

        # Parse bit_position
        child = ARObject._find_child_element(element, "BIT-POSITION")
        if child is not None:
            bit_position_value = child.text
            obj.bit_position = bit_position_value

        # Parse is_default
        child = ARObject._find_child_element(element, "IS-DEFAULT")
        if child is not None:
            is_default_value = child.text
            obj.is_default = is_default_value

        return obj



class DiagnosticAuthRoleBuilder:
    """Builder for DiagnosticAuthRole."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticAuthRole = DiagnosticAuthRole()

    def build(self) -> DiagnosticAuthRole:
        """Build and return DiagnosticAuthRole object.

        Returns:
            DiagnosticAuthRole instance
        """
        # TODO: Add validation
        return self._obj
