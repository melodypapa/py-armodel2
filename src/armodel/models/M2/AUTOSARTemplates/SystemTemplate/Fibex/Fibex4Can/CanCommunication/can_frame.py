"""CanFrame AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 442)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Can_CanCommunication.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.frame import (
    Frame,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject


class CanFrame(Frame):
    """AUTOSAR CanFrame."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    def __init__(self) -> None:
        """Initialize CanFrame."""
        super().__init__()
    def serialize(self) -> ET.Element:
        """Serialize CanFrame to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = ARObject._get_xml_tag(self)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(CanFrame, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "CanFrame":
        """Deserialize XML element to CanFrame object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized CanFrame object
        """
        # Delegate to parent class to handle inherited attributes
        return super(CanFrame, cls).deserialize(element)



class CanFrameBuilder:
    """Builder for CanFrame."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: CanFrame = CanFrame()

    def build(self) -> CanFrame:
        """Build and return CanFrame object.

        Returns:
            CanFrame instance
        """
        # TODO: Add validation
        return self._obj
