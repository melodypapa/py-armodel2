"""BusMirrorChannelMapping AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 697)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_BusMirror.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.fibex_element import (
    FibexElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.BusMirror import (
    MirroringProtocolEnum,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.BusMirror.bus_mirror_channel import (
    BusMirrorChannel,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.pdu_triggering import (
    PduTriggering,
)
from abc import ABC, abstractmethod


class BusMirrorChannelMapping(FibexElement, ABC):
    """AUTOSAR BusMirrorChannelMapping."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    mirroring: Optional[MirroringProtocolEnum]
    source_channel: Optional[BusMirrorChannel]
    target_channel: Optional[BusMirrorChannel]
    target_pdu_refs: list[ARRef]
    def __init__(self) -> None:
        """Initialize BusMirrorChannelMapping."""
        super().__init__()
        self.mirroring: Optional[MirroringProtocolEnum] = None
        self.source_channel: Optional[BusMirrorChannel] = None
        self.target_channel: Optional[BusMirrorChannel] = None
        self.target_pdu_refs: list[ARRef] = []

    def serialize(self) -> ET.Element:
        """Serialize BusMirrorChannelMapping to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(BusMirrorChannelMapping, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize mirroring
        if self.mirroring is not None:
            serialized = SerializationHelper.serialize_item(self.mirroring, "MirroringProtocolEnum")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MIRRORING")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize source_channel
        if self.source_channel is not None:
            serialized = SerializationHelper.serialize_item(self.source_channel, "BusMirrorChannel")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SOURCE-CHANNEL")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize target_channel
        if self.target_channel is not None:
            serialized = SerializationHelper.serialize_item(self.target_channel, "BusMirrorChannel")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TARGET-CHANNEL")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize target_pdu_refs (list to container "TARGET-PDU-REFS")
        if self.target_pdu_refs:
            wrapper = ET.Element("TARGET-PDU-REFS")
            for item in self.target_pdu_refs:
                serialized = SerializationHelper.serialize_item(item, "PduTriggering")
                if serialized is not None:
                    child_elem = ET.Element("TARGET-PDU-REF")
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
    def deserialize(cls, element: ET.Element) -> "BusMirrorChannelMapping":
        """Deserialize XML element to BusMirrorChannelMapping object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized BusMirrorChannelMapping object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(BusMirrorChannelMapping, cls).deserialize(element)

        # Parse mirroring
        child = SerializationHelper.find_child_element(element, "MIRRORING")
        if child is not None:
            mirroring_value = MirroringProtocolEnum.deserialize(child)
            obj.mirroring = mirroring_value

        # Parse source_channel
        child = SerializationHelper.find_child_element(element, "SOURCE-CHANNEL")
        if child is not None:
            source_channel_value = SerializationHelper.deserialize_by_tag(child, "BusMirrorChannel")
            obj.source_channel = source_channel_value

        # Parse target_channel
        child = SerializationHelper.find_child_element(element, "TARGET-CHANNEL")
        if child is not None:
            target_channel_value = SerializationHelper.deserialize_by_tag(child, "BusMirrorChannel")
            obj.target_channel = target_channel_value

        # Parse target_pdu_refs (list from container "TARGET-PDU-REFS")
        obj.target_pdu_refs = []
        container = SerializationHelper.find_child_element(element, "TARGET-PDU-REFS")
        if container is not None:
            for child in container:
                # Check if child is a reference element (ends with -REF or -TREF)
                child_element_tag = SerializationHelper.strip_namespace(child.tag)
                if child_element_tag.endswith("-REF") or child_element_tag.endswith("-TREF"):
                    # Use ARRef.deserialize() for reference elements
                    child_value = ARRef.deserialize(child)
                else:
                    # Deserialize each child element dynamically based on its tag
                    child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.target_pdu_refs.append(child_value)

        return obj



