"""BusMirrorChannel AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 698)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_BusMirror.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology.physical_channel import (
    PhysicalChannel,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class BusMirrorChannel(ARObject):
    """AUTOSAR BusMirrorChannel."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "BUS-MIRROR-CHANNEL"


    bus_mirror: Optional[PositiveInteger]
    channel_ref: Optional[ARRef]
    _DESERIALIZE_DISPATCH = {
        "BUS-MIRROR": lambda obj, elem: setattr(obj, "bus_mirror", SerializationHelper.deserialize_by_tag(elem, "PositiveInteger")),
        "CHANNEL-REF": ("_POLYMORPHIC", "channel_ref", ["AbstractCanPhysicalChannel", "CanPhysicalChannel", "EthernetPhysicalChannel", "FlexrayPhysicalChannel", "LinPhysicalChannel", "TtcanPhysicalChannel"]),
    }


    def __init__(self) -> None:
        """Initialize BusMirrorChannel."""
        super().__init__()
        self.bus_mirror: Optional[PositiveInteger] = None
        self.channel_ref: Optional[ARRef] = None

    def serialize(self) -> ET.Element:
        """Serialize BusMirrorChannel to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(BusMirrorChannel, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize bus_mirror
        if self.bus_mirror is not None:
            serialized = SerializationHelper.serialize_item(self.bus_mirror, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("BUS-MIRROR")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize channel_ref
        if self.channel_ref is not None:
            serialized = SerializationHelper.serialize_item(self.channel_ref, "PhysicalChannel")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("CHANNEL-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "BusMirrorChannel":
        """Deserialize XML element to BusMirrorChannel object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized BusMirrorChannel object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(BusMirrorChannel, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "BUS-MIRROR":
                setattr(obj, "bus_mirror", SerializationHelper.deserialize_by_tag(child, "PositiveInteger"))
            elif tag == "CHANNEL-REF":
                setattr(obj, "channel_ref", ARRef.deserialize(child))

        return obj



class BusMirrorChannelBuilder(BuilderBase):
    """Builder for BusMirrorChannel with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: BusMirrorChannel = BusMirrorChannel()


    def with_bus_mirror(self, value: Optional[PositiveInteger]) -> "BusMirrorChannelBuilder":
        """Set bus_mirror attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'bus_mirror' is required and cannot be None")
        self._obj.bus_mirror = value
        return self

    def with_channel(self, value: Optional[PhysicalChannel]) -> "BusMirrorChannelBuilder":
        """Set channel attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'channel' is required and cannot be None")
        self._obj.channel = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "busMirror",
        "channel",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> BusMirrorChannel:
        """Build and return the BusMirrorChannel instance with validation."""
        self._validate_instance()
        return self._obj