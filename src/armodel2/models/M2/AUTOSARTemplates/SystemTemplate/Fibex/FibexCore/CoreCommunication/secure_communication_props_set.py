"""SecureCommunicationPropsSet AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 370)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_FibexCore_CoreCommunication.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.fibex_element import (
    FibexElement,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.fibex_element import FibexElementBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class SecureCommunicationPropsSet(FibexElement):
    """AUTOSAR SecureCommunicationPropsSet."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    authentications: list[Any]
    freshness_propses: list[Any]
    def __init__(self) -> None:
        """Initialize SecureCommunicationPropsSet."""
        super().__init__()
        self.authentications: list[Any] = []
        self.freshness_propses: list[Any] = []

    def serialize(self) -> ET.Element:
        """Serialize SecureCommunicationPropsSet to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(SecureCommunicationPropsSet, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize authentications (list to container "AUTHENTICATIONS")
        if self.authentications:
            wrapper = ET.Element("AUTHENTICATIONS")
            for item in self.authentications:
                serialized = SerializationHelper.serialize_item(item, "Any")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize freshness_propses (list to container "FRESHNESS-PROPSES")
        if self.freshness_propses:
            wrapper = ET.Element("FRESHNESS-PROPSES")
            for item in self.freshness_propses:
                serialized = SerializationHelper.serialize_item(item, "Any")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "SecureCommunicationPropsSet":
        """Deserialize XML element to SecureCommunicationPropsSet object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized SecureCommunicationPropsSet object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(SecureCommunicationPropsSet, cls).deserialize(element)

        # Parse authentications (list from container "AUTHENTICATIONS")
        obj.authentications = []
        container = SerializationHelper.find_child_element(element, "AUTHENTICATIONS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.authentications.append(child_value)

        # Parse freshness_propses (list from container "FRESHNESS-PROPSES")
        obj.freshness_propses = []
        container = SerializationHelper.find_child_element(element, "FRESHNESS-PROPSES")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.freshness_propses.append(child_value)

        return obj



class SecureCommunicationPropsSetBuilder(FibexElementBuilder):
    """Builder for SecureCommunicationPropsSet with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: SecureCommunicationPropsSet = SecureCommunicationPropsSet()


    def with_authentications(self, items: list[any (SecureCommunication)]) -> "SecureCommunicationPropsSetBuilder":
        """Set authentications list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.authentications = list(items) if items else []
        return self

    def with_freshness_propses(self, items: list[any (SecureCommunication)]) -> "SecureCommunicationPropsSetBuilder":
        """Set freshness_propses list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.freshness_propses = list(items) if items else []
        return self


    def add_authentication(self, item: any (SecureCommunication)) -> "SecureCommunicationPropsSetBuilder":
        """Add a single item to authentications list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.authentications.append(item)
        return self

    def clear_authentications(self) -> "SecureCommunicationPropsSetBuilder":
        """Clear all items from authentications list.

        Returns:
            self for method chaining
        """
        self._obj.authentications = []
        return self

    def add_freshness_props(self, item: any (SecureCommunication)) -> "SecureCommunicationPropsSetBuilder":
        """Add a single item to freshness_propses list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.freshness_propses.append(item)
        return self

    def clear_freshness_propses(self) -> "SecureCommunicationPropsSetBuilder":
        """Clear all items from freshness_propses list.

        Returns:
            self for method chaining
        """
        self._obj.freshness_propses = []
        return self



    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from typing import get_type_hints
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

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


    def build(self) -> SecureCommunicationPropsSet:
        """Build and return the SecureCommunicationPropsSet instance with validation."""
        self._validate_instance()
        pass
        return self._obj