"""CanControllerConfiguration AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 64)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Can_CanTopology.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Can.CanTopology.abstract_can_communication_controller_attributes import (
    AbstractCanCommunicationControllerAttributes,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Can.CanTopology.abstract_can_communication_controller_attributes import AbstractCanCommunicationControllerAttributesBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Integer,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class CanControllerConfiguration(AbstractCanCommunicationControllerAttributes):
    """AUTOSAR CanControllerConfiguration."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "CAN-CONTROLLER-CONFIGURATION"


    prop_seg: Optional[Integer]
    sync_jump_width: Optional[Integer]
    time_seg1: Optional[Integer]
    time_seg2: Optional[Integer]
    _DESERIALIZE_DISPATCH = {
        "PROP-SEG": lambda obj, elem: setattr(obj, "prop_seg", SerializationHelper.deserialize_by_tag(elem, "Integer")),
        "SYNC-JUMP-WIDTH": lambda obj, elem: setattr(obj, "sync_jump_width", SerializationHelper.deserialize_by_tag(elem, "Integer")),
        "TIME-SEG1": lambda obj, elem: setattr(obj, "time_seg1", SerializationHelper.deserialize_by_tag(elem, "Integer")),
        "TIME-SEG2": lambda obj, elem: setattr(obj, "time_seg2", SerializationHelper.deserialize_by_tag(elem, "Integer")),
    }


    def __init__(self) -> None:
        """Initialize CanControllerConfiguration."""
        super().__init__()
        self.prop_seg: Optional[Integer] = None
        self.sync_jump_width: Optional[Integer] = None
        self.time_seg1: Optional[Integer] = None
        self.time_seg2: Optional[Integer] = None

    def serialize(self) -> ET.Element:
        """Serialize CanControllerConfiguration to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(CanControllerConfiguration, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize prop_seg
        if self.prop_seg is not None:
            serialized = SerializationHelper.serialize_item(self.prop_seg, "Integer")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("PROP-SEG")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize sync_jump_width
        if self.sync_jump_width is not None:
            serialized = SerializationHelper.serialize_item(self.sync_jump_width, "Integer")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SYNC-JUMP-WIDTH")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize time_seg1
        if self.time_seg1 is not None:
            serialized = SerializationHelper.serialize_item(self.time_seg1, "Integer")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TIME-SEG1")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize time_seg2
        if self.time_seg2 is not None:
            serialized = SerializationHelper.serialize_item(self.time_seg2, "Integer")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TIME-SEG2")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "CanControllerConfiguration":
        """Deserialize XML element to CanControllerConfiguration object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized CanControllerConfiguration object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(CanControllerConfiguration, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "PROP-SEG":
                setattr(obj, "prop_seg", SerializationHelper.deserialize_by_tag(child, "Integer"))
            elif tag == "SYNC-JUMP-WIDTH":
                setattr(obj, "sync_jump_width", SerializationHelper.deserialize_by_tag(child, "Integer"))
            elif tag == "TIME-SEG1":
                setattr(obj, "time_seg1", SerializationHelper.deserialize_by_tag(child, "Integer"))
            elif tag == "TIME-SEG2":
                setattr(obj, "time_seg2", SerializationHelper.deserialize_by_tag(child, "Integer"))

        return obj



class CanControllerConfigurationBuilder(AbstractCanCommunicationControllerAttributesBuilder):
    """Builder for CanControllerConfiguration with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: CanControllerConfiguration = CanControllerConfiguration()


    def with_prop_seg(self, value: Optional[Integer]) -> "CanControllerConfigurationBuilder":
        """Set prop_seg attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'prop_seg' is required and cannot be None")
        self._obj.prop_seg = value
        return self

    def with_sync_jump_width(self, value: Optional[Integer]) -> "CanControllerConfigurationBuilder":
        """Set sync_jump_width attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'sync_jump_width' is required and cannot be None")
        self._obj.sync_jump_width = value
        return self

    def with_time_seg1(self, value: Optional[Integer]) -> "CanControllerConfigurationBuilder":
        """Set time_seg1 attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'time_seg1' is required and cannot be None")
        self._obj.time_seg1 = value
        return self

    def with_time_seg2(self, value: Optional[Integer]) -> "CanControllerConfigurationBuilder":
        """Set time_seg2 attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'time_seg2' is required and cannot be None")
        self._obj.time_seg2 = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "propSeg",
        "syncJumpWidth",
        "timeSeg1",
        "timeSeg2",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> CanControllerConfiguration:
        """Build and return the CanControllerConfiguration instance with validation."""
        self._validate_instance()
        return self._obj