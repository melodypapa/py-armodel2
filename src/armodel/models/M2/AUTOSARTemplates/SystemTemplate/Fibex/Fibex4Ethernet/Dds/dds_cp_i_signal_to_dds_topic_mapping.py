"""DdsCpISignalToDdsTopicMapping AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 293)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_Dds.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.Dds.dds_cp_topic import (
    DdsCpTopic,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.i_signal import (
    ISignal,
)


class DdsCpISignalToDdsTopicMapping(ARObject):
    """AUTOSAR DdsCpISignalToDdsTopicMapping."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    dds_topic_ref: Optional[ARRef]
    i_signal_ref: Optional[ARRef]
    def __init__(self) -> None:
        """Initialize DdsCpISignalToDdsTopicMapping."""
        super().__init__()
        self.dds_topic_ref: Optional[ARRef] = None
        self.i_signal_ref: Optional[ARRef] = None

    def serialize(self) -> ET.Element:
        """Serialize DdsCpISignalToDdsTopicMapping to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DdsCpISignalToDdsTopicMapping, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize dds_topic_ref
        if self.dds_topic_ref is not None:
            serialized = SerializationHelper.serialize_item(self.dds_topic_ref, "DdsCpTopic")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("DDS-TOPIC-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize i_signal_ref
        if self.i_signal_ref is not None:
            serialized = SerializationHelper.serialize_item(self.i_signal_ref, "ISignal")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("I-SIGNAL-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DdsCpISignalToDdsTopicMapping":
        """Deserialize XML element to DdsCpISignalToDdsTopicMapping object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DdsCpISignalToDdsTopicMapping object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DdsCpISignalToDdsTopicMapping, cls).deserialize(element)

        # Parse dds_topic_ref
        child = SerializationHelper.find_child_element(element, "DDS-TOPIC-REF")
        if child is not None:
            dds_topic_ref_value = ARRef.deserialize(child)
            obj.dds_topic_ref = dds_topic_ref_value

        # Parse i_signal_ref
        child = SerializationHelper.find_child_element(element, "I-SIGNAL-REF")
        if child is not None:
            i_signal_ref_value = ARRef.deserialize(child)
            obj.i_signal_ref = i_signal_ref_value

        return obj



class DdsCpISignalToDdsTopicMappingBuilder:
    """Builder for DdsCpISignalToDdsTopicMapping."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DdsCpISignalToDdsTopicMapping = DdsCpISignalToDdsTopicMapping()

    def build(self) -> DdsCpISignalToDdsTopicMapping:
        """Build and return DdsCpISignalToDdsTopicMapping object.

        Returns:
            DdsCpISignalToDdsTopicMapping instance
        """
        # TODO: Add validation
        return self._obj
