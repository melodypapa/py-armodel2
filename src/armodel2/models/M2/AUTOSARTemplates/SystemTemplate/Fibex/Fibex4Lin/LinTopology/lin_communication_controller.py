"""LinCommunicationController AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 93)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Lin_LinTopology.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    String,
)
from abc import ABC, abstractmethod
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class LinCommunicationController(ARObject, ABC):
    """AUTOSAR LinCommunicationController."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    protocol_version: Optional[String]
    _DESERIALIZE_DISPATCH = {
        "PROTOCOL-VERSION": lambda obj, elem: setattr(obj, "protocol_version", SerializationHelper.deserialize_by_tag(elem, "String")),
    }


    def __init__(self) -> None:
        """Initialize LinCommunicationController."""
        super().__init__()
        self.protocol_version: Optional[String] = None

    def serialize(self) -> ET.Element:
        """Serialize LinCommunicationController to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(LinCommunicationController, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize protocol_version
        if self.protocol_version is not None:
            serialized = SerializationHelper.serialize_item(self.protocol_version, "String")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("PROTOCOL-VERSION")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "LinCommunicationController":
        """Deserialize XML element to LinCommunicationController object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized LinCommunicationController object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(LinCommunicationController, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "PROTOCOL-VERSION":
                setattr(obj, "protocol_version", SerializationHelper.deserialize_by_tag(child, "String"))

        return obj



class LinCommunicationControllerBuilder(BuilderBase, ABC):
    """Builder for LinCommunicationController with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: LinCommunicationController = LinCommunicationController()


    def with_protocol_version(self, value: Optional[String]) -> "LinCommunicationControllerBuilder":
        """Set protocol_version attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.protocol_version = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "protocolVersion",
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
    def build(self) -> LinCommunicationController:
        """Build and return the LinCommunicationController instance (abstract)."""
        raise NotImplementedError