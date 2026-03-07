"""DataPrototypeInPortInterfaceInstanceRef AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 1009)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Transformer_InstanceRef.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes.autosar_data_prototype import (
    AutosarDataPrototype,
)
from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes.data_prototype import (
    DataPrototype,
)
from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface.port_interface import (
    PortInterface,
)
from abc import ABC, abstractmethod
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class DataPrototypeInPortInterfaceInstanceRef(ARObject, ABC):
    """AUTOSAR DataPrototypeInPortInterfaceInstanceRef."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    abstract_base_ref: Optional[ARRef]
    context_data_refs: list[Any]
    root_data_ref: Optional[ARRef]
    target_data_ref: ARRef
    _DESERIALIZE_DISPATCH = {
        "ABSTRACT-BASE-REF": ("_POLYMORPHIC", "abstract_base_ref", ["ClientServerInterface", "DataInterface", "ModeSwitchInterface", "NvDataInterface", "ParameterInterface", "SenderReceiverInterface", "TriggerInterface"]),
        "CONTEXT-DATA-REFS": lambda obj, elem: [obj.context_data_refs.append(ARRef.deserialize(item_elem)) for item_elem in elem],
        "ROOT-DATA-REF": ("_POLYMORPHIC", "root_data_ref", ["ArgumentDataPrototype", "ParameterDataPrototype", "VariableDataPrototype"]),
        "TARGET-DATA-REF": ("_POLYMORPHIC", "target_data_ref", ["ApplicationArrayElement", "ApplicationCompositeElementDataPrototype", "ApplicationRecordElement", "ArgumentDataPrototype", "AutosarDataPrototype", "ParameterDataPrototype", "VariableDataPrototype"]),
    }


    def __init__(self) -> None:
        """Initialize DataPrototypeInPortInterfaceInstanceRef."""
        super().__init__()
        self.abstract_base_ref: Optional[ARRef] = None
        self.context_data_refs: list[Any] = []
        self.root_data_ref: Optional[ARRef] = None
        self.target_data_ref: ARRef = None

    def serialize(self) -> ET.Element:
        """Serialize DataPrototypeInPortInterfaceInstanceRef to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DataPrototypeInPortInterfaceInstanceRef, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize abstract_base_ref
        if self.abstract_base_ref is not None:
            serialized = SerializationHelper.serialize_item(self.abstract_base_ref, "PortInterface")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ABSTRACT-BASE-REF")
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
            serialized = SerializationHelper.serialize_item(self.target_data_ref, "DataPrototype")
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
    def deserialize(cls, element: ET.Element) -> "DataPrototypeInPortInterfaceInstanceRef":
        """Deserialize XML element to DataPrototypeInPortInterfaceInstanceRef object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DataPrototypeInPortInterfaceInstanceRef object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DataPrototypeInPortInterfaceInstanceRef, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "ABSTRACT-BASE-REF":
                setattr(obj, "abstract_base_ref", ARRef.deserialize(child))
            elif tag == "CONTEXT-DATA-REFS":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.context_data_refs.append(ARRef.deserialize(item_elem))
            elif tag == "ROOT-DATA-REF":
                setattr(obj, "root_data_ref", ARRef.deserialize(child))
            elif tag == "TARGET-DATA-REF":
                setattr(obj, "target_data_ref", ARRef.deserialize(child))

        return obj



class DataPrototypeInPortInterfaceInstanceRefBuilder(BuilderBase, ABC):
    """Builder for DataPrototypeInPortInterfaceInstanceRef with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: DataPrototypeInPortInterfaceInstanceRef = DataPrototypeInPortInterfaceInstanceRef()


    def with_abstract_base(self, value: Optional[PortInterface]) -> "DataPrototypeInPortInterfaceInstanceRefBuilder":
        """Set abstract_base attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'abstract_base' is required and cannot be None")
        self._obj.abstract_base = value
        return self

    def with_context_datas(self, items: list[Any]) -> "DataPrototypeInPortInterfaceInstanceRefBuilder":
        """Set context_datas list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.context_datas = list(items) if items else []
        return self

    def with_root_data(self, value: Optional[AutosarDataPrototype]) -> "DataPrototypeInPortInterfaceInstanceRefBuilder":
        """Set root_data attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'root_data' is required and cannot be None")
        self._obj.root_data = value
        return self

    def with_target_data(self, value: DataPrototype) -> "DataPrototypeInPortInterfaceInstanceRefBuilder":
        """Set target_data attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not False:
            raise ValueError("Attribute 'target_data' is required and cannot be None")
        self._obj.target_data = value
        return self


    def add_context_data(self, item: Any) -> "DataPrototypeInPortInterfaceInstanceRefBuilder":
        """Add a single item to context_datas list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.context_datas.append(item)
        return self

    def clear_context_datas(self) -> "DataPrototypeInPortInterfaceInstanceRefBuilder":
        """Clear all items from context_datas list.

        Returns:
            self for method chaining
        """
        self._obj.context_datas = []
        return self


    # Pre-computed validation constants (generated from JSON schema)
    _REQUIRED_ATTRIBUTES = {
        "targetData",
    }
    _OPTIONAL_ATTRIBUTES = {
        "abstractBase",
        "contextData",
        "rootData",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # Validate required attributes using pre-computed constants (O(1) lookup)
        # This is much faster than calling get_type_hints() at runtime
        if getattr(self._obj, "targetData", None) is None:
            if mode == BuilderValidationMode.STRICT:
                raise ValueError("Required attribute 'targetData' is None")
            elif mode == BuilderValidationMode.LENIENT:
                import warnings
                warnings.warn("Required attribute 'targetData' is None", UserWarning)


    @abstractmethod
    def build(self) -> DataPrototypeInPortInterfaceInstanceRef:
        """Build and return the DataPrototypeInPortInterfaceInstanceRef instance (abstract)."""
        raise NotImplementedError