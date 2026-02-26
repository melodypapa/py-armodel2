"""SwComponentPrototype AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 330)
  - AUTOSAR_CP_TPS_ECUConfiguration.pdf (page 307)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 77)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 896)
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 245)
  - AUTOSAR_FO_TPS_AbstractPlatformSpecification.pdf (page 21)
  - AUTOSAR_FO_TPS_FeatureModelExchangeFormat.pdf (page 79)
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 466)
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 210)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_Composition.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import IdentifiableBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.sw_component_type import (
    SwComponentType,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class SwComponentPrototype(Identifiable):
    """AUTOSAR SwComponentPrototype."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    type_ref: Optional[ARRef]
    def __init__(self) -> None:
        """Initialize SwComponentPrototype."""
        super().__init__()
        self.type_ref: Optional[ARRef] = None

    def serialize(self) -> ET.Element:
        """Serialize SwComponentPrototype to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(SwComponentPrototype, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize type_ref
        if self.type_ref is not None:
            serialized = SerializationHelper.serialize_item(self.type_ref, "SwComponentType")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TYPE-TREF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "SwComponentPrototype":
        """Deserialize XML element to SwComponentPrototype object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized SwComponentPrototype object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(SwComponentPrototype, cls).deserialize(element)

        # Parse type_ref
        child = SerializationHelper.find_child_element(element, "TYPE-TREF")
        if child is not None:
            type_ref_value = ARRef.deserialize(child)
            obj.type_ref = type_ref_value

        return obj



class SwComponentPrototypeBuilder(IdentifiableBuilder):
    """Builder for SwComponentPrototype with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: SwComponentPrototype = SwComponentPrototype()


    def with_type(self, value: Optional[SwComponentType]) -> "SwComponentPrototypeBuilder":
        """Set type attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.type = value
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


    def build(self) -> SwComponentPrototype:
        """Build and return the SwComponentPrototype instance with validation."""
        self._validate_instance()
        pass
        return self._obj