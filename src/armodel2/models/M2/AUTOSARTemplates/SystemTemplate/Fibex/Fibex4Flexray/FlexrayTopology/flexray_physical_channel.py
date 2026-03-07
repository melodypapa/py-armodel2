"""FlexrayPhysicalChannel AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 89)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Flexray_FlexrayTopology.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology.physical_channel import (
    PhysicalChannel,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology.physical_channel import PhysicalChannelBuilder
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Flexray.FlexrayTopology import (
    FlexrayChannelName,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class FlexrayPhysicalChannel(PhysicalChannel):
    """AUTOSAR FlexrayPhysicalChannel."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "FLEXRAY-PHYSICAL-CHANNEL"


    channel_name: Optional[FlexrayChannelName]
    _DESERIALIZE_DISPATCH = {
        "CHANNEL-NAME": lambda obj, elem: setattr(obj, "channel_name", FlexrayChannelName.deserialize(elem)),
    }


    def __init__(self) -> None:
        """Initialize FlexrayPhysicalChannel."""
        super().__init__()
        self.channel_name: Optional[FlexrayChannelName] = None

    def serialize(self) -> ET.Element:
        """Serialize FlexrayPhysicalChannel to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(FlexrayPhysicalChannel, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize channel_name
        if self.channel_name is not None:
            serialized = SerializationHelper.serialize_item(self.channel_name, "FlexrayChannelName")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("CHANNEL-NAME")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "FlexrayPhysicalChannel":
        """Deserialize XML element to FlexrayPhysicalChannel object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized FlexrayPhysicalChannel object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(FlexrayPhysicalChannel, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "CHANNEL-NAME":
                setattr(obj, "channel_name", FlexrayChannelName.deserialize(child))

        return obj



class FlexrayPhysicalChannelBuilder(PhysicalChannelBuilder):
    """Builder for FlexrayPhysicalChannel with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: FlexrayPhysicalChannel = FlexrayPhysicalChannel()


    def with_channel_name(self, value: Optional[FlexrayChannelName]) -> "FlexrayPhysicalChannelBuilder":
        """Set channel_name attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'channel_name' is required and cannot be None")
        self._obj.channel_name = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "channelName",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> FlexrayPhysicalChannel:
        """Build and return the FlexrayPhysicalChannel instance with validation."""
        self._validate_instance()
        return self._obj