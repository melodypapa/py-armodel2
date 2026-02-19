"""CompuScaleConstantContents AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 390)

JSON Source: docs/json/packages/M2_MSR_AsamHdo_ComputationMethod.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.MSR.AsamHdo.ComputationMethod.compu_scale_contents import (
    CompuScaleContents,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.MSR.AsamHdo.ComputationMethod.compu_const import (
    CompuConst,
)


class CompuScaleConstantContents(CompuScaleContents):
    """AUTOSAR CompuScaleConstantContents."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    compu_const: Optional[CompuConst]
    def __init__(self) -> None:
        """Initialize CompuScaleConstantContents."""
        super().__init__()
        self.compu_const: Optional[CompuConst] = None
    def serialize(self) -> ET.Element:
        """Serialize CompuScaleConstantContents to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(CompuScaleConstantContents, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize compu_const
        if self.compu_const is not None:
            serialized = ARObject._serialize_item(self.compu_const, "CompuConst")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("COMPU-CONST")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "CompuScaleConstantContents":
        """Deserialize XML element to CompuScaleConstantContents object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized CompuScaleConstantContents object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(CompuScaleConstantContents, cls).deserialize(element)

        # Parse compu_const
        child = ARObject._find_child_element(element, "COMPU-CONST")
        if child is not None:
            compu_const_value = ARObject._deserialize_by_tag(child, "CompuConst")
            obj.compu_const = compu_const_value

        return obj



class CompuScaleConstantContentsBuilder:
    """Builder for CompuScaleConstantContents."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: CompuScaleConstantContents = CompuScaleConstantContents()

    def build(self) -> CompuScaleConstantContents:
        """Build and return CompuScaleConstantContents object.

        Returns:
            CompuScaleConstantContents instance
        """
        # TODO: Add validation
        return self._obj
