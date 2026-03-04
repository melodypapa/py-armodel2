"""BusMirrorCanIdToCanIdMapping AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 702)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_BusMirror.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Can.CanCommunication.can_frame_triggering import (
    CanFrameTriggering,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class BusMirrorCanIdToCanIdMapping(ARObject):
    """AUTOSAR BusMirrorCanIdToCanIdMapping."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "BUS-MIRROR-CAN-ID-TO-CAN-ID-MAPPING"


    remapped_can_id: Optional[PositiveInteger]
    souce_can_id_ref: Optional[ARRef]
    _DESERIALIZE_DISPATCH = {
        "REMAPPED-CAN-ID": lambda obj, elem: setattr(obj, "remapped_can_id", SerializationHelper.deserialize_by_tag(elem, "PositiveInteger")),
        "SOUCE-CAN-ID-REF": lambda obj, elem: setattr(obj, "souce_can_id_ref", ARRef.deserialize(elem)),
    }


    def __init__(self) -> None:
        """Initialize BusMirrorCanIdToCanIdMapping."""
        super().__init__()
        self.remapped_can_id: Optional[PositiveInteger] = None
        self.souce_can_id_ref: Optional[ARRef] = None

    def serialize(self) -> ET.Element:
        """Serialize BusMirrorCanIdToCanIdMapping to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(BusMirrorCanIdToCanIdMapping, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize remapped_can_id
        if self.remapped_can_id is not None:
            serialized = SerializationHelper.serialize_item(self.remapped_can_id, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("REMAPPED-CAN-ID")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize souce_can_id_ref
        if self.souce_can_id_ref is not None:
            serialized = SerializationHelper.serialize_item(self.souce_can_id_ref, "CanFrameTriggering")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SOUCE-CAN-ID-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "BusMirrorCanIdToCanIdMapping":
        """Deserialize XML element to BusMirrorCanIdToCanIdMapping object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized BusMirrorCanIdToCanIdMapping object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(BusMirrorCanIdToCanIdMapping, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "REMAPPED-CAN-ID":
                setattr(obj, "remapped_can_id", SerializationHelper.deserialize_by_tag(child, "PositiveInteger"))
            elif tag == "SOUCE-CAN-ID-REF":
                setattr(obj, "souce_can_id_ref", ARRef.deserialize(child))

        return obj



class BusMirrorCanIdToCanIdMappingBuilder(BuilderBase):
    """Builder for BusMirrorCanIdToCanIdMapping with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: BusMirrorCanIdToCanIdMapping = BusMirrorCanIdToCanIdMapping()


    def with_remapped_can_id(self, value: Optional[PositiveInteger]) -> "BusMirrorCanIdToCanIdMappingBuilder":
        """Set remapped_can_id attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.remapped_can_id = value
        return self

    def with_souce_can_id(self, value: Optional[CanFrameTriggering]) -> "BusMirrorCanIdToCanIdMappingBuilder":
        """Set souce_can_id attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.souce_can_id = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "remappedCanId",
        "souceCanId",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> BusMirrorCanIdToCanIdMapping:
        """Build and return the BusMirrorCanIdToCanIdMapping instance with validation."""
        self._validate_instance()
        return self._obj