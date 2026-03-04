"""BusMirrorChannelMapping AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 697)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_BusMirror.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.fibex_element import (
    FibexElement,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.fibex_element import FibexElementBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.BusMirror import (
    MirroringProtocolEnum,
)
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.BusMirror.bus_mirror_channel import (
    BusMirrorChannel,
)
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.pdu_triggering import (
    PduTriggering,
)
from abc import ABC, abstractmethod
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


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
    _DESERIALIZE_DISPATCH = {
        "MIRRORING": lambda obj, elem: setattr(obj, "mirroring", MirroringProtocolEnum.deserialize(elem)),
        "SOURCE-CHANNEL": lambda obj, elem: setattr(obj, "source_channel", SerializationHelper.deserialize_by_tag(elem, "BusMirrorChannel")),
        "TARGET-CHANNEL": lambda obj, elem: setattr(obj, "target_channel", SerializationHelper.deserialize_by_tag(elem, "BusMirrorChannel")),
        "TARGET-PDU-REFS": lambda obj, elem: [obj.target_pdu_refs.append(ARRef.deserialize(item_elem)) for item_elem in elem],
    }


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
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

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

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "MIRRORING":
                setattr(obj, "mirroring", MirroringProtocolEnum.deserialize(child))
            elif tag == "SOURCE-CHANNEL":
                setattr(obj, "source_channel", SerializationHelper.deserialize_by_tag(child, "BusMirrorChannel"))
            elif tag == "TARGET-CHANNEL":
                setattr(obj, "target_channel", SerializationHelper.deserialize_by_tag(child, "BusMirrorChannel"))
            elif tag == "TARGET-PDU-REFS":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.target_pdu_refs.append(ARRef.deserialize(item_elem))

        return obj



class BusMirrorChannelMappingBuilder(FibexElementBuilder):
    """Builder for BusMirrorChannelMapping with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: BusMirrorChannelMapping = BusMirrorChannelMapping()


    def with_mirroring(self, value: Optional[MirroringProtocolEnum]) -> "BusMirrorChannelMappingBuilder":
        """Set mirroring attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.mirroring = value
        return self

    def with_source_channel(self, value: Optional[BusMirrorChannel]) -> "BusMirrorChannelMappingBuilder":
        """Set source_channel attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.source_channel = value
        return self

    def with_target_channel(self, value: Optional[BusMirrorChannel]) -> "BusMirrorChannelMappingBuilder":
        """Set target_channel attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.target_channel = value
        return self

    def with_target_pdus(self, items: list[PduTriggering]) -> "BusMirrorChannelMappingBuilder":
        """Set target_pdus list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.target_pdus = list(items) if items else []
        return self


    def add_target_pdu(self, item: PduTriggering) -> "BusMirrorChannelMappingBuilder":
        """Add a single item to target_pdus list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.target_pdus.append(item)
        return self

    def clear_target_pdus(self) -> "BusMirrorChannelMappingBuilder":
        """Clear all items from target_pdus list.

        Returns:
            self for method chaining
        """
        self._obj.target_pdus = []
        return self


    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "mirroring",
        "sourceChannel",
        "targetChannel",
        "targetPdu",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    @abstractmethod
    def build(self) -> BusMirrorChannelMapping:
        """Build and return the BusMirrorChannelMapping instance (abstract)."""
        raise NotImplementedError