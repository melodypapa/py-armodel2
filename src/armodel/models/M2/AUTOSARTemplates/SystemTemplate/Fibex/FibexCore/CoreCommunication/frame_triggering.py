"""FrameTriggering AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_ECUConfiguration.pdf (page 295)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 418)
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 224)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_FibexCore_CoreCommunication.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.frame import (
    Frame,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.frame_port import (
    FramePort,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.pdu_triggering import (
    PduTriggering,
)
from abc import ABC, abstractmethod


class FrameTriggering(Identifiable, ABC):
    """AUTOSAR FrameTriggering."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    frame: Optional[Frame]
    frame_ports: list[FramePort]
    pdu_triggering_refs: list[ARRef]
    def __init__(self) -> None:
        """Initialize FrameTriggering."""
        super().__init__()
        self.frame: Optional[Frame] = None
        self.frame_ports: list[FramePort] = []
        self.pdu_triggering_refs: list[ARRef] = []
    def serialize(self) -> ET.Element:
        """Serialize FrameTriggering to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(FrameTriggering, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize frame
        if self.frame is not None:
            serialized = ARObject._serialize_item(self.frame, "Frame")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("FRAME")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize frame_ports (list to container "FRAME-PORTS")
        if self.frame_ports:
            wrapper = ET.Element("FRAME-PORTS")
            for item in self.frame_ports:
                serialized = ARObject._serialize_item(item, "FramePort")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize pdu_triggering_refs (list to container "PDU-TRIGGERINGS")
        if self.pdu_triggering_refs:
            wrapper = ET.Element("PDU-TRIGGERINGS")
            for item in self.pdu_triggering_refs:
                serialized = ARObject._serialize_item(item, "PduTriggering")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "FrameTriggering":
        """Deserialize XML element to FrameTriggering object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized FrameTriggering object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(FrameTriggering, cls).deserialize(element)

        # Parse frame
        child = ARObject._find_child_element(element, "FRAME")
        if child is not None:
            frame_value = ARObject._deserialize_by_tag(child, "Frame")
            obj.frame = frame_value

        # Parse frame_ports (list from container "FRAME-PORTS")
        obj.frame_ports = []
        container = ARObject._find_child_element(element, "FRAME-PORTS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.frame_ports.append(child_value)

        # Parse pdu_triggering_refs (list from container "PDU-TRIGGERINGS")
        obj.pdu_triggering_refs = []
        container = ARObject._find_child_element(element, "PDU-TRIGGERINGS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.pdu_triggering_refs.append(child_value)

        return obj



class FrameTriggeringBuilder:
    """Builder for FrameTriggering."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: FrameTriggering = FrameTriggering()

    def build(self) -> FrameTriggering:
        """Build and return FrameTriggering object.

        Returns:
            FrameTriggering instance
        """
        # TODO: Add validation
        return self._obj
