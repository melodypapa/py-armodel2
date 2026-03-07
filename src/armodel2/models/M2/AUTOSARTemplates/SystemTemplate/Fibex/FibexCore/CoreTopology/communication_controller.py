"""CommunicationController AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 53)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_FibexCore_CoreTopology.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
)
from abc import ABC, abstractmethod
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class CommunicationController(Identifiable, ABC):
    """AUTOSAR CommunicationController."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    wake_up_by_controller_supported: Optional[Boolean]
    _DESERIALIZE_DISPATCH = {
        "WAKE-UP-BY-CONTROLLER-SUPPORTED": lambda obj, elem: setattr(obj, "wake_up_by_controller_supported", SerializationHelper.deserialize_by_tag(elem, "Boolean")),
    }


    def __init__(self) -> None:
        """Initialize CommunicationController."""
        super().__init__()
        self.wake_up_by_controller_supported: Optional[Boolean] = None

    def serialize(self) -> ET.Element:
        """Serialize CommunicationController to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(CommunicationController, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize wake_up_by_controller_supported
        if self.wake_up_by_controller_supported is not None:
            serialized = SerializationHelper.serialize_item(self.wake_up_by_controller_supported, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("WAKE-UP-BY-CONTROLLER-SUPPORTED")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "CommunicationController":
        """Deserialize XML element to CommunicationController object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized CommunicationController object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(CommunicationController, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "WAKE-UP-BY-CONTROLLER-SUPPORTED":
                setattr(obj, "wake_up_by_controller_supported", SerializationHelper.deserialize_by_tag(child, "Boolean"))

        return obj



class CommunicationControllerBuilder(BuilderBase, ABC):
    """Builder for CommunicationController with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: CommunicationController = CommunicationController()


    def with_wake_up_by_controller_supported(self, value: Optional[Boolean]) -> "CommunicationControllerBuilder":
        """Set wake_up_by_controller_supported attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'wake_up_by_controller_supported' is required and cannot be None")
        self._obj.wake_up_by_controller_supported = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "wakeUpByControllerSupported",
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
    def build(self) -> CommunicationController:
        """Build and return the CommunicationController instance (abstract)."""
        raise NotImplementedError