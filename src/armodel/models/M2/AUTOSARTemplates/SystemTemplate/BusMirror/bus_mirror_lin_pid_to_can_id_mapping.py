"""BusMirrorLinPidToCanIdMapping AUTOSAR element.

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
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Lin.LinCommunication.lin_frame_triggering import (
    LinFrameTriggering,
)


class BusMirrorLinPidToCanIdMapping(ARObject):
    """AUTOSAR BusMirrorLinPidToCanIdMapping."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    remapped_can_id: Optional[PositiveInteger]
    source_lin_pid_ref: Optional[ARRef]
    def __init__(self) -> None:
        """Initialize BusMirrorLinPidToCanIdMapping."""
        super().__init__()
        self.remapped_can_id: Optional[PositiveInteger] = None
        self.source_lin_pid_ref: Optional[ARRef] = None
    def serialize(self) -> ET.Element:
        """Serialize BusMirrorLinPidToCanIdMapping to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = ARObject._get_xml_tag(self)
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

        # Serialize source_lin_pid_ref
        if self.source_lin_pid_ref is not None:
            serialized = ARObject._serialize_item(self.source_lin_pid_ref, "LinFrameTriggering")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SOURCE-LIN-PID")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "BusMirrorLinPidToCanIdMapping":
        """Deserialize XML element to BusMirrorLinPidToCanIdMapping object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized BusMirrorLinPidToCanIdMapping object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse remapped_can_id
        child = ARObject._find_child_element(element, "REMAPPED-CAN-ID")
        if child is not None:
            remapped_can_id_value = child.text
            obj.remapped_can_id = remapped_can_id_value

        # Parse source_lin_pid_ref
        child = ARObject._find_child_element(element, "SOURCE-LIN-PID")
        if child is not None:
            source_lin_pid_ref_value = ARObject._deserialize_by_tag(child, "LinFrameTriggering")
            obj.source_lin_pid_ref = source_lin_pid_ref_value

        return obj



class BusMirrorLinPidToCanIdMappingBuilder:
    """Builder for BusMirrorLinPidToCanIdMapping."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: BusMirrorLinPidToCanIdMapping = BusMirrorLinPidToCanIdMapping()

    def build(self) -> BusMirrorLinPidToCanIdMapping:
        """Build and return BusMirrorLinPidToCanIdMapping object.

        Returns:
            BusMirrorLinPidToCanIdMapping instance
        """
        # TODO: Add validation
        return self._obj
