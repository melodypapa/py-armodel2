"""CommConnectorPort AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 303)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_FibexCore_CoreTopology.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import IdentifiableBuilder
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication import (
    CommunicationDirectionType,
)
from abc import ABC, abstractmethod
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class CommConnectorPort(Identifiable, ABC):
    """AUTOSAR CommConnectorPort."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    communication_direction: Optional[CommunicationDirectionType]
    _DESERIALIZE_DISPATCH = {
        "COMMUNICATION-DIRECTION": lambda obj, elem: setattr(obj, "communication_direction", CommunicationDirectionType.deserialize(elem)),
    }


    def __init__(self) -> None:
        """Initialize CommConnectorPort."""
        super().__init__()
        self.communication_direction: Optional[CommunicationDirectionType] = None

    def serialize(self) -> ET.Element:
        """Serialize CommConnectorPort to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(CommConnectorPort, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize communication_direction
        if self.communication_direction is not None:
            serialized = SerializationHelper.serialize_item(self.communication_direction, "CommunicationDirectionType")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("COMMUNICATION-DIRECTION")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "CommConnectorPort":
        """Deserialize XML element to CommConnectorPort object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized CommConnectorPort object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(CommConnectorPort, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "COMMUNICATION-DIRECTION":
                setattr(obj, "communication_direction", CommunicationDirectionType.deserialize(child))

        return obj



class CommConnectorPortBuilder(IdentifiableBuilder):
    """Builder for CommConnectorPort with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: CommConnectorPort = CommConnectorPort()


    def with_communication_direction(self, value: Optional[CommunicationDirectionType]) -> "CommConnectorPortBuilder":
        """Set communication_direction attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.communication_direction = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "communicationDirection",
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
    def build(self) -> CommConnectorPort:
        """Build and return the CommConnectorPort instance (abstract)."""
        raise NotImplementedError