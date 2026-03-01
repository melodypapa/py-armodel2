"""ApplicationCompositeElementInPortInterfaceInstanceRef AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 952)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_PortInterface_InstanceRefs.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes.autosar_data_prototype import (
    AutosarDataPrototype,
)
from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface.data_interface import (
    DataInterface,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class ApplicationCompositeElementInPortInterfaceInstanceRef(ARObject):
    """AUTOSAR ApplicationCompositeElementInPortInterfaceInstanceRef."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "APPLICATION-COMPOSITE-ELEMENT-IN-PORT-INTERFACE-INSTANCE-REF"


    base_ref: Optional[ARRef]
    context_data_refs: list[Any]
    root_data_ref: Optional[ARRef]
    target_data_ref: Optional[Any]
    _DESERIALIZE_DISPATCH = {
        "BASE-REF": ("_POLYMORPHIC", "base_ref", ["NvDataInterface", "ParameterInterface", "SenderReceiverInterface"]),
        "CONTEXT-DATA-REFS": lambda obj, elem: obj.context_data_refs.append(ARRef.deserialize(elem)),
        "ROOT-DATA-REF": ("_POLYMORPHIC", "root_data_ref", ["ArgumentDataPrototype", "ParameterDataPrototype", "VariableDataPrototype"]),
        "TARGET-DATA-REF": lambda obj, elem: setattr(obj, "target_data_ref", ARRef.deserialize(elem)),
    }


    def __init__(self) -> None:
        """Initialize ApplicationCompositeElementInPortInterfaceInstanceRef."""
        super().__init__()
        self.base_ref: Optional[ARRef] = None
        self.context_data_refs: list[Any] = []
        self.root_data_ref: Optional[ARRef] = None
        self.target_data_ref: Optional[Any] = None

    def serialize(self) -> ET.Element:
        """Serialize ApplicationCompositeElementInPortInterfaceInstanceRef to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(ApplicationCompositeElementInPortInterfaceInstanceRef, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize base_ref
        if self.base_ref is not None:
            serialized = SerializationHelper.serialize_item(self.base_ref, "DataInterface")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("BASE-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize context_data_refs (list to container "CONTEXT-DATA-REFS")
        if self.context_data_refs:
            wrapper = ET.Element("CONTEXT-DATA-REFS")
            for item in self.context_data_refs:
                serialized = SerializationHelper.serialize_item(item, "Any")
                if serialized is not None:
                    child_elem = ET.Element("CONTEXT-DATA-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize root_data_ref
        if self.root_data_ref is not None:
            serialized = SerializationHelper.serialize_item(self.root_data_ref, "AutosarDataPrototype")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ROOT-DATA-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize target_data_ref
        if self.target_data_ref is not None:
            serialized = SerializationHelper.serialize_item(self.target_data_ref, "Any")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TARGET-DATA-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ApplicationCompositeElementInPortInterfaceInstanceRef":
        """Deserialize XML element to ApplicationCompositeElementInPortInterfaceInstanceRef object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized ApplicationCompositeElementInPortInterfaceInstanceRef object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(ApplicationCompositeElementInPortInterfaceInstanceRef, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "BASE-REF":
                setattr(obj, "base_ref", ARRef.deserialize(child))
            elif tag == "CONTEXT-DATA-REFS":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.context_data_refs.append(SerializationHelper.deserialize_by_tag(item_elem, "any (ApplicationComposite)"))
            elif tag == "ROOT-DATA-REF":
                setattr(obj, "root_data_ref", ARRef.deserialize(child))
            elif tag == "TARGET-DATA-REF":
                setattr(obj, "target_data_ref", ARRef.deserialize(child))

        return obj



class ApplicationCompositeElementInPortInterfaceInstanceRefBuilder(BuilderBase):
    """Builder for ApplicationCompositeElementInPortInterfaceInstanceRef with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: ApplicationCompositeElementInPortInterfaceInstanceRef = ApplicationCompositeElementInPortInterfaceInstanceRef()


    def with_base(self, value: Optional[DataInterface]) -> "ApplicationCompositeElementInPortInterfaceInstanceRefBuilder":
        """Set base attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.base = value
        return self

    def with_context_datas(self, items: list[any (ApplicationComposite)]) -> "ApplicationCompositeElementInPortInterfaceInstanceRefBuilder":
        """Set context_datas list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.context_datas = list(items) if items else []
        return self

    def with_root_data(self, value: Optional[AutosarDataPrototype]) -> "ApplicationCompositeElementInPortInterfaceInstanceRefBuilder":
        """Set root_data attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.root_data = value
        return self

    def with_target_data(self, value: Optional[any (ApplicationComposite)]) -> "ApplicationCompositeElementInPortInterfaceInstanceRefBuilder":
        """Set target_data attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.target_data = value
        return self


    def add_context_data(self, item: any (ApplicationComposite)) -> "ApplicationCompositeElementInPortInterfaceInstanceRefBuilder":
        """Add a single item to context_datas list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.context_datas.append(item)
        return self

    def clear_context_datas(self) -> "ApplicationCompositeElementInPortInterfaceInstanceRefBuilder":
        """Clear all items from context_datas list.

        Returns:
            self for method chaining
        """
        self._obj.context_datas = []
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


    def build(self) -> ApplicationCompositeElementInPortInterfaceInstanceRef:
        """Build and return the ApplicationCompositeElementInPortInterfaceInstanceRef instance with validation."""
        self._validate_instance()
        pass
        return self._obj