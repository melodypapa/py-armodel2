"""RPortPrototype AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 68)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 2047)
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 237)
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 460)
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 202)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_Components.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.abstract_required_port_prototype import (
    AbstractRequiredPortPrototype,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.abstract_required_port_prototype import AbstractRequiredPortPrototypeBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
)
from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface.port_interface import (
    PortInterface,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class RPortPrototype(AbstractRequiredPortPrototype):
    """AUTOSAR RPortPrototype."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "R-PORT-PROTOTYPE"


    may_be_unconnected: Optional[Boolean]
    required_interface_ref: Optional[ARRef]
    _DESERIALIZE_DISPATCH = {
        "MAY-BE-UNCONNECTED": lambda obj, elem: setattr(obj, "may_be_unconnected", elem.text),
        "REQUIRED-INTERFACE-TREF": lambda obj, elem: setattr(obj, "required_interface_ref", ARRef.deserialize(elem)),
    }


    def __init__(self) -> None:
        """Initialize RPortPrototype."""
        super().__init__()
        self.may_be_unconnected: Optional[Boolean] = None
        self.required_interface_ref: Optional[ARRef] = None

    def serialize(self) -> ET.Element:
        """Serialize RPortPrototype to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(RPortPrototype, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize may_be_unconnected
        if self.may_be_unconnected is not None:
            serialized = SerializationHelper.serialize_item(self.may_be_unconnected, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MAY-BE-UNCONNECTED")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize required_interface_ref
        if self.required_interface_ref is not None:
            serialized = SerializationHelper.serialize_item(self.required_interface_ref, "PortInterface")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("REQUIRED-INTERFACE-TREF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "RPortPrototype":
        """Deserialize XML element to RPortPrototype object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized RPortPrototype object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(RPortPrototype, cls).deserialize(element)

        # Parse may_be_unconnected
        child = SerializationHelper.find_child_element(element, "MAY-BE-UNCONNECTED")
        if child is not None:
            may_be_unconnected_value = child.text
            obj.may_be_unconnected = may_be_unconnected_value

        # Parse required_interface_ref
        child = SerializationHelper.find_child_element(element, "REQUIRED-INTERFACE-TREF")
        if child is not None:
            required_interface_ref_value = ARRef.deserialize(child)
            obj.required_interface_ref = required_interface_ref_value

        return obj



class RPortPrototypeBuilder(AbstractRequiredPortPrototypeBuilder):
    """Builder for RPortPrototype with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: RPortPrototype = RPortPrototype()


    def with_may_be_unconnected(self, value: Optional[Boolean]) -> "RPortPrototypeBuilder":
        """Set may_be_unconnected attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.may_be_unconnected = value
        return self

    def with_required_interface(self, value: Optional[PortInterface]) -> "RPortPrototypeBuilder":
        """Set required_interface attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.required_interface = value
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


    def build(self) -> RPortPrototype:
        """Build and return the RPortPrototype instance with validation."""
        self._validate_instance()
        pass
        return self._obj