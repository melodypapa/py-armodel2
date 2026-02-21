"""SwBaseType AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 337)
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 329)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 290)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 2060)
  - AUTOSAR_FO_TPS_LogAndTraceExtract.pdf (page 33)
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 210)

JSON Source: docs/json/packages/M2_MSR_AsamHdo_BaseTypes.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.MSR.AsamHdo.BaseTypes.base_type import (
    BaseType,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject


class SwBaseType(BaseType):
    """AUTOSAR SwBaseType."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    def __init__(self) -> None:
        """Initialize SwBaseType."""
        super().__init__()

    def serialize(self) -> ET.Element:
        """Serialize SwBaseType to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(SwBaseType, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "SwBaseType":
        """Deserialize XML element to SwBaseType object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized SwBaseType object
        """
        # Delegate to parent class to handle inherited attributes
        return super(SwBaseType, cls).deserialize(element)



class SwBaseTypeBuilder:
    """Builder for SwBaseType."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SwBaseType = SwBaseType()

    def build(self) -> SwBaseType:
        """Build and return SwBaseType object.

        Returns:
            SwBaseType instance
        """
        # TODO: Add validation
        return self._obj
