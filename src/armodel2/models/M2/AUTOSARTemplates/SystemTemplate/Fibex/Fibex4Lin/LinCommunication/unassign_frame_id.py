"""UnassignFrameId AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 436)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Lin_LinCommunication.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Lin.LinCommunication.lin_configuration_entry import (
    LinConfigurationEntry,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Lin.LinCommunication.lin_configuration_entry import LinConfigurationEntryBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Lin.LinCommunication.lin_frame_triggering import (
    LinFrameTriggering,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class UnassignFrameId(LinConfigurationEntry):
    """AUTOSAR UnassignFrameId."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "UNASSIGN-FRAME-ID"


    unassigned_ref: Optional[ARRef]
    _DESERIALIZE_DISPATCH = {
        "UNASSIGNED-REF": lambda obj, elem: setattr(obj, "unassigned_ref", ARRef.deserialize(elem)),
    }


    def __init__(self) -> None:
        """Initialize UnassignFrameId."""
        super().__init__()
        self.unassigned_ref: Optional[ARRef] = None

    def serialize(self) -> ET.Element:
        """Serialize UnassignFrameId to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(UnassignFrameId, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize unassigned_ref
        if self.unassigned_ref is not None:
            serialized = SerializationHelper.serialize_item(self.unassigned_ref, "LinFrameTriggering")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("UNASSIGNED-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "UnassignFrameId":
        """Deserialize XML element to UnassignFrameId object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized UnassignFrameId object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(UnassignFrameId, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "UNASSIGNED-REF":
                setattr(obj, "unassigned_ref", ARRef.deserialize(child))

        return obj



class UnassignFrameIdBuilder(LinConfigurationEntryBuilder):
    """Builder for UnassignFrameId with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: UnassignFrameId = UnassignFrameId()


    def with_unassigned(self, value: Optional[LinFrameTriggering]) -> "UnassignFrameIdBuilder":
        """Set unassigned attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'unassigned' is required and cannot be None")
        self._obj.unassigned = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "unassigned",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> UnassignFrameId:
        """Build and return the UnassignFrameId instance with validation."""
        self._validate_instance()
        return self._obj