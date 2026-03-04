"""LinConfigurableFrame AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 99)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Lin_LinTopology.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Lin.LinCommunication.lin_frame import (
    LinFrame,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class LinConfigurableFrame(ARObject):
    """AUTOSAR LinConfigurableFrame."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "LIN-CONFIGURABLE-FRAME"


    frame_ref: Optional[ARRef]
    message_id: Optional[PositiveInteger]
    _DESERIALIZE_DISPATCH = {
        "FRAME-REF": ("_POLYMORPHIC", "frame_ref", ["LinEventTriggeredFrame", "LinSporadicFrame", "LinUnconditionalFrame"]),
        "MESSAGE-ID": lambda obj, elem: setattr(obj, "message_id", SerializationHelper.deserialize_by_tag(elem, "PositiveInteger")),
    }


    def __init__(self) -> None:
        """Initialize LinConfigurableFrame."""
        super().__init__()
        self.frame_ref: Optional[ARRef] = None
        self.message_id: Optional[PositiveInteger] = None

    def serialize(self) -> ET.Element:
        """Serialize LinConfigurableFrame to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(LinConfigurableFrame, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize frame_ref
        if self.frame_ref is not None:
            serialized = SerializationHelper.serialize_item(self.frame_ref, "LinFrame")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("FRAME-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize message_id
        if self.message_id is not None:
            serialized = SerializationHelper.serialize_item(self.message_id, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MESSAGE-ID")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "LinConfigurableFrame":
        """Deserialize XML element to LinConfigurableFrame object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized LinConfigurableFrame object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(LinConfigurableFrame, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "FRAME-REF":
                setattr(obj, "frame_ref", ARRef.deserialize(child))
            elif tag == "MESSAGE-ID":
                setattr(obj, "message_id", SerializationHelper.deserialize_by_tag(child, "PositiveInteger"))

        return obj



class LinConfigurableFrameBuilder(BuilderBase):
    """Builder for LinConfigurableFrame with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: LinConfigurableFrame = LinConfigurableFrame()


    def with_frame(self, value: Optional[LinFrame]) -> "LinConfigurableFrameBuilder":
        """Set frame attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.frame = value
        return self

    def with_message_id(self, value: Optional[PositiveInteger]) -> "LinConfigurableFrameBuilder":
        """Set message_id attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.message_id = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "frame",
        "messageId",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> LinConfigurableFrame:
        """Build and return the LinConfigurableFrame instance with validation."""
        self._validate_instance()
        return self._obj