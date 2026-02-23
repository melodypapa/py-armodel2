"""AbstractProvidedPortPrototype AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 67)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_Components.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.port_prototype import (
    PortPrototype,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from abc import ABC, abstractmethod
from armodel.models.M2.builder_base import BuilderBase
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.port_prototype import PortPrototypeBuilder
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Communication.p_port_com_spec import (
    PPortComSpec,
)


class AbstractProvidedPortPrototype(PortPrototype, ABC):
    """AUTOSAR AbstractProvidedPortPrototype."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    provided_coms: list[PPortComSpec]
    def __init__(self) -> None:
        """Initialize AbstractProvidedPortPrototype."""
        super().__init__()
        self.provided_coms: list[PPortComSpec] = []

    def serialize(self) -> ET.Element:
        """Serialize AbstractProvidedPortPrototype to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(AbstractProvidedPortPrototype, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize provided_coms (list to container "PROVIDED-COMS")
        if self.provided_coms:
            wrapper = ET.Element("PROVIDED-COMS")
            for item in self.provided_coms:
                serialized = SerializationHelper.serialize_item(item, "PPortComSpec")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "AbstractProvidedPortPrototype":
        """Deserialize XML element to AbstractProvidedPortPrototype object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized AbstractProvidedPortPrototype object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(AbstractProvidedPortPrototype, cls).deserialize(element)

        # Parse provided_coms (list from container "PROVIDED-COMS")
        obj.provided_coms = []
        container = SerializationHelper.find_child_element(element, "PROVIDED-COMS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.provided_coms.append(child_value)

        return obj



class AbstractProvidedPortPrototypeBuilder(PortPrototypeBuilder):
    """Builder for AbstractProvidedPortPrototype with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: AbstractProvidedPortPrototype = AbstractProvidedPortPrototype()


    def with_provided_coms(self, items: list[PPortComSpec]) -> "AbstractProvidedPortPrototypeBuilder":
        """Set provided_coms list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.provided_coms = list(items) if items else []
        return self


    def add_provided_com(self, item: PPortComSpec) -> "AbstractProvidedPortPrototypeBuilder":
        """Add a single item to provided_coms list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.provided_coms.append(item)
        return self

    def clear_provided_coms(self) -> "AbstractProvidedPortPrototypeBuilder":
        """Clear all items from provided_coms list.

        Returns:
            self for method chaining
        """
        self._obj.provided_coms = []
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
    def build(self) -> AbstractProvidedPortPrototype:
        """Build and return the AbstractProvidedPortPrototype instance (abstract)."""
        raise NotImplementedError