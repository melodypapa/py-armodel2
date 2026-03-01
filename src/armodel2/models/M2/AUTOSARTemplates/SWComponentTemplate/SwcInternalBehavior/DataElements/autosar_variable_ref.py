"""AutosarVariableRef AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 307)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 315)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_SwcInternalBehavior_DataElements.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef

if TYPE_CHECKING:
    from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.DataElements.ar_variable_in_implementation_data_instance_ref import (
        ArVariableInImplementationDataInstanceRef,
    )
    from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes.variable_data_prototype import (
        VariableDataPrototype,
    )
    from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.DataElements.InstanceRefs.variable_in_atomic_swc_type_instance_ref import (
        VariableInAtomicSWCTypeInstanceRef,
    )



from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper
class AutosarVariableRef(ARObject):
    """AUTOSAR AutosarVariableRef."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "AUTOSAR-VARIABLE-REF"


    autosar_variable_iref: Optional[VariableInAtomicSWCTypeInstanceRef]
    autosar_variable_in_impl_datatype: Optional[ArVariableInImplementationDataInstanceRef]
    local_variable_ref: Optional[ARRef]
    _DESERIALIZE_DISPATCH = {
        "AUTOSAR-VARIABLE-IREF": lambda obj, elem: setattr(obj, "autosar_variable_iref", SerializationHelper.deserialize_by_tag(elem, "VariableInAtomicSWCTypeInstanceRef")),
        "AUTOSAR-VARIABLE-IN-IMPL-DATATYPE": lambda obj, elem: setattr(obj, "autosar_variable_in_impl_datatype", SerializationHelper.deserialize_by_tag(elem, "ArVariableInImplementationDataInstanceRef")),
        "LOCAL-VARIABLE-REF": lambda obj, elem: setattr(obj, "local_variable_ref", ARRef.deserialize(elem)),
    }


    def __init__(self) -> None:
        """Initialize AutosarVariableRef."""
        super().__init__()
        self.autosar_variable_iref: Optional[VariableInAtomicSWCTypeInstanceRef] = None
        self.autosar_variable_in_impl_datatype: Optional[ArVariableInImplementationDataInstanceRef] = None
        self.local_variable_ref: Optional[ARRef] = None

    def serialize(self) -> ET.Element:
        """Serialize AutosarVariableRef to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(AutosarVariableRef, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize autosar_variable_iref (instance reference with wrapper "AUTOSAR-VARIABLE-IREF")
        if self.autosar_variable_iref is not None:
            serialized = SerializationHelper.serialize_item(self.autosar_variable_iref, "VariableInAtomicSWCTypeInstanceRef")
            if serialized is not None:
                # Wrap in IREF wrapper element
                iref_wrapper = ET.Element("AUTOSAR-VARIABLE-IREF")
                # Append the serialized element as a child (don't flatten it)
                iref_wrapper.append(serialized)
                elem.append(iref_wrapper)

        # Serialize autosar_variable_in_impl_datatype
        if self.autosar_variable_in_impl_datatype is not None:
            serialized = SerializationHelper.serialize_item(self.autosar_variable_in_impl_datatype, "ArVariableInImplementationDataInstanceRef")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("AUTOSAR-VARIABLE-IN-IMPL-DATATYPE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize local_variable_ref
        if self.local_variable_ref is not None:
            serialized = SerializationHelper.serialize_item(self.local_variable_ref, "VariableDataPrototype")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("LOCAL-VARIABLE-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "AutosarVariableRef":
        """Deserialize XML element to AutosarVariableRef object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized AutosarVariableRef object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(AutosarVariableRef, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "AUTOSAR-VARIABLE-IREF":
                setattr(obj, "autosar_variable_iref", SerializationHelper.deserialize_by_tag(child, "VariableInAtomicSWCTypeInstanceRef"))
            elif tag == "AUTOSAR-VARIABLE-IN-IMPL-DATATYPE":
                setattr(obj, "autosar_variable_in_impl_datatype", SerializationHelper.deserialize_by_tag(child, "ArVariableInImplementationDataInstanceRef"))
            elif tag == "LOCAL-VARIABLE-REF":
                setattr(obj, "local_variable_ref", ARRef.deserialize(child))

        return obj



class AutosarVariableRefBuilder(BuilderBase):
    """Builder for AutosarVariableRef with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: AutosarVariableRef = AutosarVariableRef()


    def with_autosar_variable(self, value: Optional[VariableInAtomicSWCTypeInstanceRef]) -> "AutosarVariableRefBuilder":
        """Set autosar_variable attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.autosar_variable = value
        return self

    def with_autosar_variable_in_impl_datatype(self, value: Optional[ArVariableInImplementationDataInstanceRef]) -> "AutosarVariableRefBuilder":
        """Set autosar_variable_in_impl_datatype attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.autosar_variable_in_impl_datatype = value
        return self

    def with_local_variable(self, value: Optional[VariableDataPrototype]) -> "AutosarVariableRefBuilder":
        """Set local_variable attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.local_variable = value
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


    def build(self) -> AutosarVariableRef:
        """Build and return the AutosarVariableRef instance with validation."""
        self._validate_instance()
        pass
        return self._obj