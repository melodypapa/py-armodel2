"""BusMirrorCanIdToCanIdMapping AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 702)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_BusMirror.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Can.CanCommunication.can_frame_triggering import (
    CanFrameTriggering,
)


class BusMirrorCanIdToCanIdMapping(ARObject):
    """AUTOSAR BusMirrorCanIdToCanIdMapping."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    remapped_can_id: Optional[PositiveInteger]
    souce_can_id_ref: Optional[ARRef]
    def __init__(self) -> None:
        """Initialize BusMirrorCanIdToCanIdMapping."""
        super().__init__()
        self.remapped_can_id: Optional[PositiveInteger] = None
        self.souce_can_id_ref: Optional[ARRef] = None
    def serialize(self) -> ET.Element:
        """Serialize BusMirrorCanIdToCanIdMapping to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # Serialize remapped_can_id
        if self.remapped_can_id is not None:
            serialized = ARObject._serialize_item(self.remapped_can_id, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("REMAPPED-CAN-ID")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize souce_can_id_ref
        if self.souce_can_id_ref is not None:
            serialized = ARObject._serialize_item(self.souce_can_id_ref, "CanFrameTriggering")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SOUCE-CAN-ID-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "BusMirrorCanIdToCanIdMapping":
        """Deserialize XML element to BusMirrorCanIdToCanIdMapping object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized BusMirrorCanIdToCanIdMapping object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse remapped_can_id
        child = ARObject._find_child_element(element, "REMAPPED-CAN-ID")
        if child is not None:
            remapped_can_id_value = child.text
            obj.remapped_can_id = remapped_can_id_value

        # Parse souce_can_id_ref
        child = ARObject._find_child_element(element, "SOUCE-CAN-ID-REF")
        if child is not None:
            souce_can_id_ref_value = ARRef.deserialize(child)
            obj.souce_can_id_ref = souce_can_id_ref_value

        return obj



class BusMirrorCanIdToCanIdMappingBuilder:
    """Builder for BusMirrorCanIdToCanIdMapping."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: BusMirrorCanIdToCanIdMapping = BusMirrorCanIdToCanIdMapping()

    def build(self) -> BusMirrorCanIdToCanIdMapping:
        """Build and return BusMirrorCanIdToCanIdMapping object.

        Returns:
            BusMirrorCanIdToCanIdMapping instance
        """
        # TODO: Add validation
        return self._obj
