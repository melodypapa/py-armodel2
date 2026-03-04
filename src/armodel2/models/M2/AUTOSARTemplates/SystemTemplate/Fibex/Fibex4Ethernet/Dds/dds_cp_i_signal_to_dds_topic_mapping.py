"""DdsCpISignalToDdsTopicMapping AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 293)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_Dds.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.Dds.dds_cp_topic import (
    DdsCpTopic,
)
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.i_signal import (
    ISignal,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class DdsCpISignalToDdsTopicMapping(ARObject):
    """AUTOSAR DdsCpISignalToDdsTopicMapping."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "DDS-CP-I-SIGNAL-TO-DDS-TOPIC-MAPPING"


    dds_topic_ref: Optional[ARRef]
    i_signal_ref: Optional[ARRef]
    _DESERIALIZE_DISPATCH = {
        "DDS-TOPIC-REF": lambda obj, elem: setattr(obj, "dds_topic_ref", ARRef.deserialize(elem)),
        "I-SIGNAL-REF": lambda obj, elem: setattr(obj, "i_signal_ref", ARRef.deserialize(elem)),
    }


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
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

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

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "DDS-TOPIC-REF":
                setattr(obj, "dds_topic_ref", ARRef.deserialize(child))
            elif tag == "I-SIGNAL-REF":
                setattr(obj, "i_signal_ref", ARRef.deserialize(child))

        return obj



class DdsCpISignalToDdsTopicMappingBuilder(BuilderBase):
    """Builder for DdsCpISignalToDdsTopicMapping with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: DdsCpISignalToDdsTopicMapping = DdsCpISignalToDdsTopicMapping()


    def with_dds_topic(self, value: Optional[DdsCpTopic]) -> "DdsCpISignalToDdsTopicMappingBuilder":
        """Set dds_topic attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.dds_topic = value
        return self

    def with_i_signal(self, value: Optional[ISignal]) -> "DdsCpISignalToDdsTopicMappingBuilder":
        """Set i_signal attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.i_signal = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "ddsTopic",
        "iSignal",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> DdsCpISignalToDdsTopicMapping:
        """Build and return the DdsCpISignalToDdsTopicMapping instance with validation."""
        self._validate_instance()
        return self._obj