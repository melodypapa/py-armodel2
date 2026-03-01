"""DataPrototypeInPortInterfaceRef AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 787)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Transformer.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Transformer.data_prototype_reference import (
    DataPrototypeReference,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Transformer.data_prototype_reference import DataPrototypeReferenceBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes.data_prototype import (
    DataPrototype,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class DataPrototypeInPortInterfaceRef(DataPrototypeReference):
    """AUTOSAR DataPrototypeInPortInterfaceRef."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "DATA-PROTOTYPE-IN-PORT-INTERFACE-REF"


    data_prototype_in_ref: Optional[ARRef]
    _DESERIALIZE_DISPATCH = {
        "DATA-PROTOTYPE-IN-REF": ("_POLYMORPHIC", "data_prototype_in_ref", ["ApplicationArrayElement", "ApplicationCompositeElementDataPrototype", "ApplicationRecordElement", "ArgumentDataPrototype", "AutosarDataPrototype", "ParameterDataPrototype", "VariableDataPrototype"]),
    }


    def __init__(self) -> None:
        """Initialize DataPrototypeInPortInterfaceRef."""
        super().__init__()
        self.data_prototype_in_ref: Optional[ARRef] = None

    def serialize(self) -> ET.Element:
        """Serialize DataPrototypeInPortInterfaceRef to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DataPrototypeInPortInterfaceRef, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize data_prototype_in_ref
        if self.data_prototype_in_ref is not None:
            serialized = SerializationHelper.serialize_item(self.data_prototype_in_ref, "DataPrototype")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("DATA-PROTOTYPE-IN-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DataPrototypeInPortInterfaceRef":
        """Deserialize XML element to DataPrototypeInPortInterfaceRef object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DataPrototypeInPortInterfaceRef object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DataPrototypeInPortInterfaceRef, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "DATA-PROTOTYPE-IN-REF":
                setattr(obj, "data_prototype_in_ref", ARRef.deserialize(child))

        return obj



class DataPrototypeInPortInterfaceRefBuilder(DataPrototypeReferenceBuilder):
    """Builder for DataPrototypeInPortInterfaceRef with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: DataPrototypeInPortInterfaceRef = DataPrototypeInPortInterfaceRef()


    def with_data_prototype_in(self, value: Optional[DataPrototype]) -> "DataPrototypeInPortInterfaceRefBuilder":
        """Set data_prototype_in attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.data_prototype_in = value
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


    def build(self) -> DataPrototypeInPortInterfaceRef:
        """Build and return the DataPrototypeInPortInterfaceRef instance with validation."""
        self._validate_instance()
        pass
        return self._obj