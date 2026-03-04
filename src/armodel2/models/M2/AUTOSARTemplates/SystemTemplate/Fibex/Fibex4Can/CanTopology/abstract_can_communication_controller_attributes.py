"""AbstractCanCommunicationControllerAttributes AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 64)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Can_CanTopology.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel2.models.M2.builder_base import BuilderBase
from abc import ABC, abstractmethod
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class AbstractCanCommunicationControllerAttributes(ARObject, ABC):
    """AUTOSAR AbstractCanCommunicationControllerAttributes."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    can_controller_fd: Optional[Any]
    can_controller_xl: Optional[Any]
    _DESERIALIZE_DISPATCH = {
        "CAN-CONTROLLER-FD": lambda obj, elem: setattr(obj, "can_controller_fd", SerializationHelper.deserialize_by_tag(elem, "any (CanControllerFd)")),
        "CAN-CONTROLLER-XL": lambda obj, elem: setattr(obj, "can_controller_xl", SerializationHelper.deserialize_by_tag(elem, "any (CanControllerXl)")),
    }


    def __init__(self) -> None:
        """Initialize AbstractCanCommunicationControllerAttributes."""
        super().__init__()
        self.can_controller_fd: Optional[Any] = None
        self.can_controller_xl: Optional[Any] = None

    def serialize(self) -> ET.Element:
        """Serialize AbstractCanCommunicationControllerAttributes to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(AbstractCanCommunicationControllerAttributes, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize can_controller_fd
        if self.can_controller_fd is not None:
            serialized = SerializationHelper.serialize_item(self.can_controller_fd, "Any")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("CAN-CONTROLLER-FD")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize can_controller_xl
        if self.can_controller_xl is not None:
            serialized = SerializationHelper.serialize_item(self.can_controller_xl, "Any")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("CAN-CONTROLLER-XL")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "AbstractCanCommunicationControllerAttributes":
        """Deserialize XML element to AbstractCanCommunicationControllerAttributes object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized AbstractCanCommunicationControllerAttributes object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(AbstractCanCommunicationControllerAttributes, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "CAN-CONTROLLER-FD":
                setattr(obj, "can_controller_fd", SerializationHelper.deserialize_by_tag(child, "any (CanControllerFd)"))
            elif tag == "CAN-CONTROLLER-XL":
                setattr(obj, "can_controller_xl", SerializationHelper.deserialize_by_tag(child, "any (CanControllerXl)"))

        return obj



class AbstractCanCommunicationControllerAttributesBuilder(BuilderBase, ABC):
    """Builder for AbstractCanCommunicationControllerAttributes with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: AbstractCanCommunicationControllerAttributes = AbstractCanCommunicationControllerAttributes()


    def with_can_controller_fd(self, value: Optional[any (CanControllerFd)]) -> "AbstractCanCommunicationControllerAttributesBuilder":
        """Set can_controller_fd attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.can_controller_fd = value
        return self

    def with_can_controller_xl(self, value: Optional[any (CanControllerXl)]) -> "AbstractCanCommunicationControllerAttributesBuilder":
        """Set can_controller_xl attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.can_controller_xl = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "canControllerFd",
        "canControllerXl",
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
    def build(self) -> AbstractCanCommunicationControllerAttributes:
        """Build and return the AbstractCanCommunicationControllerAttributes instance (abstract)."""
        raise NotImplementedError