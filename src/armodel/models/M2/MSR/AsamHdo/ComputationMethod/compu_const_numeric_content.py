"""CompuConstNumericContent AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 389)

JSON Source: docs/json/packages/M2_MSR_AsamHdo_ComputationMethod.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.MSR.AsamHdo.ComputationMethod.compu_const_content import (
    CompuConstContent,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Numerical,
)


class CompuConstNumericContent(CompuConstContent):
    """AUTOSAR CompuConstNumericContent."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    v: Optional[Numerical]
    def __init__(self) -> None:
        """Initialize CompuConstNumericContent."""
        super().__init__()
        self.v: Optional[Numerical] = None
    def serialize(self) -> ET.Element:
        """Serialize CompuConstNumericContent to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = ARObject._get_xml_tag(self)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(CompuConstNumericContent, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize v
        if self.v is not None:
            serialized = ARObject._serialize_item(self.v, "Numerical")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("V")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "CompuConstNumericContent":
        """Deserialize XML element to CompuConstNumericContent object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized CompuConstNumericContent object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(CompuConstNumericContent, cls).deserialize(element)

        # Parse v
        child = ARObject._find_child_element(element, "V")
        if child is not None:
            v_value = child.text
            obj.v = v_value

        return obj



class CompuConstNumericContentBuilder:
    """Builder for CompuConstNumericContent."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: CompuConstNumericContent = CompuConstNumericContent()

    def build(self) -> CompuConstNumericContent:
        """Build and return CompuConstNumericContent object.

        Returns:
            CompuConstNumericContent instance
        """
        # TODO: Add validation
        return self._obj
