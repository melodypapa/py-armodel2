"""FlexrayCommunicationConnector AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 89)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Flexray_FlexrayTopology.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology.communication_connector import (
    CommunicationConnector,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology.communication_connector import CommunicationConnectorBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    Float,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class FlexrayCommunicationConnector(CommunicationConnector):
    """AUTOSAR FlexrayCommunicationConnector."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "FLEXRAY-COMMUNICATION-CONNECTOR"


    nm_ready_sleep: Optional[Float]
    wake_up: Optional[Boolean]
    _DESERIALIZE_DISPATCH = {
        "NM-READY-SLEEP": lambda obj, elem: setattr(obj, "nm_ready_sleep", SerializationHelper.deserialize_by_tag(elem, "Float")),
        "WAKE-UP": lambda obj, elem: setattr(obj, "wake_up", SerializationHelper.deserialize_by_tag(elem, "Boolean")),
    }


    def __init__(self) -> None:
        """Initialize FlexrayCommunicationConnector."""
        super().__init__()
        self.nm_ready_sleep: Optional[Float] = None
        self.wake_up: Optional[Boolean] = None

    def serialize(self) -> ET.Element:
        """Serialize FlexrayCommunicationConnector to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(FlexrayCommunicationConnector, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize nm_ready_sleep
        if self.nm_ready_sleep is not None:
            serialized = SerializationHelper.serialize_item(self.nm_ready_sleep, "Float")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("NM-READY-SLEEP")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize wake_up
        if self.wake_up is not None:
            serialized = SerializationHelper.serialize_item(self.wake_up, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("WAKE-UP")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "FlexrayCommunicationConnector":
        """Deserialize XML element to FlexrayCommunicationConnector object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized FlexrayCommunicationConnector object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(FlexrayCommunicationConnector, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "NM-READY-SLEEP":
                setattr(obj, "nm_ready_sleep", SerializationHelper.deserialize_by_tag(child, "Float"))
            elif tag == "WAKE-UP":
                setattr(obj, "wake_up", SerializationHelper.deserialize_by_tag(child, "Boolean"))

        return obj



class FlexrayCommunicationConnectorBuilder(CommunicationConnectorBuilder):
    """Builder for FlexrayCommunicationConnector with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: FlexrayCommunicationConnector = FlexrayCommunicationConnector()


    def with_nm_ready_sleep(self, value: Optional[Float]) -> "FlexrayCommunicationConnectorBuilder":
        """Set nm_ready_sleep attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'nm_ready_sleep' is required and cannot be None")
        self._obj.nm_ready_sleep = value
        return self

    def with_wake_up(self, value: Optional[Boolean]) -> "FlexrayCommunicationConnectorBuilder":
        """Set wake_up attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'wake_up' is required and cannot be None")
        self._obj.wake_up = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "nmReadySleep",
        "wakeUp",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> FlexrayCommunicationConnector:
        """Build and return the FlexrayCommunicationConnector instance with validation."""
        self._validate_instance()
        return self._obj