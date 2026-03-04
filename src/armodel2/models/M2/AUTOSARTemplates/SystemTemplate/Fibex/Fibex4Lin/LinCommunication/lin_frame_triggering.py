"""LinFrameTriggering AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 428)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Lin_LinCommunication.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.frame_triggering import (
    FrameTriggering,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.frame_triggering import FrameTriggeringBuilder
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Lin.LinCommunication import (
    LinChecksumType,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Integer,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class LinFrameTriggering(FrameTriggering):
    """AUTOSAR LinFrameTriggering."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "LIN-FRAME-TRIGGERING"


    identifier: Optional[Integer]
    lin_checksum: Optional[LinChecksumType]
    _DESERIALIZE_DISPATCH = {
        "IDENTIFIER": lambda obj, elem: setattr(obj, "identifier", SerializationHelper.deserialize_by_tag(elem, "Integer")),
        "LIN-CHECKSUM": lambda obj, elem: setattr(obj, "lin_checksum", LinChecksumType.deserialize(elem)),
    }


    def __init__(self) -> None:
        """Initialize LinFrameTriggering."""
        super().__init__()
        self.identifier: Optional[Integer] = None
        self.lin_checksum: Optional[LinChecksumType] = None

    def serialize(self) -> ET.Element:
        """Serialize LinFrameTriggering to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(LinFrameTriggering, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize identifier
        if self.identifier is not None:
            serialized = SerializationHelper.serialize_item(self.identifier, "Integer")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("IDENTIFIER")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize lin_checksum
        if self.lin_checksum is not None:
            serialized = SerializationHelper.serialize_item(self.lin_checksum, "LinChecksumType")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("LIN-CHECKSUM")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "LinFrameTriggering":
        """Deserialize XML element to LinFrameTriggering object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized LinFrameTriggering object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(LinFrameTriggering, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "IDENTIFIER":
                setattr(obj, "identifier", SerializationHelper.deserialize_by_tag(child, "Integer"))
            elif tag == "LIN-CHECKSUM":
                setattr(obj, "lin_checksum", LinChecksumType.deserialize(child))

        return obj



class LinFrameTriggeringBuilder(FrameTriggeringBuilder):
    """Builder for LinFrameTriggering with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: LinFrameTriggering = LinFrameTriggering()


    def with_identifier(self, value: Optional[Integer]) -> "LinFrameTriggeringBuilder":
        """Set identifier attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.identifier = value
        return self

    def with_lin_checksum(self, value: Optional[LinChecksumType]) -> "LinFrameTriggeringBuilder":
        """Set lin_checksum attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.lin_checksum = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "identifier",
        "linChecksum",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> LinFrameTriggering:
        """Build and return the LinFrameTriggering instance with validation."""
        self._validate_instance()
        return self._obj