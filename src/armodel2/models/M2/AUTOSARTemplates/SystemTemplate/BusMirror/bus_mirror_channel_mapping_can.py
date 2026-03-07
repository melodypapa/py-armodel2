"""BusMirrorChannelMappingCan AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 700)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_BusMirror.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.BusMirror.bus_mirror_channel_mapping import (
    BusMirrorChannelMapping,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.BusMirror.bus_mirror_channel_mapping import BusMirrorChannelMappingBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.BusMirror.bus_mirror_can_id_range_mapping import (
    BusMirrorCanIdRangeMapping,
)
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.BusMirror.bus_mirror_can_id_to_can_id_mapping import (
    BusMirrorCanIdToCanIdMapping,
)
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.BusMirror.bus_mirror_lin_pid_to_can_id_mapping import (
    BusMirrorLinPidToCanIdMapping,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class BusMirrorChannelMappingCan(BusMirrorChannelMapping):
    """AUTOSAR BusMirrorChannelMappingCan."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "BUS-MIRROR-CHANNEL-MAPPING-CAN"


    can_id_ranges: list[BusMirrorCanIdRangeMapping]
    can_id_to_can_ids: list[BusMirrorCanIdToCanIdMapping]
    lin_pid_to_can_ids: list[BusMirrorLinPidToCanIdMapping]
    mirror_source_lin: Optional[PositiveInteger]
    mirror_status: Optional[PositiveInteger]
    _DESERIALIZE_DISPATCH = {
        "CAN-ID-RANGES": lambda obj, elem: obj.can_id_ranges.append(SerializationHelper.deserialize_by_tag(elem, "BusMirrorCanIdRangeMapping")),
        "CAN-ID-TO-CAN-IDS": lambda obj, elem: obj.can_id_to_can_ids.append(SerializationHelper.deserialize_by_tag(elem, "BusMirrorCanIdToCanIdMapping")),
        "LIN-PID-TO-CAN-IDS": lambda obj, elem: obj.lin_pid_to_can_ids.append(SerializationHelper.deserialize_by_tag(elem, "BusMirrorLinPidToCanIdMapping")),
        "MIRROR-SOURCE-LIN": lambda obj, elem: setattr(obj, "mirror_source_lin", SerializationHelper.deserialize_by_tag(elem, "PositiveInteger")),
        "MIRROR-STATUS": lambda obj, elem: setattr(obj, "mirror_status", SerializationHelper.deserialize_by_tag(elem, "PositiveInteger")),
    }


    def __init__(self) -> None:
        """Initialize BusMirrorChannelMappingCan."""
        super().__init__()
        self.can_id_ranges: list[BusMirrorCanIdRangeMapping] = []
        self.can_id_to_can_ids: list[BusMirrorCanIdToCanIdMapping] = []
        self.lin_pid_to_can_ids: list[BusMirrorLinPidToCanIdMapping] = []
        self.mirror_source_lin: Optional[PositiveInteger] = None
        self.mirror_status: Optional[PositiveInteger] = None

    def serialize(self) -> ET.Element:
        """Serialize BusMirrorChannelMappingCan to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(BusMirrorChannelMappingCan, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize can_id_ranges (list to container "CAN-ID-RANGES")
        if self.can_id_ranges:
            wrapper = ET.Element("CAN-ID-RANGES")
            for item in self.can_id_ranges:
                serialized = SerializationHelper.serialize_item(item, "BusMirrorCanIdRangeMapping")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize can_id_to_can_ids (list to container "CAN-ID-TO-CAN-IDS")
        if self.can_id_to_can_ids:
            wrapper = ET.Element("CAN-ID-TO-CAN-IDS")
            for item in self.can_id_to_can_ids:
                serialized = SerializationHelper.serialize_item(item, "BusMirrorCanIdToCanIdMapping")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize lin_pid_to_can_ids (list to container "LIN-PID-TO-CAN-IDS")
        if self.lin_pid_to_can_ids:
            wrapper = ET.Element("LIN-PID-TO-CAN-IDS")
            for item in self.lin_pid_to_can_ids:
                serialized = SerializationHelper.serialize_item(item, "BusMirrorLinPidToCanIdMapping")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize mirror_source_lin
        if self.mirror_source_lin is not None:
            serialized = SerializationHelper.serialize_item(self.mirror_source_lin, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MIRROR-SOURCE-LIN")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize mirror_status
        if self.mirror_status is not None:
            serialized = SerializationHelper.serialize_item(self.mirror_status, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MIRROR-STATUS")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "BusMirrorChannelMappingCan":
        """Deserialize XML element to BusMirrorChannelMappingCan object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized BusMirrorChannelMappingCan object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(BusMirrorChannelMappingCan, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "CAN-ID-RANGES":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.can_id_ranges.append(SerializationHelper.deserialize_by_tag(item_elem, "BusMirrorCanIdRangeMapping"))
            elif tag == "CAN-ID-TO-CAN-IDS":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.can_id_to_can_ids.append(SerializationHelper.deserialize_by_tag(item_elem, "BusMirrorCanIdToCanIdMapping"))
            elif tag == "LIN-PID-TO-CAN-IDS":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.lin_pid_to_can_ids.append(SerializationHelper.deserialize_by_tag(item_elem, "BusMirrorLinPidToCanIdMapping"))
            elif tag == "MIRROR-SOURCE-LIN":
                setattr(obj, "mirror_source_lin", SerializationHelper.deserialize_by_tag(child, "PositiveInteger"))
            elif tag == "MIRROR-STATUS":
                setattr(obj, "mirror_status", SerializationHelper.deserialize_by_tag(child, "PositiveInteger"))

        return obj



class BusMirrorChannelMappingCanBuilder(BusMirrorChannelMappingBuilder):
    """Builder for BusMirrorChannelMappingCan with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: BusMirrorChannelMappingCan = BusMirrorChannelMappingCan()


    def with_can_id_ranges(self, items: list[BusMirrorCanIdRangeMapping]) -> "BusMirrorChannelMappingCanBuilder":
        """Set can_id_ranges list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.can_id_ranges = list(items) if items else []
        return self

    def with_can_id_to_can_ids(self, items: list[BusMirrorCanIdToCanIdMapping]) -> "BusMirrorChannelMappingCanBuilder":
        """Set can_id_to_can_ids list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.can_id_to_can_ids = list(items) if items else []
        return self

    def with_lin_pid_to_can_ids(self, items: list[BusMirrorLinPidToCanIdMapping]) -> "BusMirrorChannelMappingCanBuilder":
        """Set lin_pid_to_can_ids list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.lin_pid_to_can_ids = list(items) if items else []
        return self

    def with_mirror_source_lin(self, value: Optional[PositiveInteger]) -> "BusMirrorChannelMappingCanBuilder":
        """Set mirror_source_lin attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'mirror_source_lin' is required and cannot be None")
        self._obj.mirror_source_lin = value
        return self

    def with_mirror_status(self, value: Optional[PositiveInteger]) -> "BusMirrorChannelMappingCanBuilder":
        """Set mirror_status attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'mirror_status' is required and cannot be None")
        self._obj.mirror_status = value
        return self


    def add_can_id_range(self, item: BusMirrorCanIdRangeMapping) -> "BusMirrorChannelMappingCanBuilder":
        """Add a single item to can_id_ranges list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.can_id_ranges.append(item)
        return self

    def clear_can_id_ranges(self) -> "BusMirrorChannelMappingCanBuilder":
        """Clear all items from can_id_ranges list.

        Returns:
            self for method chaining
        """
        self._obj.can_id_ranges = []
        return self

    def add_can_id_to_can_id(self, item: BusMirrorCanIdToCanIdMapping) -> "BusMirrorChannelMappingCanBuilder":
        """Add a single item to can_id_to_can_ids list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.can_id_to_can_ids.append(item)
        return self

    def clear_can_id_to_can_ids(self) -> "BusMirrorChannelMappingCanBuilder":
        """Clear all items from can_id_to_can_ids list.

        Returns:
            self for method chaining
        """
        self._obj.can_id_to_can_ids = []
        return self

    def add_lin_pid_to_can_id(self, item: BusMirrorLinPidToCanIdMapping) -> "BusMirrorChannelMappingCanBuilder":
        """Add a single item to lin_pid_to_can_ids list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.lin_pid_to_can_ids.append(item)
        return self

    def clear_lin_pid_to_can_ids(self) -> "BusMirrorChannelMappingCanBuilder":
        """Clear all items from lin_pid_to_can_ids list.

        Returns:
            self for method chaining
        """
        self._obj.lin_pid_to_can_ids = []
        return self


    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "canIdRange",
        "canIdToCanId",
        "linPidToCanId",
        "mirrorSourceLin",
        "mirrorStatus",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> BusMirrorChannelMappingCan:
        """Build and return the BusMirrorChannelMappingCan instance with validation."""
        self._validate_instance()
        return self._obj