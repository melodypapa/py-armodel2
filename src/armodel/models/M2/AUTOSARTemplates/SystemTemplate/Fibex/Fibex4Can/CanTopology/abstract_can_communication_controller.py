"""AbstractCanCommunicationController AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 63)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Can_CanTopology.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET
from armodel.serialization.decorators import atp_variant

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from abc import ABC, abstractmethod
from armodel.models.M2.builder_base import BuilderBase


class AbstractCanCommunicationController(ARObject, ABC):
    """AUTOSAR AbstractCanCommunicationController."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    can_controller_controller_attributes: Optional[Any]
    def __init__(self) -> None:
        """Initialize AbstractCanCommunicationController."""
        super().__init__()
        self.can_controller_controller_attributes: Optional[Any] = None

    def serialize(self) -> ET.Element:
        """Serialize AbstractCanCommunicationController to XML element with atp_variant wrapper.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(AbstractCanCommunicationController, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Create inner element to hold attributes before wrapping
        inner_elem = ET.Element("INNER")

        # Serialize can_controller_controller_attributes
        if self.can_controller_controller_attributes is not None:
            serialized = SerializationHelper.serialize_item(self.can_controller_controller_attributes, "Any")
            if serialized is not None:
                wrapped = ET.Element("CAN-CONTROLLER-CONTROLLER-ATTRIBUTES")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                inner_elem.append(wrapped)

        # Wrap inner element in atp_variant VARIANTS/CONDITIONAL structure
        wrapped = SerializationHelper.serialize_with_atp_variant(inner_elem, "AbstractCanCommunicationController")
        elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "AbstractCanCommunicationController":
        """Deserialize XML element to AbstractCanCommunicationController object with atp_variant unwrapping.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized AbstractCanCommunicationController object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(AbstractCanCommunicationController, cls).deserialize(element)

        # Unwrap atp_variant VARIANTS/CONDITIONAL structure
        inner_elem = SerializationHelper.deserialize_from_atp_variant(element, "AbstractCanCommunicationController")
        if inner_elem is None:
            # No wrapper structure found, return object with default values
            return obj

        # Parse can_controller_controller_attributes
        child = SerializationHelper.find_child_element(inner_elem, "CAN-CONTROLLER-CONTROLLER-ATTRIBUTES")
        if child is not None:
            can_controller_controller_attributes_value = child.text
            obj.can_controller_controller_attributes = can_controller_controller_attributes_value

        return obj



class AbstractCanCommunicationControllerBuilder(BuilderBase, ABC):
    """Builder for AbstractCanCommunicationController with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: AbstractCanCommunicationController = AbstractCanCommunicationController()


    def with_can_controller_controller_attributes(self, value: Optional[any (AbstractCan)]) -> "AbstractCanCommunicationControllerBuilder":
        """Set can_controller_controller_attributes attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.can_controller_controller_attributes = value
        return self




    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from typing import get_type_hints
        from armodel.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # Get type hints for the class
        try:
            type_hints_dict = get_type_hints(type(self._obj))
        except Exception:
            # Cannot resolve type hints (e.g., forward references), skip validation
            return

        for attr_name, attr_type in type_hints_dict.items():
            if attr_name.startswith("_"):
                continue

            value = getattr(self._obj, attr_name)

            # Check required fields (not Optional)
            if value is None and not self._is_optional_type(attr_type):
                if mode == BuilderValidationMode.STRICT:
                    raise ValueError(
                        f"Required attribute '{attr_name}' is None"
                    )
                elif mode == BuilderValidationMode.LENIENT:
                    import warnings
                    warnings.warn(
                        f"Required attribute '{attr_name}' is None",
                        UserWarning
                    )

    @staticmethod
    def _is_optional_type(type_hint: Any) -> bool:
        """Check if a type hint is Optional.

        Args:
            type_hint: Type hint to check

        Returns:
            True if type is Optional, False otherwise
        """
        origin = getattr(type_hint, "__origin__", None)
        return origin is Union

    @staticmethod
    def _get_expected_type(type_hint: Any) -> type:
        """Extract expected type from type hint.

        Args:
            type_hint: Type hint to extract from

        Returns:
            Expected type
        """
        if isinstance(type_hint, str):
            return object
        origin = getattr(type_hint, "__origin__", None)
        if origin is Union:
            args = getattr(type_hint, "__args__", [])
            for arg in args:
                if arg is not type(None):
                    return arg
        elif origin is list:
            args = getattr(type_hint, "__args__", [object])
            return args[0] if args else object
        return type_hint if isinstance(type_hint, type) else object


    @abstractmethod
    def build(self) -> AbstractCanCommunicationController:
        """Build and return the AbstractCanCommunicationController instance (abstract)."""
        raise NotImplementedError