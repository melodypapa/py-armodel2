"""LinFrameTriggering AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 428)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Lin_LinCommunication.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.frame_triggering import (
    FrameTriggering,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Lin.LinCommunication import (
    LinChecksumType,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Integer,
)


class LinFrameTriggering(FrameTriggering):
    """AUTOSAR LinFrameTriggering."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    identifier: Optional[Integer]
    lin_checksum: Optional[LinChecksumType]
    def __init__(self) -> None:
        """Initialize LinFrameTriggering."""
        super().__init__()
        self.identifier: Optional[Integer] = None
        self.lin_checksum: Optional[LinChecksumType] = None

    def serialize(self) -> ET.Element:
        """Serialize LinFrameTriggering to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(LinFrameTriggering, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize identifier
        if self.identifier is not None:
            serialized = ARObject._serialize_item(self.identifier, "Integer")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("IDENTIFIER")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize lin_checksum
        if self.lin_checksum is not None:
            serialized = ARObject._serialize_item(self.lin_checksum, "LinChecksumType")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("LIN-CHECKSUM")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "LinFrameTriggering":
        """Deserialize XML element to LinFrameTriggering object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized LinFrameTriggering object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(LinFrameTriggering, cls).deserialize(element)

        # Parse identifier
        child = ARObject._find_child_element(element, "IDENTIFIER")
        if child is not None:
            identifier_value = child.text
            obj.identifier = identifier_value

        # Parse lin_checksum
        child = ARObject._find_child_element(element, "LIN-CHECKSUM")
        if child is not None:
            lin_checksum_value = LinChecksumType.deserialize(child)
            obj.lin_checksum = lin_checksum_value

        return obj



class LinFrameTriggeringBuilder:
    """Builder for LinFrameTriggering."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: LinFrameTriggering = LinFrameTriggering()

    def build(self) -> LinFrameTriggering:
        """Build and return LinFrameTriggering object.

        Returns:
            LinFrameTriggering instance
        """
        # TODO: Add validation
        return self._obj
