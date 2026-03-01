"""VariationPointProxy AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 613)
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 479)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_SwcInternalBehavior_VariantHandling.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import IdentifiableBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.VariantHandling.condition_by_formula import (
    ConditionByFormula,
)

if TYPE_CHECKING:
    from armodel2.models.M2.AUTOSARTemplates.CommonStructure.ImplementationDataTypes.abstract_implementation_data_type import (
        AbstractImplementationDataType,
    )



from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper
class VariationPointProxy(Identifiable):
    """AUTOSAR VariationPointProxy."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "VARIATION-POINT-PROXY"


    condition_access: Optional[ConditionByFormula]
    implementation_ref: Optional[ARRef]
    post_build_value_ref: Optional[Any]
    _DESERIALIZE_DISPATCH = {
        "CONDITION-ACCESS": lambda obj, elem: setattr(obj, "condition_access", SerializationHelper.deserialize_by_tag(elem, "ConditionByFormula")),
        "IMPLEMENTATION-REF": ("_POLYMORPHIC", "implementation_ref", ["ImplementationDataType"]),
        "POST-BUILD-VALUE-REF": lambda obj, elem: setattr(obj, "post_build_value_ref", ARRef.deserialize(elem)),
    }


    def __init__(self) -> None:
        """Initialize VariationPointProxy."""
        super().__init__()
        self.condition_access: Optional[ConditionByFormula] = None
        self.implementation_ref: Optional[ARRef] = None
        self.post_build_value_ref: Optional[Any] = None

    def serialize(self) -> ET.Element:
        """Serialize VariationPointProxy to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(VariationPointProxy, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize condition_access
        if self.condition_access is not None:
            serialized = SerializationHelper.serialize_item(self.condition_access, "ConditionByFormula")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("CONDITION-ACCESS")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize implementation_ref
        if self.implementation_ref is not None:
            serialized = SerializationHelper.serialize_item(self.implementation_ref, "AbstractImplementationDataType")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("IMPLEMENTATION-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize post_build_value_ref
        if self.post_build_value_ref is not None:
            serialized = SerializationHelper.serialize_item(self.post_build_value_ref, "Any")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("POST-BUILD-VALUE-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "VariationPointProxy":
        """Deserialize XML element to VariationPointProxy object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized VariationPointProxy object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(VariationPointProxy, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "CONDITION-ACCESS":
                setattr(obj, "condition_access", SerializationHelper.deserialize_by_tag(child, "ConditionByFormula"))
            elif tag == "IMPLEMENTATION-REF":
                setattr(obj, "implementation_ref", ARRef.deserialize(child))
            elif tag == "POST-BUILD-VALUE-REF":
                setattr(obj, "post_build_value_ref", ARRef.deserialize(child))

        return obj



class VariationPointProxyBuilder(IdentifiableBuilder):
    """Builder for VariationPointProxy with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: VariationPointProxy = VariationPointProxy()


    def with_condition_access(self, value: Optional[ConditionByFormula]) -> "VariationPointProxyBuilder":
        """Set condition_access attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.condition_access = value
        return self

    def with_implementation(self, value: Optional[AbstractImplementationDataType]) -> "VariationPointProxyBuilder":
        """Set implementation attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.implementation = value
        return self

    def with_post_build_value(self, value: Optional[any (PostBuildVariant)]) -> "VariationPointProxyBuilder":
        """Set post_build_value attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.post_build_value = value
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


    def build(self) -> VariationPointProxy:
        """Build and return the VariationPointProxy instance with validation."""
        self._validate_instance()
        pass
        return self._obj