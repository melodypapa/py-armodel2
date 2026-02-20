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

    frame_ref: Optional[ARRef]
    frame_port_refs: list[ARRef]
    pdu_triggering_refs: list[ARRef]
    def __init__(self) -> None:
        """Initialize FrameTriggering."""
        super().__init__()
        self.frame_ref: Optional[ARRef] = None
        self.frame_port_refs: list[ARRef] = []
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

        # Serialize frame_ref
        if self.frame_ref is not None:
            serialized = ARObject._serialize_item(self.frame_ref, "Frame")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("FRAME-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize frame_port_refs (list to container "FRAME-PORT-REFS")
        if self.frame_port_refs:
            wrapper = ET.Element("FRAME-PORT-REFS")
            for item in self.frame_port_refs:
                serialized = ARObject._serialize_item(item, "FramePort")
                if serialized is not None:
                    child_elem = ET.Element("FRAME-PORT-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize pdu_triggering_refs (list to container "PDU-TRIGGERING-REFS")
        if self.pdu_triggering_refs:
            wrapper = ET.Element("PDU-TRIGGERING-REFS")
            for item in self.pdu_triggering_refs:
                serialized = ARObject._serialize_item(item, "PduTriggering")
                if serialized is not None:
                    child_elem = ET.Element("PDU-TRIGGERING-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
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

        # Parse frame_ref
        child = ARObject._find_child_element(element, "FRAME-REF")
        if child is not None:
            frame_ref_value = ARRef.deserialize(child)
            obj.frame_ref = frame_ref_value

        # Parse frame_port_refs (list from container "FRAME-PORT-REFS")
        obj.frame_port_refs = []
        container = ARObject._find_child_element(element, "FRAME-PORT-REFS")
        if container is not None:
            for child in container:
                # Check if child is a reference element (ends with -REF or -TREF)
                child_tag = ARObject._strip_namespace(child.tag)
                if child_tag.endswith("-REF") or child_tag.endswith("-TREF"):
                    # Use ARRef.deserialize() for reference elements
                    child_value = ARRef.deserialize(child)
                else:
                    # Deserialize each child element dynamically based on its tag
                    child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.frame_port_refs.append(child_value)

        # Parse pdu_triggering_refs (list from container "PDU-TRIGGERING-REFS")
        obj.pdu_triggering_refs = []
        container = ARObject._find_child_element(element, "PDU-TRIGGERING-REFS")
        if container is not None:
            for child in container:
                # Check if child is a reference element (ends with -REF or -TREF)
                child_tag = ARObject._strip_namespace(child.tag)
                if child_tag.endswith("-REF") or child_tag.endswith("-TREF"):
                    # Use ARRef.deserialize() for reference elements
                    child_value = ARRef.deserialize(child)
                else:
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
