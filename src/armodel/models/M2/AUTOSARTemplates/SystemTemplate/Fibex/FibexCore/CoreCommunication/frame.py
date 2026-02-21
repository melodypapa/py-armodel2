"""Frame AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_ECUConfiguration.pdf (page 295)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 418)
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 224)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_FibexCore_CoreCommunication.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.fibex_element import (
    FibexElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Integer,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.pdu_to_frame_mapping import (
    PduToFrameMapping,
)
from abc import ABC, abstractmethod


class Frame(FibexElement, ABC):
    """AUTOSAR Frame."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    frame_length: Optional[Integer]
    pdu_to_frame_refs: list[ARRef]
    def __init__(self) -> None:
        """Initialize Frame."""
        super().__init__()
        self.frame_length: Optional[Integer] = None
        self.pdu_to_frame_refs: list[ARRef] = []

    def serialize(self) -> ET.Element:
        """Serialize Frame to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(Frame, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize frame_length
        if self.frame_length is not None:
            serialized = ARObject._serialize_item(self.frame_length, "Integer")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("FRAME-LENGTH")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize pdu_to_frame_refs (list to container "PDU-TO-FRAME-REFS")
        if self.pdu_to_frame_refs:
            wrapper = ET.Element("PDU-TO-FRAME-REFS")
            for item in self.pdu_to_frame_refs:
                serialized = ARObject._serialize_item(item, "PduToFrameMapping")
                if serialized is not None:
                    child_elem = ET.Element("PDU-TO-FRAME-REF")
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
    def deserialize(cls, element: ET.Element) -> "Frame":
        """Deserialize XML element to Frame object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized Frame object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(Frame, cls).deserialize(element)

        # Parse frame_length
        child = ARObject._find_child_element(element, "FRAME-LENGTH")
        if child is not None:
            frame_length_value = child.text
            obj.frame_length = frame_length_value

        # Parse pdu_to_frame_refs (list from container "PDU-TO-FRAME-REFS")
        obj.pdu_to_frame_refs = []
        container = ARObject._find_child_element(element, "PDU-TO-FRAME-REFS")
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
                    obj.pdu_to_frame_refs.append(child_value)

        return obj



class FrameBuilder:
    """Builder for Frame."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: Frame = Frame()

    def build(self) -> Frame:
        """Build and return Frame object.

        Returns:
            Frame instance
        """
        # TODO: Add validation
        return self._obj
